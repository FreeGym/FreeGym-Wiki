# Contributing to FreeGym Wiki

This document explains how to contribute, what counts as valid evidence, and how you build trust in this community.

---

## Why Contribute

Your contribution history becomes your credibility.

On social media, anyone can call themselves a "nutrition expert" or "fitness coach." Here, your expertise is demonstrated, not declared. You either have a track record of accurate, well-cited contributions to the nutrition folder, or you don't. The history speaks for itself.

Corrections build trust here instead of destroying it. In the influencer world, admitting you were wrong is brand suicide. You delete and pretend. Here, updating your position based on new evidence is visible in the commit history. That transparency signals intellectual honesty, which is rare and valuable in health content.

You become associated with specific topics. If someone wants to know who actually understands sleep science, they can look at who has contributed the most reviewed and accepted content to the sleep folder. That's a different kind of authority than follower count. It's earned through work, not performance.

Building authority on social media means playing the engagement game. Hot takes. Controversy. Fear-mongering gets views. Here, you build authority by being right and being helpful. No algorithm punishes you for being accurate but boring.

A tweet disappears in hours. A contribution to this wiki is permanent, linkable, and citable. When someone asks "why should I trust you on this topic?" you can point to a body of work instead of a follower count.

Most health creators are indistinguishable. Same content, same format, same engagement tactics. Contributing here signals you're different. You care about accuracy enough to participate in a peer-reviewed, version-controlled system. That matters to the people worth reaching.

---

## How Contributions Work

You contribute by opening a Pull Request. That's it.

Find something wrong? Open a PR with the fix. Have evidence to add? Open a PR. Disagree with a claim? Open an Issue first, discuss it, then open a PR if the community agrees.

When your first PR gets merged, you're automatically added to [contributors.yaml](contributors.yaml). A bot handles this. You don't need to ask anyone.

---

## Step-by-Step: Submitting Your First Contribution

If you've never contributed to a GitHub project before, here's exactly what to do.

**1. Fork the repository**

Click the "Fork" button in the top-right corner of [the repo page](https://github.com/FreeGym/FreeGym-Wiki). This creates your own copy under your GitHub account.

**2. Make your changes**

You can edit files directly on GitHub (click any file, then the pencil icon) or clone your fork locally if you prefer working on your computer.

**3. Commit your changes**

If editing on GitHub, scroll down and write a short description of what you changed. Click "Commit changes."

If working locally, stage and commit your changes with Git, then push to your fork.

**4. Open a Pull Request**

Go back to the original FreeGym-Wiki repo. GitHub will show a banner saying you recently pushed to your fork. Click "Compare & pull request."

Write a clear title and description. Explain what you changed and why. If you're adding citations, mention which studies you're referencing.

**5. Wait for review**

A maintainer will review your PR. They might approve it, request changes, or ask questions. This is normal. Respond to feedback, make adjustments if needed.

**6. Get merged**

Once approved, a maintainer merges your PR. Your changes are now part of the wiki. The bot automatically adds you to [contributors.yaml](contributors.yaml).

That's it. You've contributed to open-source health knowledge.

---

## What Counts as Valid Evidence

Not all sources are equal. We use a hierarchy.

**Tier 1: Strongest**
- Systematic reviews and meta-analyses from peer-reviewed journals
- Cochrane reviews
- Large RCTs (randomized controlled trials) with pre-registration

**Tier 2: Strong**
- Individual RCTs from peer-reviewed journals
- Prospective cohort studies with large sample sizes

**Tier 3: Acceptable with caveats**
- Observational studies (note limitations clearly)
- Mechanistic studies (cell/animal, must be labeled as such)
- Expert consensus statements from recognized bodies

**Tier 4: Not acceptable as primary evidence**
- Blog posts, podcasts, YouTube videos
- Unpublished preprints (can be mentioned, not cited as proof)
- Single case studies
- "Someone said" or personal anecdotes

When you add a claim, cite the strongest available evidence. If only Tier 3 evidence exists, say so explicitly.

---

## How to Format Citations

Use inline links with the study title or a brief description. Put the full reference at the bottom of the file.

**In the text:**
```markdown
Creatine supplementation improves strength output in resistance training
([Rawson & Volek, 2003](https://pubmed.ncbi.nlm.nih.gov/14636102/)).
```

**At the bottom of the file:**
```markdown
## References

- Rawson ES, Volek JS. Effects of creatine supplementation and resistance
  training on muscle strength and weightlifting performance. J Strength
  Cond Res. 2003 Nov;17(4):822-31. [PMID: 14636102]
```

Always include:
- Author names
- Publication year
- Journal name
- PMID or DOI when available

---

## The Trust System

GitHub tracks activity. We track trust. They're different.

Activity means you've done stuff. Trust means the community believes your stuff is accurate.

**Three levels exist:**

| Level | What it means | How you get there |
|-------|---------------|-------------------|
| Contributor | You've had a PR merged | Automatic on first merge |
| Trusted | Maintainers vouch for your work | Maintainers decide |
| Maintainer | You can merge PRs and promote others | Existing maintainers invite you |

**How promotion works:**

There's no fixed threshold. After you've contributed for a while, a maintainer might open an Issue proposing to promote you. They'll link to your past contributions. Other maintainers weigh in. If there's consensus, someone updates [contributors.yaml](contributors.yaml) with your new status and who vouched for you.

This means promotions are transparent. Anyone can see who vouched for whom and why.

**What we look at (but don't automate):**

- Do your citations check out?
- Do you represent studies accurately, including limitations?
- When someone challenges your work, do you engage constructively?
- Do your contributions survive, or do they get reverted often?

We value quality over quantity. Ten well-cited paragraphs matter more than a hundred sloppy ones.

**What counts as substantive (for verification):**

- Adds new claims backed by Tier 1–2 evidence
- Major edit with **≥3 citations** or **≥20 substantive lines**
- Corrects an existing claim with stronger evidence or clearer limitations
- **Does not count:** formatting, wording tweaks, or link fixes only

---

## Challenging Existing Content

Disagreement is welcome. Here's the process.

1. **Open an Issue first.** Title it clearly: "Dispute: [Topic] - [Your concern]"

2. **State your case with evidence.** Link to studies that contradict the current claim. Explain why your evidence is stronger (larger sample, better methodology, more recent).

3. **Wait for discussion.** Give others time to respond. A few days minimum.

4. **If consensus forms, open a PR.** Reference the Issue number in your PR description.

5. **If no consensus, that's okay.** The Issue stays open as a documented debate. Future readers can see both sides.

Don't just edit things you disagree with. The Issue trail matters. It shows the community considered the evidence.

---

## Pull Request Checklist

Before submitting:

- [ ] Claims are supported by Tier 1 or Tier 2 evidence where possible
- [ ] Citations include author, year, journal, and PMID/DOI
- [ ] Limitations are noted when using weaker evidence
- [ ] You've checked that linked URLs actually work
- [ ] The writing is clear and accessible (avoid unnecessary jargon)
- [ ] You've searched existing Issues to see if this was already discussed

---

## Style Guide

Write for someone smart but unfamiliar with the topic.

- Define technical terms on first use
- Use active voice
- Keep sentences varied in length
- No hype or sensationalism
- State uncertainty when it exists ("evidence suggests" vs "studies prove")

Avoid:
- Clickbait framing
- Absolute statements when evidence is mixed
- Dismissing legitimate scientific debate
- Cherry-picking studies that support one view

---

## What Happens After You Contribute

Your PR gets reviewed. Someone might request changes. This is normal and not personal. We're checking the evidence, not judging you.

Once merged:
- You appear in [contributors.yaml](contributors.yaml) automatically
- Your contribution is part of the permanent Git history
- The "last update" badge on the README changes
- If you touched a new folder, it's noted in your contributor profile

Keep contributing, engage constructively in Issues, and maintain quality. That's how you build trust here.

---

## Questions?

Open an Issue with the `question` label. Someone will respond.
