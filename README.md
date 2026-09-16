# Newsbot

Newsbot is a portable agent skill for comparing how major media systems cover the
same event, claim, or controversy. It separates verifiable facts from selection,
framing, institutional incentives, and inferred narrative effects.

The first version is conversational. Give it a topic, claim, article, or URL and
ask for a brief, comparison, deep dive, claim check, or coverage audit.

```text
$newsbot Compare how CNN, Fox, BBC, DW, RT, and Chinese state media frame the
latest development in this story.
```

Natural-language invocation should also work when the host supports implicit
skill discovery:

```text
Which facts are broadly agreed on, where do the narratives diverge, and what is
each outlet making more or less visible?
```

## Layout

- `newsbot/SKILL.md` is the portable entry point.
- `newsbot/references/methodology.md` defines the research workflow.
- `newsbot/references/media-profiles.yaml` contains versioned analytical priors.
- `newsbot/references/profile-schema.md` documents the profile model.
- `newsbot/references/output-formats.md` defines response shapes.
- `newsbot/scripts/validate_profiles.py` validates the catalog.
- `adapters/generic/system-prompt.md` is a thin adapter for agents without skill
  discovery.

## Installation

For Codex, copy or symlink the `newsbot` directory into the configured skills
directory. Invoke it explicitly as `$newsbot`, or let Codex select it from the
request when implicit skill invocation is enabled.

For Claude Code:

```bash
git clone https://github.com/kognium/newsbot.git
cp -R newsbot/newsbot ~/.claude/skills/newsbot
```

Then invoke it with `/newsbot`, or ask naturally for a cross-outlet news and
narrative comparison.

For another agent, use the same `newsbot/SKILL.md` when its skill format is
compatible. Otherwise load `adapters/generic/system-prompt.md` together with the
files under `newsbot/references/`.

The host agent needs live web access for current-event analysis. Without it,
Newsbot can analyze supplied material but must not claim a current or exhaustive
coverage survey.

## License

MIT
