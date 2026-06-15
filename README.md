Live site: https://freegym.github.io/FreeGym-Wiki/

# FreeGym Wiki

> **"Your GitHub profile will matter more than Twitter, Instagram, and YouTube combined."**

<p align="center">
  <a href="https://github.com/FreeGym/FreeGym-Wiki/actions/workflows/link-checker.yml"><img src="https://img.shields.io/github/actions/workflow/status/FreeGym/FreeGym-Wiki/link-checker.yml?style=flat-square&label=links%20verified" alt="Link Status"></a>
  <a href="https://github.com/FreeGym/FreeGym-Wiki/issues"><img src="https://img.shields.io/github/issues-raw/FreeGym/FreeGym-Wiki?style=flat-square&label=open%20debates" alt="Open Debates"></a>
  <a href="https://github.com/FreeGym/FreeGym-Wiki/commits"><img src="https://img.shields.io/github/last-commit/FreeGym/FreeGym-Wiki?style=flat-square&label=last%20update" alt="Last Update"></a>
  <a href="https://github.com/FreeGym/FreeGym-Wiki/graphs/contributors"><img src="https://img.shields.io/github/contributors/FreeGym/FreeGym-Wiki?style=flat-square&label=contributors" alt="Contributors"></a>
  <a href="https://github.com/FreeGym/FreeGym-Wiki/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-CC_BY--SA_4.0-lightgrey?style=flat-square" alt="License"></a>
</p>

---

## The Premise

It is January 2026, and trying to find reliable health information online is exhausting.

The problem is not that people do not care about evidence. The problem is that most health advice now arrives through feeds built for speed, outrage, and sales. A weak study becomes a supplement pitch. A half-true warning becomes a 60-second Reel. When a creator gets something wrong, the post can disappear and the record disappears with it.

That is why this project uses GitHub.

Social media is built around attention. A repository is built around history, review, and version control. For health information, that difference is not cosmetic. It changes how mistakes are corrected, how disagreements are handled, and how trust is earned.

---

## What We're Fixing

Health content on social media has a few recurring problems. They are familiar enough that they can start to feel normal.

**Fear presented as education.** Seed oils will kill you. Sugar is poison. The ingredient you cannot pronounce must be toxic. Claims like this spread because fear travels quickly, not because the evidence supports panic. A rat study, a mechanistic speculation, or one out-of-context chart can become a confident public warning while dose, population, and real-world risk get ignored.

**Cherry-picked studies.** One paper finds an association and suddenly the claim is "proven." The studies showing no effect are left out. So are the limitations, the study design, the confidence intervals, and whether the result applies to humans in the first place.

**Contradictory advice with no place to reconcile it.** Keto is the answer. Vegan is the answer. Carnivore is the answer. Fasting is essential. Fasting is dangerous. Cardio kills gains. Cardio is mandatory. Plenty of people cite studies while giving advice that directly conflicts with someone else citing studies. The hard part is not finding a confident opinion. The hard part is knowing which claim survives scrutiny.

**No durable record of being wrong.** A creator makes a claim, gets corrected, deletes the post, and moves on. Their page can look clean even if thousands of people saw the original mistake. There is no public trail showing what changed or why.

**Credentials used as shortcuts for proof.** Follower counts, blue checkmarks, degrees, and certifications can matter, but none of them settle whether a claim is true. A weekend certification does not make someone right. A PhD does not make every claim right either. This wiki puts the claim and the evidence first. Anyone can contribute if the evidence is strong enough.

**Financial incentives hidden inside education.** A supplement recommendation may come with an affiliate link. A diet claim may lead to a course. An attack on an ingredient may benefit a sponsor. Disclosures exist, but the incentives are often hard to see from the post itself.

**Anecdotes treated like data.** Personal experience can be useful, but it is not the same as controlled evidence. "I did this and improved" does not tell us what caused the improvement, what else changed, or whether the same thing applies to someone else.

**Risky advice for serious conditions.** Fitness tips and medical advice now sit beside each other in the same feed. People with real conditions can be pushed toward unproven alternatives, vaccine misinformation, cancer "cures," or mental health advice from people who are not equipped to give it. The stakes are not always harmless.

**Unrealistic standards made to look normal.** Drug-assisted physiques are presented as natural. Before-and-after images are edited, lit, pumped, and timed for effect. People compare themselves to a performance and assume they are failing.

**Exercise advice that ignores bodies.** Some form cues sound authoritative but make little biomechanical sense. Some programming ignores injury history, recovery, anatomy, or training age. "No pain, no gain" is easy to repeat and easy to misuse.

**Nutrition claims with no context.** "This food is bad" often leaves out dose, pattern, health status, culture, access, and goals. Most useful nutrition answers are conditional. Social media rewards absolute ones.

This repo exists because misinformation is cheap to produce and expensive to clean up. We are trying to make the clean-up work public, organized, and easier to build on.

---

## Why a Repository Beats Social Media

**The diff shows the work.**

On social media, a correction usually means an old post gets deleted or a new post contradicts it. Either the history vanishes or the audience is left to piece it together.

In a repository, the history stays visible. Open an article, click "History," and you can see what changed:

```text
Jan 2024: Added warning regarding hair loss (Citation X)
Mar 2025: Removed hair loss warning. New meta-analysis (Citation Y) does not support the claim.
```

That is not a weakness. That is what honest updating looks like.

**Issues give debate somewhere to live.**

Comment sections are built for reactions. GitHub Issues are better suited for slow disagreement.

If a citation is wrong, someone can open an Issue explaining the problem, link the better evidence, and let others respond. If the correction holds up, a Pull Request changes the article and links back to the discussion. The debate becomes part of the public record instead of disappearing into a comment thread.

**Forks make disagreement visible.**

The main repository is the shared evidence base. Someone with a specific hypothesis can fork it and make their case without hiding where they differ from the main version.

That matters. If a coach, clinic, or creator uses a modified version, readers can compare the fork to the main repo and see exactly what changed. There is less room for vague claims about "the science" when the differences are visible line by line.

**Automation catches the boring failures.**

Broken citations, dead links, and stale references are not glamorous problems, but they matter. This repo uses automated checks so basic maintenance does not depend only on memory. Automation does not decide what is true, but it helps keep the evidence trail inspectable.

---

## The Comparison

| Feature | Instagram / YouTube | Evidence-Based Repository |
|---------|---------------------|---------------------------|
| **Updates** | New post buries the old | `git push` updates the document |
| **Corrections** | Apology video or deletion | Commit history with an explanation |
| **Debate** | Comment threads | Structured Issues with labels |
| **Sources** | "Link in bio" | Linked references with DOI or PMID |
| **State** | Static post | Versioned living document |
| **Credibility** | Follower count | Contribution history |
| **Accountability** | Delete and move on | Public history |

---

## The Paradigm Shift

Right now, hundreds of creators can make separate versions of "How to Build Muscle," each with different claims, different citations, and no shared way to resolve conflicts.

This project is built around a different model: one public article that can be challenged, corrected, improved, forked, and cited. Experts can open Pull Requests. Readers can inspect the sources. Contributors build a public body of work instead of asking people to trust a persona.

Trust should come from process, not performance.

---

## Why Your GitHub Profile Will Matter

In health and fitness, a useful public record is more valuable than a polished feed.

Your GitHub profile can show that you contributed to accurate, evidence-based material. Commits become receipts. Pull Requests show how your work was reviewed. Issues show how you handle disagreement and correction.

That kind of credibility is harder to fake.

---

## Verification and FreeGym

This repository powers the verification system for [FreeGym](https://freegym.ai/), a health and fitness social network.

**Red Checkmark**: Contributors who have merged substantive, evidence-based content earn verification. The checkmark appears on their FreeGym profile and links back to their contribution history here.

**Topic Badges**: Contributors can earn badges for specific domains, such as nutrition, exercise, and sleep, by doing accepted work in those areas.

**Maintainer Star**: People who review contributions and help maintain quality standards receive a star designation instead of a checkmark.

The difference from most verification systems is simple: you cannot buy it or claim it. You earn it through work that other people can inspect.

See [VERIFICATION.md](VERIFICATION.md) for the full rules.

---

## Automation and Internals

If you want to audit or extend the verification system, start here:
[docs/automation.md](docs/automation.md)

---

## Contributing

This wiki is open source. Truth should not have a paywall.

If you want to add evidence, correct an error, or propose a new topic, read the [Contribution Guidelines](CONTRIBUTING.md).

---

## License

This work is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Share it freely, attribute it properly, and keep derivatives open.
