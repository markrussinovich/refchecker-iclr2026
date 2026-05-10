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

    return [
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


def write_run_script(run_dir: Path, refchecker: Path, command: list[str]) -> Path:
    script_path = run_dir / "run_full.sh"
    command_line = " \\\n  ".join(shlex.quote(part) for part in command)
    body = "\n".join(
        [
            "#!/usr/bin/env bash",
            "set -euo pipefail",
            "",
            "export REFCHECKER_KEEP_CHECKPOINT=1",
            f"cd {shlex.quote(str(refchecker))}",
            command_line,
            "",
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
    parser.add_argument("--background", "--detach", action="store_true", help="Start the scan in a detached background process.")
    parser.add_argument("--dry-run", action="store_true", help="Print the resolved command without running it.")
    args = parser.parse_args()

    root = args.root.resolve()
    conference, year = parse_conference_and_year(args.conference, args.year)
    paper_list = root / "conferences" / conference / year / f"{conference}-{year}-accepted.txt"
    if not paper_list.exists():
        raise SystemExit(f"Paper list not found: {paper_list}")

    run_dir = root / "_workspace" / f"{conference}{year}"
    for subdir in ("fresh_cache", "logs", "results"):
        (run_dir / subdir).mkdir(parents=True, exist_ok=True)

    command = build_command(args, paper_list, run_dir)
    run_script = write_run_script(run_dir, args.refchecker.resolve(), command)
    log_path = run_dir / "logs" / "run.log"

    print(f"conference: {conference}")
    print(f"year: {year}")
    print(f"paper_list: {paper_list}")
    print(f"run_dir: {run_dir}")
    print(f"run_script: {run_script}")
    print(f"log: {log_path}")

    if args.dry_run:
        print("command:")
        print(" ".join(shlex.quote(part) for part in command))
        return 0

    env = os.environ.copy()
    env["REFCHECKER_KEEP_CHECKPOINT"] = "1"
    if args.background:
        log_file = log_path.open("ab")
        process = subprocess.Popen(
            command,
            cwd=args.refchecker,
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
            command,
            cwd=args.refchecker,
            env=env,
            stdout=log_file,
            stderr=subprocess.STDOUT,
        )


if __name__ == "__main__":
    sys.exit(main())