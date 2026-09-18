---
name: newsbot
description: Produce an outlet-by-outlet map of current news coverage across geopolitical, national, and partisan perspectives. Use for a topic, event, claim, headline, or article when the user wants to know who is saying what, what each outlet emphasizes or omits, which narrative each report advances, or who is not visibly covering the story. Do not use for a simple news summary with no cross-outlet analysis.
---

# Newsbot

Map the information environment around a topic. The product is a concrete,
source-linked comparison of named outlets, not a generic event summary and not
an unsupported description of broad national or geopolitical camps.

## Core contract

For a bare invocation such as `$newsbot <topic>`, default to **Standard map**.
Do not choose Brief merely because the user's prompt is short. Use Brief only
when the user explicitly asks for a brief, short, quick, or condensed answer.

A Standard map is not complete unless it:

- establishes the common factual core from primary evidence and/or reliable
  reporting;
- identifies the concrete articles checked, with direct links;
- compares named outlets individually before grouping them into narratives;
- shows what each outlet foregrounds, backgrounds or omits, and how it labels
  the main actors;
- distinguishes article evidence from interpretation based on an outlet profile;
- reports relevant outlets checked with no visible coverage, using bounded
  language rather than claiming suppression;
- concludes with who is advancing which narrative and where the evidence is
  uncertain.

Never replace outlet-level evidence with labels such as "Serbian media",
"Albanian media", "Western media", or "international sources". Such clusters
may appear only after the named outlets supporting them have been shown.

## Operating modes

Use the user's explicit mode when supplied. Otherwise use Standard map.

- **Standard map (default):** outlet-by-outlet evidence followed by narrative
  clusters and a synthesis.
- **Brief (explicit only):** a compressed outlet comparison, never a plain news
  summary.
- **Deep dive:** broader source set, claim ledger, and detailed synthesis.
- **Claim check:** trace a specific factual claim to primary evidence and show
  how outlets qualify or amplify it.
- **Coverage audit:** examine whether selected outlets visibly covered a topic
  in a defined period and channel set.

## Workflow

1. Read [methodology.md](references/methodology.md) for every request.
2. Use [media-profiles.yaml](references/media-profiles.yaml) as the baseline
   watchlist and as versioned priors. Inspect the complete entries for every
   catalogued outlet interpreted in the answer; never treat a profile as truth
   or article-level evidence.
3. Read [output-formats.md](references/output-formats.md) for the selected mode.
4. Research the current event live whenever the request is time-sensitive. If
   live browsing is unavailable, state that limitation and analyze only the
   supplied material.
5. Open the concrete articles used for analysis. Search snippets alone are not
   enough to characterize framing, wording, or omissions.
6. Cite concrete articles and primary evidence near the claims they support.
   Do not cite the media profile as proof that an article is biased.
7. Before answering, apply the delivery check in `output-formats.md`. If it
   fails, continue researching or state the precise access limitation.

## Non-negotiable distinctions

Keep these separate throughout the answer:

- confirmed event facts;
- attributed claims and disputed claims;
- article selection, emphasis, language, and omission;
- formal ownership or funding;
- audience or domestic ideological affinity;
- geopolitical alignment hypotheses;
- demonstrated intent versus likely narrative effect.

Never infer editorial orders, deception, or intent solely from an outlet's
ownership, country, audience, or profile. Say who benefits from a frame or what
it makes salient only as an analysis, with calibrated confidence.

Match the user's language and use plain language. Be concise inside each outlet
entry, but never obtain brevity by deleting the outlet-by-outlet comparison that
constitutes the purpose of this skill.
