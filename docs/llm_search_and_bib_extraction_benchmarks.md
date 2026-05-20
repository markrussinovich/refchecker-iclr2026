# LLM Search and Bibliography Extraction Benchmarks

Date: 2026-04-27

This note summarizes two seven-paper benchmark experiments run from the RefChecker `hallucref` branch against high-search ICLR 2026 papers:

1. Hallucination adjudication with grounded/web-search LLMs.
2. Bibliography extraction model comparison.

The benchmark paper list was:

- `https://openreview.net/forum?id=6wDp8XRmNI`
- `https://openreview.net/forum?id=xxsacQ3tdb`
- `https://openreview.net/forum?id=RqwEzZqMFv`
- `https://openreview.net/forum?id=9ZogcRkhoG`
- `https://openreview.net/forum?id=gjvTNxVd2f`
- `https://openreview.net/forum?id=owZ6KNAtYU`
- `https://openreview.net/forum?id=w025bYRVkO`

All runs used `--max-workers 6` and the local Semantic Scholar database at `/datadrive/refcheckercache/db`.

## Experiment 1: Hallucination Search Model

### Goal

Compare Gemini grounded search against Anthropic web search for hallucination adjudication, while keeping bibliography extraction fixed to Gemini. This isolates the LLM+search adjudication behavior after references have already been extracted.

### Configurations

| Label | Bibliography extraction | Hallucination/search model | Output report |
|---|---|---|---|
| Gemini | `google/gemini-3.1-flash-lite-preview` | `google/gemini-3.1-flash-lite-preview` | `bench_runs/gemini31_report.json` |
| Haiku | `google/gemini-3.1-flash-lite-preview` | `anthropic/claude-haiku-4-5` | `bench_runs/haiku45_report.json` |
| Sonnet | `google/gemini-3.1-flash-lite-preview` | `anthropic/claude-sonnet-4-6` | `bench_runs/sonnet46_report.json` |

The three runs shared an isolated benchmark cache at `/datadrive/refchecker-neurips/data/iclr2026/bench_cache`. The shared cache is acceptable here because bibliography extraction is intentionally fixed to Gemini; LLM response cache keys include model name.

### Results

| Search model | Wall time | References processed | Assessment calls | Likely hallucinated | Uncertain | Unlikely | Unverified refs | Flagged records | Flagged papers |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Gemini 3.1 Flash Lite | 197.82s | 741 | 76 | 8 | 10 | 58 | 19 | 8 | 5 |
| Claude Haiku 4.5 | 157.31s | 741 | 76 | 8 | 1 | 67 | 9 | 8 | 4 |
| Claude Sonnet 4.6 | 210.26s | 741 | 76 | 5 | 2 | 69 | 7 | 5 | 2 |

No run showed `Traceback`, `429`, `too_many_requests`, `rate limit`, or `overloaded` markers in the logs.

### Interpretation

Haiku was the fastest adjudication backend on this set, about 20 percent faster than Gemini. Sonnet was the slowest of the three, about 6 percent slower than Gemini and 34 percent slower than Haiku.

The Anthropic models were less likely than Gemini to return uncertain/unverified outcomes. Gemini produced 10 uncertain verdicts and 19 unverified refs, while Haiku produced 1 uncertain verdict and 9 unverified refs, and Sonnet produced 2 uncertain verdicts and 7 unverified refs. Sonnet was also more conservative about labeling references as likely hallucinated, with 5 likely verdicts versus 8 for Gemini and Haiku.

Operationally, Haiku looks like the best first Anthropic alternative for search adjudication because it was fastest and produced fewer uncertain outcomes than Gemini in this run. Sonnet may be useful as a spot-check or escalation model, but it did not justify its extra latency as the default adjudicator on this sample.

### Cost Notes

The benchmark artifacts record wall time, verdicts, cached response text, and web URLs, but they do not record token usage. That means exact API spend cannot be reconstructed from these outputs alone.

Measured request volume for this seven-paper hallucination-search benchmark was 76 LLM+search adjudications per model. For planning purposes:

- Gemini grounded-search cost is proportional to 76 Gemini calls plus any grounding/search pricing that applies to the account and model.
- Anthropic cost is proportional to 76 Messages API calls, prompt/output tokens, and any Anthropic web-search tool pricing or web-search result charges that apply.
- Earlier analysis of the first 500 ICLR 2026 papers found 1,437 actual hallucination/search assessments across 424 papers, so multiply the per-call provider pricing by about 1,437 for that batch, then add token costs.

To make future cost comparisons exact, RefChecker should persist response usage metadata from provider responses, including prompt tokens, completion tokens, cache-read/cache-write tokens, and any tool/search charges exposed by the provider SDK.

## Experiment 2: Bibliography Extraction Model

### Goal

Compare Gemini, Haiku, and Sonnet as bibliography extraction models on the same seven papers, measuring both extraction speed and output quality. To isolate extraction quality, hallucination adjudication was fixed to Gemini for all three runs.

### Configurations

| Label | Bibliography extraction model | Hallucination/search model | Cache |
|---|---|---|---|
| Gemini | `google/gemini-3.1-flash-lite-preview` | `google/gemini-3.1-flash-lite-preview` | `bench_bib_cache/gemini31` |
| Haiku | `anthropic/claude-haiku-4-5` | `google/gemini-3.1-flash-lite-preview` | `bench_bib_cache/haiku45` |
| Sonnet | `anthropic/claude-sonnet-4-6` | `google/gemini-3.1-flash-lite-preview` | `bench_bib_cache/sonnet46` |

Separate bibliography caches were required because bibliography caches are keyed by paper input, not by model. Sharing a bibliography cache would have made the extraction comparison invalid. All three runs produced seven bibliography cache files.

### Overall Results

| Extraction model | Wall time | Extracted refs | Records written | Errors | Warnings | Info | Unverified refs | Flagged records | Flagged papers | LLM cache entries |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Gemini 3.1 Flash Lite | 116.79s | 741 | 438 | 60 | 161 | 281 | 14 | 7 | 3 | 102 |
| Claude Haiku 4.5 | 223.42s | 736 | 416 | 42 | 155 | 284 | 6 | 6 | 5 | 90 |
| Claude Sonnet 4.6 | 400.71s | 740 | 432 | 50 | 163 | 286 | 13 | 7 | 3 | 94 |

No run showed `Traceback`, `429`, `too_many_requests`, `rate limit`, or `overloaded` markers in the logs.

### Per-Paper Extraction Time

| Paper | Gemini | Haiku | Sonnet |
|---|---:|---:|---:|
| `owZ6KNAtYU` | 126 refs, 15.6s | 126 refs, 33.5s | 126 refs, 52.5s |
| `6wDp8XRmNI` | 74 refs, 37.5s | 74 refs, 104.9s | 76 refs, 142.2s |
| `xxsacQ3tdb` | 91 refs, 32.3s | 89 refs, 91.3s | 89 refs, 174.5s |
| `gjvTNxVd2f` | 104 refs, 42.6s | 103 refs, 120.6s | 103 refs, 195.3s |
| `RqwEzZqMFv` | 75 refs, 60.1s | 73 refs, 142.0s | 75 refs, 238.1s |
| `9ZogcRkhoG` | 72 refs, 65.0s | 72 refs, 157.0s | 72 refs, 269.0s |
| `w025bYRVkO` | 199 refs, 53.9s | 199 refs, 177.6s | 199 refs, 311.5s |

### Title Overlap Against Gemini

This comparison normalizes extracted reference titles and treats Gemini as the baseline because Gemini was the existing extraction model.

| Model | Common with Gemini | Missing vs Gemini | Extra vs Gemini |
|---|---:|---:|---:|
| Haiku | 712 | 29 | 24 |
| Sonnet | 719 | 22 | 21 |

Most differences were title normalization or formatting differences rather than obvious semantic misses. Examples include smart quotes, `p k a` versus `pka`, `LLaV A-Med` versus `LLaVA-Med`, `W APITI` versus `WAPITI`, and spacing in license titles.

### Interpretation

Gemini was the clear speed winner for bibliography extraction. Haiku was about 1.9x slower than Gemini, and Sonnet was about 3.4x slower than Gemini. Sonnet was also about 1.8x slower than Haiku.

Extraction quality was broadly similar. Sonnet tracked Gemini slightly more closely than Haiku by normalized-title overlap: 719 common titles versus Haiku's 712, with fewer missing and extra titles. However, Sonnet's quality gain over Haiku was small relative to the latency cost.

Haiku produced fewer downstream errors and unverified refs, but this should not be read as strictly better extraction without manual review. It extracted fewer total references and wrote fewer records, so some reduction in downstream findings may come from omission or normalization differences rather than improved correctness.

## Recommendations

For hallucination/search adjudication, use Haiku as the primary Anthropic alternative to Gemini when the goal is lower latency and fewer uncertain outcomes. Keep Sonnet available for selective escalation or audit cases, not as the default search adjudicator.

For bibliography extraction, keep Gemini as the default. It was much faster and extracted the most references. Haiku is the practical Anthropic fallback when Gemini extraction is unavailable or throttled. Sonnet was slightly closer to Gemini by title overlap, but its latency is hard to justify for bulk extraction.

For cost/performance decisions at 500-paper scale, prioritize reducing the number of hallucination-search adjudications, because those are the calls most exposed to external search-tool throttling and pricing. The first-500-paper analysis found 1,437 actual hallucination/search assessments across 424 papers. Even small changes in adjudication rate or provider search pricing can dominate the marginal cost of a large run.

## Reproducibility Artifacts

Input list:

- `/datadrive/refchecker-neurips/data/iclr2026/bench_high_search_papers.txt`

Hallucination-search benchmark artifacts:

- `/datadrive/refchecker-neurips/data/iclr2026/bench_runs/gemini31_report.json`
- `/datadrive/refchecker-neurips/data/iclr2026/bench_runs/haiku45_report.json`
- `/datadrive/refchecker-neurips/data/iclr2026/bench_runs/sonnet46_report.json`
- `/datadrive/refchecker-neurips/data/iclr2026/bench_runs/gemini31.log`
- `/datadrive/refchecker-neurips/data/iclr2026/bench_runs/haiku45.log`
- `/datadrive/refchecker-neurips/data/iclr2026/bench_runs/sonnet46.log`

Bibliography extraction benchmark artifacts:

- `/datadrive/refchecker-neurips/data/iclr2026/bench_bib_runs/gemini31_bib_report.json`
- `/datadrive/refchecker-neurips/data/iclr2026/bench_bib_runs/haiku45_bib_report.json`
- `/datadrive/refchecker-neurips/data/iclr2026/bench_bib_runs/sonnet46_bib_report.json`
- `/datadrive/refchecker-neurips/data/iclr2026/bench_bib_runs/gemini31_bib.log`
- `/datadrive/refchecker-neurips/data/iclr2026/bench_bib_runs/haiku45_bib.log`
- `/datadrive/refchecker-neurips/data/iclr2026/bench_bib_runs/sonnet46_bib.log`
- `/datadrive/refchecker-neurips/data/iclr2026/bench_bib_cache/gemini31`
- `/datadrive/refchecker-neurips/data/iclr2026/bench_bib_cache/haiku45`
- `/datadrive/refchecker-neurips/data/iclr2026/bench_bib_cache/sonnet46`

## Caveats

This is a seven-paper targeted benchmark selected from high-search papers, not a random sample of the full ICLR 2026 set. Results should be treated as directional for provider choice and pipeline behavior.

The quality comparison uses downstream RefChecker findings and normalized-title overlap. It is useful for finding extraction differences, but it is not a full human-labeled precision/recall evaluation.

Exact dollar costs were not computed because the cache artifacts do not preserve token usage or provider-specific search billing metadata. Future runs should persist provider usage fields to enable exact cost accounting.
