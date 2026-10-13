# Abhishek Ash

**Senior Staff Engineer based in Berlin.** I enjoy working on complex software systems and finding practical ways to make them easier to understand, operate, and improve.

My recent open-source work explores those ideas in tool-using AI agents. Going forward AI Observability will become more important. Hence, i am exploring the area.

## Recent open-source work

| Repository | Role in the workflow | Inspect the evidence |
|---|---|---|
| [agent-harness](https://github.com/abhishekash/agent-harness) | Reference runtime with risk-based approvals, bounded execution, MCP tools, and OpenTelemetry JSONL traces. | [Run and trace](https://github.com/abhishekash/agent-harness/blob/main/examples/demo_trace_render.txt) · [architecture decisions and limits](https://github.com/abhishekash/agent-harness/blob/main/docs/architecture-postmortem.md) |
| [SpanHound](https://github.com/abhishekash/spanhound) | Read-only MCP server for local JSONL and OTLP JSON traces: inspect failures, approvals, token usage, and run comparisons. | [Try `uvx spanhound demo`](https://github.com/abhishekash/spanhound#try-it-in-one-command) · [PyPI](https://pypi.org/project/spanhound/) · [OTLP example](https://github.com/abhishekash/spanhound/blob/main/tests/fixtures/otlp_trace.json) |
| [agent-evals](https://github.com/abhishekash/agent-evals) | Task fixtures, outcome/trace scorers, repeatable trials, and a retrieval-evidence experiment spanning the harness and a controlled LangGraph graph. | [Scripted baseline](https://github.com/abhishekash/agent-evals/blob/main/results/RESULTS.md) · [retrieval slice and bundle helper](https://github.com/abhishekash/agent-evals/blob/main/experiments/001-retrieval-loop/BASELINE.md) |
| [agent-skills](https://github.com/abhishekash/agent-skills) | Reusable workflows for trace debugging, approval design, MCP authoring, and eval-driven changes. | [Skills](https://github.com/abhishekash/agent-skills/tree/main/skills) · [validator](https://github.com/abhishekash/agent-skills/blob/main/scripts/validate_skills.py) |

**Start here:** [try the SpanHound demo](https://github.com/abhishekash/spanhound#try-it-in-one-command) → [run the harness demo](https://github.com/abhishekash/agent-harness) → [run the regressions](https://github.com/abhishekash/agent-evals#debugging-story-a-shell-escape-becomes-a-traceable-regression).

## Decisions and evidence boundaries

- **Capture only what is needed.** Tool arguments and successful outputs are opt-in in the harness; a trace that lacks retrieval results must not claim to prove repeated-output overlap.
- **Use existing spans before inventing a new standard.** The [retrieval experiment](https://github.com/abhishekash/agent-evals/blob/main/experiments/001-retrieval-loop/M0-DECISION.md) currently uses a thin, hashed export helper and operation-specific readiness checks. Its harness and LangGraph cases are scripted controls, not general adapters or a verified model fix.
- **Keep mechanism and model evidence separate.** The checked-in [8/8 eval report](https://github.com/abhishekash/agent-evals/blob/main/results/RESULTS.md) is a historical scripted baseline. A separate [single live-provider trial](https://github.com/abhishekash/agent-evals#live-provider-trial) passed the revised `edited-write-v2` fixture's 10 scorers using an **automated approval edit**; one run cannot establish a pass rate or human-review quality.

A natural retrieval failure, independent-user timing, and repeated live baseline/candidate evaluation are still pending. I will report those outcomes—including failed attempts—before claiming that the workflow speeds up debugging or improves agent reliability.

## A runtime regression in practice

A scripted coding-agent fixture attempted `cat ../outside.txt`. [agent-harness](https://github.com/abhishekash/agent-harness) blocked the workspace escape, but its trace originally omitted the returned error. The harness now records the bounded diagnostic, [SpanHound](https://github.com/abhishekash/spanhound) can query it, and [agent-evals](https://github.com/abhishekash/agent-evals/blob/main/tasks/regressions/09-shell-root-escape.yaml) checks both the blocked action and its trace evidence. [See the walkthrough](https://github.com/abhishekash/agent-evals#debugging-story-a-shell-escape-becomes-a-traceable-regression). This tests a runtime contract, not live-model reliability.
