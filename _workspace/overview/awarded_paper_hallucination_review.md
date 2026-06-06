# Review of Awarded-Paper Hallucinated Reference Flags

Generated from `_workspace/overview/awarded_paper_hallucinated_references.json` on 2026-06-06.

## Review Standard

I treated a scan flag as a **TP** when the cited reference appears materially fabricated or conflated: a non-existent title/source, a title grafted onto the wrong work, a fake URL/source, or a substantially fabricated author attribution. I treated it as **FP** when the intended source is real and the issue is better explained as citation formatting, incomplete metadata, editor/coauthor ambiguity, source-type mismatch, or a recoverable bibliographic error rather than a hallucinated reference. Per follow-up policy, I also mark references as **FP** when they are websites/webpages, references to code files or code artifacts, newspaper articles, works prior to 1970, or otherwise-correct references that omit a single author. A later evidence pass also marks specific references as **FP** when the user supplied a verifying source or identified a parsing/extraction/metadata issue.

## Totals

| Metric | Count |
|---|---:|
| Awarded papers reviewed | 56 |
| References reviewed | 70 |
| References reclassified as FP by follow-up policy | 29 |
| References additionally reclassified as FP by supplied evidence | 14 |
| TP references | 11 |
| FP references | 59 |
| TP reference rate | 15.7% |
| FP reference rate | 84.3% |
| Papers with at least one TP | 11 |
| Papers with at least one FP | 45 |

## Top-Level Review Table

<p><strong>Row colors:</strong> <span style="background-color: #fff4f4; color: #111827; padding: 0.1em 0.4em; border-left: 6px solid #b91c1c; border-top: 1px solid #fca5a5; border-bottom: 1px solid #fca5a5; border-right: 1px solid #fca5a5;">TP</span> true positive; <span style="background-color: #f0fff4; color: #111827; padding: 0.1em 0.4em; border-left: 6px solid #15803d; border-top: 1px solid #86efac; border-bottom: 1px solid #86efac; border-right: 1px solid #86efac;">FP</span> false positive.</p>

<table style="border-collapse: collapse; width: 100%; font-size: 0.95em;">
  <thead>
    <tr style="background-color: #1f2937; color: #ffffff;">
      <th style="padding: 0.55em 0.7em; border: 1px solid #9ca3af; text-align: left; color: #ffffff;">#</th>
      <th style="padding: 0.55em 0.7em; border: 1px solid #9ca3af; text-align: left; color: #ffffff;">Conference/Year</th>
      <th style="padding: 0.55em 0.7em; border: 1px solid #9ca3af; text-align: left; color: #ffffff;">Award</th>
      <th style="padding: 0.55em 0.7em; border: 1px solid #9ca3af; text-align: left; color: #ffffff;">Paper</th>
      <th style="padding: 0.55em 0.7em; border: 1px solid #9ca3af; text-align: left; color: #ffffff;">Reference</th>
      <th style="padding: 0.55em 0.7em; border: 1px solid #9ca3af; text-align: left; color: #ffffff;">FP/TP</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">1</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">ICLR 2023</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Outstanding Paper</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://openreview.net/forum?id=lTt4KjHSsyl" style="color: #075985; font-weight: 600; text-decoration: underline;">Emergence of Maps in the Memories of Blind Navigation Agents</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-1" style="color: #075985; font-weight: 600; text-decoration: underline;">Cognitive maps in wolves and men</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">2</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">ICLR 2023</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Outstanding Paper</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://openreview.net/forum?id=88nT0j5jAn" style="color: #075985; font-weight: 600; text-decoration: underline;">Universal Few-shot Learning of Dense Prediction Tasks with Visual Token Matching</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-2" style="color: #075985; font-weight: 600; text-decoration: underline;">Bert: Pre-training of deep bidirectional transformers for language understanding</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">3</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">ICLR 2024</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Honorable Mention</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://openreview.net/forum?id=g7ohDlTITL" style="color: #075985; font-weight: 600; text-decoration: underline;">Flow Matching on General Geometries</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-3" style="color: #075985; font-weight: 600; text-decoration: underline;">Python reference manual</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #fff4f4; color: #111827; border-left: 6px solid #b91c1c;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">4</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">ICLR 2024</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Outstanding Paper</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://openreview.net/forum?id=sFyTZEqmUY" style="color: #075985; font-weight: 600; text-decoration: underline;">Learning Interactive Real-World Simulators</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-4" style="color: #075985; font-weight: 600; text-decoration: underline;">Adaptive control of linear time-invariant systems</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #7f1d1d; background-color: #fecaca; border: 1px solid #dc2626; border-radius: 4px; padding: 0.1em 0.35em;">TP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">5</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">ICLR 2025</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Honorable Mention</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://openreview.net/forum?id=HD6bWcj87Y" style="color: #075985; font-weight: 600; text-decoration: underline;">Data Shapley in One Training Run</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-5" style="color: #075985; font-weight: 600; text-decoration: underline;">Valuation with weighted banzhaf values</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #fff4f4; color: #111827; border-left: 6px solid #b91c1c;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">6</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">ICML 2022</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Outstanding Paper</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://proceedings.mlr.press/v162/lotfi22a/lotfi22a.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Bayesian Model Selection, the Marginal Likelihood, and Generalization</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-6" style="color: #075985; font-weight: 600; text-decoration: underline;">Inference, method, and decision: Towards a bayesian philosophy of science</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #7f1d1d; background-color: #fecaca; border: 1px solid #dc2626; border-radius: 4px; padding: 0.1em 0.35em;">TP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">7</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">ICML 2022</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Outstanding Paper</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://proceedings.mlr.press/v162/suh22b/suh22b.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Do Differentiable Simulators Give Better Policy Gradients?</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-7" style="color: #075985; font-weight: 600; text-decoration: underline;">Principles of mathematical analysis, volume 3</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #fff4f4; color: #111827; border-left: 6px solid #b91c1c;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">8</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">ICML 2022</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Outstanding Paper</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://proceedings.mlr.press/v162/chen22t/chen22t.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Learning Mixtures of Linear Dynamical Systems</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-8" style="color: #075985; font-weight: 600; text-decoration: underline;">Robust and Optimal Control</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #7f1d1d; background-color: #fecaca; border: 1px solid #dc2626; border-radius: 4px; padding: 0.1em 0.35em;">TP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">9</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">ICML 2022</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Outstanding Paper Runner Up</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://proceedings.mlr.press/v162/yan22c/yan22c.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Active fairness auditing</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-9" style="color: #075985; font-weight: 600; text-decoration: underline;">Towards efﬁcient evaluation of risk via herding</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #fff4f4; color: #111827; border-left: 6px solid #b91c1c;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">10</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">ICML 2022</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Outstanding Paper Runner Up</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://proceedings.mlr.press/v162/hsu22a/hsu22a.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Learning inverse folding from millions of predicted structures</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-10" style="color: #075985; font-weight: 600; text-decoration: underline;">Unified rational protein engineering Learning inverse folding from millions of predicted structures with sequence-based deep representation learning</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #7f1d1d; background-color: #fecaca; border: 1px solid #dc2626; border-radius: 4px; padding: 0.1em 0.35em;">TP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">11</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">ICML 2022</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Outstanding Paper Runner Up</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://proceedings.mlr.press/v162/akbari22a/akbari22a.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Minimum Cost Intervention Design for Causal Effect Identification</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-11" style="color: #075985; font-weight: 600; text-decoration: underline;">Models, reasoning and inference</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">12</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">ICML 2023</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Outstanding Paper</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://proceedings.mlr.press/v202/defazio23a/defazio23a.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Learning-Rate-Free Learning by D-Adaptation</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-12" style="color: #075985; font-weight: 600; text-decoration: underline;">Gradient descent: The ultimate optimizer</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">13</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">ICML 2024</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Best Paper</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://openreview.net/forum?id=iLCZtl7FTa" style="color: #075985; font-weight: 600; text-decoration: underline;">Debating with More Persuasive LLMs Leads to More Truthful Answers</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-13" style="color: #075985; font-weight: 600; text-decoration: underline;">Debate update: Obfuscated arguments problem</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">14</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">ICML 2024</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Best Paper</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://openreview.net/forum?id=CyEJn71Z00" style="color: #075985; font-weight: 600; text-decoration: underline;">Information Complexity of Stochastic Convex Optimization: Applications to Generalization, Memorization, and Tracing</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-14" style="color: #075985; font-weight: 600; text-decoration: underline;">Understanding Generalization via Leave-One-Out Conditional Mutual Information</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #fff4f4; color: #111827; border-left: 6px solid #b91c1c;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">15</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">ICML 2024</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Best Paper</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://openreview.net/forum?id=ncjhi4qAPV" style="color: #075985; font-weight: 600; text-decoration: underline;">Position: Considerations for Differentially Private Learning with Large-Scale Public Pretraining</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-15" style="color: #075985; font-weight: 600; text-decoration: underline;">Prochlo: Strong privacy for analytics in the wild</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #7f1d1d; background-color: #fecaca; border: 1px solid #dc2626; border-radius: 4px; padding: 0.1em 0.35em;">TP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">16</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">ICML 2024</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Best Paper</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://openreview.net/forum?id=jsKr6RVDDs" style="color: #075985; font-weight: 600; text-decoration: underline;">Position: Measure Dataset Diversity, Don&#x27;t Just Claim It</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-16" style="color: #075985; font-weight: 600; text-decoration: underline;">An american puzzle: Fitting race in a box</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #fff4f4; color: #111827; border-left: 6px solid #b91c1c;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">17</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">ICML 2025</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Outstanding Paper</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://openreview.net/forum?id=DmH4HHVb3y" style="color: #075985; font-weight: 600; text-decoration: underline;">CollabLLM: From Passive Responders to Active Collaborators</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-17" style="color: #075985; font-weight: 600; text-decoration: underline;">Rethinking conversational agents in the era of llms: Proactivity, non-collaborativity, and beyond</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #7f1d1d; background-color: #fecaca; border: 1px solid #dc2626; border-radius: 4px; padding: 0.1em 0.35em;">TP</strong></td>
    </tr>
    <tr style="background-color: #fff4f4; color: #111827; border-left: 6px solid #b91c1c;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">18</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">ICML 2025</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Outstanding Paper</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://openreview.net/forum?id=PNmkjIzHB7" style="color: #075985; font-weight: 600; text-decoration: underline;">Conformal Prediction as Bayesian Quadrature</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-18" style="color: #075985; font-weight: 600; text-decoration: underline;">de Finetti’s theorem, induction, and An or Bayesian nonparametric predictive inference (with discussion)</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #7f1d1d; background-color: #fecaca; border: 1px solid #dc2626; border-radius: 4px; padding: 0.1em 0.35em;">TP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">19</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">NEURIPS 2021</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Outstanding Paper</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://papers.nips.cc/paper_files/paper/2021/file/ec26fc2eb2b75aece19c70392dc744c2-Paper.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Continuized Accelerations of Deterministic and Stochastic Gradient Descents, and of Gossip Algorithms</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-19" style="color: #075985; font-weight: 600; text-decoration: underline;">A method of solving a convex programming problem with convergence rate O(1/k2)</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #fff4f4; color: #111827; border-left: 6px solid #b91c1c;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">20</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">NEURIPS 2021</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Outstanding Paper</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://papers.nips.cc/paper_files/paper/2021/file/4079016d940210b4ae9ae7d41c4a2065-Paper.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">On the Expressivity of Markov Reward</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-20" style="color: #075985; font-weight: 600; text-decoration: underline;">On separating agent designer goals from agent goals: Breaking the preferences–parameters confound</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #7f1d1d; background-color: #fecaca; border: 1px solid #dc2626; border-radius: 4px; padding: 0.1em 0.35em;">TP</strong></td>
    </tr>
    <tr style="background-color: #fff4f4; color: #111827; border-left: 6px solid #b91c1c;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">21</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">NEURIPS 2022</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Outstanding Paper</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://proceedings.neurips.cc/paper_files/paper/2022/file/a46156bd3579c3b268108ea6aca71d13-Paper-Conference.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">A Neural Corpus Indexer for Document Retrieval</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-21" style="color: #075985; font-weight: 600; text-decoration: underline;">From doc2query to doctttttquery</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #7f1d1d; background-color: #fecaca; border: 1px solid #dc2626; border-radius: 4px; padding: 0.1em 0.35em;">TP</strong></td>
    </tr>
    <tr style="background-color: #fff4f4; color: #111827; border-left: 6px solid #b91c1c;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">22</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">NEURIPS 2022</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Outstanding Paper</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://proceedings.neurips.cc/paper_files/paper/2022/file/c1e2faff6f588870935f114ebe04a3e5-Paper-Conference.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">An empirical analysis of compute-optimal large language model training</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-22" style="color: #075985; font-weight: 600; text-decoration: underline;">Compressive transformers for long-range sequence modelling</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #7f1d1d; background-color: #fecaca; border: 1px solid #dc2626; border-radius: 4px; padding: 0.1em 0.35em;">TP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">23</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">NEURIPS 2022</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Outstanding Paper</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://proceedings.neurips.cc/paper_files/paper/2022/file/a98846e9d9cc01cfb87eb694d946ce6b-Paper-Conference.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Elucidating the Design Space of Diffusion-Based Generative Models</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-23" style="color: #075985; font-weight: 600; text-decoration: underline;">Théorie analytique de la chaleur</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">24</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">NEURIPS 2022</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Outstanding Paper</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://proceedings.neurips.cc/paper_files/paper/2022/file/a98846e9d9cc01cfb87eb694d946ce6b-Paper-Conference.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Elucidating the Design Space of Diffusion-Based Generative Models</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-24" style="color: #075985; font-weight: 600; text-decoration: underline;">Learning multiple layers of features from tiny images</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">25</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">NEURIPS 2022</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Outstanding Paper</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://proceedings.neurips.cc/paper_files/paper/2022/file/f0e91b1314fa5eabf1d7ef6d1561ecec-Paper-Conference.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Is Out-of-Distribution Detection Learnable?</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-25" style="color: #075985; font-weight: 600; text-decoration: underline;">Convolutional deep belief networks on cifar-10</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">26</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">NEURIPS 2022</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Outstanding Paper</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://proceedings.neurips.cc/paper_files/paper/2022/file/74a67268c5cc5910f64938cac4526a90-Paper-Datasets_and_Benchmarks.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">MineDojo: Building Open-Ended Embodied Agents with Internet-Scale Knowledge</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-26" style="color: #075985; font-weight: 600; text-decoration: underline;">Embodied reasoning through planning with language models</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">27</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">NEURIPS 2022</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Outstanding Paper</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://proceedings.neurips.cc/paper_files/paper/2022/file/02917acec264a52a729b99d9bc857909-Paper-Conference.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">On-Demand Sampling: Learning Optimally from Multiple Distributions</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-27" style="color: #075985; font-weight: 600; text-decoration: underline;">Information-theoretic lower bounds of PAC sample complexity</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">28</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">NEURIPS 2022</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Outstanding Paper</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://proceedings.neurips.cc/paper_files/paper/2022/file/0113ef4642264adc2e6924a3cbbdf532-Paper-Conference.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Using natural language and program abstractions to instill human inductive biases in machines</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-28" style="color: #075985; font-weight: 600; text-decoration: underline;">What makes us smart? core knowledge and natural language</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">29</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">NEURIPS 2022</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Outstanding Paper</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://proceedings.neurips.cc/paper_files/paper/2022/file/27c546ab1e4f1d7d638e6a8dfbad9a07-Paper-Conference.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">🏘️ ProcTHOR: Large-Scale Embodied AI Using Procedural Generation</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-29" style="color: #075985; font-weight: 600; text-decoration: underline;">Openai gym</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">30</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">NEURIPS 2023</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Outstanding Paper</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://proceedings.neurips.cc/paper_files/paper/2023/file/adc98a266f45005c403b8311ca7e8bd7-Paper-Conference.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Are Emergent Abilities of Large Language Models a Mirage?</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-30" style="color: #075985; font-weight: 600; text-decoration: underline;">Refining the sharp left turn threat model, part 2: applying alignment techniques</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">31</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">NEURIPS 2023</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Outstanding Paper</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://proceedings.neurips.cc/paper_files/paper/2023/file/adc98a266f45005c403b8311ca7e8bd7-Paper-Conference.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Are Emergent Abilities of Large Language Models a Mirage?</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-31" style="color: #075985; font-weight: 600; text-decoration: underline;">Aligning language models to follow instructions</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">32</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">NEURIPS 2025</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Best Paper</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://openreview.net/forum?id=s0JVsx3bx1" style="color: #075985; font-weight: 600; text-decoration: underline;">1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-32" style="color: #075985; font-weight: 600; text-decoration: underline;">Improving language understanding by generative pre-training</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">33</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">NEURIPS 2025</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Best Paper</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://openreview.net/forum?id=BSZqpqgqM0" style="color: #075985; font-weight: 600; text-decoration: underline;">Why Diffusion Models Don’t Memorize:  The Role of Implicit Dynamical Regularization in Training</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-33" style="color: #075985; font-weight: 600; text-decoration: underline;">An analytical theory of power law spectral bias in the learning dynamics of diffusion models</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">34</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">NEURIPS 2025</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Best Paper Runner-up</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://openreview.net/forum?id=knPz7gtjPW" style="color: #075985; font-weight: 600; text-decoration: underline;">Superposition Yields Robust Neural Scaling</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-34" style="color: #075985; font-weight: 600; text-decoration: underline;">Wolfram|alpha as the computation engine for gpt models</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">35</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2021</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/sec21-ragab.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Rage Against the Machine Clear: A Systematic Analysis of Machine Clears and Their Implications for Transient Execution Attacks</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-35" style="color: #075985; font-weight: 600; text-decoration: underline;">Return after free discussion</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">36</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2021</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/sec21-ragab.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Rage Against the Machine Clear: A Systematic Analysis of Machine Clears and Their Implications for Transient Execution Attacks</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-36" style="color: #075985; font-weight: 600; text-decoration: underline;">block_speculation function call in invoke_stub</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">37</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2021</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/sec21-ragab.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Rage Against the Machine Clear: A Systematic Analysis of Machine Clears and Their Implications for Transient Execution Attacks</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-37" style="color: #075985; font-weight: 600; text-decoration: underline;">block_speculation function call in io_emul_stub_setup</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">38</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2021</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/sec21-ragab.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Rage Against the Machine Clear: A Systematic Analysis of Machine Clears and Their Implications for Transient Execution Attacks</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-38" style="color: #075985; font-weight: 600; text-decoration: underline;">Intel deep-dive: snoop-assisted L1 Data Sampling</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">39</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2021</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner and Third Prize winner of the 2021 Internet Defense Prize</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/sec21-bock.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Weaponizing Middleboxes for TCP Reflected Amplification</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-39" style="color: #075985; font-weight: 600; text-decoration: underline;">The Eavesdropper’s Dilemma</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">40</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2021</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/sec21-mcdonald.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">“It’s stressful having all these phones”:</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-40" style="color: #075985; font-weight: 600; text-decoration: underline;">North American, Western and Central Europe: AIDS epidemic update regional summary</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">41</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2021</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/sec21-consolvo.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">“Why wouldn’t someone think of democracy as a target?”: Security practices &amp; challenges of people involved with U.S. political campaigns</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-41" style="color: #075985; font-weight: 600; text-decoration: underline;">2020 Campaigns Remain Vulnerable as Signs of Russian Hackers Re-Emerge</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">42</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2022</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/sec22-arp.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Dos and Don’ts of Machine Learning in Computer Security</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-42" style="color: #075985; font-weight: 600; text-decoration: underline;">Borderline-smote: A new over-sampling method in imbalanced data sets learning</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">43</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2022</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/sec22-hoang.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Faster Yet Safer: Logging System Via Fixed-Key Blockcipher</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-43" style="color: #075985; font-weight: 600; text-decoration: underline;">Worldwide Security and Information Event Management Market Shares, 2020: SaaS-Focused Rise</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">44</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2022</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/sec22-hoang.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Faster Yet Safer: Logging System Via Fixed-Key Blockcipher</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-44" style="color: #075985; font-weight: 600; text-decoration: underline;">Reproducibility by Ontological representation of Provenance</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">45</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2022</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/sec22-zhang-zenong.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">FixReverter: A Realistic Bug Injection Methodology for Benchmarking Fuzz Testing</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-45" style="color: #075985; font-weight: 600; text-decoration: underline;">Elkhound: A fast, practical glr parser generator</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">46</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2022</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/sec22-madathil.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Private Signaling</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-46" style="color: #075985; font-weight: 600; text-decoration: underline;">Discreet log</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">47</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2022</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner and Second Prize Winner (tie) of the 2022 Internet Defense Prize</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/sec22-bosamiya.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Provably-Safe Multilingual Software Sandboxing using WebAssembly</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-47" style="color: #075985; font-weight: 600; text-decoration: underline;">Position paper: Bringing memory safety to WebAssembly</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">48</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2022</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/sec22-halderman.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">The Antrim County 2020 Election Incident: An Independent Forensic Investigation</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-48" style="color: #075985; font-weight: 600; text-decoration: underline;">Democracy Suite EMS Results Tally &amp; Reporting user guide, version 5.5::16</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">49</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2023</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/usenixsecurity23-choi.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">BotScreen: Trust Everybody, but Cut the Aimbots Yourself</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-49" style="color: #075985; font-weight: 600; text-decoration: underline;">Project infinity</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">50</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2023</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/usenixsecurity23-albayaydh.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Examining Power Dynamics and User Privacy in Smart Technology Use Among Jordanian Households</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-50" style="color: #075985; font-weight: 600; text-decoration: underline;">Cyber Crimes in Jordan: A Legal Assessment on the Effectiveness of Information System Crimes Law No (30) of</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">51</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2023</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/usenixsecurity23-albayaydh.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Examining Power Dynamics and User Privacy in Smart Technology Use Among Jordanian Households</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-51" style="color: #075985; font-weight: 600; text-decoration: underline;">New Data Protection Bill, Draft</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">52</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2023</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/usenixsecurity23-albayaydh.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Examining Power Dynamics and User Privacy in Smart Technology Use Among Jordanian Households</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-52" style="color: #075985; font-weight: 600; text-decoration: underline;">JORDANIAN PEOPLE PERSPECTIVE ABOUT SMART HOMES</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">53</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2023</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner and Co-Winner of the 2023 Internet Defense Prize</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/usenixsecurity23-shan.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Glaze: Protecting Artists from Style Mimicry by Text-to-Image Models</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-53" style="color: #075985; font-weight: 600; text-decoration: underline;">What does the rise of AI mean for the future of art?</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">54</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2023</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner and Co-Winner of the 2023 Internet Defense Prize</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/usenixsecurity23-shan.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Glaze: Protecting Artists from Style Mimicry by Text-to-Image Models</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-54" style="color: #075985; font-weight: 600; text-decoration: underline;">AI art &amp; the ethical concerns of artists</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">55</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2023</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/usenixsecurity23-cheval.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Hash Gone Bad: Automated discovery of protocol attacks that exploit hash function weaknesses</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-55" style="color: #075985; font-weight: 600; text-decoration: underline;">Long version of this paper</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">56</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2024</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/usenixsecurity24-kirchner.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Dancer in the Dark: Synthesizing and Evaluating Polyglots for Blind Cross-Site Scripting</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-56" style="color: #075985; font-weight: 600; text-decoration: underline;">Artificial intelligence a modern approach</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">57</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2024</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/usenixsecurity24-ablove.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Digital Discrimination of Users in Sanctioned States: The Case of the Cuba Embargo</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-57" style="color: #075985; font-weight: 600; text-decoration: underline;">Empresa de telecomunicaciones de cuba s.a</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">58</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2024</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/usenixsecurity24-ablove.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Digital Discrimination of Users in Sanctioned States: The Case of the Cuba Embargo</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-58" style="color: #075985; font-weight: 600; text-decoration: underline;">Iran, Social Media, and U.S. Trade Sanctions: The First Amendment Implications of U.S. Foreign Policy</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">59</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2024</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/usenixsecurity24-ablove.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Digital Discrimination of Users in Sanctioned States: The Case of the Cuba Embargo</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-59" style="color: #075985; font-weight: 600; text-decoration: underline;">Letter and Report for the Congressional Record</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">60</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2024</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/usenixsecurity24-zhang-jipeng.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">ENG25519: Faster TLS 1.3 handshake using optimized X25519 and Ed25519</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-60" style="color: #075985; font-weight: 600; text-decoration: underline;">Artifact of the paper &quot;Batching CSIDH group actions using AVX-512</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">61</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2024</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/usenixsecurity24-zhang-jipeng.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">ENG25519: Faster TLS 1.3 handshake using optimized X25519 and Ed25519</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-61" style="color: #075985; font-weight: 600; text-decoration: underline;">Artifact of the paper &quot;Highly vectorized SIKE for AVX-512</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">62</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2024</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/usenixsecurity24-zhang-jipeng.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">ENG25519: Faster TLS 1.3 handshake using optimized X25519 and Ed25519</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-62" style="color: #075985; font-weight: 600; text-decoration: underline;">Artifact of the paper &quot;High-Throughput Elliptic Curve Cryptography Using AVX2 Vector Instructions</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">63</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2024</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/usenixsecurity24-wiebing.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">InSpectre Gadget: Inspecting the Residual Attack Surface of Cross-privilege Spectre v2</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-63" style="color: #075985; font-weight: 600; text-decoration: underline;">Cache attacks and countermeasures: the case of AES</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">64</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2024</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/usenixsecurity24-coppola.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">PURE: Payments with UWB RElay-protection</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-64" style="color: #075985; font-weight: 600; text-decoration: underline;">Chip and PIN Fraud</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">65</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2024</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/usenixsecurity24-borkar.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">WhisperFuzz: White-Box Fuzzing for Detecting and Locating Timing Vulnerabilities in Processors</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-65" style="color: #075985; font-weight: 600; text-decoration: underline;">Cascade: CPU Fuzzing via Intricate Program Generation</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">66</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2024</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/usenixsecurity24-li-shaofeng.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Yes, One-Bit-Flip Matters! Universal DNN Model Inference Depletion with Runtime Code Fault Injection</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-66" style="color: #075985; font-weight: 600; text-decoration: underline;">Apache mxnet: A flexible and efficient library for deep learning</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">67</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2024</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/usenixsecurity24-li-shaofeng.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Yes, One-Bit-Flip Matters! Universal DNN Model Inference Depletion with Runtime Code Fault Injection</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-67" style="color: #075985; font-weight: 600; text-decoration: underline;">Learning multiple layers of features from tiny images</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">68</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2025</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/usenixsecurity25-munteanu.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Catch-22: Uncovering Compromised Hosts using SSH Public Keys</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-68" style="color: #075985; font-weight: 600; text-decoration: underline;">Getting back at Trudy: SSH Botnet Member Credential Collection using Connect Back Honeypots</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #f0fff4; color: #111827; border-left: 6px solid #15803d;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">69</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2025</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/usenixsecurity25-kireev.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Characterizing and Detecting Propaganda-Spreading Accounts on Telegram</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-69" style="color: #075985; font-weight: 600; text-decoration: underline;">Amazon inference on demand</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #14532d; background-color: #bbf7d0; border: 1px solid #16a34a; border-radius: 4px; padding: 0.1em 0.35em;">FP</strong></td>
    </tr>
    <tr style="background-color: #fff4f4; color: #111827; border-left: 6px solid #b91c1c;">
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">70</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">USENIX Security 2025</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;">Distinguished Paper Award Winner</td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="https://www.usenix.org/system/files/usenixsecurity25-jiang-yuancheng.pdf" style="color: #075985; font-weight: 600; text-decoration: underline;">Fuzzing the PHP Interpreter via Dataflow Fusion</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><a href="#reference-70" style="color: #075985; font-weight: 600; text-decoration: underline;">Understanding and reusing test suites across database systems</a></td>
      <td style="padding: 0.55em 0.7em; border: 1px solid #d1d5db; vertical-align: top; color: #111827;"><strong style="display: inline-block; min-width: 2.5em; text-align: center; color: #7f1d1d; background-color: #fecaca; border: 1px solid #dc2626; border-radius: 4px; padding: 0.1em 0.35em;">TP</strong></td>
    </tr>
  </tbody>
</table>

## Detailed Reviews

<a id="reference-1"></a>
### Reference 1: Cognitive maps in wolves and men (FP)

#### Paper Metadata

- Conference: ICLR 2023
- Award/Nomination: Outstanding Paper
- Awarded paper title: Emergence of Maps in the Memories of Blind Navigation Agents
- Source paper title in scan: Emergence of Maps in the Memories of Blind Navigation Agents
- Source authors: Erik Wijmans, Manolis Savva, Irfan Essa, Stefan Lee, Ari S. Morcos, Dhruv Batra
- Source year: 2022
- Source URL: https://openreview.net/forum?id=lTt4KjHSsyl
- Scan report: _workspace/iclr2023/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Cognitive maps in wolves and men
- Cited authors: R. Peters
- Cited year: 1976
- Cited URL:
- Raw reference: R. Peters#Cognitive maps in wolves and men#Environmental design research#1976#
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The exact title \"Cognitive maps in wolves and men\" in Environmental design research (1976) could not be found. Web search identified different Peters publications with similar titles: \"Mental maps in wolves\" (1979) in The Behavior and Ecology of Wolves, and \"Communication, Cognitive Mapping, and Strategy in Wolves and Hominids\" (1978). The cited title does not appear in any search results.",
  "link": null,
  "found_title": null,
  "found_authors": null,
  "found_venue": null,
  "found_year": null,
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://link.springer.com/chapter/10.1007/978-94-009-3531-0_1",
      "https://www.sciencedirect.com/science/article/abs/pii/B978012319250950013X",
      "https://www.semanticscholar.org/paper/Communication,-Cognitive-Mapping,-and-Strategy-in-Peters/0b6261c4cfc77d66054c92ee0afbca8f72710d2c",
      "https://www.originalwisdom.com/wp-content/uploads/bsk-pdf-manager/2019/04/Peters-and-Mech_1975_Scent-marking-in-wolves.pdf",
      "https://www.sciencedirect.com/book/9780123192509/wolf-and-man"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: User-provided correction: this is a real reference in the EDRA proceedings table of contents (https://cdn.ymaws.com/www.edra.org/resource/resmgr/proceedings/toc/edra04_v1_v2_content.pdf), so the scan flag is a false positive.

<a id="reference-2"></a>
### Reference 2: Bert: Pre-training of deep bidirectional transformers for language understanding (FP)

#### Paper Metadata

- Conference: ICLR 2023
- Award/Nomination: Outstanding Paper
- Awarded paper title: Universal Few-shot Learning of Dense Prediction Tasks with Visual Token Matching
- Source paper title in scan: Universal Few-shot Learning of Dense Prediction Tasks with Visual Token Matching
- Source authors: Donggyun Kim, Jinwoo Kim, Seongwoong Cho, Chong Luo, Seunghoon Hong
- Source year: 2022
- Source URL: https://openreview.net/forum?id=88nT0j5jAn
- Scan report: _workspace/iclr2023/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Bert: Pre-training of deep bidirectional transformers for language understanding
- Cited authors: Jacob Devlin Ming-Wei Chang Kenton, Lee Kristina Toutanova
- Cited year: 2019
- Cited URL:
- Raw reference: Jacob Devlin Ming-Wei Chang Kenton*Lee Kristina Toutanova#Bert: Pre-training of deep bidirectional transformers for language understanding#Proceedings of NAACL-HLT#2019#
- Scan error type: multiple

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The cited reference contains the correct title and all four correct authors with minor formatting issues in the author field (improper name separation), and matches the 2019 NAACL publication. (Verdict corrected: the cited author list has low overlap with the verified paper, and the LLM did not provide found authors that substantially match the cited authors. A real title with fabricated coauthors is treated as hallucinated.)",
  "link": "https://aclanthology.org/N19-1423/",
  "found_title": "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
  "found_authors": "Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova",
  "found_venue": "Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies",
  "found_year": "2019",
  "source": "deep_hallucination_cache",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://arxiv.org/abs/1810.04805",
      "https://arxiv.org/pdf/1810.04805",
      "https://aclanthology.org/N19-1423/",
      "https://research.google/pubs/bert-pre-training-of-deep-bidirectional-transformers-for-language-understanding/",
      "https://sh-tsang.medium.com/review-bert-pre-training-of-deep-bidirectional-transformers-for-language-understanding-59b1684882db",
      "https://medium.com/analytics-vidhya/paper-summary-bert-pre-training-of-deep-bidirectional-transformers-for-language-understanding-861456fed1f9",
      "https://blog.paperspace.com/bert-pre-training-of-deep-bidirectional-transformers-for-language-understanding/"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: The BERT paper is real and the cited author string contains the right names, mostly mangled by missing separators; this is a formatting/year-source issue rather than a hallucinated reference.

<a id="reference-3"></a>
### Reference 3: Python reference manual (FP)

#### Paper Metadata

- Conference: ICLR 2024
- Award/Nomination: Honorable Mention
- Awarded paper title: Flow Matching on General Geometries
- Source paper title in scan: Flow Matching on General Geometries
- Source authors: Ricky T. Q. Chen, Yaron Lipman
- Source year: 2023
- Source URL: https://openreview.net/forum?id=g7ohDlTITL
- Scan report: _workspace/iclr2024/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Python reference manual
- Cited authors: Guido Van Rossum, Fred L Drake Jr
- Cited year: 1995
- Cited URL:
- Raw reference: Guido Van Rossum*Fred L Drake Jr#Python reference manual#Centrum voor Wiskunde en Informatica Amsterdam#1995
- Scan error type: multiple

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The 1995 Python Reference Manual (CWI Report CS-R9525) was authored solely by Guido van Rossum; Fred L Drake Jr. was not a co-author of the original 1995 publication but rather became editor on later versions. The cited reference fabricates Drake's authorship on the original 1995 report.",
  "link": "https://ir.cwi.nl/pub/5008",
  "found_title": "Python reference manual",
  "found_authors": "G. van Rossum (Guido)",
  "found_venue": "Centrum voor Wiskunde en Informatica (CWI)",
  "found_year": "1995",
  "source": "deep_hallucination_cache",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=09b1d693676a152621799e2cfff562a369d10204",
      "https://www.amazon.com/Python-Reference-Manual-February-Release/dp/1583483748",
      "https://ir.cwi.nl/pub/5008",
      "https://web.mit.edu/18.417/doc/pydocs/ref.pdf",
      "https://gvanrossum.github.io/Publications.html",
      "https://www.amazon.com/Python-Reference-Manual-Guido-Rossum/dp/0595136680",
      "https://dl.acm.org/doi/10.5555/869369",
      "https://dl.acm.org/doi/book/10.5555/869369",
      "https://mail.python.org/pipermail/python-list/2002-May/152619.html",
      "https://www.oalib.com/references/12583079",
      "https://dl.acm.org/doi/book/10.5555/869377",
      "https://newbe.dev/how-do-i-reference-the-python-programming-language-in-a-thesis-or-a-paper",
      "https://bcrf.biochem.wisc.edu/all-tutorials/tutorial-materials-python/python3/"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: documentation/manual-style web sources are treated as false positives under the requested rule for website references; this is bibliographic/editor metadata, not a hallucinated paper.

<a id="reference-4"></a>
### Reference 4: Adaptive control of linear time-invariant systems (TP)

#### Paper Metadata

- Conference: ICLR 2024
- Award/Nomination: Outstanding Paper
- Awarded paper title: Learning Interactive Real-World Simulators
- Source paper title in scan: Learning Interactive Real-World Simulators
- Source authors: Sherry Yang, Yilun Du, Seyed Kamyar Seyed Ghasemipour, Jonathan Tompson, Leslie Pack Kaelbling, Dale Schuurmans, Pieter Abbeel
- Source year: 2023
- Source URL: https://openreview.net/forum?id=sFyTZEqmUY
- Scan report: _workspace/iclr2024/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Adaptive control of linear time-invariant systems
- Cited authors: Karl J. Åström, Björn Wittenmark
- Cited year: 1973
- Cited URL:
- Raw reference: Karl J. Åström*Björn Wittenmark#Adaptive control of linear time-invariant systems#Automatica#1973#
- Scan error type: multiple

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The title matches a real 2021 paper by Petros A. Ioannou in the Encyclopedia of Systems and Control, but the citation attributes it to different authors (Åström and Wittenmark) with a 1973 publication date in Automatica—a clear author and metadata fabrication.",
  "link": "https://link.springer.com/10.1007/978-3-030-44184-5_111",
  "found_title": "Adaptive Control of Linear Time-Invariant Systems",
  "found_authors": "Petros A. Ioannou",
  "found_venue": "Encyclopedia of Systems and Control",
  "found_year": "2021",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://link.springer.com/10.1007/978-3-030-44184-5_111"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **TP**
- Rationale: The cited title is attached to the wrong authors, venue, and year; the scan found a different real work by Ioannou, making the Åström/Wittenmark Automatica citation materially fabricated.

<a id="reference-5"></a>
### Reference 5: Valuation with weighted banzhaf values (FP)

#### Paper Metadata

- Conference: ICLR 2025
- Award/Nomination: Honorable Mention
- Awarded paper title: Data Shapley in One Training Run
- Source paper title in scan: Data Shapley in One Training Run
- Source authors: Jiachen T. Wang, Prateek Mittal, Dawn Song, Ruoxi Jia
- Source year: 2024
- Source URL: https://openreview.net/forum?id=HD6bWcj87Y
- Scan report: _workspace/iclr2025/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Valuation with weighted banzhaf values
- Cited authors:
- Cited year: 2024
- Cited URL:
- Raw reference: #Valuation with weighted banzhaf values#Advances in Neural Information Processing Systems#2024
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "No paper with the exact title \"Valuation with weighted banzhaf values\" was found. The actual published paper has the title \"Robust Data Valuation with Weighted Banzhaf Values\" and was published at NeurIPS 2023, not 2024.",
  "link": "https://papers.nips.cc/paper_files/paper/2023/hash/bdb0596d13cfccf2db6f0cc5280d2a3f-Abstract-Conference.html",
  "found_title": "Robust Data Valuation with Weighted Banzhaf Values",
  "found_authors": "W. Li, Y. Yu",
  "found_venue": "Advances in Neural Information Processing Systems (NeurIPS)",
  "found_year": "2023",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://openreview.net/forum?id=u359tNBpxF",
      "https://dl.acm.org/doi/10.5555/3666122.3668759",
      "https://neurips.cc/virtual/2023/poster/70172",
      "https://papers.nips.cc/paper_files/paper/2023/hash/bdb0596d13cfccf2db6f0cc5280d2a3f-Abstract-Conference.html",
      "https://bytez.com/docs/neurips/70172/paper?_c=eyJ2IjoxLCJyZWxhdGVkIjpbImNvZGUiLCJyZWZlcmVuY2VzIiwiY29uZmVyZW5jZSJdfQ%3D%3D"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: User-provided correction: this is a parsing error for the weighted Banzhaf values reference, so it should be counted as a false positive rather than a hallucinated citation.

<a id="reference-6"></a>
### Reference 6: Inference, method, and decision: Towards a bayesian philosophy of science (TP)

#### Paper Metadata

- Conference: ICML 2022
- Award/Nomination: Outstanding Paper
- Awarded paper title: Bayesian Model Selection, the Marginal Likelihood, and Generalization
- Source paper title in scan: Lotfi22A
- Source authors: Unknown
- Source year: 2026
- Source URL: https://proceedings.mlr.press/v162/lotfi22a/lotfi22a.pdf
- Scan report: _workspace/icml2022/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Inference, method, and decision: Towards a bayesian philosophy of science
- Cited authors: E. T. Jaynes
- Cited year: 1991
- Cited URL:
- Raw reference: E. T. Jaynes#Inference, method, and decision: Towards a bayesian philosophy of science#n.d. W. H. Jefferys*J. O. Berger#Sharpening ockham’s razor on a bayesian strop#Technical Report#1991
- Scan error type: multiple

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The cited reference incorrectly attributes the book \"Inference, Method, and Decision: Towards a Bayesian Philosophy of Science\" to E. T. Jaynes as the author with a 1991 publication date. In reality, this is a book by Roger D. Rosenkrantz published in 1977, which Jaynes reviewed in 1979 for the Journal of the American Statistical Association.",
  "link": "https://archive.org/details/inferencemethodd0000rose",
  "found_title": "Inference, method, and decision: towards a Bayesian philosophy of science",
  "found_authors": "Roger D. Rosenkrantz",
  "found_venue": "D. Reidel Publishing Co.",
  "found_year": "1977",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://imaging.mrc-cbu.cam.ac.uk/imaging/CbuImaging/Bayesian_theory?action=AttachFile&do=get&target=Rosenkrantz+1979+(from+session+2).pdf",
      "https://link.springer.com/chapter/10.1007/978-94-011-4710-1_1",
      "https://statmodeling.stat.columbia.edu/2016/04/18/david-mackay/",
      "https://books.google.de/books/about/Inference_method_and_decision.html?id=HHdIAQAAIAAJ&redir_esc=y",
      "https://cognition.princeton.edu/document/125"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **TP**
- Rationale: The book exists, but the citation attributes Rosenkrantz’s book to E. T. Jaynes and gives an incorrect date; this is a substantive fabricated authorship claim.

<a id="reference-7"></a>
### Reference 7: Principles of mathematical analysis, volume 3 (FP)

#### Paper Metadata

- Conference: ICML 2022
- Award/Nomination: Outstanding Paper
- Awarded paper title: Do Differentiable Simulators Give Better Policy Gradients?
- Source paper title in scan: Suh22B
- Source authors: Unknown
- Source year: 2026
- Source URL: https://proceedings.mlr.press/v162/suh22b/suh22b.pdf
- Scan report: _workspace/icml2022/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Principles of mathematical analysis, volume 3
- Cited authors: W. Rudin, et al
- Cited year: 1964
- Cited URL:
- Raw reference: W. Rudin*et al.#Principles of mathematical analysis, volume 3#McGraw-hill New York#1964#
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The reference cites a non-existent \"volume 3\" of Rudin's textbook; the book was published in three editions (1953, 1964, 1976), not three volumes. The 1964 publication was the second edition, not a \"volume 3.\" Rudin was the sole author, not co-authored with others.",
  "link": null,
  "found_title": null,
  "found_authors": null,
  "found_venue": null,
  "found_year": null,
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://dokumen.pub/principles-of-mathematical-analysis-3nbsped-007054235x.html",
      "https://www.biblio.com/book/principles-mathematical-analysis-3rd-international-edition/d/1468602328",
      "https://dokumen.pub/principles-of-mathematical-analysis-35th-ed.html",
      "https://booksrun.com/9780070542358-principles-of-mathematical-analysis-international-series-in-pure-and-applied-mathematics-international-series-in-pure-applied-mathematics-3rd-edition",
      "https://www.slideshare.net/slideshow/principles-of-mathematical-analysis-third-edition-retyped-edited-updated-3-modernized-updated-walter-rudin/278906349"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: the cited work predates 1970, so under the requested rule I mark it as a false positive even though the volume/edition metadata is confused.

<a id="reference-8"></a>
### Reference 8: Robust and Optimal Control (TP)

#### Paper Metadata

- Conference: ICML 2022
- Award/Nomination: Outstanding Paper
- Awarded paper title: Learning Mixtures of Linear Dynamical Systems
- Source paper title in scan: Chen22T
- Source authors: Unknown
- Source year: 2026
- Source URL: https://proceedings.mlr.press/v162/chen22t/chen22t.pdf
- Scan report: _workspace/icml2022/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Robust and Optimal Control
- Cited authors: I. S. Khalil, J. Doyle, K. Glover
- Cited year: 1996
- Cited URL:
- Raw reference: I. S. Khalil*J. Doyle*K. Glover#Robust and Optimal Control#Prentice Hall#1996#
- Scan error type: author

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The book \"Robust and Optimal Control\" (Prentice Hall, 1996) exists with the correct title and year, but the cited first author \"I. S. Khalil\" is incorrect—the actual first author is Kemin Zhou. This is a fabricated author substitution.",
  "link": "https://www.amazon.com/Robust-Optimal-Control-Kemin-Zhou/dp/0134565673",
  "found_title": "Robust and Optimal Control",
  "found_authors": "Kemin Zhou, John C. Doyle, Keith Glover",
  "found_venue": "Prentice Hall",
  "found_year": "1996",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.scirp.org/(S(czeh2tfqyw2orz553k1w0r45))/reference/ReferencesPapers.aspx?ReferenceID=376613",
      "https://www.scirp.org/(S(i43dyn45te-exjx455qlt3d2q))/reference/referencespapers?referenceid=962015",
      "https://www.ece.lsu.edu/kemin/robust.htm",
      "https://www.semanticscholar.org/paper/Robust-and-optimal-control-Doyle/b0dc50b566596f4b74a6317e260fee169336dc48",
      "https://dl.acm.org/doi/abs/10.5555/225507"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **TP**
- Rationale: The cited reference substitutes I. S. Khalil for the actual first author Kemin Zhou on a real book, which is a material fabricated-author error.

<a id="reference-9"></a>
### Reference 9: Towards efﬁcient evaluation of risk via herding (FP)

#### Paper Metadata

- Conference: ICML 2022
- Award/Nomination: Outstanding Paper Runner Up
- Awarded paper title: Active fairness auditing
- Source paper title in scan: Yan22C
- Source authors: Unknown
- Source year: 2026
- Source URL: https://proceedings.mlr.press/v162/yan22c/yan22c.pdf
- Scan report: _workspace/icml2022/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Towards efﬁcient evaluation of risk via herding
- Cited authors: Z. Xu, T. Yu, S. Sra
- Cited year: 2019
- Cited URL:
- Raw reference: Z. Xu*T. Yu*S. Sra#Towards efﬁcient evaluation of risk via herding#Negative Dependence: Theory and Applications in Machine Learning#2019
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The paper \"Towards Efficient Evaluation of Risk via Herding\" exists and was presented by Zelai Xu at a 2019 workshop on \"Negative Dependence: Theory and Applications in Machine Learning,\" but the citation attributes the work to three authors (Z. Xu, T. Yu, S. Sra) when the actual paper appears to be authored by Zelai Xu alone or primarily.",
  "link": "https://slideslive.com/38917390/towards-efficient-evaluation-of-risk-via-herding",
  "found_title": "Towards Efficient Evaluation of Risk via Herding",
  "found_authors": "Zelai Xu",
  "found_venue": "Negative Dependence: Theory and Applications in Machine Learning",
  "found_year": "2019",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://slideslive.com/38917390/towards-efficient-evaluation-of-risk-via-herding",
      "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7485832/",
      "https://arxiv.org/pdf/0906.0552",
      "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10020420/",
      "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7070376/"
    ],
    "provider": "anthropic"
  },
  "previous_verdict": "UNLIKELY"
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: this appears to be a workshop/presentation web page rather than a conventional paper record, so under the requested website-source rule I mark it false positive.

<a id="reference-10"></a>
### Reference 10: Unified rational protein engineering Learning inverse folding from millions of predicted structures with sequence-based deep representation learning (TP)

#### Paper Metadata

- Conference: ICML 2022
- Award/Nomination: Outstanding Paper Runner Up
- Awarded paper title: Learning inverse folding from millions of predicted structures
- Source paper title in scan: Hsu22A
- Source authors: Unknown
- Source year: 2026
- Source URL: https://proceedings.mlr.press/v162/hsu22a/hsu22a.pdf
- Scan report: _workspace/icml2022/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Unified rational protein engineering Learning inverse folding from millions of predicted structures with sequence-based deep representation learning
- Cited authors: E. C. Alley, G. Khimulya, S. Biswas, M. AlQuraishi, G. M. Church
- Cited year: 2019
- Cited URL:
- Raw reference: E. C. Alley*G. Khimulya*S. Biswas*M. AlQuraishi*G. M. Church#Unified rational protein engineering Learning inverse folding from millions of predicted structures with sequence-based deep representation learning#Nature methods#2019#
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The citation combines the title of a real 2019 Alley et al. paper with a different 2022 paper on inverse folding, creating a non-existent hybrid title. The cited title does not match any published paper.",
  "link": "https://www.nature.com/articles/s41592-019-0598-1",
  "found_title": "Unified rational protein engineering with sequence-based deep representation learning",
  "found_authors": "Ethan C. Alley, Grigory Khimulya, Surojit Biswas, Mohammed AlQuraishi, George M. Church",
  "found_venue": "Nature Methods",
  "found_year": "2019",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.media.mit.edu/publications/unified-rational-protein-engineering-with-sequence-based-deep-representation-learning/",
      "https://www.nature.com/articles/s41592-019-0598-1",
      "https://www.semanticscholar.org/paper/Unified-rational-protein-engineering-with-deep-Alley-Khimulya/06eb3c3ccae16fced2222f8a45877906f54f2164",
      "https://www.researchgate.net/publication/336711828_Unified_rational_protein_engineering_with_sequence-based_deep_representation_learning",
      "https://www.researchgate.net/publication/345387964_Unified_rational_protein_engineering_with_sequence-based_deep_representation_learning"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **TP**
- Rationale: The title is a hybrid of two different protein-engineering/inverse-folding papers, producing a non-existent cited work.

<a id="reference-11"></a>
### Reference 11: Models, reasoning and inference (FP)

#### Paper Metadata

- Conference: ICML 2022
- Award/Nomination: Outstanding Paper Runner Up
- Awarded paper title: Minimum Cost Intervention Design for Causal Effect Identification
- Source paper title in scan: Akbari22A
- Source authors: Unknown
- Source year: 2026
- Source URL: https://proceedings.mlr.press/v162/akbari22a/akbari22a.pdf
- Scan report: _workspace/icml2022/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Models, reasoning and inference
- Cited authors: J. Pearl, et al
- Cited year: 2000
- Cited URL:
- Raw reference: J. Pearl*et al.#Models, reasoning and inference#Cambridge, UK: CambridgeUniversityPress#2000#
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The cited title is incomplete—the actual book is \"Causality: Models, Reasoning and Inference\" by Judea Pearl alone, not \"Models, reasoning and inference\" by \"J. Pearl, et al.\" The citation omits \"Causality:\" and incorrectly implies multiple authors.",
  "link": "https://www.amazon.com/Causality-Reasoning-Inference-Judea-Pearl/dp/0521773628",
  "found_title": "Causality: Models, Reasoning and Inference",
  "found_authors": "Judea Pearl",
  "found_venue": "Cambridge University Press",
  "found_year": "2000",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.scirp.org/reference/referencespapers?referenceid=1691236",
      "https://www.scirp.org/reference/referencespapers?referenceid=4008083",
      "https://philpapers.org/rec/HITCMR-2",
      "https://www.amazon.com/Causality-Reasoning-Inference-Judea-Pearl/dp/0521773628",
      "https://onlinelibrary.wiley.com/doi/abs/10.1002/sim.1006"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Pearl’s Causality book is plainly the intended source; the title is truncated and “et al.” is wrong, but the reference remains recognizable rather than hallucinated.

<a id="reference-12"></a>
### Reference 12: Gradient descent: The ultimate optimizer (FP)

#### Paper Metadata

- Conference: ICML 2023
- Award/Nomination: Outstanding Paper
- Awarded paper title: Learning-Rate-Free Learning by D-Adaptation
- Source paper title in scan: Defazio23A
- Source authors: Unknown
- Source year: 2026
- Source URL: https://proceedings.mlr.press/v202/defazio23a/defazio23a.pdf
- Scan report: _workspace/icml2023/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Gradient descent: The ultimate optimizer
- Cited authors: K. Chandra, A. Xie, J. Ragan-Kelley, E. Meijer
- Cited year: 2022
- Cited URL:
- Raw reference: K. Chandra*A. Xie*J. Ragan-Kelley*E. Meijer#Gradient descent: The ultimate optimizer#36th Conference on Neural Information Processing Systems (NeurIPS)#2022#
- Scan error type: multiple

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The cited reference lists authors that do not all appear on the actual published paper. While Chandra and Meijer are correctly cited, the inclusion of Audrey Xie and Jonathan Ragan-Kelley as the only co-authors, and the exclusion of the 9 co-authors listed on the actual paper's title page, represents a substantially incomplete and inaccurate author attribution. EXPLANATION: The paper with this exact title exists and was published at NeurIPS 2022 with Chandra and Meijer as authors, but the citation lists only four authors (omitting nine co-authors listed on the actual paper: Andow, Arroyo-Fang, Dea, George, Grueter, Hosmer, Stumpos, Tempest, and Yang). (Verdict corrected: the cited author list has low overlap with the verified paper, and the LLM did not provide found authors that substantially match the cited authors. A real title with fabricated coauthors is treated as hallucinated.)",
  "link": "https://arxiv.org/abs/1909.13371",
  "found_title": "Gradient Descent: The Ultimate Optimizer",
  "found_authors": "Kartik Chandra, Erik Meijer, Samantha Andow, Emilio Arroyo-Fang, Irene Dea, Johann George, Melissa Grueter, Basil Hosmer, Steffi Stumpos, Alanna Tempest, Shannon Yang",
  "found_venue": "Advances in Neural Information Processing Systems 35 (NeurIPS 2022)",
  "found_year": "2022",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://slideslive.com/38991668/gradient-descent-the-ultimate-optimizer",
      "https://pypi.org/project/gradient-descent-the-ultimate-optimizer/",
      "https://github.com/kach/gradient-descent-the-ultimate-optimizer/blob/main/README.md",
      "https://github.com/kach/gradient-descent-the-ultimate-optimizer",
      "https://arxiv.org/abs/1909.13371"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: The cited four-author list for “Gradient Descent: The Ultimate Optimizer” is the known paper’s author list; the scan appears to have matched/used bad metadata.

<a id="reference-13"></a>
### Reference 13: Debate update: Obfuscated arguments problem (FP)

#### Paper Metadata

- Conference: ICML 2024
- Award/Nomination: Best Paper
- Awarded paper title: Debating with More Persuasive LLMs Leads to More Truthful Answers
- Source paper title in scan: Debating with More Persuasive LLMs Leads to More Truthful Answers
- Source authors: Akbir Khan, John Hughes, Dan Valentine, Laura Ruis, Kshitij Sachan, Ansh Radhakrishnan, Edward Grefenstette, Samuel R. Bowman, Tim Rocktäschel, Ethan Perez
- Source year: 2024
- Source URL: https://openreview.net/forum?id=iLCZtl7FTa
- Scan report: _workspace/icml2024/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Debate update: Obfuscated arguments problem
- Cited authors: B. Barnes
- Cited year: 2020
- Cited URL:
- Raw reference: B. Barnes#Debate update: Obfuscated arguments problem#AI Alignment Forum#2020
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The exact title and year match a real post on the AI Alignment Forum, but the cited authors are incomplete; the actual post was co-authored by Beth Barnes and Paul Christiano, not B. Barnes alone. This is a fabricated author attribution.",
  "link": "https://www.alignmentforum.org/posts/PJLABqQ962hZEqhdB/debate-update-obfuscated-arguments-problem",
  "found_title": "Debate update: Obfuscated arguments problem",
  "found_authors": "Beth Barnes, Paul Christiano",
  "found_venue": "AI Alignment Forum",
  "found_year": "2020",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.lesswrong.com/posts/PJLABqQ962hZEqhdB/debate-update-obfuscated-arguments-problem",
      "https://player.fm/series/ai-safety-fundamentals-alignment/week-5-debate-update-obfuscated-arguments-problem-by-beth-barnes",
      "https://uk-podcasts.co.uk/podcast/ai-safety-fundamentals-alignment/-week-5-debate-update-obfuscated-arguments-problem",
      "https://www.lesswrong.com/posts/WP4fciGn3rNtmq3tY/ai-safety-101-chapter-5-1-debate",
      "https://arxiv.org/pdf/2311.14125"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: this is an Alignment Forum web post, so under the requested website-source rule it should be counted as a false positive despite incomplete authorship.

<a id="reference-14"></a>
### Reference 14: Understanding Generalization via Leave-One-Out Conditional Mutual Information (FP)

#### Paper Metadata

- Conference: ICML 2024
- Award/Nomination: Best Paper
- Awarded paper title: Information Complexity of Stochastic Convex Optimization: Applications to Generalization, Memorization, and Tracing
- Source paper title in scan: Information Complexity of Stochastic Convex Optimization: Applications to Generalization, Memorization, and Tracing
- Source authors: Idan Attias, Gintare Karolina Dziugaite, Mahdi Haghifam, Roi Livni, Daniel M. Roy
- Source year: 2024
- Source URL: https://openreview.net/forum?id=CyEJn71Z00
- Scan report: _workspace/icml2024/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Understanding Generalization via Leave-One-Out Conditional Mutual Information
- Cited authors: Karolina Dziugaite
- Cited year: 2022
- Cited URL:
- Raw reference: Karolina Dziugaite#Understanding Generalization via Leave-One-Out Conditional Mutual Information#2022 IEEE International Symposium on Information Theory (ISIT)#2022
- Scan error type: multiple

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The paper exists with the exact title, but the cited author list is incomplete and incorrect. The actual paper has four authors (Mahdi Haghifam, Shay Moran, Daniel M. Roy, and Gintare Karolina Dziugaite), but the citation lists only Karolina Dziugaite, omitting three co-authors entirely. This constitutes a fabricated author attribution for a real paper.",
  "link": "https://arxiv.org/abs/2206.14800",
  "found_title": "Understanding Generalization via Leave-One-Out Conditional Mutual Information",
  "found_authors": "Mahdi Haghifam, Shay Moran, Daniel M. Roy, Gintare Karolina Dziugaite",
  "found_venue": "2022 IEEE International Symposium on Information Theory (ISIT)",
  "found_year": "2022",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://arxiv.org/abs/2206.14800v1",
      "https://arxiv.org/abs/2206.14800",
      "https://arxiv.org/pdf/2206.14800",
      "https://gkdz.org/publication/hdmr22/",
      "https://ieeexplore.ieee.org/document/9834400/"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: The cited paper exists with the same title and includes Dziugaite as an author; listing only one author is incomplete but not enough to call the reference fabricated.

<a id="reference-15"></a>
### Reference 15: Prochlo: Strong privacy for analytics in the wild (TP)

#### Paper Metadata

- Conference: ICML 2024
- Award/Nomination: Best Paper
- Awarded paper title: Position: Considerations for Differentially Private Learning with Large-Scale Public Pretraining
- Source paper title in scan: Position: Considerations for Differentially Private Learning with Large-Scale Public Pretraining
- Source authors: Florian Tramèr, Gautam Kamath, Nicholas Carlini
- Source year: 2024
- Source URL: https://openreview.net/forum?id=ncjhi4qAPV
- Scan report: _workspace/icml2024/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Prochlo: Strong privacy for analytics in the wild
- Cited authors: Andrea Bittau, Úlfar Erlingsson, Petros Maniatis, Ilya Mironov, Ananth Raghunathan, David Lie, Matthew Rudder, Xunwen Xin
- Cited year: 2017
- Cited URL:
- Raw reference: Andrea Bittau*Úlfar Erlingsson*Petros Maniatis*Ilya Mironov*Ananth Raghunathan*David Lie*Matthew Rudder*Xunwen Xin#Prochlo: Strong privacy for analytics in the wild#Proceedings of the 26th Symposium on Operating Systems Principles#2017
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The cited title \"Prochlo: Strong privacy for analytics in the wild\" does not match the actual published paper title, which is \"Prochlo: Strong Privacy for Analytics in the Crowd.\" Multiple authoritative sources (arXiv, ACM Digital Library, Google Research, and SOSP 2017 proceedings) consistently show the correct title ends in \"Crowd,\" not \"wild.\" The first eight authors match, but the cited reference omits two coauthors (Mitch Rudominer and Ushasree Kode) who appear on all official versions of the published paper.",
  "link": "https://arxiv.org/abs/1710.00901",
  "found_title": "Prochlo: Strong Privacy for Analytics in the Crowd",
  "found_authors": "Andrea Bittau, Úlfar Erlingsson, Petros Maniatis, Ilya Mironov, Ananth Raghunathan, David Lie, Mitch Rudominer, Ushasree Kode, Julien Tinnes, Bernhard Seefeld",
  "found_venue": "Proceedings of the 26th Symposium on Operating Systems Principles (SOSP)",
  "found_year": "2017",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://utoronto.scholaris.ca/items/7f90dc1b-15b3-4f06-8765-83cd0076b706",
      "https://research.google/pubs/prochlo-strong-privacy-for-analytics-in-the-crowd/",
      "https://arxiv.org/abs/1710.00901",
      "https://www.researchgate.net/publication/320362737_Prochlo_Strong_Privacy_for_Analytics_in_the_Crowd",
      "https://cs523.github.io/jinyang7/"
    ],
    "provider": "anthropic"
  },
  "previous_verdict": "UNLIKELY"
}
```

#### Independent Assessment

- FP/TP flag: **TP**
- Rationale: The Prochlo citation changes the published title from “Crowd” to “wild” and omits coauthors; this materially creates a distinct, unsupported reference.

<a id="reference-16"></a>
### Reference 16: An american puzzle: Fitting race in a box (FP)

#### Paper Metadata

- Conference: ICML 2024
- Award/Nomination: Best Paper
- Awarded paper title: Position: Measure Dataset Diversity, Don't Just Claim It
- Source paper title in scan: Position: Measure Dataset Diversity, Don't Just Claim It
- Source authors: Dora Zhao, Jerone Andrews, Orestis Papakyriakopoulos, Alice Xiang
- Source year: 2024
- Source URL: https://openreview.net/forum?id=jsKr6RVDDs
- Scan report: _workspace/icml2024/results/scan_report.json

#### Cited Reference Metadata

- Cited title: An american puzzle: Fitting race in a box
- Cited authors: K. R. Lai, J. Medina
- Cited year: 2023
- Cited URL:
- Raw reference: K. R. Lai*J. Medina#An american puzzle: Fitting race in a box#The New York Times#2023
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The New York Times article exists with the exact title and correct authors, but the cited author names are incorrect. The reference lists \"K. R. Lai\" when the actual author is \"K.K. Rebecca Lai.\" (Verdict corrected: finding the title only as a citation or reference in another paper is not proof that the cited paper has its own dedicated publication page.)",
  "link": null,
  "found_title": "An American Puzzle: Fitting Race in a Box",
  "found_authors": "K.K. Rebecca Lai, Jennifer Medina",
  "found_venue": "The New York Times",
  "found_year": "2023",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://mixedracestudies.org/wp/?tag=k-k-rebecca-lai",
      "https://mixedracestudies.org/wp/?tag=u-s-census-bureau",
      "https://mixedracestudies.org/wp/?p=64320",
      "https://mixedracestudies.org/wp/?m=kzmpwtcmrazbvhzn&paged=3",
      "https://talkaboutrace.org/an-american-puzzle-fitting-race-in-a-box/"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: this is a newspaper article, and the requested rule treats newspaper-article references as false positives; the author-name issue is not enough to call it hallucinated.

<a id="reference-17"></a>
### Reference 17: Rethinking conversational agents in the era of llms: Proactivity, non-collaborativity, and beyond (TP)

#### Paper Metadata

- Conference: ICML 2025
- Award/Nomination: Outstanding Paper
- Awarded paper title: CollabLLM: From Passive Responders to Active Collaborators
- Source paper title in scan: CollabLLM: From Passive Responders to Active Collaborators
- Source authors: Shirley Wu, Michel Galley, Baolin Peng, Hao Cheng, Gavin Li, Yao Dou, Weixin Cai, James Zou, Jure Leskovec, Jianfeng Gao
- Source year: 2025
- Source URL: https://openreview.net/forum?id=DmH4HHVb3y
- Scan report: _workspace/icml2025/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Rethinking conversational agents in the era of llms: Proactivity, non-collaborativity, and beyond
- Cited authors: K. Balog, C. Zhai
- Cited year: 2023
- Cited URL:
- Raw reference: K. Balog*C. Zhai#Rethinking conversational agents in the era of llms: Proactivity, non-collaborativity, and beyond#SIGIR-AP#2023
- Scan error type: author

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The cited paper has the correct title and was published at SIGIR-AP 2023, but the authors are entirely fabricated. The actual paper was written by Yang Deng, Wenqiang Lei, Minlie Huang, and Tat-Seng Chua—not K. Balog and C. Zhai.",
  "link": "https://dl.acm.org/doi/10.1145/3624918.3629548",
  "found_title": "Rethinking Conversational Agents in the Era of LLMs: Proactivity, Non-collaborativity, and Beyond",
  "found_authors": "Yang Deng, Wenqiang Lei, Minlie Huang, Tat-Seng Chua",
  "found_venue": "SIGIR-AP 2023 (Annual International ACM SIGIR Conference on Research and Development in Information Retrieval in the Asia Pacific Region)",
  "found_year": "2023",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://dl.acm.org/doi/10.1145/3624918.3629548",
      "https://experts.illinois.edu/en/publications/rethinking-conversational-agents-in-the-era-of-llms-proactivity-n/",
      "https://www.researchgate.net/publication/375922833_Rethinking_Conversational_Agents_in_the_Era_of_LLMs_Proactivity_Non-collaborativity_and_Beyond",
      "https://www.semanticscholar.org/paper/Rethinking-Conversational-Agents-in-the-Era-of-and-Deng-Lei/ac1ce912a8a3614ad4c5f467eca8f20b315a3428",
      "https://www.sigir-ap.org/sigir-ap-2023//assets/files/SIGIRAP2023-Tutorial-ConvAI.pdf"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **TP**
- Rationale: The title exists, but the cited authors are entirely different from the real authors; this is a clear fabricated-author attribution.

<a id="reference-18"></a>
### Reference 18: de Finetti’s theorem, induction, and An or Bayesian nonparametric predictive inference (with discussion) (TP)

#### Paper Metadata

- Conference: ICML 2025
- Award/Nomination: Outstanding Paper
- Awarded paper title: Conformal Prediction as Bayesian Quadrature
- Source paper title in scan: Conformal Prediction as Bayesian Quadrature
- Source authors: Jake C. Snell, Thomas L. Griffiths
- Source year: 2025
- Source URL: https://openreview.net/forum?id=PNmkjIzHB7
- Scan report: _workspace/icml2025/results/scan_report.json

#### Cited Reference Metadata

- Cited title: de Finetti’s theorem, induction, and An or Bayesian nonparametric predictive inference (with discussion)
- Cited authors: B. M. Hill
- Cited year: 1988
- Cited URL:
- Raw reference: B. M. Hill#de Finetti’s theorem, induction, and An or Bayesian nonparametric predictive inference (with discussion)#Bayesian statistics#1988#
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The exact title could not be located in any academic database or through web search, despite the legitimate 1988 \"Bayesian Statistics\" conference series being confirmed. The title contains awkward phrasing and does not appear in available records.",
  "link": null,
  "found_title": null,
  "found_authors": null,
  "found_venue": null,
  "found_year": null,
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://en.wikipedia.org/wiki/De_Finetti's_theorem",
      "https://www.stat.berkeley.edu/~ryantibs/papers/defin.pdf",
      "https://link.springer.com/article/10.1007/BF00276788",
      "https://www.stats.ox.ac.uk/~steffen/teaching/grad/definetti.pdf",
      "http://blog.nullspace.io/motivating-bayesian.html"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **TP**
- Rationale: The exact Hill/Bayesian nonparametric title could not be located and the title itself appears malformed; this is likely a non-existent reference.

<a id="reference-19"></a>
### Reference 19: A method of solving a convex programming problem with convergence rate O(1/k2) (FP)

#### Paper Metadata

- Conference: NEURIPS 2021
- Award/Nomination: Outstanding Paper
- Awarded paper title: Continuized Accelerations of Deterministic and Stochastic Gradient Descents, and of Gossip Algorithms
- Source paper title in scan: Ec26Fc2Eb2B75Aece19C70392Dc744C2-Paper
- Source authors: Unknown
- Source year: 2026
- Source URL: https://papers.nips.cc/paper_files/paper/2021/file/ec26fc2eb2b75aece19c70392dc744c2-Paper.pdf
- Scan report: _workspace/neurips2021/results/scan_report.json

#### Cited Reference Metadata

- Cited title: A method of solving a convex programming problem with convergence rate O(1/k2)
- Cited authors: Yurii Nesterov
- Cited year: 1983
- Cited URL:
- Raw reference: Yurii Nesterov#A method of solving a convex programming problem with convergence rate O(1/k2)#Dokl. Akad. Nauk SSSR#1983#
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The paper was found in multiple academic sources including Math-Net.Ru, Semantic Scholar, and the SIAM Review reference list, confirming its existence with matching title, author, year, and venue. (Verdict corrected: finding the title only as a citation or reference in another paper is not proof that the cited paper has its own dedicated publication page.)",
  "link": "https://www.mathnet.ru/eng/dan46009",
  "found_title": "A method of solving a convex programming problem with convergence rate O(1/k²)",
  "found_authors": "Yu. E. Nesterov",
  "found_venue": "Dokl. Akad. Nauk SSSR",
  "found_year": "1983",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://epubs.siam.org/doi/10.1137/21M1390037",
      "https://cir.nii.ac.jp/crid/1370862715914709505",
      "https://www.mathnet.ru/eng/dan46009",
      "https://www.scirp.org/reference/referencespapers?referenceid=1769491",
      "https://www.semanticscholar.org/paper/A-method-for-solving-the-convex-programming-problem-Nesterov/8d3a318b62d2e970122da35b2a2e70a5d12cc16f"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: The Nesterov paper was found with matching title, author, and year at Math-Net; this should be treated as a real reference.

<a id="reference-20"></a>
### Reference 20: On separating agent designer goals from agent goals: Breaking the preferences–parameters confound (TP)

#### Paper Metadata

- Conference: NEURIPS 2021
- Award/Nomination: Outstanding Paper
- Awarded paper title: On the Expressivity of Markov Reward
- Source paper title in scan: 4079016D940210B4Ae9Ae7D41C4A2065-Paper
- Source authors: Unknown
- Source year: 2026
- Source URL: https://papers.nips.cc/paper_files/paper/2021/file/4079016d940210b4ae9ae7d41c4a2065-Paper.pdf
- Scan report: _workspace/neurips2021/results/scan_report.json

#### Cited Reference Metadata

- Cited title: On separating agent designer goals from agent goals: Breaking the preferences–parameters confound
- Cited authors: Satinder Singh, Richard L. Lewis, Jonathan Sorg, Andrew G. Barto, Akram Helou
- Cited year: 2010
- Cited URL:
- Raw reference: Satinder Singh*Richard L. Lewis*Jonathan Sorg*Andrew G. Barto*Akram Helou#On separating agent designer goals from agent goals: Breaking the preferences–parameters confound#2010#
- Scan error type: author

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The paper exists with a matching title, but the cited author list contains three names (Richard L. Lewis, Jonathan Sorg, Akram Helou) that do not appear as authors on the actual paper, which lists only Satinder Singh and A. Barto.",
  "link": "https://api.semanticscholar.org/CorpusID:122252",
  "found_title": "On separating agent designer goals from agent goals: Breaking the preferences–parameters confound",
  "found_authors": "Satinder Singh, A. Barto",
  "found_venue": null,
  "found_year": "2010",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.lesswrong.com/posts/EA9gHyPZ5J7FPoQiL/understanding-agent-preferences",
      "https://www.mindstudio.ai/blog/managing-ai-agents-by-goals-not-terminals",
      "https://medium.com/data-science-collective/architects-guide-to-agentic-design-patterns-a184216c1660",
      "https://venturebeat.com/orchestration/claude-codes-goals-separates-the-agent-that-works-from-the-one-that-decides-its-done",
      "https://www.sciencedirect.com/science/article/abs/pii/S0899825618300034"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **TP**
- Rationale: The cited work exists but three extra authors are grafted onto a two-author paper; that is a material fabricated-author error.

<a id="reference-21"></a>
### Reference 21: From doc2query to doctttttquery (TP)

#### Paper Metadata

- Conference: NEURIPS 2022
- Award/Nomination: Outstanding Paper
- Awarded paper title: A Neural Corpus Indexer for Document Retrieval
- Source paper title in scan: A46156Bd3579C3B268108Ea6Aca71D13-Paper-Conference
- Source authors: Unknown
- Source year: 2026
- Source URL: https://proceedings.neurips.cc/paper_files/paper/2022/file/a46156bd3579c3b268108ea6aca71d13-Paper-Conference.pdf
- Scan report: _workspace/neurips2022/results/scan_report.json

#### Cited Reference Metadata

- Cited title: From doc2query to doctttttquery
- Cited authors: Rodrigo Nogueira, Jimmy Lin, AI Epistemic
- Cited year: 2019
- Cited URL:
- Raw reference: Rodrigo Nogueira*Jimmy Lin*AI Epistemic#From doc2query to doctttttquery#Online preprint#2019
- Scan error type: author

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The paper exists and the title and two primary authors match, but \"AI Epistemic\" is incorrectly listed as a third author when it is actually Rodrigo Nogueira's affiliation (Epistemic AI). The reference grafts a real institution name onto the author list as if it were a person.",
  "link": "https://cs.uwaterloo.ca/~jimmylin/publications/Nogueira_Lin_2019_docTTTTTquery-v2.pdf",
  "found_title": "From doc2query to docTTTTTquery",
  "found_authors": "Rodrigo Nogueira, Jimmy Lin",
  "found_venue": "Online preprint",
  "found_year": "2019",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.semanticscholar.org/paper/From-doc2query-to-docTTTTTquery-Nogueira/61e5cb85c846b1d3e5f90dc36d60f6ad4ea9d683",
      "https://cs.uwaterloo.ca/~jimmylin/publications/Nogueira_Lin_2019_docTTTTTquery-v2.pdf",
      "https://www.researchgate.net/publication/360973404_From_doc2query_to_docTTTTTquery_An_MS_MARCO_passage_retrieval_task_1_publication",
      "https://www.researchgate.net/publication/360890853_From_doc2query_to_docTTTTTquery",
      "https://github.com/castorini/docTTTTTquery"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **TP**
- Rationale: The citation turns an affiliation/company name (“Epistemic AI”) into an author, adding a fabricated third author to a real paper.

<a id="reference-22"></a>
### Reference 22: Compressive transformers for long-range sequence modelling (TP)

#### Paper Metadata

- Conference: NEURIPS 2022
- Award/Nomination: Outstanding Paper
- Awarded paper title: An empirical analysis of compute-optimal large language model training
- Source paper title in scan: C1E2Faff6F588870935F114Ebe04A3E5-Paper-Conference
- Source authors: Unknown
- Source year: 2026
- Source URL: https://proceedings.neurips.cc/paper_files/paper/2022/file/c1e2faff6f588870935f114ebe04a3e5-Paper-Conference.pdf
- Scan report: _workspace/neurips2022/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Compressive transformers for long-range sequence modelling
- Cited authors: D. Dohan, X. Song, A. Gane, T. Sarlos, et al
- Cited year: 2020
- Cited URL:
- Raw reference: D. Dohan*X. Song*A. Gane*T. Sarlos*et al.#Compressive transformers for long-range sequence modelling#Advances in Neural Information Processing Systems#2020#
- Scan error type: multiple

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The paper exists with the exact cited title, but the author list is entirely fabricated. The actual authors are Jack W. Rae, Anna Potapenko, Siddhant M. Jayakumar, Chloe Hillier, and Timothy P. Lillicrap, not D. Dohan, X. Song, A. Gane, T. Sarlos and others.",
  "link": "https://openreview.net/forum?id=SylKikSYDH",
  "found_title": "Compressive Transformers for Long-Range Sequence Modelling",
  "found_authors": "Jack W. Rae, Anna Potapenko, Siddhant M. Jayakumar, Chloe Hillier, Timothy P. Lillicrap",
  "found_venue": "International Conference on Learning Representations (ICLR)",
  "found_year": "2020",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://iclr.cc/virtual_2020/poster_SylKikSYDH.html",
      "https://huggingface.co/papers/1911.05507",
      "https://ui.adsabs.harvard.edu/abs/2019arXiv191105507R/abstract",
      "https://arxiv.org/pdf/1911.05507",
      "https://openreview.net/forum?id=SylKikSYDH"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **TP**
- Rationale: The Compressive Transformers paper exists, but the cited author list is unrelated to the actual authors; this is a true fabricated-author citation.

<a id="reference-23"></a>
### Reference 23: Théorie analytique de la chaleur (FP)

#### Paper Metadata

- Conference: NEURIPS 2022
- Award/Nomination: Outstanding Paper
- Awarded paper title: Elucidating the Design Space of Diffusion-Based Generative Models
- Source paper title in scan: A98846E9D9Cc01Cfb87Eb694D946Ce6B-Paper-Conference
- Source authors: Unknown
- Source year: 2026
- Source URL: https://proceedings.neurips.cc/paper_files/paper/2022/file/a98846e9d9cc01cfb87eb694d946ce6b-Paper-Conference.pdf
- Scan report: _workspace/neurips2022/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Théorie analytique de la chaleur
- Cited authors: J. B. J. Fourier, G. Darboux, et al
- Cited year: 1822
- Cited URL:
- Raw reference: J. B. J. Fourier*G. Darboux*et al.#Théorie analytique de la chaleur#Didot Paris#1822#
- Scan error type: multiple

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The original 1822 work was authored by Jean-Baptiste Joseph Fourier alone; Gaston Darboux was not a co-author but rather an editor of a later collected edition of Fourier's works. Listing Darboux as a co-author of the original 1822 publication is historically inaccurate.",
  "link": "https://archive.org/details/thorieanalytiq00four",
  "found_title": "Théorie analytique de la chaleur",
  "found_authors": "Jean-Baptiste Joseph Fourier",
  "found_venue": "F. Didot, Paris",
  "found_year": "1822",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.amazon.com/OEuvres-Fourier-Th%C3%A9orie-Analytique-Chaleur/dp/1018470743",
      "http://www.bibnum.education.fr/mathematiques/analyse/theorie-analytique-de-la-chaleur",
      "https://dbc.wroc.pl/dlibra/doccontent?id=1505",
      "https://www.amazon.com/Oeuvres-Fourier-Th%C3%A9orie-Analytique-Chaleur/dp/0270873023",
      "https://www.cambridge.org/core/books/abs/oeuvres-de-fourier/memoire-sur-la-theorie-analytique-de-la-chaleur/8FB7B13A9412846345CE032B4747B7F8"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: the cited work is prior to 1970, so under the requested rule it should be marked false positive even though later-editor authorship is confused.

<a id="reference-24"></a>
### Reference 24: Learning multiple layers of features from tiny images (FP)

#### Paper Metadata

- Conference: NEURIPS 2022
- Award/Nomination: Outstanding Paper
- Awarded paper title: Elucidating the Design Space of Diffusion-Based Generative Models
- Source paper title in scan: A98846E9D9Cc01Cfb87Eb694D946Ce6B-Paper-Conference
- Source authors: Unknown
- Source year: 2026
- Source URL: https://proceedings.neurips.cc/paper_files/paper/2022/file/a98846e9d9cc01cfb87eb694d946ce6b-Paper-Conference.pdf
- Scan report: _workspace/neurips2022/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Learning multiple layers of features from tiny images
- Cited authors: A. Krizhevsky
- Cited year: 2009
- Cited URL:
- Raw reference: A. Krizhevsky#Learning multiple layers of features from tiny images#Technical report, University of Toronto#2009#
- Scan error type: author

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The paper exists with the exact title and year, but the cited author list is incomplete; Geoffrey Hinton is a co-author who has been omitted from the citation.",
  "link": "https://www.cs.toronto.edu/~kriz/learning-features-2009-TR.pdf",
  "found_title": "Learning Multiple Layers of Features from Tiny Images",
  "found_authors": "Alex Krizhevsky, Geoffrey Hinton",
  "found_venue": "Technical Report, University of Toronto",
  "found_year": "2009",
  "source": "deep_hallucination_cache",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.scirp.org/reference/referencespapers?referenceid=3462454",
      "https://www.scirp.org/reference/referencespapers?referenceid=3680969",
      "https://www.scirp.org/reference/referencespapers?referenceid=2208762",
      "https://bibbase.org/network/publication/krizhevsky-hinton-learningmultiplelayersoffeaturesfromtinyimages-2009",
      "https://www.bibsonomy.org/bibtex/cc2d42f2b7ef6a4e76e47d1a50c8cd86",
      "https://www.cs.toronto.edu/~kriz/learning-features-2009-TR.pdf",
      "https://www.semanticscholar.org/paper/Learning-Multiple-Layers-of-Features-from-Tiny-Krizhevsky/5d90f06bb70a0a3dced62413346235c02b1aa086",
      "https://www.researchgate.net/publication/265748773_Learning_Multiple_Layers_of_Features_from_Tiny_Images",
      "https://scispace.com/papers/learning-multiple-layers-of-features-from-tiny-images-5eum9uf4g8",
      "https://archives.mountainscholar.org/digital/api/collection/p17393coll24/id/52709/download"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: the source is otherwise identifiable and the issue is an omitted single author, so under the requested rule it is a false positive.

<a id="reference-25"></a>
### Reference 25: Convolutional deep belief networks on cifar-10 (FP)

#### Paper Metadata

- Conference: NEURIPS 2022
- Award/Nomination: Outstanding Paper
- Awarded paper title: Is Out-of-Distribution Detection Learnable?
- Source paper title in scan: F0E91B1314Fa5Eabf1D7Ef6D1561Ecec-Paper-Conference
- Source authors: Unknown
- Source year: 2026
- Source URL: https://proceedings.neurips.cc/paper_files/paper/2022/file/f0e91b1314fa5eabf1d7ef6d1561ecec-Paper-Conference.pdf
- Scan report: _workspace/neurips2022/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Convolutional deep belief networks on cifar-10
- Cited authors: Alex Krizhevsky, Geoff Hinton
- Cited year: 2009
- Cited URL:
- Raw reference: Alex Krizhevsky*Geoff Hinton#Convolutional deep belief networks on cifar-10#Technical report, Citeseer#2009
- Scan error type: author

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The paper exists with the exact cited title and was authored by Alex Krizhevsky alone; Geoffrey E. Hinton is acknowledged for suggestions but is not an author. The citation incorrectly lists Hinton as a co-author.",
  "link": "https://www.cs.toronto.edu/~kriz/conv-cifar10-aug2010.pdf",
  "found_title": "Convolutional Deep Belief Networks on CIFAR-10",
  "found_authors": "Alex Krizhevsky",
  "found_venue": "Technical report",
  "found_year": "2010",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.cs.toronto.edu/~kriz/conv-cifar10-aug2010.pdf",
      "https://www.cs.utoronto.ca/~kriz/conv-cifar10-aug2010.pdf",
      "https://www.semanticscholar.org/paper/Convolutional-Deep-Belief-Networks-on-CIFAR-10-Krizhevsky/bea5780d621e669e8069f05d0f2fc0db9df4b50f",
      "https://www.researchgate.net/publication/265147627_Convolutional_Deep_Belief_Networks_on_CIFAR-10",
      "http://users.ics.aalto.fi/perellm1/thesis/summaries_html/node49.html"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: The CIFAR-10 technical report exists and Hinton is closely associated/acknowledged; listing him as coauthor is a citation error, not a fabricated work.

<a id="reference-26"></a>
### Reference 26: Embodied reasoning through planning with language models (FP)

#### Paper Metadata

- Conference: NEURIPS 2022
- Award/Nomination: Outstanding Paper
- Awarded paper title: MineDojo: Building Open-Ended Embodied Agents with Internet-Scale Knowledge
- Source paper title in scan: 74A67268C5Cc5910F64938Cac4526A90-Paper-Datasets And Benchmarks
- Source authors: Unknown
- Source year: 2026
- Source URL: https://proceedings.neurips.cc/paper_files/paper/2022/file/74a67268c5cc5910f64938cac4526a90-Paper-Datasets_and_Benchmarks.pdf
- Scan report: _workspace/neurips2022/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Embodied reasoning through planning with language models
- Cited authors: Wenlong Huang, Fei Xia, Ted Xiao, Harris Chan, Jacky Liang, Pete Florence, Andy Zeng, Jonathan Tompson, Igor Mordatch, Yevgen Chebotar, Pierre Sermanet, Noah Brown, Tomas
- Cited year: 2022
- Cited URL:
- Raw reference: Wenlong Huang*Fei Xia*Ted Xiao*Harris Chan*Jacky Liang*Pete Florence*Andy Zeng*Jonathan Tompson*Igor Mordatch*Yevgen Chebotar*Pierre Sermanet*Noah Brown*Tomas#Embodied reasoning through planning with language models#arXiv preprint arXiv: Arxiv-2207.05608#2022
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The cited reference truncates the actual paper title by omitting \"Inner Monologue:\" and provides an incomplete author list and incomplete author name. The actual paper is \"Inner Monologue: Embodied Reasoning through Planning with Language Models\" with 17 authors including Tomas Jackson, Linda Luu, Sergey Levine, Karol Hausman, and Brian Ichter.",
  "link": "https://arxiv.org/abs/2207.05608",
  "found_title": "Inner Monologue: Embodied Reasoning through Planning with Language Models",
  "found_authors": "Wenlong Huang, Fei Xia, Ted Xiao, Harris Chan, Jacky Liang, Pete Florence, Andy Zeng, Jonathan Tompson, Igor Mordatch, Yevgen Chebotar, Pierre Sermanet, Noah Brown, Tomas Jackson, Linda Luu, Sergey Levine, Karol Hausman, Brian Ichter",
  "found_venue": "arXiv",
  "found_year": "2022",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://research.google/pubs/innermonologue-embodied-reasoning-through-planning-with-language-models/",
      "https://arxiv.org/abs/2207.05608",
      "https://arxiv.org/abs/2207.05608v1",
      "https://deepai.org/publication/inner-monologue-embodied-reasoning-through-planning-with-language-models",
      "https://arxiv.org/pdf/2207.05608"
    ],
    "provider": "anthropic"
  },
  "previous_verdict": "UNLIKELY"
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: The Inner Monologue paper exists; the citation shortens the title and truncates a long author list, but the intended reference is clear.

<a id="reference-27"></a>
### Reference 27: Information-theoretic lower bounds of PAC sample complexity (FP)

#### Paper Metadata

- Conference: NEURIPS 2022
- Award/Nomination: Outstanding Paper
- Awarded paper title: On-Demand Sampling: Learning Optimally from Multiple Distributions
- Source paper title in scan: 02917Acec264A52A729B99D9Bc857909-Paper-Conference
- Source authors: Unknown
- Source year: 2026
- Source URL: https://proceedings.neurips.cc/paper_files/paper/2022/file/02917acec264a52a729b99d9bc857909-Paper-Conference.pdf
- Scan report: _workspace/neurips2022/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Information-theoretic lower bounds of PAC sample complexity
- Cited authors: C. Zhang
- Cited year: 2019
- Cited URL:
- Raw reference: C. Zhang#Information-theoretic lower bounds of PAC sample complexity#2019#
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "No paper with this exact title was found in any academic database or web search results despite searches for the title and author combination.",
  "link": null,
  "found_title": null,
  "found_authors": null,
  "found_venue": null,
  "found_year": null,
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://homepages.cwi.nl/~rdewolf/publ/qc/optimalquantumpac.pdf",
      "https://arxiv.org/pdf/2301.02227",
      "https://jmlr.org/papers/volume19/18-195/18-195.pdf",
      "https://www.cs.cornell.edu/courses/cs6781/2020sp/lectures/06-lower.pdf",
      "https://homepages.cwi.nl/~rdewolf/publ/qc/ccc17_final.pdf"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: User-provided correction: the paper exists at https://zcc1307.github.io/courses/csc665fa19/notes/lower_bound.pdf, so this is a false positive.

<a id="reference-28"></a>
### Reference 28: What makes us smart? core knowledge and natural language (FP)

#### Paper Metadata

- Conference: NEURIPS 2022
- Award/Nomination: Outstanding Paper
- Awarded paper title: Using natural language and program abstractions to instill human inductive biases in machines
- Source paper title in scan: 0113Ef4642264Adc2E6924A3Cbbdf532-Paper-Conference
- Source authors: Unknown
- Source year: 2026
- Source URL: https://proceedings.neurips.cc/paper_files/paper/2022/file/0113ef4642264adc2e6924a3cbbdf532-Paper-Conference.pdf
- Scan report: _workspace/neurips2022/results/scan_report.json

#### Cited Reference Metadata

- Cited title: What makes us smart? core knowledge and natural language
- Cited authors: Elizabeth S Spelke
- Cited year: 2003
- Cited URL:
- Raw reference: Elizabeth S Spelke#What makes us smart? core knowledge and natural language#Language in Mind: Advances in the Study of Language and Thought#2003#
- Scan error type: author

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The paper exists with the correct title and year, but the citation omits two of the three authors (Dedre Gentner and Susan Goldin-Meadow), representing the work as solely by Elizabeth S. Spelke when it is a co-authored work.",
  "link": "https://www.semanticscholar.org/paper/What-makes-us-smart-Core-knowledge-and-natural-Spelke-Gentner/e6ebd66dfd6c5cd8cee0be6745ca2c4d7b3a47e0",
  "found_title": "What makes us smart? Core knowledge and natural language",
  "found_authors": "Elizabeth S. Spelke, Dedre Gentner, Susan Goldin-Meadow",
  "found_venue": "Language in Mind: Advances in the Study of Language and Thought",
  "found_year": "2003",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://direct.mit.edu/books/edited-volume/chapter-pdf/2305231/9780262273664_cak.pdf",
      "https://www.semanticscholar.org/paper/What-makes-us-smart-Core-knowledge-and-natural-Spelke-Gentner/e6ebd66dfd6c5cd8cee0be6745ca2c4d7b3a47e0",
      "https://philpapers.org/rec/SPEWMU",
      "https://www.researchgate.net/publication/375492274_What_Makes_Us_Smart_Core_Knowledge_and_Natural_Language",
      "https://psycnet.apa.org/record/2003-06311-010"
    ],
    "provider": "anthropic"
  },
  "previous_verdict": "UNLIKELY"
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: This appears to be a real Spelke chapter/paper where Gentner and Goldin-Meadow may be editors rather than coauthors; the scan likely over-penalized book-chapter metadata.

<a id="reference-29"></a>
### Reference 29: Openai gym (FP)

#### Paper Metadata

- Conference: NEURIPS 2022
- Award/Nomination: Outstanding Paper
- Awarded paper title: 🏘️ ProcTHOR: Large-Scale Embodied AI Using Procedural Generation
- Source paper title in scan: 27C546Ab1E4F1D7D638E6A8Dfbad9A07-Paper-Conference
- Source authors: Unknown
- Source year: 2026
- Source URL: https://proceedings.neurips.cc/paper_files/paper/2022/file/27c546ab1e4f1d7d638e6a8dfbad9a07-Paper-Conference.pdf
- Scan report: _workspace/neurips2022/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Openai gym
- Cited authors: Wojciech Zaremba
- Cited year: 2016
- Cited URL:
- Raw reference: Wojciech Zaremba#Openai gym#arXiv#2016#
- Scan error type: multiple

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The paper \"OpenAI Gym\" exists with the exact title and was published in 2016 on arXiv. However, the citation lists only Wojciech Zaremba as the author, while the actual paper has seven authors: Greg Brockman, Vicki Cheung, Ludwig Pettersson, Jonas Schneider, John Schulman, Jie Tang, and Wojciech Zaremba. Zaremba is one of the seven co-authors, not the sole author.",
  "link": "https://arxiv.org/abs/1606.01540",
  "found_title": "OpenAI Gym",
  "found_authors": "Greg Brockman, Vicki Cheung, Ludwig Pettersson, Jonas Schneider, John Schulman, Jie Tang, Wojciech Zaremba",
  "found_venue": "arXiv",
  "found_year": "2016",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://arxiv.org/abs/1606.01540v1",
      "https://ui.adsabs.harvard.edu/abs/2016arXiv160601540B/abstract",
      "https://arxiv.org/abs/1606.01540",
      "https://arxiv.org/pdf/1606.01540",
      "https://www.researchgate.net/publication/303822031_OpenAI_Gym"
    ],
    "provider": "anthropic"
  },
  "previous_verdict": "UNLIKELY"
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: User-provided correction: this is an extraction issue; the reference has the correct authors, so it should be marked false positive.

<a id="reference-30"></a>
### Reference 30: Refining the sharp left turn threat model, part 2: applying alignment techniques (FP)

#### Paper Metadata

- Conference: NEURIPS 2023
- Award/Nomination: Outstanding Paper
- Awarded paper title: Are Emergent Abilities of Large Language Models a Mirage?
- Source paper title in scan: Adc98A266F45005C403B8311Ca7E8Bd7-Paper-Conference
- Source authors: Unknown
- Source year: 2026
- Source URL: https://proceedings.neurips.cc/paper_files/paper/2023/file/adc98a266f45005c403b8311ca7e8bd7-Paper-Conference.pdf
- Scan report: _workspace/neurips2023/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Refining the sharp left turn threat model, part 2: applying alignment techniques
- Cited authors: Victoria Krakovna, Vikrant Varma, Ramana Kumar, Mary Phuong
- Cited year: 2022
- Cited URL:
- Raw reference: Victoria Krakovna*Vikrant Varma*Ramana Kumar*Mary Phuong#Refining the sharp left turn threat model, part 2: applying alignment techniques#2022
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The cited reference lists Mary Phuong as an author of Part 2, but the actual Part 2 post credits Rohin Shah instead. Part 1 had Mary Phuong as an author; the reference incorrectly grafts Part 1's author list onto Part 2's title.",
  "link": "https://www.alignmentforum.org/posts/dfXwJh4X5aAcS8gF5/refining-the-sharp-left-turn-threat-model-part-2-applying",
  "found_title": "Refining the Sharp Left Turn threat model, part 2: applying alignment techniques",
  "found_authors": "Victoria Krakovna (Vika), Vikrant Varma, Ramana Kumar, Rohin Shah",
  "found_venue": "AI Alignment Forum",
  "found_year": "2022",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://vkrakovna.wordpress.com/2022/11/25/refining-the-sharp-left-turn-threat-model/",
      "https://www.alignmentforum.org/posts/dfXwJh4X5aAcS8gF5/refining-the-sharp-left-turn-threat-model-part-2-applying",
      "https://www.greaterwrong.com/posts/GNhMPAWcfBCASy8e6/a-central-ai-alignment-problem-capabilities-generalization",
      "https://www.lesswrong.com/posts/usKXS5jGDzjwqv3FJ/refining-the-sharp-left-turn-threat-model",
      "https://www.alignmentforum.org/posts/usKXS5jGDzjwqv3FJ/refining-the-sharp-left-turn-threat-model-part-1-claims-and"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: this is an Alignment Forum web post; website references are now treated as false positives even when the author list is mixed with a related post.

<a id="reference-31"></a>
### Reference 31: Aligning language models to follow instructions (FP)

#### Paper Metadata

- Conference: NEURIPS 2023
- Award/Nomination: Outstanding Paper
- Awarded paper title: Are Emergent Abilities of Large Language Models a Mirage?
- Source paper title in scan: Adc98A266F45005C403B8311Ca7E8Bd7-Paper-Conference
- Source authors: Unknown
- Source year: 2026
- Source URL: https://proceedings.neurips.cc/paper_files/paper/2023/file/adc98a266f45005c403b8311ca7e8bd7-Paper-Conference.pdf
- Scan report: _workspace/neurips2023/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Aligning language models to follow instructions
- Cited authors: Ryan Lowe, Jan Leike
- Cited year: 2022
- Cited URL:
- Raw reference: Ryan Lowe*Jan Leike#Aligning language models to follow instructions#2022
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The cited reference has the wrong title and lists only 2 of 20 actual authors. The actual published paper is \"Training language models to follow instructions with human feedback\" by 20 authors (including Ouyang, Wu, and others), with Ryan Lowe and Jan Leike as co-leads, not sole authors.",
  "link": "https://arxiv.org/pdf/2203.02155",
  "found_title": "Training language models to follow instructions with human feedback",
  "found_authors": "Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul Christiano, Jan Leike, Ryan Lowe",
  "found_venue": "OpenAI",
  "found_year": "2022",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://openai.com/index/instruction-following/",
      "https://arxiv.org/pdf/2203.02155",
      "https://arxiv.org/pdf/2302.05206",
      "https://arxiv.org/pdf/2410.12877",
      "https://arxiv.org/pdf/1508.06491"
    ],
    "provider": "anthropic"
  },
  "previous_verdict": "UNLIKELY"
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: User-provided correction: this references the OpenAI instruction-following blog post with the two cited authors matching (https://openai.com/index/instruction-following/), so it is a false positive.

<a id="reference-32"></a>
### Reference 32: Improving language understanding by generative pre-training (FP)

#### Paper Metadata

- Conference: NEURIPS 2025
- Award/Nomination: Best Paper
- Awarded paper title: 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities
- Source paper title in scan: 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities
- Source authors: Kevin Wang, Ishaan Javali, Michał Bortkiewicz, Tomasz Trzcinski, Benjamin Eysenbach
- Source year: 2025
- Source URL: https://openreview.net/forum?id=s0JVsx3bx1
- Scan report: _workspace/neurips2025/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Improving language understanding by generative pre-training
- Cited authors: A. Radford
- Cited year: 2021
- Cited URL:
- Raw reference: A. Radford#Improving language understanding by generative pre-training#n.d.# A. Radford*J. W. Kim*C. Hallacy*A. Ramesh*A. Goh*S. Agarwal*G. Sastry*A. Askell*P. Mishkin*J. Clark*G. Krueger*I. Sutskever#Learning transferable visual models from natural language supervision#International Conference on Machine Learning#2021#
- Scan error type: multiple

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The reference lists a real paper's title but provides incomplete and incorrect author information (listing only A. Radford instead of all four authors: Radford, Narasimhan, Salimans, and Sutskever) and the wrong publication year (2021 instead of 2018).",
  "link": "https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf",
  "found_title": "Improving Language Understanding by Generative Pre-Training",
  "found_authors": "Alec Radford, Karthik Narasimhan, Tim Salimans, Ilya Sutskever",
  "found_venue": "OpenAI Research",
  "found_year": "2018",
  "source": "deep_hallucination_cache",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf",
      "https://www.semanticscholar.org/paper/Improving-Language-Understanding-by-Generative-Radford-Narasimhan/cd18800a0fe0b668a1cc19f2ec95b5003d0a5035",
      "https://scholar.google.com/citations?user=dOad5HoAAAAJ&hl=en",
      "https://www.freecodecamp.org/news/ai-paper-review-improving-language-understanding-by-generative-pre-training-gpt-1",
      "https://medium.com/@malachy.moran/llm-reading-list-week-2-improving-language-understanding-by-generative-pre-training-b4168cbd7c16",
      "https://www.linkedin.com/pulse/improving-language-understanding-generative-vasilis-kalyvas-7bm3f",
      "https://openai.com/index/language-unsupervised/",
      "https://dl.acm.org/doi/10.5555/3454287.3455457",
      "https://bibbase.org/network/publication/radford-narasimhan-salimans-sutskever-improvinglanguageunderstandingbygenerativepretraining-2018",
      "https://www.topbots.com/ai-nlp-research-pretrained-language-models/"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: The GPT-1 report is real and Radford is the lead author; missing coauthors and wrong year are metadata errors, not a fabricated reference.

<a id="reference-33"></a>
### Reference 33: An analytical theory of power law spectral bias in the learning dynamics of diffusion models (FP)

#### Paper Metadata

- Conference: NEURIPS 2025
- Award/Nomination: Best Paper
- Awarded paper title: Why Diffusion Models Don’t Memorize:  The Role of Implicit Dynamical Regularization in Training
- Source paper title in scan: Why Diffusion Models Don’t Memorize:  The Role of Implicit Dynamical Regularization in Training
- Source authors: Tony Bonnaire, Raphaël Urfin, Giulio Biroli, Marc Mezard
- Source year: 2025
- Source URL: https://openreview.net/forum?id=BSZqpqgqM0
- Scan report: _workspace/neurips2025/results/scan_report.json

#### Cited Reference Metadata

- Cited title: An analytical theory of power law spectral bias in the learning dynamics of diffusion models
- Cited authors: B. Wang
- Cited year: 2025
- Cited URL:
- Raw reference: B. Wang#An analytical theory of power law spectral bias in the learning dynamics of diffusion models#n.d.#2025
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The paper was found on arXiv (2503.03206) with the exact title \"An Analytical Theory of Power Law Spectral Bias in the Learning Dynamics of Diffusion Models\" by Binxu Wang and one co-author. The cited reference lists only \"B. Wang\" as the author when the paper has at least two authors, which is a significant author attribution error. (Verdict corrected: finding the title only as a citation or reference in another paper is not proof that the cited paper has its own dedicated publication page.)",
  "link": "https://arxiv.org/abs/2503.03206",
  "found_title": "An Analytical Theory of Power Law Spectral Bias in the Learning Dynamics of Diffusion Models",
  "found_authors": "Binxu Wang, [one additional co-author]",
  "found_venue": "arXiv (2503.03206)",
  "found_year": "2025",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://arxiv.org/abs/2503.03206",
      "https://arxiv.org/html/2503.03206v1",
      "https://arxiv.org/html/2503.03206v2",
      "https://openreview.net/forum?id=SDhOClkyqC",
      "https://neurips.cc/virtual/2025/loc/san-diego/poster/117950"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: the arXiv paper is otherwise identifiable and the issue is omission of a single coauthor, so the requested single-author-omission rule makes this a false positive.

<a id="reference-34"></a>
### Reference 34: Wolfram|alpha as the computation engine for gpt models (FP)

#### Paper Metadata

- Conference: NEURIPS 2025
- Award/Nomination: Best Paper Runner-up
- Awarded paper title: Superposition Yields Robust Neural Scaling
- Source paper title in scan: Superposition Yields Robust Neural Scaling
- Source authors: Yizhou Liu, Ziming Liu, Jeff Gore
- Source year: 2025
- Source URL: https://openreview.net/forum?id=knPz7gtjPW
- Scan report: _workspace/neurips2025/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Wolfram|alpha as the computation engine for gpt models
- Cited authors: Stephen Wolfram
- Cited year: 2023
- Cited URL: https://www.wolfram.com/wolfram-alpha-openai-plugin
- Raw reference: Stephen Wolfram#Wolfram|alpha as the computation engine for gpt models#2023#https://www.wolfram.com/wolfram-alpha-openai-plugin
- Scan error type: multiple

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The cited title does not match any publication exactly. A closely related article by Stephen Wolfram from January 2023 with a different title exists at a different URL, but the specific cited title and URL do not correspond to any published work.",
  "link": null,
  "found_title": null,
  "found_authors": null,
  "found_venue": null,
  "found_year": null,
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://writings.stephenwolfram.com/2023/01/wolframalpha-as-the-way-to-bring-computational-knowledge-superpowers-to-chatgpt/",
      "https://intuitionlabs.ai/articles/symbolic-ai-vs-generative-ai-wolfram-chatgpt",
      "https://writings.stephenwolfram.com/2023/03/chatgpt-gets-its-wolfram-superpowers/",
      "https://gpt.wolfram.com/",
      "https://www.packtpub.com/en-us/learning/how-to-tutorials/unleashing-the-power-of-wolfram-alpha-api-with-python-and-chatgpt"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: this is a web-site/webpage-style reference to Wolfram content, so the requested website-source rule makes it a false positive.

<a id="reference-35"></a>
### Reference 35: Return after free discussion (FP)

#### Paper Metadata

- Conference: USENIX Security 2021
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: Rage Against the Machine Clear: A Systematic Analysis of Machine Clears and Their Implications for Transient Execution Attacks
- Source paper title in scan: Sec21-Ragab
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/sec21-ragab.pdf
- Scan report: _workspace/usenix-security2021/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Return after free discussion
- Cited authors: Thomas Dullien
- Cited year: 2020
- Cited URL: https://twitter.com/halvarflake/status/1273220345525415937
- Raw reference: Thomas Dullien#Return after free discussion#n.d.#2020#https://twitter.com/halvarflake/status/1273220345525415937
- Scan error type: multiple

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "No paper titled \"Return after free discussion\" by Thomas Dullien was found in any academic database or dedicated publication page. Thomas Dullien is a real researcher, but this specific work does not appear to exist as a published paper.",
  "link": null,
  "found_title": null,
  "found_authors": null,
  "found_venue": null,
  "found_year": null,
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.elastic.co/blog/author/thomas-dullien",
      "https://www.crunchbase.com/person/thomas-dullien",
      "https://www.researchgate.net/profile/Thomas-Dullien-3",
      "https://orcid.org/0000-0003-2368-3898",
      "https://www.infoq.com/profile/Thomas-Dullien/"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: this is a social-media/web discussion reference, so under the requested website-source rule it is a false positive.

<a id="reference-36"></a>
### Reference 36: block_speculation function call in invoke_stub (FP)

#### Paper Metadata

- Conference: USENIX Security 2021
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: Rage Against the Machine Clear: A Systematic Analysis of Machine Clears and Their Implications for Transient Execution Attacks
- Source paper title in scan: Sec21-Ragab
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/sec21-ragab.pdf
- Scan report: _workspace/usenix-security2021/results/scan_report.json

#### Cited Reference Metadata

- Cited title: block_speculation function call in invoke_stub
- Cited authors: Xen Hypervisor
- Cited year:
- Cited URL: https://xenbits.xen.org/gitweb/?p=xen.git;a=blob;f=xen/arch/x86/x86_emulate/x86_emulate.c;hb=HEAD
- Raw reference: Xen Hypervisor#block_speculation function call in invoke_stub#n.d.#n.d.#https://xenbits.xen.org/gitweb/?p=xen.git;a=blob;f=xen/arch/x86/x86_emulate/x86_emulate.c;hb=HEAD
- Scan error type: multiple

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "No paper with the exact title \"block_speculation function call in invoke_stub\" exists in any academic database or public online source. The title appears to be a source code artifact description rather than a publication, and the cited URL is to a Xen source code file, not a published paper or documentation.",
  "link": null,
  "found_title": null,
  "found_authors": null,
  "found_venue": null,
  "found_year": null,
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://github.com/sinonjs/sinon/issues/118",
      "https://cinish.medium.com/sinon-stubs-e373424b548b",
      "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5526491",
      "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5701415",
      "http://google.github.io/googletest/gmock_cook_book.html"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: this is a reference to a Xen source-code file, and the requested code-file rule makes it a false positive.

<a id="reference-37"></a>
### Reference 37: block_speculation function call in io_emul_stub_setup (FP)

#### Paper Metadata

- Conference: USENIX Security 2021
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: Rage Against the Machine Clear: A Systematic Analysis of Machine Clears and Their Implications for Transient Execution Attacks
- Source paper title in scan: Sec21-Ragab
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/sec21-ragab.pdf
- Scan report: _workspace/usenix-security2021/results/scan_report.json

#### Cited Reference Metadata

- Cited title: block_speculation function call in io_emul_stub_setup
- Cited authors: Xen Hypervisor
- Cited year:
- Cited URL: https://xenbits.xen.org/gitweb/?p=xen.git;a=blob;f=xen/arch/x86/pv/emul-priv-op.c;hb=HEAD
- Raw reference: Xen Hypervisor#block_speculation function call in io_emul_stub_setup#n.d.#n.d.#https://xenbits.xen.org/gitweb/?p=xen.git;a=blob;f=xen/arch/x86/pv/emul-priv-op.c;hb=HEAD
- Scan error type: multiple

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "No paper with this title exists. The citation appears to reference Xen source code rather than an academic publication, with \"Xen Hypervisor\" as an inappropriate author attribution for what would be a paper.",
  "link": null,
  "found_title": null,
  "found_authors": null,
  "found_venue": null,
  "found_year": null,
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.mail-archive.com/xen-devel@lists.xenproject.org/msg199326.html",
      "https://wiki.archlinux.org/title/Xen",
      "https://xenbits.xen.org/docs/unstable/misc/xen-command-line.html",
      "https://xenbits.xen.org/docs/4.5-testing/misc/xen-command-line.html",
      "https://lore.kernel.org/all/20200616175913.7368-1-julien@xen.org/T/"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: this is another Xen source-code file reference, so it is a false positive under the requested code-file rule.

<a id="reference-38"></a>
### Reference 38: Intel deep-dive: snoop-assisted L1 Data Sampling (FP)

#### Paper Metadata

- Conference: USENIX Security 2021
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: Rage Against the Machine Clear: A Systematic Analysis of Machine Clears and Their Implications for Transient Execution Attacks
- Source paper title in scan: Sec21-Ragab
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/sec21-ragab.pdf
- Scan report: _workspace/usenix-security2021/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Intel deep-dive: snoop-assisted L1 Data Sampling
- Cited authors: Pawel Wieczorkiewicz
- Cited year:
- Cited URL:
- Raw reference: Pawel Wieczorkiewicz#Intel deep-dive: snoop-assisted L1 Data Sampling#n.d.#n.d.#
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "No published reference with the exact title \"Intel deep-dive: snoop-assisted L1 Data Sampling\" by Pawel Wieczorkiewicz was found in web search results, though the Snoop-assisted L1 Data Sampling vulnerability itself is real and was discovered by Wieczorkiewicz.",
  "link": null,
  "found_title": null,
  "found_authors": null,
  "found_venue": null,
  "found_year": null,
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.msn.com/en-us/news/technology/intel-cpus-vulnerable-to-new-snoop-attack/ar-BB11gZMs?ocid=FinanceShimLayer",
      "https://malwaretips.com/threads/intel-cpus-vulnerable-to-new-snoop-attack.99125/",
      "https://lacomparacion.com/en/Intel-processors-threatened-by-the-new-snoop-attack/",
      "https://www.techradar.com/news/intel-cpus-at-risk-from-new-snoop-attack",
      "https://www.techzine.eu/news/security/45633/intel-cpus-vulnerable-to-new-snoop-attack/"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: this is best treated as a web/technical-page reference rather than a paper, so the requested website-source rule makes it false positive.

<a id="reference-39"></a>
### Reference 39: The Eavesdropper’s Dilemma (FP)

#### Paper Metadata

- Conference: USENIX Security 2021
- Award/Nomination: Distinguished Paper Award Winner and Third Prize winner of the 2021 Internet Defense Prize
- Awarded paper title: Weaponizing Middleboxes for TCP Reflected Amplification
- Source paper title in scan: Sec21-Bock
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/sec21-bock.pdf
- Scan report: _workspace/usenix-security2021/results/scan_report.json

#### Cited Reference Metadata

- Cited title: The Eavesdropper’s Dilemma
- Cited authors: Eric Cronin, Micah Sherr, Matthew A. Blaze
- Cited year: 2006
- Cited URL:
- Raw reference: Eric Cronin*Micah Sherr*Matthew A. Blaze#The Eavesdropper’s Dilemma#Technical report, Penn Engineering#2006#
- Scan error type: author

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The paper exists and is verifiable, but the cited second author name \"Micah Sherr\" does not match the actual author \"Michael E. Sherr\" found in the paper's official database entry. (Verdict corrected: the cited author list has low overlap with the verified paper, and the LLM did not provide found authors that substantially match the cited authors. A real title with fabricated coauthors is treated as hallucinated.)",
  "link": "https://www.semanticscholar.org/paper/The-Eavesdropper's-Dilemma-Cronin-Sherr/f4581c9e598403622a308ca943a5ab565fa2e758",
  "found_title": "The Eavesdropper's Dilemma",
  "found_authors": "Eric Cronin, Michael E. Sherr, Matt Blaze",
  "found_venue": "Technical report (IFIP International Conference on Digital Forensics)",
  "found_year": "2006",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.semanticscholar.org/paper/The-Eavesdropper's-Dilemma-Cronin-Sherr/f4581c9e598403622a308ca943a5ab565fa2e758",
      "https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=fd67bc1c7f87a2ddfdbb827294b3fd49cd0bb4fb"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: The cited paper exists and “Micah” versus “Michael E.” Sherr looks like a name/metadata error, not a hallucinated reference.

<a id="reference-40"></a>
### Reference 40: North American, Western and Central Europe: AIDS epidemic update regional summary (FP)

#### Paper Metadata

- Conference: USENIX Security 2021
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: “It’s stressful having all these phones”:
- Source paper title in scan: Sec21-Mcdonald
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/sec21-mcdonald.pdf
- Scan report: _workspace/usenix-security2021/results/scan_report.json

#### Cited Reference Metadata

- Cited title: North American, Western and Central Europe: AIDS epidemic update regional summary
- Cited authors: Joint United Nations Programme on HIV/AIDS (UNAIDS), Data UNAIDS, et al
- Cited year: 2019
- Cited URL:
- Raw reference: Joint United Nations Programme on HIV/AIDS (UNAIDS)*Data UNAIDS*et al.#North American, Western and Central Europe: AIDS epidemic update regional summary#n.d.#2019
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "No document with the exact title \"North American, Western and Central Europe: AIDS epidemic update regional summary\" was found in web search results, despite evidence that UNAIDS published regional summaries and estimates for 2019 using different title formats.",
  "link": null,
  "found_title": null,
  "found_authors": null,
  "found_venue": null,
  "found_year": null,
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.unaids.org/en/resources/documents/2024/2024-unaids-global-aids-update-western-central-europe-north-america",
      "https://pmc.ncbi.nlm.nih.gov/articles/PMC6919222/",
      "https://www.unaids.org/sites/default/files/media_asset/2024-unaids-global-aids-update-western-central-europe-north-america_en.pdf",
      "https://www.unaids.org/sites/default/files/media_asset/2019-UNAIDS-data_en.pdf",
      "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6202722/"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: this is an institutional web/report-style reference rather than a paper, so under the requested website-source rule it is false positive.

<a id="reference-41"></a>
### Reference 41: 2020 Campaigns Remain Vulnerable as Signs of Russian Hackers Re-Emerge (FP)

#### Paper Metadata

- Conference: USENIX Security 2021
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: “Why wouldn’t someone think of democracy as a target?”: Security practices & challenges of people involved with U.S. political campaigns
- Source paper title in scan: Sec21-Consolvo
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/sec21-consolvo.pdf
- Scan report: _workspace/usenix-security2021/results/scan_report.json

#### Cited Reference Metadata

- Cited title: 2020 Campaigns Remain Vulnerable as Signs of Russian Hackers Re-Emerge
- Cited authors: D. Volz, T. Parti
- Cited year: 2019
- Cited URL: https://www.wsj.com/articles/presidential-campaigns-remain-vulnerable-on-cybersecurity-11560448372
- Raw reference: D. Volz*T. Parti#2020 Campaigns Remain Vulnerable as Signs of Russian Hackers Re-Emerge#n.d.#2019#https://www.wsj.com/articles/presidential-campaigns-remain-vulnerable-on-cybersecurity-11560448372
- Scan error type: multiple

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "No web page with this exact title and author combination was found. While Dustin Volz is a confirmed WSJ cybersecurity reporter, the cited URL does not exist and no evidence was found of an article co-authored by Volz and \"T. Parti\" with this exact title.",
  "link": null,
  "found_title": null,
  "found_authors": null,
  "found_venue": null,
  "found_year": null,
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.npr.org/2020/09/11/911828426/microsoft-warns-russian-spies-who-hacked-2016-election-are-back",
      "https://www.technologyreview.com/2020/09/10/1008297/the-russian-hackers-who-interfered-in-2016-were-spotted-targeting-the-2020-us-election/",
      "https://www.technologyreview.com/2020/09/10/1008297/the-russian-hackers-who-interfered-in-2016-were-spotted-targeting-the-2020-us-election/amp",
      "https://cyberpress.org/russian-hackers-phishing-campaigns/",
      "https://talkingbiznews.com/media-news/wsj-wins-award-for-cybersecurity-coverage/"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: this is a newspaper article reference, and newspaper articles are now to be marked false positive.

<a id="reference-42"></a>
### Reference 42: Borderline-smote: A new over-sampling method in imbalanced data sets learning (FP)

#### Paper Metadata

- Conference: USENIX Security 2022
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: Dos and Don’ts of Machine Learning in Computer Security
- Source paper title in scan: Sec22-Arp
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/sec22-arp.pdf
- Scan report: _workspace/usenix-security2022/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Borderline-smote: A new over-sampling method in imbalanced data sets learning
- Cited authors: H. Han, W.-Y . Wang, B.-H. Mao
- Cited year: 2005
- Cited URL:
- Raw reference: H. Han*W.-Y . Wang*B.-H. Mao#Borderline-smote: A new over-sampling method in imbalanced data sets learning#Advances in Intelligent Computing#2005
- Scan error type: author

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The paper exists and was found with a matching title and substantially matching authors. The cited author \"W.-Y. Wang\" matches the full name \"Wen-Yuan Wang\" (or \"Wenyuan Wang\") shown on the official publication, which is a minor formatting variation. The venue is correctly identified as \"Advances in Intelligent Computing,\" published by Springer in the proceedings of the 2005 International Conference on Intelligent Computing. This is a real, well-documented paper with a permanent DOI. (Verdict corrected: the cited author list has low overlap with the verified paper, and the LLM did not provide found authors that substantially match the cited authors. A real title with fabricated coauthors is treated as hallucinated.)",
  "link": "https://link.springer.com/chapter/10.1007/11538059_91",
  "found_title": "Borderline-SMOTE: A New Over-Sampling Method in Imbalanced Data Sets Learning",
  "found_authors": "Han H., Wang W.Y., Mao B.H.",
  "found_venue": "Advances in Intelligent Computing, Proceedings of the 2005 International Conference on Intelligent Computing",
  "found_year": "2005",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.scirp.org/reference/referencespapers?referenceid=1603045",
      "https://link.springer.com/chapter/10.1007/11538059_91",
      "https://rdrr.io/cran/smotefamily/man/BLSMOTE.html",
      "https://rdrr.io/cran/SMOTEWB/man/BLSMOTE.html",
      "https://sci2s.ugr.es/keel/pdf/specific/congreso/han_borderline_smote.pdf"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Borderline-SMOTE is real and W.-Y. Wang matches Wen-Yuan/Wenyuan Wang; this is a false positive due to name normalization.

<a id="reference-43"></a>
### Reference 43: Worldwide Security and Information Event Management Market Shares, 2020: SaaS-Focused Rise (FP)

#### Paper Metadata

- Conference: USENIX Security 2022
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: Faster Yet Safer: Logging System Via Fixed-Key Blockcipher
- Source paper title in scan: Sec22-Hoang
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/sec22-hoang.pdf
- Scan report: _workspace/usenix-security2022/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Worldwide Security and Information Event Management Market Shares, 2020: SaaS-Focused Rise
- Cited authors: Michelle Abraham, Christopher Kissel
- Cited year: 2020
- Cited URL:
- Raw reference: Michelle Abraham*Christopher Kissel#Worldwide Security and Information Event Management Market Shares, 2020: SaaS-Focused Rise#Technical report, Splunk#2020#
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The cited authors (Michelle Abraham and Christopher Kissel) are IDC researchers who published SIEM market share reports in 2020, but the cited venue is incorrect—these reports are from IDC, not from Splunk. The exact title matching a Splunk publication cannot be verified and appears to be a misattribution.",
  "link": null,
  "found_title": null,
  "found_authors": null,
  "found_venue": null,
  "found_year": null,
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.mordorintelligence.com/industry-reports/global-security-information-and-event-management",
      "https://www.alliedmarketresearch.com/security-information-and-event-management-market",
      "https://www.globenewswire.com/news-release/2023/10/30/2769365/0/en/Security-Information-and-Event-Management-Market-Size-worth-9-91-Billion-Globally-by-2030-Exclusive-Report-by-The-Insight-Partners.html",
      "https://www.kbvresearch.com/security-information-event-management-market/",
      "https://www.marketsandmarkets.com/Market-Reports/security-information-event-management-market-183343191.html"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: this is a market-report/web-report style source, so under the requested website-source rule I mark it false positive.

<a id="reference-44"></a>
### Reference 44: Reproducibility by Ontological representation of Provenance (FP)

#### Paper Metadata

- Conference: USENIX Security 2022
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: Faster Yet Safer: Logging System Via Fixed-Key Blockcipher
- Source paper title in scan: Sec22-Hoang
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/sec22-hoang.pdf
- Scan report: _workspace/usenix-security2022/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Reproducibility by Ontological representation of Provenance
- Cited authors: Richard Roth
- Cited year: 2018
- Cited URL:
- Raw reference: Richard Roth#Reproducibility by Ontological representation of Provenance#Master’s thesis, TU Wien#2018
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The thesis with this exact title by Richard Roth was not found in web search results or any of the major academic databases. No dedicated page for this master's thesis could be located despite targeted searches for the title and author.",
  "link": null,
  "found_title": null,
  "found_authors": null,
  "found_venue": null,
  "found_year": null,
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.sciencedirect.com/science/article/abs/pii/S1570826811000163",
      "https://pmc.ncbi.nlm.nih.gov/articles/PMC12376154/",
      "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8734275/",
      "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12376154/",
      "https://pubmed.ncbi.nlm.nih.gov/34991705/"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: User-provided correction: the thesis reference is correct and exists at TU Wien (https://repositum.tuwien.at/handle/20.500.12708/3505?mode=full), so it is a false positive.

<a id="reference-45"></a>
### Reference 45: Elkhound: A fast, practical glr parser generator (FP)

#### Paper Metadata

- Conference: USENIX Security 2022
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: FixReverter: A Realistic Bug Injection Methodology for Benchmarking Fuzz Testing
- Source paper title in scan: Sec22-Zhang-Zenong
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/sec22-zhang-zenong.pdf
- Scan report: _workspace/usenix-security2022/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Elkhound: A fast, practical glr parser generator
- Cited authors: S. G. McPeak
- Cited year: 2003
- Cited URL:
- Raw reference: S. G. McPeak#Elkhound: A fast, practical glr parser generator#Tech. Rep.#2003#
- Scan error type: multiple

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The cited reference lists only \"S. G. McPeak\" as author and \"Tech. Rep.\" as venue, but the published conference version has two authors (McPeak and Necula) and was published at the International Conference on Compiler Construction, not as a standalone technical report. The reference conflates the 2002 technical report (single author) with the 2003/2004 conference publication (two authors), creating a fabricated author attribution.",
  "link": "https://link.springer.com/chapter/10.1007/978-3-540-24723-4_6",
  "found_title": "Elkhound: A Fast, Practical GLR Parser Generator",
  "found_authors": "Scott McPeak, George C. Necula",
  "found_venue": "International Conference on Compiler Construction",
  "found_year": "2004",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www2.eecs.berkeley.edu/Pubs/TechRpts/2002/6187.html",
      "https://www2.eecs.berkeley.edu/Pubs/TechRpts/2002/CSD-02-1214.pdf",
      "https://dl.acm.org/doi/10.5555/894195",
      "https://www.semanticscholar.org/paper/Elkhound:-A-Fast,-Practical-GLR-Parser-Generator-McPeak-Necula/e41b70c409c1c4d40c94638d1aa0697a79e845c9",
      "https://osq.cs.berkeley.edu/public/McPeak-Elkhound.ppt"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Elkhound exists as both technical-report and conference forms; the citation conflates venue/version metadata but points to a real work.

<a id="reference-46"></a>
### Reference 46: Discreet log (FP)

#### Paper Metadata

- Conference: USENIX Security 2022
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: Private Signaling
- Source paper title in scan: Sec22-Madathil
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/sec22-madathil.pdf
- Scan report: _workspace/usenix-security2022/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Discreet log
- Cited authors: Sarah Lewis
- Cited year:
- Cited URL:
- Raw reference: Sarah Lewis#Discreet log #1: Anonymity, bandwidth and fuzzytags#n.d.#
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "\"Discreet Log\" is a technical development blog series by Open Privacy Research Society, not a standalone academic paper. The reference conflates a blog post title with a publication venue, and the author is Sarah Jamie Lewis, not \"Sarah Lewis.\"",
  "link": "https://openprivacy.ca/discreet-log/01-anonymity-bandwidth-and-fuzzytags/",
  "found_title": "Discreet Log #1: Anonymity, Bandwidth and Fuzzytags",
  "found_authors": "Sarah Jamie Lewis",
  "found_venue": "Open Privacy Research Society (blog)",
  "found_year": "2020",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://openprivacy.ca/discreet-log/19-cwtch-roadmap/",
      "https://www.openprivacy.ca/discreet-log/10-cwtch-beta-and-beyond/",
      "https://openprivacy.ca/discreet-log/13-metadata-resistant-filesharing/",
      "https://openprivacy.ca/discreet-log/16-cwtch-secure-development-handboook/",
      "https://openprivacy.ca/discreet-log/22-building-on-cwtch-2022/"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: this is a technical blog/web series, so the requested website-source rule makes it a false positive.

<a id="reference-47"></a>
### Reference 47: Position paper: Bringing memory safety to WebAssembly (FP)

#### Paper Metadata

- Conference: USENIX Security 2022
- Award/Nomination: Distinguished Paper Award Winner and Second Prize Winner (tie) of the 2022 Internet Defense Prize
- Awarded paper title: Provably-Safe Multilingual Software Sandboxing using WebAssembly
- Source paper title in scan: Sec22-Bosamiya
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/sec22-bosamiya.pdf
- Scan report: _workspace/usenix-security2022/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Position paper: Bringing memory safety to WebAssembly
- Cited authors: Craig Disselkoen, John Renner, Conrad Watt, Tal Garfinkel, Amit Levy, Deian Stefan
- Cited year: 2019
- Cited URL:
- Raw reference: Craig Disselkoen*John Renner*Conrad Watt*Tal Garfinkel*Amit Levy*Deian Stefan#Position paper: Bringing memory safety to WebAssembly#Hardware and Architectural Support for Security and Privacy (HASP)#2019
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The paper by these authors on WebAssembly memory safety exists, but the cited title is incorrect. The actual published title is \"Position Paper: Progressive Memory Safety for WebAssembly,\" not \"Bringing memory safety to WebAssembly.\"",
  "link": "https://dl.acm.org/doi/10.1145/3337167.3337171",
  "found_title": "Position Paper: Progressive Memory Safety for WebAssembly",
  "found_authors": "Craig Disselkoen, John Renner, Conrad Watt, Tal Garfinkel, Amit Levy, Deian Stefan",
  "found_venue": "Hardware and Architectural Support for Security and Privacy (HASP)",
  "found_year": "2019",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.researchgate.net/publication/333988764_Position_Paper_Progressive_Memory_Safety_for_WebAssembly",
      "https://cseweb.ucsd.edu/~dstefan/pubs/disselkoen:2019:ms-wasm.pdf",
      "https://dl.acm.org/doi/10.1145/3571208",
      "https://www.semanticscholar.org/paper/Position-Paper:-Progressive-Memory-Safety-for-Disselkoen-Renner/87d8a94f2d2d56d813b9edff13007d324d0c6c67",
      "https://sns.cs.princeton.edu/assets/papers/2019-hasp-disselkoen.pdf"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: User-provided correction: the paper exists at https://www.amitlevy.com/papers/ms-wasm-hasp19.pdf, so this should be marked false positive.

<a id="reference-48"></a>
### Reference 48: Democracy Suite EMS Results Tally & Reporting user guide, version 5.5::16 (FP)

#### Paper Metadata

- Conference: USENIX Security 2022
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: The Antrim County 2020 Election Incident: An Independent Forensic Investigation
- Source paper title in scan: Sec22-Halderman
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/sec22-halderman.pdf
- Scan report: _workspace/usenix-security2022/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Democracy Suite EMS Results Tally & Reporting user guide, version 5.5::16
- Cited authors: Dominion Voting Systems
- Cited year: 2017
- Cited URL:
- Raw reference: Dominion Voting Systems#Democracy Suite EMS Results Tally & Reporting user guide, version 5.5::16#Dominion Voting Systems#2017#
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "No web search found a Democracy Suite EMS Results Tally & Reporting user guide with version 5.5::16; available versions found include 5.0, 5.11-CO, 5.13, 5.17-CO, and a 5.5-A Implementation Statement, but not this specific version designation.",
  "link": null,
  "found_title": null,
  "found_authors": null,
  "found_venue": null,
  "found_year": null,
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.sos.state.co.us/pubs/elections/VotingSystems/DVS-DemocracySuite517/documentation/UGRTRUserGuide5-17CO.pdf",
      "https://votingsystems.cdn.sos.ca.gov/vendors/dominion/ds52remote.pdf",
      "https://www.johnscreekpost.com/wp-content/uploads/2020/11/UG-RTR-UserGuide-5-11-CO.pdf",
      "https://www.coloradosos.gov/pubs/elections/VotingSystems/DVS-DemocracySuite513/documentation/UG-RTR-UserGuide-5-13.pdf",
      "https://www.eac.gov/sites/default/files/voting_system/files/Attachment_A_-_Dominion_D-Suite_5.5-A_Implementation_Statement.pdf"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: User-provided correction: this is likely a false positive, so I treat it as a real/acceptable non-paper technical reference rather than a hallucinated citation.

<a id="reference-49"></a>
### Reference 49: Project infinity (FP)

#### Paper Metadata

- Conference: USENIX Security 2023
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: BotScreen: Trust Everybody, but Cut the Aimbots Yourself
- Source paper title in scan: Usenixsecurity23-Choi
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/usenixsecurity23-choi.pdf
- Scan report: _workspace/usenix-security2023/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Project infinity
- Cited authors: Hype
- Cited year: 2022
- Cited URL: https://project-infinity.cloud/#2022
- Raw reference: Hype#Project infinity#https://project-infinity.cloud/#2022
- Scan error type: multiple

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "No academic paper titled \"Project infinity\" by author \"Hype\" exists. The URL resolves to a gaming cheat website where \"Hype\" is a forum username, not an academic work.",
  "link": null,
  "found_title": null,
  "found_authors": null,
  "found_venue": null,
  "found_year": null,
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://project-infinity.cloud/",
      "https://www.curseforge.com/minecraft/modpacks/project-infinity-0-1",
      "https://vetygt.itch.io/project-infinity",
      "https://www.fraseryachts.com/en/yacht/project-infinity/",
      "https://github.com/ALIENQuake/ProjectInfinity"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: this is a gaming-cheat website/forum reference, and website references are now false positives by policy.

<a id="reference-50"></a>
### Reference 50: Cyber Crimes in Jordan: A Legal Assessment on the Effectiveness of Information System Crimes Law No (30) of (FP)

#### Paper Metadata

- Conference: USENIX Security 2023
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: Examining Power Dynamics and User Privacy in Smart Technology Use Among Jordanian Households
- Source paper title in scan: Usenixsecurity23-Albayaydh
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/usenixsecurity23-albayaydh.pdf
- Scan report: _workspace/usenix-security2023/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Cyber Crimes in Jordan: A Legal Assessment on the Effectiveness of Information System Crimes Law No (30) of
- Cited authors: R. S. A. Faqir
- Cited year: 2010
- Cited URL:
- Raw reference: R. S. A. Faqir#Cyber Crimes in Jordan: A Legal Assessment on the Effectiveness of Information System Crimes Law No (30) of 2010#n.d. U. N. Foundation#About the Universal Declaration of Human Rights, Curated Article#n.d.#2017
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The paper exists but with significant metadata mismatches: it was published in 2013 in the International Journal of Cyber Criminology, not in 2010 by \"n.d. U. N. Foundation.\" The title matches exactly, but the publication venue and year are incorrect.",
  "link": "http://www.cybercrimejournal.com/Faqir2013janijcc.pdf",
  "found_title": "Cyber Crimes in Jordan: A Legal Assessment on the Effectiveness of Information System Crimes Law No (30) of 2010",
  "found_authors": "Raed Faqir",
  "found_venue": "International Journal of Cyber Criminology",
  "found_year": "2013",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.researchgate.net/publication/298462830_Cyber_crimes_in_jordan_A_legal_assessment_on_the_effectiveness_of_information_system_crimes_law_no_30_of_2010",
      "https://www.cell.com/heliyon/fulltext/S2405-8440(24)08402-0",
      "https://medium.com/@yazankhalaf766/cyber-crimes-in-jordan-c2e653a38270",
      "https://www.academia.edu/38286288/Cyber_Crimes_and_Technical_Issues_under_the_Jordanian_Information_System_Crimes_Law",
      "https://www.researchgate.net/publication/271061650_Cyber_Crimes_and_Technical_Issues_under_the_Jordanian_Information_System_Crimes_Law"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: The Jordan cyber-crimes paper exists with the same title and author; year/venue mismatches are metadata errors.

<a id="reference-51"></a>
### Reference 51: New Data Protection Bill, Draft (FP)

#### Paper Metadata

- Conference: USENIX Security 2023
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: Examining Power Dynamics and User Privacy in Smart Technology Use Among Jordanian Households
- Source paper title in scan: Usenixsecurity23-Albayaydh
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/usenixsecurity23-albayaydh.pdf
- Scan report: _workspace/usenix-security2023/results/scan_report.json

#### Cited Reference Metadata

- Cited title: New Data Protection Bill, Draft
- Cited authors: J. Modee
- Cited year: 2021
- Cited URL:
- Raw reference: J. Modee#New Data Protection Bill, Draft#Ministry of Digital Economy And Entrepreneurship, Jordan#2021#
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "No paper titled \"New Data Protection Bill, Draft\" authored by J. Modee was found in any academic database or web search. While Jordan's 2021 Data Protection Draft Law is real and well-documented, it is not attributed to an author named \"J. Modee\" in any official government source or policy analysis.",
  "link": null,
  "found_title": null,
  "found_authors": null,
  "found_venue": null,
  "found_year": null,
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.dataguidance.com/jurisdictions/jordan",
      "https://iapp.org/news/a/jordans-senate-approves-draft-personal-data-protection-law/",
      "https://globalvoices.org/2022/02/21/jordans-personal-data-protection-draft-bill-is-it-enough/",
      "https://www.accessnow.org/wp-content/uploads/2022/05/Access-Now-Policy-Brief_Jordan-Data-Protection-bill-vs-GDPR.pdf",
      "https://legacy.dataguidance.com/opinion/jordan-overview-draft-data-protection-bill"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: User-provided correction: this is likely a real government document, so it should be treated as a false positive rather than a hallucinated reference.

<a id="reference-52"></a>
### Reference 52: JORDANIAN PEOPLE PERSPECTIVE ABOUT SMART HOMES (FP)

#### Paper Metadata

- Conference: USENIX Security 2023
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: Examining Power Dynamics and User Privacy in Smart Technology Use Among Jordanian Households
- Source paper title in scan: Usenixsecurity23-Albayaydh
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/usenixsecurity23-albayaydh.pdf
- Scan report: _workspace/usenix-security2023/results/scan_report.json

#### Cited Reference Metadata

- Cited title: JORDANIAN PEOPLE PERSPECTIVE ABOUT SMART HOMES
- Cited authors: A. Shehadeh, S. Sarhan
- Cited year: 2022
- Cited URL:
- Raw reference: A. Shehadeh*S. Sarhan#JORDANIAN PEOPLE PERSPECTIVE ABOUT SMART HOMES#n.d.# S. Smex#Will the New Jordanian Law Protect Personal Data?#News#2022#
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "No paper with this exact title and author combination was found in academic databases or web search results, despite multiple similar papers on Jordanian smart home perspectives published around 2022.",
  "link": null,
  "found_title": null,
  "found_authors": null,
  "found_venue": null,
  "found_year": null,
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.homes-jordan.com/en/blogs/detail/the-smart-homes",
      "https://www.sciencedirect.com/science/article/abs/pii/S0160791X18300484",
      "https://www.statista.com/outlook/cmo/smart-home/jordan",
      "https://www.researchgate.net/publication/340914490_Factors_influencing_the_acceptance_of_smart_homes_in_Jordan",
      "https://www.researchgate.net/publication/357858334_Enhancing_Smart_System_Platforms_Factors_Affecting_People's_Intentions_Toward_Smart_Homes_in_Jordan"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: User-provided correction: this is likely a real government document, so it should be treated as a false positive rather than a hallucinated reference.

<a id="reference-53"></a>
### Reference 53: What does the rise of AI mean for the future of art? (FP)

#### Paper Metadata

- Conference: USENIX Security 2023
- Award/Nomination: Distinguished Paper Award Winner and Co-Winner of the 2023 Internet Defense Prize
- Awarded paper title: Glaze: Protecting Artists from Style Mimicry by Text-to-Image Models
- Source paper title in scan: Usenixsecurity23-Shan
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/usenixsecurity23-shan.pdf
- Scan report: _workspace/usenix-security2023/results/scan_report.json

#### Cited Reference Metadata

- Cited title: What does the rise of AI mean for the future of art?
- Cited authors: E. Flux
- Cited year: 2022
- Cited URL:
- Raw reference: E. Flux#What does the rise of AI mean for the future of art?#Sydney Morning Herald#2022#
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "No dedicated Sydney Morning Herald article page was found with this exact title and author. While an article with a similar title is referenced in secondary sources, the author \"E. Flux\" cannot be verified, and no direct link to the original Sydney Morning Herald piece exists.",
  "link": null,
  "found_title": null,
  "found_authors": null,
  "found_venue": null,
  "found_year": null,
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://cfvts.org/18203/teen-scene/bc-early-college-high-school/ai-art-is-dangerous-for-artists-and-their-careers-in-the-future/",
      "https://www.aifire.co/p/the-ultimate-art-ai-generator-why-flux-1-is-a-game-changer",
      "https://flux-ai.ai/blog/how-ai-and-technology-are-shaping-creativity",
      "https://www.e-flux.com/criticism/650116/value-in-garbage-out-on-ai-art-and-hegemony",
      "https://www.e-flux.com/architecture/intensification/6782975/eating-the-future-the-metabolic-logic-of-ai-slop"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: this is a newspaper/news-article reference, so under the requested newspaper-article rule it is false positive.

<a id="reference-54"></a>
### Reference 54: AI art & the ethical concerns of artists (FP)

#### Paper Metadata

- Conference: USENIX Security 2023
- Award/Nomination: Distinguished Paper Award Winner and Co-Winner of the 2023 Internet Defense Prize
- Awarded paper title: Glaze: Protecting Artists from Style Mimicry by Text-to-Image Models
- Source paper title in scan: Usenixsecurity23-Shan
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/usenixsecurity23-shan.pdf
- Scan report: _workspace/usenix-security2023/results/scan_report.json

#### Cited Reference Metadata

- Cited title: AI art & the ethical concerns of artists
- Cited authors: V. Fox
- Cited year: 2023
- Cited URL:
- Raw reference: V. Fox#AI art & the ethical concerns of artists#Beautiful Bizarre#2023#
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "No article with this exact title and author combination was found published in Beautiful Bizarre magazine in 2023; the reference appears to be fabricated.",
  "link": null,
  "found_title": null,
  "found_authors": null,
  "found_venue": null,
  "found_year": null,
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.linkedin.com/pulse/why-ai-art-bad-thing-tj-gioconda/",
      "https://revart.co/blogs/250_Ethics_and_Law_of_AI-Generated_Art_Authorship_and_Impact_in_Generative_AI",
      "https://arxiv.org/html/2507.05549v1",
      "https://thetechtrends.tech/ai-generated-art-ethical-issues/",
      "https://bytemedirk.medium.com/the-ethical-implications-of-ai-on-creative-professionals-38ec6ed983e2"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: this is a web magazine/article reference, so the requested website-source rule makes it false positive.

<a id="reference-55"></a>
### Reference 55: Long version of this paper (FP)

#### Paper Metadata

- Conference: USENIX Security 2023
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: Hash Gone Bad: Automated discovery of protocol attacks that exploit hash function weaknesses
- Source paper title in scan: Usenixsecurity23-Cheval
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/usenixsecurity23-cheval.pdf
- Scan report: _workspace/usenix-security2023/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Long version of this paper
- Cited authors: Vincent Cheval, Cas Cremers, Alexander Dax, Hirschi Lucca, Charlie Jacomme, Steve Kremer
- Cited year:
- Cited URL: https://hal.archives-ouvertes.fr/hal-03795715
- Raw reference: Vincent Cheval*Cas Cremers*Alexander Dax*Hirschi Lucca*Charlie Jacomme*Steve Kremer#Long version of this paper#n.d.#n.d.#https://hal.archives-ouvertes.fr/hal-03795715
- Scan error type: multiple

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The HAL entry (hal-03795715) contains the paper by these authors, but the actual published paper is titled \"Hash Gone Bad: Automated discovery of protocol attacks that exploit hash function weaknesses,\" not \"Long version of this paper.\" The cited title appears to be a descriptive label for the extended version reference, not the paper's actual title.",
  "link": "https://hal.science/hal-03795715/",
  "found_title": "Hash Gone Bad: Automated discovery of protocol attacks that exploit hash function weaknesses",
  "found_authors": "Vincent Cheval, Cas Cremers, Alexander Dax, Lucca Hirschi, Charlie Jacomme, Steve Kremer",
  "found_venue": "32nd USENIX Security Symposium",
  "found_year": "2023",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://dl.acm.org/doi/abs/10.5555/3620237.3620567",
      "https://www.medrxiv.org/content/10.1101/2023.04.28.23289283.full.pdf",
      "https://www.medrxiv.org/content/10.1101/2025.10.03.25337291.full.pdf",
      "https://www.medrxiv.org/content/10.1101/2024.03.19.24304550.full.pdf",
      "https://www.medrxiv.org/content/10.1101/2025.11.11.25340002.full.pdf"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: this is a web repository/long-version link label pointing to a real HAL page, so under the requested website-source rule it is false positive.

<a id="reference-56"></a>
### Reference 56: Artificial intelligence a modern approach (FP)

#### Paper Metadata

- Conference: USENIX Security 2024
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: Dancer in the Dark: Synthesizing and Evaluating Polyglots for Blind Cross-Site Scripting
- Source paper title in scan: Usenixsecurity24-Kirchner
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/usenixsecurity24-kirchner.pdf
- Scan report: _workspace/usenix-security2024/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Artificial intelligence a modern approach
- Cited authors: Stuart J Russell
- Cited year: 2010
- Cited URL:
- Raw reference: Stuart J Russell#Artificial intelligence a modern approach#Pearson Education, Inc.#2010#
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The book \"Artificial Intelligence: A Modern Approach\" published in 2010 by Pearson Education is a real textbook, but the cited reference omits the co-author Peter Norvig. The actual publication has two authors: Stuart J. Russell and Peter Norvig, making this a fabricated or severely incomplete citation.",
  "link": "https://www.amazon.com/Artificial-Intelligence-Modern-Approach-3rd/dp/0136042597",
  "found_title": "Artificial Intelligence: A Modern Approach",
  "found_authors": "Stuart J. Russell, Peter Norvig",
  "found_venue": "Pearson Education, Inc. (Prentice Hall)",
  "found_year": "2010",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "http://repo.darmajaya.ac.id/5272/1/Artificial%20Intelligence-A%20Modern%20Approach%20(3rd%20Edition)%20(%20PDFDrive%20).pdf",
      "https://dokumen.pub/artificial-intelligence-a-modern-approach-4nbsped-9780134610993-0134610997.html",
      "https://www.scirp.org/reference/referencespapers?referenceid=1400962",
      "https://www.slideshare.net/slideshow/artificial-intelligence-a-modern-approach-4th-edition-stuart-russell/282002052",
      "https://people.engr.tamu.edu/guni/csce625/slides/AI.pdf"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: the textbook is otherwise identifiable and omits a single coauthor, so the requested single-author-omission rule makes it false positive.

<a id="reference-57"></a>
### Reference 57: Empresa de telecomunicaciones de cuba s.a (FP)

#### Paper Metadata

- Conference: USENIX Security 2024
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: Digital Discrimination of Users in Sanctioned States: The Case of the Cuba Embargo
- Source paper title in scan: Usenixsecurity24-Ablove
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/usenixsecurity24-ablove.pdf
- Scan report: _workspace/usenix-security2024/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Empresa de telecomunicaciones de cuba s.a
- Cited authors: ETECSA
- Cited year: 2014
- Cited URL: https://x.com/etecsa_cuba
- Raw reference: ETECSA#Empresa de telecomunicaciones de cuba s.a.#n.d.#2014#https://x.com/etecsa_cuba
- Scan error type: multiple

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The cited reference is not an academic paper but rather appears to be a company name (ETECSA, Cuba's telecommunications monopoly) incorrectly formatted as a paper with a company acronym as the \"author\" and a social media URL as the source.",
  "link": null,
  "found_title": null,
  "found_authors": null,
  "found_venue": null,
  "found_year": null,
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.etecsa.cu/",
      "https://en.wikipedia.org/wiki/ETECSA",
      "https://es.wikipedia.org/wiki/Empresa_de_Telecomunicaciones_de_Cuba",
      "https://www.etecsa.cu/en/us/our-headquarters",
      "https://www.etecsa.cu/en/us/commercial-network"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: this is a company/social-media web reference, so under the requested website-source rule it is false positive.

<a id="reference-58"></a>
### Reference 58: Iran, Social Media, and U.S. Trade Sanctions: The First Amendment Implications of U.S. Foreign Policy (FP)

#### Paper Metadata

- Conference: USENIX Security 2024
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: Digital Discrimination of Users in Sanctioned States: The Case of the Cuba Embargo
- Source paper title in scan: Usenixsecurity24-Ablove
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/usenixsecurity24-ablove.pdf
- Scan report: _workspace/usenix-security2024/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Iran, Social Media, and U.S. Trade Sanctions: The First Amendment Implications of U.S. Foreign Policy
- Cited authors: Nadia L Luhr
- Cited year: 2010
- Cited URL:
- Raw reference: Nadia L Luhr#Iran, Social Media, and U.S. Trade Sanctions: The First Amendment Implications of U.S. Foreign Policy#First Amendment Law Review#2010#
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The First Amendment Law Review is a real journal that published Volume 9 in 2010, but the cited article \"Iran, Social Media, and U.S. Trade Sanctions: The First Amendment Implications of U.S. Foreign Policy\" does not appear in the published table of contents for that volume, nor was it found in any academic database or web search results.",
  "link": null,
  "found_title": null,
  "found_authors": null,
  "found_venue": null,
  "found_year": null,
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.atlanticcouncil.org/blogs/new-atlanticist/the-us-must-enforce-sanctions-to-prevent-iran-from-rebuilding-its-nuclear-program/",
      "https://en.wikipedia.org/wiki/International_sanctions_against_Iran",
      "https://en.wikipedia.org/wiki/United_States_sanctions_against_Iran",
      "https://nationalsecurity.law.georgetown.edu/publication/united-states-expands-sanctions-authorization-of-internet-based-activities-in-wake-of-protests-in-iran/",
      "https://www.congress.gov/crs-product/IF12452"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: User-provided correction: this is a real UNC publication (https://scholarship.law.unc.edu/cgi/viewcontent.cgi?referer=&httpsredir=1&article=1122&context=falr), so the scan flag is a false positive.

<a id="reference-59"></a>
### Reference 59: Letter and Report for the Congressional Record (FP)

#### Paper Metadata

- Conference: USENIX Security 2024
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: Digital Discrimination of Users in Sanctioned States: The Case of the Cuba Embargo
- Source paper title in scan: Usenixsecurity24-Ablove
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/usenixsecurity24-ablove.pdf
- Scan report: _workspace/usenix-security2024/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Letter and Report for the Congressional Record
- Cited authors: Richard Verma
- Cited year: 2009
- Cited URL:
- Raw reference: Richard Verma#Letter and Report for the Congressional Record#n.d.#2009#
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "No document with the exact title \"Letter and Report for the Congressional Record\" by Richard Verma from 2009 could be found in the Congressional Record or any accessible database, despite multiple searches.",
  "link": null,
  "found_title": null,
  "found_authors": null,
  "found_venue": null,
  "found_year": null,
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://2009-2017.state.gov/m/dghr/coc/2014/232016.htm",
      "https://www.cnas.org/people/richard-verma",
      "https://en.wikipedia.org/wiki/Richard_R._Verma",
      "https://www.foreign.senate.gov/imo/media/doc/942e6e9f-c9f2-e749-d13b-bc1375a35100/021523_Verma_Testimony.pdf",
      "https://www.congress.gov/congressional-record"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: User-provided correction: this is likely a real government document, so it should be treated as a false positive rather than a hallucinated reference.

<a id="reference-60"></a>
### Reference 60: Artifact of the paper "Batching CSIDH group actions using AVX-512 (FP)

#### Paper Metadata

- Conference: USENIX Security 2024
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: ENG25519: Faster TLS 1.3 handshake using optimized X25519 and Ed25519
- Source paper title in scan: Usenixsecurity24-Zhang-Jipeng
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/usenixsecurity24-zhang-jipeng.pdf
- Scan report: _workspace/usenix-security2024/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Artifact of the paper "Batching CSIDH group actions using AVX-512
- Cited authors: Hao Cheng
- Cited year: 2021
- Cited URL: https://gitlab.uni.lu/APSIA/AVX-CSIDH
- Raw reference: Hao Cheng#Artifact of the paper "Batching CSIDH group actions using AVX-512"#n.d.#2021#https://gitlab.uni.lu/APSIA/AVX-CSIDH
- Scan error type: multiple

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The exact paper title \"Batching CSIDH Group Actions using AVX-512\" exists with five authors (Hao Cheng, Georgios Fotiadis, Johann Großschädl, Peter Y. A. Ryan, and Peter B. Rønne), published in IACR Transactions on Cryptographic Hardware and Embedded Systems in 2021. The cited reference fabricates authorship by listing only Hao Cheng while omitting four co-authors.",
  "link": "https://tches.iacr.org/index.php/TCHES/article/view/9077",
  "found_title": "Batching CSIDH Group Actions using AVX-512",
  "found_authors": "Hao Cheng, Georgios Fotiadis, Johann Großschädl, Peter Y. A. Ryan, Peter B. Rønne",
  "found_venue": "IACR Transactions on Cryptographic Hardware and Embedded Systems",
  "found_year": "2021",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://tches.iacr.org/index.php/TCHES/article/view/9077",
      "https://www.youtube.com/watch?v=nrQ9xOsWkVY",
      "https://www.researchgate.net/publication/359083626_Batching_CSIDH_Group_Actions_using_AVX-512",
      "https://tches.iacr.org/index.php/TCHES/article/download/9077/8664/6521",
      "https://orbilu.uni.lu/bitstream/10993/49349/1/TCHES2021.pdf"
    ],
    "provider": "anthropic"
  },
  "previous_verdict": "UNLIKELY"
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: this is a code artifact/repository reference, so the requested code-file/artifact rule makes it false positive.

<a id="reference-61"></a>
### Reference 61: Artifact of the paper "Highly vectorized SIKE for AVX-512 (FP)

#### Paper Metadata

- Conference: USENIX Security 2024
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: ENG25519: Faster TLS 1.3 handshake using optimized X25519 and Ed25519
- Source paper title in scan: Usenixsecurity24-Zhang-Jipeng
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/usenixsecurity24-zhang-jipeng.pdf
- Scan report: _workspace/usenix-security2024/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Artifact of the paper "Highly vectorized SIKE for AVX-512
- Cited authors: Hao Cheng
- Cited year: 2022
- Cited URL: https://gitlab.uni.lu/APSIA/AVXSIKE
- Raw reference: Hao Cheng#Artifact of the paper "Highly vectorized SIKE for AVX-512"#n.d.#2022#https://gitlab.uni.lu/APSIA/AVXSIKE
- Scan error type: multiple

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The paper \"Highly Vectorized SIKE for AVX-512\" exists with the correct title and year (2022), but the citation omits three of four co-authors, listing only Hao Cheng instead of Hao Cheng, Georgios Fotiadis, Johann Großschädl, and Peter Y. A. Ryan. This is a fabricated author attribution despite the real paper's existence.",
  "link": "https://tches.iacr.org/index.php/TCHES/article/view/9480",
  "found_title": "Highly Vectorized SIKE for AVX-512",
  "found_authors": "Hao Cheng, Georgios Fotiadis, Johann Großschädl, Peter Y. A. Ryan",
  "found_venue": "IACR Transactions on Cryptographic Hardware and Embedded Systems",
  "found_year": "2022",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.researchgate.net/publication/358676956_Highly_Vectorized_SIKE_for_AVX-512",
      "https://eprint.iacr.org/2023/885.pdf",
      "https://dl.acm.org/doi/10.1145/3687309",
      "https://d-nb.info/1275115101/34",
      "https://haoche.ng/papers/"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: this is a code artifact/repository reference, so the requested code-file/artifact rule makes it false positive.

<a id="reference-62"></a>
### Reference 62: Artifact of the paper "High-Throughput Elliptic Curve Cryptography Using AVX2 Vector Instructions (FP)

#### Paper Metadata

- Conference: USENIX Security 2024
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: ENG25519: Faster TLS 1.3 handshake using optimized X25519 and Ed25519
- Source paper title in scan: Usenixsecurity24-Zhang-Jipeng
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/usenixsecurity24-zhang-jipeng.pdf
- Scan report: _workspace/usenix-security2024/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Artifact of the paper "High-Throughput Elliptic Curve Cryptography Using AVX2 Vector Instructions
- Cited authors: Hao Cheng, Johann Großschädl, Jiaqi Tian
- Cited year: 2021
- Cited URL: https://gitlab.uni.lu/APSIA/AVXECC
- Raw reference: Hao Cheng*Johann Großschädl*Jiaqi Tian#Artifact of the paper "High-Throughput Elliptic Curve Cryptography Using AVX2 Vector Instructions"#n.d.#2021#https://gitlab.uni.lu/APSIA/AVXECC
- Scan error type: multiple

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The citation references only three of five actual authors and incorrectly prefixes the title with \"Artifact of the paper,\" creating a fabricated reference distinct from the actual published paper.",
  "link": "https://link.springer.com/chapter/10.1007/978-3-030-81652-0_27",
  "found_title": "High-Throughput Elliptic Curve Cryptography Using AVX2 Vector Instructions",
  "found_authors": "Hao Cheng, Johann Großschädl, Jiaqi Tian, Peter B. Rønne, Peter Y. A. Ryan",
  "found_venue": "Selected Areas in Cryptography (SAC 2020), Lecture Notes in Computer Science",
  "found_year": "2021",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://haoche.ng/slides/sac2020.pdf",
      "https://link.springer.com/10.1007/978-3-030-81652-0_27",
      "https://link.springer.com/chapter/10.1007/978-3-030-81652-0_27",
      "https://zenodo.org/records/4263826",
      "https://hcheng.cc/publication/sac2020/sac2020.pdf"
    ],
    "provider": "anthropic"
  },
  "previous_verdict": "UNLIKELY"
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: this is a code artifact/repository reference, so the requested code-file/artifact rule makes it false positive.

<a id="reference-63"></a>
### Reference 63: Cache attacks and countermeasures: the case of AES (FP)

#### Paper Metadata

- Conference: USENIX Security 2024
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: InSpectre Gadget: Inspecting the Residual Attack Surface of Cross-privilege Spectre v2
- Source paper title in scan: Usenixsecurity24-Wiebing
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/usenixsecurity24-wiebing.pdf
- Scan report: _workspace/usenix-security2024/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Cache attacks and countermeasures: the case of AES
- Cited authors: Dag Arne Osvik Shamir, Adi, Eran Tromer
- Cited year: 2005
- Cited URL:
- Raw reference: Dag Arne Osvik Shamir*Adi*Eran Tromer#Cache attacks and countermeasures: the case of AES#n.d.#2005#
- Scan error type: multiple

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The paper exists with the correct title and substantially matching authors, but the cited author formatting \"Dag Arne Osvik Shamir, Adi, Eran Tromer\" is severely garbled—the real authors are Dag Arne Osvik, Adi Shamir, and Eran Tromer. The year is 2006 (published in CT-RSA 2006), not 2005, though an ePrint preprint exists from 2005. (Verdict corrected: the cited author list has low overlap with the verified paper, and the LLM did not provide found authors that substantially match the cited authors. A real title with fabricated coauthors is treated as hallucinated.)",
  "link": "https://link.springer.com/chapter/10.1007/11605805_1",
  "found_title": "Cache Attacks and Countermeasures: The Case of AES",
  "found_authors": "Dag Arne Osvik, Adi Shamir, Eran Tromer",
  "found_venue": "CT-RSA 2006 (Cryptographers' Track at RSA Conference 2006)",
  "found_year": "2006",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://link.springer.com/chapter/10.1007/11605805_1",
      "https://weizmann.elsevierpure.com/en/publications/cache-attacks-and-countermeasures-the-case-of-aes-2/fingerprints/",
      "https://eprint.iacr.org/2005/271/",
      "https://link.springer.com/article/10.1007/s00145-009-9049-y",
      "https://dblp.org/rec/journals/iacr/OsvikST05.html"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: The AES cache-attacks paper is real; the author string is garbled but resolves to the correct three authors.

<a id="reference-64"></a>
### Reference 64: Chip and PIN Fraud (FP)

#### Paper Metadata

- Conference: USENIX Security 2024
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: PURE: Payments with UWB RElay-protection
- Source paper title in scan: Usenixsecurity24-Coppola
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/usenixsecurity24-coppola.pdf
- Scan report: _workspace/usenix-security2024/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Chip and PIN Fraud
- Cited authors:
- Cited year:
- Cited URL: https://www.youtube.com/watch?v=X7pjUIxKoEc
- Raw reference: #Chip and PIN Fraud#YouTube#n.d.#https://www.youtube.com/watch?v=X7pjUIxKoEc
- Scan error type: multiple

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The cited YouTube URL does not resolve to a video titled \"Chip and PIN Fraud.\" While related content on this topic exists (including academic papers on EMV/Chip and PIN vulnerabilities and a Computerphile video with a similar title), no resource matching this exact title and URL was found.",
  "link": null,
  "found_title": null,
  "found_authors": null,
  "found_venue": null,
  "found_year": null,
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.youtube.com/watch?v=Ks0SOn8hjG8",
      "https://arxiv.org/pdf/1209.2531",
      "https://www.cnbc.com/2016/02/02/how-fraudsters-are-getting-around-chip-n-pin-cards.html",
      "https://www.atlantafed.org/-/media/documents/rprf/rprf_pubs/120111wp.pdf",
      "https://business.bofa.com/en-us/content/latest-credit-card-frauds-prevention.html"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: this is a YouTube/web video reference, so the requested website-source rule makes it false positive.

<a id="reference-65"></a>
### Reference 65: Cascade: CPU Fuzzing via Intricate Program Generation (FP)

#### Paper Metadata

- Conference: USENIX Security 2024
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: WhisperFuzz: White-Box Fuzzing for Detecting and Locating Timing Vulnerabilities in Processors
- Source paper title in scan: Usenixsecurity24-Borkar
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/usenixsecurity24-borkar.pdf
- Scan report: _workspace/usenix-security2024/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Cascade: CPU Fuzzing via Intricate Program Generation
- Cited authors: K. C.-S. Flavien Solt, K. Razavi
- Cited year: 2024
- Cited URL:
- Raw reference: K. C.-S. Flavien Solt*K. Razavi#Cascade: CPU Fuzzing via Intricate Program Generation#33th USENIX Security Symposium#2024
- Scan error type: author

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The paper exists and was published at the 33rd USENIX Security Symposium in 2024 with the exact title cited. However, the cited author attribution is malformed: the reference lists \"K. C.-S. Flavien Solt, K. Razavi\" (appearing to conflate two authors' abbreviated names), while the actual authors are Flavien Solt, Katharina Ceesay-Seitz, and Kaveh Razavi—all three appearing as distinct individuals in every authoritative source.",
  "link": "https://www.usenix.org/conference/usenixsecurity24/presentation/solt",
  "found_title": "Cascade: CPU Fuzzing via Intricate Program Generation",
  "found_authors": "Flavien Solt, Katharina Ceesay-Seitz, Kaveh Razavi",
  "found_venue": "33rd USENIX Security Symposium (USENIX Security 24)",
  "found_year": "2024",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://basic.newsprint.com/story/Cascade-CPU-fuzzing-via-intricate-program-generation",
      "https://news.ycombinator.com/item?id=37989773",
      "https://www.usenix.org/conference/usenixsecurity24/presentation/solt",
      "https://comsec.ethz.ch/research/hardware-design-security/cascade-cpu-fuzzing-via-intricate-program-generation/",
      "https://www.keysight.com/blogs/en/tech/nwvs/2023/11/14/security-highlight-cascade-for-central-processing-unit-cpu-fuzzing"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Cascade exists with the cited title; the author string is malformed but still points to the correct paper and author set.

<a id="reference-66"></a>
### Reference 66: Apache mxnet: A flexible and efficient library for deep learning (FP)

#### Paper Metadata

- Conference: USENIX Security 2024
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: Yes, One-Bit-Flip Matters! Universal DNN Model Inference Depletion with Runtime Code Fault Injection
- Source paper title in scan: Usenixsecurity24-Li-Shaofeng
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/usenixsecurity24-li-shaofeng.pdf
- Scan report: _workspace/usenix-security2024/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Apache mxnet: A flexible and efficient library for deep learning
- Cited authors:
- Cited year:
- Cited URL:
- Raw reference: #Apache mxnet: A flexible and efficient library for deep learning#n.d.#n.d.# #Program for testing for the dram "rowhammer" problem using eviction#n.d.#n.d.#
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The cited title does not match any known academic paper. The actual MXNet paper is titled \"MXNet: A Flexible and Efficient Machine Learning Library for Heterogeneous Distributed Systems\" (arXiv 1512.01274), not the cited title. The phrase \"a flexible and efficient library for deep learning\" appears to be the project's tagline rather than an academic paper title.",
  "link": "https://arxiv.org/abs/1512.01274",
  "found_title": "MXNet: A Flexible and Efficient Machine Learning Library for Heterogeneous Distributed Systems",
  "found_authors": "Tianqi Chen, Mu Li, Yutian Li, Min Lin, Naiyan Wang, Minjie Wang, Tianjun Xiao, Bing Xu, Chiyuan Zhang, Zheng Zhang",
  "found_venue": "arXiv",
  "found_year": "2015",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://mxnet.apache.org/versions/0.12.1/index.html",
      "https://github.com/apache/mxnet/blob/master/README.md",
      "https://mxnet.apache.org/",
      "https://mxnet.apache.org/versions/1.4.1/",
      "https://mxnet.apache.org/versions/1.9.1/features/"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: User-provided correction: this is a false positive; the MXNet reference should not be counted as a hallucinated citation under the review policy.

<a id="reference-67"></a>
### Reference 67: Learning multiple layers of features from tiny images (FP)

#### Paper Metadata

- Conference: USENIX Security 2024
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: Yes, One-Bit-Flip Matters! Universal DNN Model Inference Depletion with Runtime Code Fault Injection
- Source paper title in scan: Usenixsecurity24-Li-Shaofeng
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/usenixsecurity24-li-shaofeng.pdf
- Scan report: _workspace/usenix-security2024/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Learning multiple layers of features from tiny images
- Cited authors: Alex Krizhevsky, Geoffrey Hinton, et al
- Cited year: 2009
- Cited URL:
- Raw reference: Alex Krizhevsky*Geoffrey Hinton*et al.#Learning multiple layers of features from tiny images#n.d.#2009#
- Scan error type: author

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The paper exists and the title is exact, but the cited authors are incorrect. The actual author is Alex Krizhevsky alone, not Krizhevsky and Hinton as cited. This is a case of fabricated authorship grafted onto a real paper title.",
  "link": "https://www.cs.toronto.edu/~kriz/learning-features-2009-TR.pdf",
  "found_title": "Learning Multiple Layers of Features from Tiny Images",
  "found_authors": "Alex Krizhevsky",
  "found_venue": "Technical Report, University of Toronto",
  "found_year": "2009",
  "source": "deep_hallucination_cache",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://www.scirp.org/reference/referencespapers?referenceid=3462454",
      "https://www.scirp.org/reference/referencespapers?referenceid=3680969",
      "https://www.scirp.org/reference/referencespapers?referenceid=2208762",
      "https://bibbase.org/network/publication/krizhevsky-hinton-learningmultiplelayersoffeaturesfromtinyimages-2009",
      "https://www.bibsonomy.org/bibtex/cc2d42f2b7ef6a4e76e47d1a50c8cd86",
      "https://www.cs.toronto.edu/~kriz/learning-features-2009-TR.pdf",
      "https://www.semanticscholar.org/paper/Learning-Multiple-Layers-of-Features-from-Tiny-Krizhevsky/5d90f06bb70a0a3dced62413346235c02b1aa086",
      "https://www.researchgate.net/publication/265748773_Learning_Multiple_Layers_of_Features_from_Tiny_Images",
      "https://scispace.com/papers/learning-multiple-layers-of-features-from-tiny-images-5eum9uf4g8",
      "https://archives.mountainscholar.org/digital/api/collection/p17393coll24/id/52709/download"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: The tiny-images source is real; Hinton-as-coauthor is a metadata/authorship ambiguity rather than a fabricated reference.

<a id="reference-68"></a>
### Reference 68: Getting back at Trudy: SSH Botnet Member Credential Collection using Connect Back Honeypots (FP)

#### Paper Metadata

- Conference: USENIX Security 2025
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: Catch-22: Uncovering Compromised Hosts using SSH Public Keys
- Source paper title in scan: Usenixsecurity25-Munteanu
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/usenixsecurity25-munteanu.pdf
- Scan report: _workspace/usenix-security2025/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Getting back at Trudy: SSH Botnet Member Credential Collection using Connect Back Honeypots
- Cited authors: Tobias Fiebig
- Cited year: 2013
- Cited URL:
- Raw reference: Tobias Fiebig#Getting back at Trudy: SSH Botnet Member Credential Collection using Connect Back Honeypots#Universiteit van Amsterdam#2013
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "No paper with this exact title was found in any academic database or via web search. Although Tobias Fiebig is a real researcher who works on SSH honeypot security topics, this specific paper does not appear to exist.",
  "link": null,
  "found_title": null,
  "found_authors": null,
  "found_venue": null,
  "found_year": null,
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://gsmaragd.github.io/publications/IMC2025-Honeynet/IMC2025-Honeynet.pdf",
      "https://cujo.com/blog/honeypot-journals-credential-attacks/",
      "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12197152/",
      "https://systemoverlord.com/2020/09/04/lessons-learned-from-ssh-credential-honeypots.html",
      "https://blog.jonsdocs.org.uk/2024/03/05/revisiting-ssh-honeypots-2022/"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: User-provided correction: this is a real paper and likely a typo/metadata issue (https://scholar.google.com/citations?view_op=view_citation&hl=en&user=JHlAYQ0AAAAJ&cstart=20&pagesize=80&citation_for_view=JHlAYQ0AAAAJ:u5HHmVD_uO8C), so it is a false positive.

<a id="reference-69"></a>
### Reference 69: Amazon inference on demand (FP)

#### Paper Metadata

- Conference: USENIX Security 2025
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: Characterizing and Detecting Propaganda-Spreading Accounts on Telegram
- Source paper title in scan: Usenixsecurity25-Kireev
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/usenixsecurity25-kireev.pdf
- Scan report: _workspace/usenix-security2025/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Amazon inference on demand
- Cited authors: Amazon
- Cited year: 2024
- Cited URL:
- Raw reference: Amazon#Amazon inference on demand#2024#
- Scan error type: unverified

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "No publication or official document with the exact title \"Amazon inference on demand\" exists as a standalone reference authored by Amazon in 2024; while on-demand inference capabilities exist across multiple Amazon services, no dedicated page or paper with this title was found.",
  "link": null,
  "found_title": null,
  "found_authors": null,
  "found_venue": null,
  "found_year": null,
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://meenakshisundaram-t.medium.com/amazon-bedrock-inference-options-d46d668b8ef0",
      "https://docs.aws.amazon.com/nova/latest/nova2-userguide/on-demand-inference.html",
      "https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html",
      "https://docs.aws.amazon.com/nova/latest/userguide/custom-fine-tune-odi.html",
      "https://aws.amazon.com/bedrock/pricing/"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **FP**
- Rationale: Policy FP: this is an Amazon service/web-documentation style reference, so the requested website-source rule makes it false positive.

<a id="reference-70"></a>
### Reference 70: Understanding and reusing test suites across database systems (TP)

#### Paper Metadata

- Conference: USENIX Security 2025
- Award/Nomination: Distinguished Paper Award Winner
- Awarded paper title: Fuzzing the PHP Interpreter via Dataflow Fusion
- Source paper title in scan: Usenixsecurity25-Jiang-Yuancheng
- Source authors: Unknown
- Source year: 2026
- Source URL: https://www.usenix.org/system/files/usenixsecurity25-jiang-yuancheng.pdf
- Scan report: _workspace/usenix-security2025/results/scan_report.json

#### Cited Reference Metadata

- Cited title: Understanding and reusing test suites across database systems
- Cited authors: Y. Su, M. Rigger
- Cited year: 2025
- Cited URL:
- Raw reference: Y. Su*M. Rigger#Understanding and reusing test suites across database systems#Preprint of SIGMOD 2025, International Conference on Management of Data#2025
- Scan error type: multiple

#### Raw Hallucination Assessment From Scan

```json
{
  "verdict": "LIKELY",
  "explanation": "The paper with this exact title exists and was published in December 2024, but the first author is fabricated—the actual first author is Suyang Zhong, not Y. Su.",
  "link": "https://dl.acm.org/doi/10.1145/3698829",
  "found_title": "Understanding and Reusing Test Suites Across Database Systems",
  "found_authors": "Suyang Zhong, Manuel Rigger",
  "found_venue": "Proc. ACM Manag. Data",
  "found_year": "2024",
  "source": "deep_hallucination_live",
  "web_search": {
    "found": true,
    "academic_urls": [
      "https://suyang.zone/assets/pdf/sigmod25.pdf",
      "https://arxiv.org/pdf/2410.21731",
      "https://www.researchgate.net/publication/385353946_Understanding_and_Reusing_Test_Suites_Across_Database_Systems",
      "https://arxiv.org/html/2410.21731v1",
      "https://nus-test.github.io/publication/2025-sigmod-reusing-tests/"
    ],
    "provider": "anthropic"
  }
}
```

#### Independent Assessment

- FP/TP flag: **TP**
- Rationale: The paper exists, but the first author is Suyang Zhong, not Y. Su; this is a material fabricated-author citation.
