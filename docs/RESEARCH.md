# Research notes

Checked 2026-10-28. These are original summaries of primary sources, not reproduced papers. Publication status is from the linked venue or authors' arXiv metadata. Studies differ in tasks, models, budgets, and protocols; their numbers should not be compared as a common leaderboard. No cited study validates this exact skill on GPT-6.1 Sol or a current Claude development workflow.

| Source | Findings and relevance | Limits |
| --- | --- | --- |
| [When Debate Helps](https://arxiv.org/abs/2610.04686), 2026-10-03, preprint | Correct candidate coverage and evidence-sensitive final selection jointly matter. Motivates alternative proposals and explicit evidence checks. | Reasoning benchmarks and a particular proposal-selection mechanism, not a direct evaluation of this three-lens skill. |
| [Beyond Symmetric Agents](https://arxiv.org/abs/2609.35875), 2026-09-26, submitted to ICLR 2027 | Across small open models, debate can improve over one response yet tie/lose to budget-matched independent sampling. Persona prompting hurt; most debate benefit came from the first exchange. | Small models with benchmark headroom; do not extrapolate to all frontier models or software planning. |
| [MABPD](https://arxiv.org/html/2609.04841v1), 2026-09-04, authors report EMNLP 2026 acceptance | Same LLaMA 3.3 70B model in three roles: bias, evidence, framing. Removing structured debate reduced held-out F1 by 10.6 points. Closest architectural example to this idea. | News-bias task, domain scoring rules, and verification machinery. Original serving endpoint unavailable; per-agent logs are insufficient for a strong independent aggregation baseline. Does not isolate the value of three roles alone. |
| [Beyond Consensus](https://arxiv.org/html/2608.30373v1), 2026-08-31, authors report Findings of EMNLP 2026 acceptance | Six judge models on essay/summarization scoring: single judges aligned better with humans on average. Strict-role prompting caused downward bias that consensus did not remove. | Subjective scoring, not code review. Motivates task criteria rather than strict/lenient personalities. Its score-masking result also means hiding peer scores is not universally beneficial; first-pass isolation here is a design choice, not a proven optimum. |
| [A Diagnostic Study of Multi-Agent LLMs for Real-World Debates](https://proceedings.mlr.press/v306/pitre26a.html), ICML 2026 | Outcome-only consensus measures miss sycophancy, dominance, and premature convergence. Process diagnostics reveal additional failures. | Ground-truth-poor real-world debate; does not establish development-task accuracy. |
| [Voting or Consensus?](https://aclanthology.org/2025.findings-acl.606/), Findings of ACL 2025 | Decision protocols have task-dependent effects; more discussion rounds before voting reduced performance in these experiments. | No universal winner for planning decisions with non-negotiable constraints. |

## Design choices, not research conclusions

- Three complementary task lenses, not three personalities or a correctness guarantee.
- Same-model evaluation controls one source of variation but permits correlated errors.
- A user-accepted criteria list prevents agents from optimizing incompatible goals.
- One optional cross-check round bounds cost; unresolved evidence gaps survive into the Plan.
- Must-have constraints are not decided by majority vote. Preferences remain user decisions.
- The Plan and Goal are portable output contracts, not an assertion that every host has native Goal tooling.

## What would establish usefulness

Compare on the same tasks and host/model/version/settings: (1) one agent applying all criteria; (2) independent same-model evaluations with synthesis only; (3) the full workflow with one dispute check. Account for total model usage and elapsed time. Measure actionable omissions found, unsupported objections, correction/rework, acceptance evidence, and user decision quality. Preserve initial reports and decision changes. Do not claim gains without this comparison.

## Official implementation references

- [Codex skills](https://learn.chatgpt.com/docs/build-skills): discovery, installation paths, invocation metadata.
- [Claude Code skills](https://code.claude.com/docs/en/skills): explicit-only invocation control.
- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents): separate contexts, model inheritance/overrides.
- [Claude Code model configuration](https://code.claude.com/docs/en/model-config): availability and aliases are host/account dependent.
