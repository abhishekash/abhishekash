# Engineering notes

[← Back to the profile](../README.md)

These notes describe the evidence behind the projects and the limits of the current experiments.

## Decisions and evidence boundaries

- **Capture only what is needed.** Tool arguments and successful outputs are opt-in in the harness; a trace that lacks retrieval results must not claim to prove repeated-output overlap.
- **Use existing spans before inventing a new standard.** The [retrieval experiment](https://github.com/abhishekash/agent-evals/blob/main/experiments/001-retrieval-loop/M0-DECISION.md) currently uses a thin, hashed export helper and operation-specific readiness checks. Its harness and LangGraph cases are scripted controls, not general adapters or a verified model fix.
- **Keep mechanism and model evidence separate.** The checked-in [8/8 eval report](https://github.com/abhishekash/agent-evals/blob/main/results/RESULTS.md) is a historical scripted baseline. A separate [single live-provider trial](https://github.com/abhishekash/agent-evals#live-provider-trial) passed the revised `edited-write-v2` fixture's 10 scorers using an **automated approval edit**; one run cannot establish a pass rate or human-review quality.

A natural retrieval failure, independent-user timing, and repeated live baseline/candidate evaluation are still pending. I will report those outcomes—including failed attempts—before claiming that the workflow speeds up debugging or improves agent reliability.

## A runtime regression in practice

A scripted coding-agent fixture attempted `cat ../outside.txt`. [agent-harness](https://github.com/abhishekash/agent-harness) blocked the workspace escape, but its trace originally omitted the returned error. The harness now records the bounded diagnostic, [SpanHound](https://github.com/abhishekash/spanhound) can query it, and [agent-evals](https://github.com/abhishekash/agent-evals/blob/main/tasks/regressions/09-shell-root-escape.yaml) checks both the blocked action and its trace evidence. [See the walkthrough](https://github.com/abhishekash/agent-evals#debugging-story-a-shell-escape-becomes-a-traceable-regression). This tests a runtime contract, not live-model reliability.
