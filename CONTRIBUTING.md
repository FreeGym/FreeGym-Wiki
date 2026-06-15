# Contributing to FreeGym Wiki

This guide explains how to contribute, what kind of evidence we accept, and how trust is built in this project.

---

## Why Contribute

Your contribution history becomes your credibility.

On social media, anyone can call themselves a nutrition expert, fitness coach, or researcher. Here, the record is more concrete. If you have written accurate, well-cited material in the nutrition folder, people can see it. If you have corrected claims in the sleep folder, they can see that too. The work is the proof.

Corrections are part of the culture here. In most public-facing health content, being wrong is treated like a brand problem, so posts get deleted and everyone moves on. In this repo, changing your mind because better evidence appears is visible in the history. That is not embarrassing. It is the point.

You also become associated with topics through actual work. If someone wants to know who has contributed meaningfully to sleep science, they can look at the accepted contributions in that area. That is a different kind of authority than follower count.

Social platforms reward hot takes, speed, controversy, and fear. This project rewards accuracy, usefulness, and careful revisions. A good contribution may be quiet, but it stays linkable and citable.

Most health creators end up looking similar: same formats, same claims, same engagement tactics. Contributing here says something different. It shows that you care enough about accuracy to put your work in a public, reviewable system.

---

## How Contributions Work

You contribute by opening a Pull Request. The `main` branch is protected, so direct pushes are rejected. Every change goes through review.

If you find an error, open a PR with the fix. If you have evidence to add, open a PR. If you disagree with an existing claim, open an Issue first, discuss the evidence, and then open a PR if the discussion supports a change.

When your first PR is merged, you are automatically added to [contributors.yaml](contributors.yaml). You do not need to ask for that separately.

---

## Step-by-Step: Submitting Your First Contribution

If you have never contributed to a GitHub project before, this is the basic path.

**1. Fork the repository**

Click the "Fork" button in the top-right corner of [the repo page](https://github.com/FreeGym/FreeGym-Wiki). This creates a copy under your GitHub account.

**2. Make your changes**

You can edit files directly on GitHub by opening a file and clicking the pencil icon. If you prefer working locally, clone your fork and edit the files on your computer.

**3. Commit your changes**

If you are editing on GitHub, scroll down after making your change, write a short description, and click "Commit changes."

If you are working locally, stage and commit your changes with Git, then push them to your fork.

**4. Open a Pull Request**

Go back to the original FreeGym-Wiki repo. GitHub usually shows a banner for recently pushed branches. Click "Compare & pull request."

Write a clear title and description. Explain what you changed and why. If you added citations, mention the studies you used.

**5. Wait for review**

A maintainer will review the PR. They may approve it, ask questions, or request changes. That is normal. Respond to the feedback and update the PR if needed.

**6. Get merged**

Once the PR is approved, a maintainer merges it. Your change becomes part of the wiki, and [contributors.yaml](contributors.yaml) is updated automatically.

That is it. You have contributed to open-source health knowledge.

---

## What Counts as Valid Evidence

Not all sources carry the same weight. Use the strongest evidence available for the claim you are making.

**Tier 1: Strongest**
- Systematic reviews and meta-analyses from peer-reviewed journals
- Cochrane reviews
- Large randomized controlled trials with pre-registration

**Tier 2: Strong**
- Individual randomized controlled trials from peer-reviewed journals
- Prospective cohort studies with large sample sizes

**Tier 3: Acceptable with caveats**
- Observational studies, with limitations clearly noted
- Mechanistic studies, including cell or animal research, labeled clearly
- Expert consensus statements from recognized bodies

**Tier 4: Not acceptable as primary evidence**
- Blog posts, podcasts, or YouTube videos
- Unpublished preprints, though they can be mentioned as preliminary
- Single case studies
- Personal anecdotes or "someone said" claims

When you add a claim, cite the best available evidence. If only weaker evidence exists, say that plainly in the article.

---

## How to Format Citations

Use inline links in the text, then include the full reference at the bottom of the file.

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

GitHub tracks activity. This project tracks trust. Those are not the same thing.

Activity means you have made changes. Trust means the community has reason to believe your changes are accurate, careful, and useful.

**Three levels exist:**

| Level | What it means | How you get there |
|-------|---------------|-------------------|
| Contributor | You have had a PR merged | Automatic on first merge |
| Trusted | Maintainers vouch for your work | Maintainers decide |
| Maintainer | You can merge PRs and promote others | Existing maintainers invite you |

**How promotion works:**

There is no fixed threshold. After you have contributed for a while, a maintainer may open an Issue proposing to promote you. They will link to your past contributions, other maintainers can weigh in, and if there is consensus, someone updates [contributors.yaml](contributors.yaml) with your new status and who vouched for you.

Promotions are public by design. Anyone can see who vouched for whom and why.

**What we look at, without automating it:**

- Do your citations check out?
- Do you represent studies accurately, including limitations?
- When someone challenges your work, do you engage constructively?
- Do your contributions hold up over time, or do they often need to be reverted?

Quality matters more than volume. Ten careful, well-cited paragraphs are worth more than a hundred sloppy ones.

**What counts as substantive for verification:**

- Adds new claims backed by Tier 1-2 evidence
- Makes a major edit with **>=3 citations** or **>=20 substantive lines**
- Corrects an existing claim with stronger evidence or clearer limitations
- Does not count: formatting, wording tweaks, or link fixes only

---

## Challenging Existing Content

Disagreement is welcome, but the process matters.

1. **Open an Issue first.** Use a clear title, such as "Dispute: [Topic] - [Your concern]".

2. **State your case with evidence.** Link to studies that contradict the current claim. Explain why your evidence is stronger, such as a larger sample, better methodology, or more recent data.

3. **Wait for discussion.** Give others time to respond. A few days is usually the minimum.

4. **If consensus forms, open a PR.** Reference the Issue number in your PR description.

5. **If no consensus forms, leave the Issue open.** A documented debate is still useful. Future readers can see both sides and the evidence behind them.

Do not rewrite contested content without discussion. The Issue trail shows that the community considered the evidence.

---

## Pull Request Checklist

Before submitting:

- [ ] Claims are supported by Tier 1 or Tier 2 evidence where possible
- [ ] Citations include author, year, journal, and PMID/DOI
- [ ] Limitations are noted when using weaker evidence
- [ ] Linked URLs actually work
- [ ] The writing is clear and accessible
- [ ] Existing Issues have been checked for related discussion

---

## Style Guide

Write for someone smart who is new to the topic.

- Define technical terms on first use
- Use active voice
- Vary sentence length
- Avoid hype and sensationalism
- State uncertainty when it exists, such as "evidence suggests" instead of "studies prove"

Avoid:
- Clickbait framing
- Absolute statements when the evidence is mixed
- Dismissing legitimate scientific debate
- Cherry-picking studies that support only one view

---

## What Happens After You Contribute

Your PR gets reviewed. Someone may request changes. That is normal and not personal. The review is about the evidence and the clarity of the writing.

Once merged:
- You appear in [contributors.yaml](contributors.yaml) automatically
- Your contribution becomes part of the permanent Git history
- The "last update" badge on the README changes
- If you touched a new folder, that topic is reflected in your contributor profile

Keep contributing, engage constructively in Issues, and keep the quality high. That is how trust builds here.

---

## Questions?

Open an Issue with the `question` label. Someone will respond.
