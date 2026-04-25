# How Clean Are the References in ICLR 2026?
## A Full Scan of 180,501 Citations

Anonymous

---

With LLM-assisted writing becoming mainstream in research, a natural question is whether fake references are slipping into top-venue papers. To get the full picture, we ran RefChecker against every accepted paper at ICLR 2026. The short answer: **about 1 in 29 accepted papers contain at least one likely fabricated reference.** Out of 5,348 processed papers with 180,501 total citations, RefChecker flagged **349 likely hallucinations** across **184 papers** (3.4%).

## Summary

Between January and April 2026, we ran RefChecker, an open-source reference-verification tool, against every accepted paper at ICLR 2026. That came out to 5,348 papers and 180,501 citations. About 1 in 29 accepted papers contain at least one reference that looks fabricated. We then focused on the 12 papers with five or more flagged references. We notified the ICLR Program Committee on April 13, 2026, and emailed each of those 12 author teams. Ten of them wrote back.

This writeup covers what we found, what the authors told us about how the hallucinations got there, how ICLR's Program Chairs responded, and what we think the rest of the community should do about it. We have anonymized individual papers, authors, and institutions. Several authors asked us to, and we thought it was the right call for the ones who didn't ask too.

## Key Takeaways

1. **The rate is already at 1 in 29, and right now no one is going to fix the archival record.** 184 of the 5,348 accepted ICLR 2026 papers contain at least one likely fabricated reference. 12 of them contain five or more. All of these papers passed three rounds of human review. They are now what the field will cite for years. ICLR has told us they do not have the capacity to re-check the accepted corpus. The workflows that produced these citations are still in use. If the community is going to respond to this, the response has to be designed before the next round of submissions, not after.

2. **The most common cause is a workflow failure, not the LLM making things up.** When we asked authors how the hallucinated references got into their papers, the answer was usually some version of the same story. The author found the right paper. They read it. They decided to cite it. Then they asked an LLM or an AI-assisted browser to turn the title or URL into a formatted citation, and the formatting step got the authors wrong, or the venue wrong, or truncated the title. The output went into the paper and nobody checked it. This is a fixable failure mode, and it is a different problem from the "AI slop" framing that has dominated the coverage of LLMs in academia so far.

3. **We count two kinds of hallucinations.** The first is the obvious one: the paper being cited does not exist. The second is less obvious: the paper exists and the title is right, but the citation gets the authors or venue or DOI wrong. Several authors argued that the second category should not count as hallucination because the underlying paper is real. We disagree. A citation is supposed to tell you who did the work and where to find it. If it gets either of those wrong, it has failed.

4. **Every author who engaged moved to fix their paper.** One team withdrew the paper. Others filed emergency camera-ready correction requests with ICLR, uploaded corrected versions to arXiv, or posted acknowledgments on OpenReview. Nobody who wrote back tried to defend the references. They took the errors seriously and acted quickly.

5. **ICLR is applying its own policy unevenly because it has to.** ICLR's published policy says papers with confirmed hallucinated references get desk-rejected. At review time, that policy was enforced, and it contributed to this year's high desk-reject rate. For the papers that got past review and were accepted, the same policy has produced no action. The Program Chairs told us they are a volunteer-run non-profit and they do not have the resources to run the same human-review process on the accepted corpus. That is a fair constraint and we report it the way they described it. We also note that the same Code of Ethics violation is now producing different outcomes based on when someone happens to catch it. And ICLR has not publicly shared the specifics of how its review-time reference checks worked, which makes it harder for other conferences to learn from what went well or what did not.

6. **Stylistic decisions are now integrity decisions.** Whether to include an access date on a URL. Whether to mark forthcoming work as "to appear" with a preprint link. How to cite a commercial AI model that has no paper. These used to be judgment calls nobody cared about. Now they decide whether a citation is verifiable. Several of the references we flagged came from authors making reasonable-looking choices in the absence of any agreed-upon guidance.

7. **This problem is going to show up at every conference until the community agrees on norms.** ICLR is not a special case. Every venue that accepts a lot of submissions is going to see the same patterns: bibliography-conversion errors, references inserted by collaborators without anyone vetting them, citations to forthcoming work with no preprint, citations to URLs that change after the paper is submitted. The useful outcome here is not to grade individual papers. It is to get the community to agree on how to cite forthcoming work, how to verify AI-assisted bibliographies, and what conferences owe authors when hallucinations get caught after acceptance.


## RefChecker

RefChecker is an open-source tool for validating academic references. It extracts each bibliography entry from a PDF, parses the fields, and checks the result against multiple academic databases before escalating unresolved cases to an LLM with web search access.

## The Dataset

RefChecker processed 5,348 accepted ICLR 2026 papers and extracted 180,501 references. The typical paper cites about 33.8 references (median: 31).

![Reference-count distribution across accepted papers](figures/ref_distribution.png)
*Distribution of references per paper across the ICLR 2026 corpus.*

## Results

| Outcome | Count | Percent |
|---|---:|---:|
| Verified (matched in database) | 173,386 | 96.06% |
| Cleared after assessment | 6,735 | 3.73% |
| Uncertain (insufficient signal) | 31 | 0.02% |
| **Flagged LIKELY hallucinated** | 349 | 0.19% |

![Verification outcomes](figures/verification_outcomes.png)
*Verification outcomes for all 180,501 extracted references.*

## Confirmed Hallucinations: 349 References Across 184 Papers

RefChecker flagged **349 references as LIKELY hallucinated** across **184 papers** - 3.4% of accepted papers. Most affected papers have one or two likely hallucinations; **38 papers have 3 or more**, and **12 papers have 5 or more**.

![Hallucinated references per affected paper](figures/tp_distribution.png)
*Distribution of likely hallucinated references per affected paper.*

## Metadata Quality

| Issue | Count | Per Paper (avg) |
|---|---:|---:|
| No URL provided (available but omitted) | 79,995 | 15.0 |
| Multiple fields differ | 42,880 | 8.0 |
| Author name mismatches | 17,803 | 3.3 |
| Suboptimal URL (valid but not canonical) | 16,188 | 3.0 |
| Venue mismatches | 13,200 | 2.5 |
| Unverified references | 5,451 | 1.0 |
| Year mismatches | 3,179 | 0.6 |
| Title mismatches | 1,639 | 0.3 |

![Metadata discrepancy types](figures/error_types.png)
*Distribution of metadata discrepancy types across all references.*

URL issues alone affect 96,183 references, or about 53.3% of the corpus. That is roughly 18.0 URL-related issues per paper on average.

## State of Academic References

The current results find likely fabricated references in about 1 in 29 accepted papers, and far larger volumes of ordinary metadata noise. Both problems are small enough to catch automatically and large enough to matter operationally.

## Scan Configuration and Runtime

| Detail | Value |
|---|---|
| Tool | [RefChecker](https://github.com/markrussinovich/refchecker) v3.0.77 |
| LLM (extraction + assessment) | Claude Sonnet 4.6 (with web search for assessment) |
| Primary database | Semantic Scholar local snapshot (233M papers, 87 GB) |
| Fallback APIs | CrossRef, DBLP, OpenAlex, OpenReview |
| Papers downloaded | 5,355 |
| Papers processed | 5,348 (7 failed - corrupt PDFs or missing bibliographies) |
| Total references extracted | 180,501 |
| LLM cost | ~$1,600 |
| Total wall-clock time | ~12 hours |
| Infrastructure | 3 machines x 10 workers |

## Outreach to ICLR and Authors 

Before publishing, we wanted to give both the ICLR Program Committee and the authors of affected papers an opportunity to review the findings, respond, and correct the archival record. Our goal was to avoid surprising anyone and to treat the scan as the start of a conversation rather than a conclusion. 

We first notified the ICLR 2026 Program Committee on April 13, 2026. In that note, we shared a summary of the findings, described the RefChecker methodology, and invited comparison against ICLR's own review-time process. The Program Chairs responded thoughtfully and engaged with the findings across several exchanges. We discuss their substantive response in Section 4. 

Our scan flagged hundreds of papers containing at least one likely fabricated reference. Reaching out individually to every author team at that scale was not tractable in the time available, so we focused on the 12 papers with five or more flagged references. We emailed each of those author teams directly, attached the full report so they could examine our methodology and the specific assessments for their paper, and asked for a response by the planned blog publication date, roughly a five-day window. 

Ten of the 12 author teams responded. Several wrote back within hours. Several others coordinated with co-authors and returned more detailed responses over the following days. Every author team that responded with accepting fault — without exception — moved to correct the archival record. Corrections took the form of updated arXiv preprints, emergency camera-ready update requests submitted to ICLR, public comments acknowledging the issues on OpenReview, and in one case a decision to withdraw the paper entirely rather than allow an uncorrected version to remain in circulation. 

The discussion in section below draws on a set of exemplar responses that illustrate the distinct categories of causes authors described. It is not an exhaustive summary of every reply we received.

## Response from Affected Authors 
The tenor of the responses was, in our view, the most encouraging part of this exercise. Authors who engaged did so seriously. They examined the flagged references one by one and they acknowledged errors directly when errors existed, disputed specific findings when they believed the tool was wrong, and in most cases volunteered fixes before we asked. Several explicitly thanked us for the chance to respond before publication.  

Two author teams asked whether their paper might be excluded from a public writeup, citing concerns about lab reputation and the disproportionate effect naming might have relative to the underlying errors. After reflecting on the responses we received, we decided that the blog post would not name individual papers, institutions, or authors. The aggregate findings and the methodological observations are the contribution worth making, and naming specific papers did not add to that in a way that justified the cost to authors who had engaged in good faith. Every discussion of specific causes below is anonymized.  

The responses converged on a small number of distinct causes. In almost every case, authors reached quickly for one conclusion: the hallucinations were real, and they needed to be fixed. But the pathways that produced them varied, and the distinctions matter for any venue or tool trying to address this problem at scale. 

### Two kinds of hallucinations 
Before discussing causes, it is worth being explicit about what we counted as a hallucinated reference. The responses surfaced two distinct categories, and we treat both as hallucinations in this writeup. 

The first is fabrication: the cited paper does not exist. No real publication corresponds to the title as cited, and web and database searches surface no such work. This is the failure mode most people picture when they hear "LLM-hallucinated citation." 

The second is metadata corruption: the cited paper exists and the title is (roughly) correct, but the authors, venue, DOI, or URL are wrong. A reader who searches for the title can sometimes find the right paper, but the citation as written misattributes credit and misdirects verification. Several author responses pushed back on calling this category a hallucination, arguing that the titles were real and only auxiliary fields were wrong. We disagree, respectfully.  

A reference exists to serve two functions: to direct a reader to the work, and to credit the people who produced it. A citation that gets the authors wrong fails the second function. A citation with a wrong DOI or broken URL fails the first and Both failures harm the record and both warrant correction. 

## Different Causes of Hallucinations 

### Cause 1: Using LLMs or AI browsers to convert references into BibTeX 

This was the single most common cause described, appearing across multiple independent responses. In this pattern, the author had found real papers through normal scholarly search. They had read the papers, decided which ones to cite, and located the correct URL or title for each. At that point, they used an LLM or an AI-assisted browser tool to convert the title or URL into a formatted BibTeX entry. The conversion step introduced errors including truncated or altered titles, wrong author lists, substituted venues that the authors did not catch before submission. 

One author team described using "Perplexity's Comet browser to convert a paper URL or title to a bibtex entry." Another described using an LLM to "convert an existing reference list into BibTeX format." A third described prompting an LLM with existing paper titles to "organize a bibtex file." In each case, the intended source paper was real and correctly identified by the author, but the formatted citation that ended up in the manuscript misrepresented the authors, venue, or title. 

This is a specific and, in principle, fixable workflow vulnerability which is also notable because it is not what most people mean when they talk about "LLM-hallucinated citations." The LLM did not invent the paper; it mangled the metadata of a real one during a mechanical formatting step that authors treated as low-stakes. 

### Cause 2: References inserted by collaborators without vetting 

Several responses described references added by external collaborators, in one case during time away from lab, in another "amidst a series of edits during off hours" before a deadline  that the primary authors did not independently verify before submission. The underlying error was still a hallucination; the proximate cause was a collaboration workflow in which no one team member owned bibliographic integrity across the final manuscript. 

### Cause 3: Careless citation errors 

Some responses acknowledged errors that had nothing to do with LLMs: wrong titles pasted in, authors remembered incorrectly, venues misattributed. These are the kinds of errors that have always existed in academic bibliographies. They are worth naming separately because they get conflated with LLM hallucination in coverage of this issue, and the remedies are different. 

### Cause 4: Citing forthcoming or unindexed work without a public preprint 

One author team attributed several flagged references to work recently accepted at upcoming venues but not yet published. When asked whether preprints were available anywhere that a reader could locate — arXiv, group pages, institutional repositories — the answer was "preprints are not available currently." The works may well exist and be real, but as citations in the published ICLR paper they are not verifiable by any reader today. We noted this as a distinct category worth calling out since it is not fabrication, but it is also not a clean false positive of the verification tool. It is the functional equivalent of an unverifiable citation, and it points to a citation-hygiene norm ("to appear" markers with preprint links) that is routinely observed in ML but was not here. 

### Cause 5: Webpage-style references to living URLs and model cards 

Some flags pointed to citations of vendor documentation, model release pages, or system cards for commercial models without corresponding academic papers. In several cases, the content on those URLs changed between the author's access date and the scan date, producing a mismatch the tool read as a hallucinated citation. In other cases, the cited "title" was a descriptive label the author had assigned rather than the published title of an existing document. Authors described these as false alerts, and we think that framing is fair for some of them. But the broader pattern — citing living URLs as if they were stable academic references — is itself a citation-hygiene problem that will only grow as more of the field cites commercial model releases.

## ICLR's Response 

ICLR's Program Chairs engaged constructively from our first email. In their initial response, one of the Program Chairs described the review-time process in detail: an automated system flagged a large number of submissions (around 934), area chairs performed a first round of human review, Program Chairs reviewed the flagged references themselves, and ultimately papers with confirmed hallucinated references were desk-rejected. The automated system had a significant false positive rate, which is why multiple rounds of human review were considered necessary before any enforcement action. This process contributed to ICLR 2026's unusually high desk rejection rate. 

When we asked whether ICLR would be issuing a statement for the blog post, the response was that a coordinated statement would require coordination across all Program Chairs, the General Chair, the board, and others, and was not feasible on the timeline. The Chairs also noted that ICLR operates on a model of openness and that external analyses of the published record are expected and welcomed. 

When we asked what the policy called for in cases where hallucinations were confirmed in already-accepted papers, the answer pointed back to operational reality. As a non-profit volunteer-run organization, ICLR does not have the resources to re-run hallucination checks on the camera-ready versions of accepted papers. The review-time process required substantial human-review effort that cannot realistically be replicated on the accepted corpus. 

## Reflections

### Reflection 1: Authors bear final responsibility, whatever tools they use 

Using LLMs in manuscript preparation is permissible under ICLR's policy, and several author responses specifically disclosed LLM use in line with that policy. The responses also made clear that disclosure does not reduce the author's responsibility for the final artifact. The most striking corrective actions came from teams that took this seriously — treating the hallucinated references as their own failure of verification rather than a failure of the tool they used. That framing is the right one. Whatever an LLM, an AI browser, or a bibliography-conversion tool produces, the author is the one who submits the paper. 

### Reflection 2: The community needs clearer norms around disclosing LLM usage 

ICLR's policy requires disclosure of LLM use, and most responses indicated the authors had disclosed. But "LLM was used in manuscript preparation" covers a wide range of activities: language polishing, drafting bibliographies, converting formats, writing related-work sections, generating figures, or all of the above. Each of those carries different integrity implications. A blanket disclosure is better than no disclosure, but the field would benefit from more granular norms, specifically which part of the lifecycle saw LLM use, and what verification the authors performed on the output. The specific failure mode described most often in these responses (LLMs used to convert references to BibTeX, with no independent check of the output) is a clear example of a workflow step where targeted disclosure and targeted verification would have prevented the problem. 

### Reflection 3: ICLR's policy is being applied unevenly, and more transparency would help 

ICLR's published policy desk-rejected papers with confirmed hallucinated references during the review process. In our scan of the accepted papers, about 1 in 29 contain at least one likely fabricated reference. Several author teams have now confirmed that the flags in their specific papers are correct. The same Code of Ethics violation is producing different outcomes based only on when detection happens. We are not asking ICLR to revisit acceptance decisions but we are pointing out that the policy, as applied, is uneven — and that the community would benefit from ICLR being more transparent about the tooling and methodology it used during review.  

Beyond the high-level pipeline description in the retrospective, the specific design choices, thresholds, metrics, and execution details of ICLR's reference checks have not been shared publicly. Without that transparency, it is hard for other venues to learn from ICLR's experience, and hard for external scans like ours to calibrate findings against what the review process actually caught. 

### Reflection 4: Stylistic choices are now integrity choices, and the community lacks shared conventions 

ICLR is one of the largest and most prominent ML conferences, but the problem is not specific to ICLR. Every venue that accepts a high volume of LLM-era submissions will face the same patterns: bibliography-conversion errors, collaborator-inserted references, citations to forthcoming work without preprints, citations to living URLs that drift. 

A recurring theme across the responses is that stylistic choices which used to be minor now determine whether a citation can be verified at all. Whether to include an access date on a URL. Whether to mark forthcoming work as "to appear" with a preprint link. Whether to use a descriptive label for a model card or its published title. How to cite a model that has no corresponding paper. These decisions used to be matters of taste. In an LLM-era bibliography they are the difference between a citation a reader can follow and one they cannot. Several of the flagged references in our scan were the product of authors making reasonable-looking stylistic calls in the absence of any shared guidance — a URL with no access date, a descriptive title for a vendor page, a conference acceptance cited without a preprint. The authors were not being dishonest. They were filling gaps where the community has not yet agreed on how to cite these things. 

Without shared conventions — for how to cite forthcoming work, how to cite living documents, what constitutes adequate verification of AI-assisted bibliographic output, and what venues owe authors when hallucinations are found post-acceptance — every conference will rediscover this problem independently. We think the more useful outcome of this exercise is not to grade papers individually but to help the community converge on norms that keep scholarly citations verifiable at scale. 
