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

It's January 2026. Anyone trying to find trustworthy health information is exhausted.

Not from training. From algorithm-driven science. From cherry-picked studies weaponized to sell supplements with no scientific backing in 60-second Reels. From influencers who delete posts when proven wrong, leaving no trace of their misinformation.

So they're migrating to GitHub.

Social media is built for engagement. A repository is built for accuracy and version control. The difference matters more than it sounds.

Think of it as immutable truth with audit trails.

---

## What We're Fixing

Social media health content is broken in ways that have become so normal we barely notice them anymore.

**Fear-mongering disguised as education.** Seed oils will kill you. Sugar is poison. That ingredient you can't pronounce? Toxic. These claims spread because fear drives engagement, not because the evidence supports panic. A single rat study becomes "EXPOSED: What They Don't Want You to Know." The actual risk assessment, the dose-response relationship, the human relevance? Doesn't fit in a Reel.

**Cherry-picked studies presented as settled science.** One study shows a correlation, and suddenly it's "PROVEN." The five other studies showing no effect? Never mentioned. The limitations section of the paper? Never read. Creators screenshot the abstract, ignore the methodology, and move on to the next post.

**Contradictory advice with no way to reconcile it.** Keto is the answer. No, vegan is the answer. Actually, carnivore. Fasting is essential. Fasting is dangerous. Cardio kills gains. Cardio is mandatory. Every expert sounds confident, cites studies, and completely disagrees with the next expert. Regular people have no way to evaluate who's right.

**Deleted history when proven wrong.** An influencer makes a claim. It gets debunked. The post disappears. Their profile looks like they've never been wrong about anything. There's no record, no correction, no accountability. The audience who believed the original claim never sees the retraction.

**Proxies instead of proof.** Social media judges credibility by followers, blue checkmarks, and titles. "Certified coach." "Doctor." "Researcher." But credentials are proxies, not proof. A weekend certification doesn't make someone right. Neither does a PhD. What matters is whether the claim holds up to scrutiny. This repo puts the science first. Anyone can contribute if the evidence is solid. We remove credential-based gatekeeping, not evidence-based standards.

**Financial incentives buried under "education."** The supplement they're recommending? Affiliate link. The diet they swear by? They sell a course on it. The ingredient they're attacking? Competitor to their sponsor. Disclosure requirements exist but enforcement doesn't.

**Anecdotes treated as evidence.** "I did X and my Y improved, therefore X causes Y improvement." No control group. No accounting for other variables. No consideration of placebo effect. Personal experience is valid but it's not data, and the distinction gets erased.

**Dangerous advice for serious conditions.** People with actual medical conditions get told to try unproven alternatives. Vaccine misinformation spreads. Cancer "cures" circulate. Mental health advice comes from everywhere. The algorithm doesn't distinguish between harmless fitness tips and potentially lethal medical guidance. This repo cares only about what the science says. Science doesn't respect authority bias, follower counts, or h-index. A claim is either supported by evidence or it isn't, regardless of who made it.

**Unrealistic expectations presented as normal.** Physiques achieved with performance-enhancing drugs presented as "natural transformation." Photoshopped before-and-afters. Lighting tricks and pump timing sold as sustainable results. People compare themselves to illusions and feel like failures.

**Exercise advice that causes injury.** Form cues that sound good but biomechanically don't make sense. "No pain no gain" mentality that ignores warning signals. One-size-fits-all programming that doesn't account for individual differences, injury history, or recovery capacity.

**Nutrition claims that ignore context.** "This food is bad" without mentioning dose matters. "This diet is optimal" without mentioning it depends on the individual. Absolute statements about complex systems that don't have absolute answers.

This repo exists because Brandolini's Law is real: the amount of energy needed to refute misinformation is an order of magnitude larger than what it takes to produce it. Social media optimizes for production. We're optimizing for refutation, documentation, and collaborative truth-finding.

---

## Why a Repository Beats Social Media

**The diff is the narrative.**

On Instagram, when a creator changes their mind, they either delete the old post or publish a new one that contradicts the first. History erased or audience confused. Pick your poison.

In this repository, the history of scientific consensus lives in the Git commit history. Open `supplements/creatine.md` and click "History." You'll see something like this:

```
Jan 2024: Added warning regarding hair loss (Citation X)
Mar 2025: REMOVED hair loss warning. New meta-analysis (Citation Y) debunks connection.
```

Critics call it flip-flopping. Engineers call it updating the software based on new patches. The diff proves intellectual honesty. You can watch science correct itself in real time.

**Issues replace comments.**

YouTube comment sections are graveyards of trolls and anecdotes. GitHub Issues are structured forums for methodological debate.

Picture this. You publish a protocol on Zone 2 Cardio. A PhD student doesn't leave a nasty comment. Instead, they open Issue #402 titled "Correction on Mitochondrial Density Citation." They provide a conflicting study. The community discusses p-values and sample sizes in the thread. Someone labels the issue as a bug related to accuracy. A Pull Request resolves it by updating the wiki with a nuanced caveat.

The noise gets filtered out. Only the signal remains.

**Forking creates transparency.**

The main repo, what we call upstream, is the Gold Standard. It contains only claims proven by high-quality meta-analyses. Boring, dry, accurate.

A niche creator, say a Keto coach, forks that repo. They keep the Sleep and Hydration modules synced with upstream, but they modify the Nutrition folder to reflect their specific hypothesis.

Here's where it gets interesting. Users can view the exact diff between the Global Repo and the Coach's Fork. That diff is their Unique Value Proposition. No hidden agendas. No mystery about where someone deviates from consensus. You can see precisely what they believe that mainstream science doesn't, and you can evaluate it for yourself.

**Continuous integration validates citations.**

In 2026, "trust me, bro" is dead.

This repository uses automated workflows to validate claims. Broken link checkers flag retracted studies or dead URLs immediately. Live badges show what percentage of citations come from peer-reviewed sources versus preprints. A Twitter creator posts a screenshot of a study title. A GitHub creator posts a markdown file where the study is parsed, limitations are bolded, and confidence intervals are visualized.

That's the difference between performance and proof.

---

## The Comparison

| Feature | Instagram / YouTube | Evidence-Based Repository |
|---------|---------------------|---------------------------|
| **Updates** | New post buries the old | `git push` updates a living document |
| **Corrections** | "Sorry guys" video | `Revert commit` with explanation |
| **Debate** | Flame wars in comments | Structured Issues with labels |
| **Sources** | "Link in bio" (often broken) | Hyperlinked footnotes with DOI |
| **State** | Static snapshot | Living, breathing, versioned truth |
| **Credibility** | Follower count | Contribution history |
| **Accountability** | Delete and pretend | Immutable commit history |

---

## The Paradigm Shift

Think about how inefficient the current system is. 500 fitness YouTubers each make "How to Build Muscle" videos with slightly different opinions. Same topic, scattered across platforms, no way to synthesize or verify.

Now imagine one collaborative, peer-reviewed wiki article. It links to actual studies, not "research shows" with nothing behind it. It shows contribution history, so you know who added what, when, and why. Experts can challenge and improve claims via Pull Requests. Anyone can fork it and adapt it for specific populations. Trust builds through process, not personality.

---

## Why Your GitHub Profile Will Matter

In 2026, the most influential "Health Influencer" is a repository, not a person.

Your GitHub profile shows you contributed to truth, not that you performed for an algorithm. Commits become receipts. Pull requests become peer review. Resolved issues become corrections in the public record.

Health, fitness, and medicine drown in noise. A repo like this is pure signal.

---

## Verification and FreeGym

This repository powers the verification system for [FreeGym](https://freegym.ai/), a health and fitness social network.

**Red Checkmark**: Contributors who have merged substantive, evidence-based content earn verification. This checkmark appears on their FreeGym profile, linked directly to their contribution history here.

**Topic Badges**: Contribute to specific domains (nutrition, exercise, sleep) and earn badges showing where you've demonstrated knowledge through actual work.

**Maintainer Star**: Those who review and maintain quality standards get a star designation instead of a checkmark.

The key difference from other verification systems: you can't buy it, you can't claim it, you can only earn it through auditable contributions. When someone sees your red checkmark on FreeGym, they can click through and see exactly what you contributed.

See [VERIFICATION.md](VERIFICATION.md) for the full rules.

---

## Automation and Internals

If you want to audit or extend the verification system, start here:
[docs/automation.md](docs/automation.md)

---

## Contributing

This wiki is open source. Truth doesn't have a paywall.

If you want to contribute evidence, correct an error, or propose a new topic, see our [Contribution Guidelines](CONTRIBUTING.md).

---

## License

This work is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Share freely, attribute properly, and keep derivatives open.
