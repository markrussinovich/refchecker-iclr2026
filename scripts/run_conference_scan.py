#!/usr/bin/env python3
"""Run a RefChecker scan for a conference/year from the conferences tree."""

from __future__ import annotations

import argparse
import os
import re
import shlex
import subprocess
import sys
from pathlib import Path


DEFAULT_REFCHECKER = Path("/datadrive/refchecker")
DEFAULT_DATABASE_DIR = Path("/datadrive/refcheckercache/db")
DEFAULT_LLM_PROVIDER = "google"
DEFAULT_LLM_MODEL = "gemini-3.1-flash-lite-preview"
DEFAULT_HALLUCINATION_PROVIDER = "anthropic"
DEFAULT_HALLUCINATION_MODEL = "claude-haiku-4-5"
DEFAULT_MAX_WORKERS = 6


def parse_conference_and_year(value: str, year: str | None) -> tuple[str, str]:
    text = value.strip().lower().replace("_", "-")

    if year:
        conference = text.strip("-/ ")
        parsed_year = year.strip()
    else:
        match = re.fullmatch(r"([a-z][a-z0-9-]*?)[-/ ]?(20\d{2})", text)
        if not match:
            raise SystemExit(
                "Could not infer year. Use examples like 'iclr2024', "
                "'iclr-2024', or 'iclr --year 2024'."
            )
        conference, parsed_year = match.groups()

    if not re.fullmatch(r"[a-z][a-z0-9-]*", conference):
        raise SystemExit(f"Invalid conference name: {conference!r}")
    if not re.fullmatch(r"20\d{2}", parsed_year):
        raise SystemExit(f"Invalid year: {parsed_year!r}")
    return conference, parsed_year


def build_command(args: argparse.Namespace, paper_list: Path, run_dir: Path) -> list[str]:
    refchecker = args.refchecker.resolve()
    python_bin = refchecker / ".venv" / "bin" / "python"
    if not python_bin.exists():
        raise SystemExit(f"RefChecker Python not found: {python_bin}")

    command = [
        "/usr/bin/time",
        "-p",
        str(python_bin),
        "run_refchecker.py",
        "--paper-list",
        str(paper_list),
        "--cache",
        str(run_dir / "fresh_cache"),
        "--database-dir",
        str(args.database_dir),
        "--llm-provider",
        args.llm_provider,
        "--llm-model",
        args.llm_model,
        "--hallucination-provider",
        args.hallucination_provider,
        "--hallucination-model",
        args.hallucination_model,
        "--report-file",
        str(run_dir / "results" / "scan_report.json"),
        "--report-format",
        "json",
        "--output-file",
        str(run_dir / "results" / "scan_errors.txt"),
        "--max-workers",
        str(args.max_workers),
    ]
    if args.disable_parallel:
        command.append("--disable-parallel")
    if args.llm_no_parallel_chunks:
        command.append("--llm-no-parallel-chunks")
    if args.llm_max_chunk_workers is not None:
        command.extend(["--llm-max-chunk-workers", str(args.llm_max_chunk_workers)])
    return command


def build_stats_report_command(
    root: Path,
    conference: str,
    year: str,
    scan_report_path: Path,
    output_dir: Path,
) -> list[str]:
    return [
        sys.executable,
        str(root / "scripts" / "generate_hallucination_report.py"),
        "--conference",
        conference,
        "--year",
        year,
        "--input",
        str(scan_report_path),
        "--output",
        str(output_dir / "hallucination_report.md"),
        "--chart",
        str(output_dir / "hallucination_count_distribution.png"),
    ]


def build_overview_command(root: Path, output_dir: Path | None = None) -> list[str]:
    command = [
        sys.executable,
        str(root / "scripts" / "generate_overview_hallucination_rate_chart.py"),
        "--workspace-dir",
        str(root / "_workspace"),
    ]
    if output_dir is not None:
        command.extend(
            [
                "--output",
                str(output_dir / "papers_with_ge2_flags_by_year.png"),
                "--data-output",
                str(output_dir / "papers_with_ge2_flags_by_year.csv"),
                "--reference-output",
                str(output_dir / "hallucinated_reference_rate_by_year.png"),
                "--reference-data-output",
                str(output_dir / "hallucinated_reference_rate_by_year.csv"),
            ]
        )
    return command


def shell_command_line(command: list[str]) -> str:
    separator = " \\" + "\n  "
    return separator.join(shlex.quote(part) for part in command)


def write_run_script(run_dir: Path, refchecker: Path, commands: list[list[str]]) -> Path:
    script_path = run_dir / "run_full.sh"
    command_lines = []
    for command in commands:
        command_lines.extend([shell_command_line(command), ""])
    body = "\n".join(
        [
            "#!/usr/bin/env bash",
            "set -euo pipefail",
            "",
            "export REFCHECKER_KEEP_CHECKPOINT=1",
            f"cd {shlex.quote(str(refchecker))}",
            "",
            *command_lines,
        ]
    )
    script_path.write_text(body, encoding="utf-8")
    script_path.chmod(0o755)
    return script_path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run a RefChecker conference scan from conferences/<conference>/<year>/.",
    )
    parser.add_argument("conference", help="Conference/year, e.g. iclr2024 or iclr-2024; use --year for split form.")
    parser.add_argument("--year", help="Year when conference is supplied without a year, e.g. --year 2024.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--refchecker", type=Path, default=DEFAULT_REFCHECKER)
    parser.add_argument("--database-dir", type=Path, default=DEFAULT_DATABASE_DIR)
    parser.add_argument("--llm-provider", default=DEFAULT_LLM_PROVIDER)
    parser.add_argument("--llm-model", default=DEFAULT_LLM_MODEL)
    parser.add_argument("--hallucination-provider", default=DEFAULT_HALLUCINATION_PROVIDER)
    parser.add_argument("--hallucination-model", default=DEFAULT_HALLUCINATION_MODEL)
    parser.add_argument("--max-workers", type=int, default=DEFAULT_MAX_WORKERS)
    parser.add_argument("--disable-parallel", action="store_true", help="Disable parallel reference verification inside each paper.")
    parser.add_argument("--llm-no-parallel-chunks", action="store_true", help="Disable parallel LLM chunk processing during bibliography extraction.")
    parser.add_argument("--llm-max-chunk-workers", type=int, help="Maximum workers for parallel LLM chunk processing.")
    parser.add_argument("--background", "--detach", action="store_true", help="Start the scan in a detached background process.")
    parser.add_argument("--dry-run", action="store_true", help="Print the resolved command without running it.")
    args = parser.parse_args()

    root = args.root.resolve()
    conference, year = parse_conference_and_year(args.conference, args.year)
    paper_list = root / "conferences" / conference / year / f"{conference}-{year}-accepted.txt"
    if not paper_list.exists():
        raise SystemExit(f"Paper list not found: {paper_list}")

    run_dir = root / "_workspace" / f"{conference}{year}"
    scan_report_path = run_dir / "results" / "scan_report.json"
    public_report_dir = root / "reports" / conference / year
    public_overview_dir = root / "reports" / "overview"
    for subdir in ("fresh_cache", "logs", "results"):
        (run_dir / subdir).mkdir(parents=True, exist_ok=True)
    public_report_dir.mkdir(parents=True, exist_ok=True)
    public_overview_dir.mkdir(parents=True, exist_ok=True)

    command = build_command(args, paper_list, run_dir)
    workspace_stats_report_command = build_stats_report_command(
        root,
        conference,
        year,
        scan_report_path,
        run_dir,
    )
    public_stats_report_command = build_stats_report_command(
        root,
        conference,
        year,
        scan_report_path,
        public_report_dir,
    )
    workspace_overview_command = build_overview_command(root)
    public_overview_command = build_overview_command(root, public_overview_dir)
    commands = [
        command,
        workspace_stats_report_command,
        public_stats_report_command,
        workspace_overview_command,
        public_overview_command,
    ]
    run_script = write_run_script(run_dir, args.refchecker.resolve(), commands)
    log_path = run_dir / "logs" / "run.log"

    print(f"conference: {conference}")
    print(f"year: {year}")
    print(f"paper_list: {paper_list}")
    print(f"run_dir: {run_dir}")
    print(f"run_script: {run_script}")
    print(f"log: {log_path}")
    print(f"stats_report: {run_dir / 'hallucination_report.md'}")
    print(f"public_stats_report: {public_report_dir / 'hallucination_report.md'}")
    print(f"overview_dir: {root / '_workspace' / 'overview'}")
    print(f"public_overview_dir: {public_overview_dir}")

    if args.dry_run:
        print("commands:")
        for command_item in commands:
            print(" ".join(shlex.quote(part) for part in command_item))
        return 0

    env = os.environ.copy()
    env["REFCHECKER_KEEP_CHECKPOINT"] = "1"
    if args.background:
        log_file = log_path.open("ab")
        process = subprocess.Popen(
            [str(run_script)],
            cwd=root,
            env=env,
            stdin=subprocess.DEVNULL,
            stdout=log_file,
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )
        print(f"started background pid: {process.pid}")
        return 0

    with log_path.open("ab") as log_file:
        return subprocess.call(
            [str(run_script)],
            cwd=root,
            env=env,
            stdout=log_file,
            stderr=subprocess.STDOUT,
        )


if __name__ == "__main__":
    sys.exit(main())