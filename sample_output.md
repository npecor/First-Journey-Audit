# Sample Audit Output

This is an illustrative example of the kind of output the audit should produce. It is intentionally short, specific, and action-oriented.

```json
{
  "summary": "The page likely under-converts because the core value proposition is only partially clear, the CTA is visible but not especially motivating, and the post-click experience is not concrete enough to reduce hesitation.",
  "scores": {
    "clarity_of_value_prop": 3,
    "trust_and_credibility": 3,
    "cta_clarity_and_motivation": 3,
    "friction_and_confusion": 2,
    "onboarding_momentum": 2
  },
  "top_issues": [
    {
      "title": "Headline explains topic but not distinct outcome",
      "why_it_matters": "Visitors need to understand the practical benefit quickly or they will not invest attention in the rest of the page.",
      "evidence": "The page appears to describe the product category, but the visible copy does not clearly state the strongest end-user result or who benefits most.",
      "recommended_fix": "Rewrite the hero headline and supporting text to name the audience, primary benefit, and speed-to-value in plain language."
    },
    {
      "title": "Primary CTA lacks a strong reason to click now",
      "why_it_matters": "Even a visible CTA underperforms when the immediate value of clicking is unclear.",
      "evidence": "The action label is generic and the surrounding copy does not explain what the visitor gets immediately after the click.",
      "recommended_fix": "Pair the CTA with one short line that explains the immediate next step and why it is low-risk and worthwhile."
    },
    {
      "title": "Trust signals are present but too weak relative to the ask",
      "why_it_matters": "If the page requests commitment without enough proof or reassurance, hesitation rises.",
      "evidence": "The content does not surface strong proof, concrete outcomes, or enough contextual reassurance near the conversion path.",
      "recommended_fix": "Add concise credibility support close to the CTA, such as customer proof, implementation clarity, or credible product context."
    }
  ],
  "top_fixes": [
    {
      "fix": "Clarify the hero section around audience, outcome, and how the product works in one pass",
      "expected_impact": "Should improve first-impression comprehension and reduce bounce from confused visitors.",
      "effort": "medium"
    },
    {
      "fix": "Make the primary CTA more concrete by describing the immediate next step and time-to-value",
      "expected_impact": "Should increase willingness to click by reducing uncertainty about what happens next.",
      "effort": "low"
    },
    {
      "fix": "Add stronger proof and reassurance adjacent to the CTA",
      "expected_impact": "Should improve trust at the decision point and reduce last-minute hesitation.",
      "effort": "medium"
    }
  ],
  "quick_wins": [
    "Replace generic CTA copy with action wording that previews the next step.",
    "Add one short subheadline that states the main outcome in plain English.",
    "Remove or simplify one distracting section that competes with the primary conversion path."
  ],
  "bigger_bets": [
    "Rework the page narrative so it moves from problem to value to proof to next step with less cognitive load.",
    "Redesign the click-to-activation handoff so the first-use experience feels faster and more guided."
  ]
}
```
