# Media profile schema

`media-profiles.yaml` stores versioned analytical priors. Profiles apply to the
named edition, not automatically to every language service, program, presenter,
opinion writer, or affiliate using a similar brand.

## Top-level fields

- `schema_version`: catalog format version.
- `valid_as_of`: date of the latest catalog-wide review.
- `weight_semantics`: interpretation of numeric weights.
- `sources`: reusable evidence records.
- `outlets`: profile records.

## Outlet fields

- `id`, `name`, `edition`, `base_country`, `languages`, `outlet_type` identify
  the exact object being profiled.
- `ownership` records the formal owner, funding model, state relationship, and
  confidence. It must not collapse public service, state funding, and direct
  state control into one category.
- `alignment_priors` contains a target, dimension, weight, confidence, rationale,
  and supporting source IDs. The weight describes expected pull, not accuracy.
- `domestic_orientation` describes party, ideology, or audience affinity only
  where evidence exists. `none_established` is preferable to invented symmetry.
- `topic_modifiers` lists domains where the baseline is likely to strengthen,
  weaken, or conflict with another alignment.
- `analysis_notes` captures edition boundaries and high-value cautions.
- `evidence` references the source registry.
- `review` records status and dates.

## Confidence

- `high`: direct legal, corporate, or repeated strong evidence.
- `medium`: multiple credible indicators, but the interpretation remains
  contextual.
- `low`: provisional hypothesis requiring article-level testing.

## Review rules

Review a profile after ownership, government, charter, senior editorial
leadership, distribution strategy, or a major geopolitical relationship changes.
Do not silently overwrite old assessments: update `last_reviewed`, explain the
change in `change_note`, and preserve version history in source control.

