# Abhishek Ash

**AI engineer building reliable infrastructure for tool-using agents.** I focus on the boundary between model output and real actions: approvals, tool execution, observability, and evaluations. Based in Berlin.

My engineering question: **when an agent fails, can we explain what happened, turn it into a regression, and tell whether a change actually helped?**

## A trace-to-regression example

A coding-agent fixture attempted `cat ../outside.txt`. [agent-harness](https://github.com/abhishekash/agent-harness) blocked the workspace escape, but the original trace recorded the tool call without its returned error. That made the failure hard to diagnose from traces alone.

The harness now records a bounded tool-error status and message; [mcp-trace-inspector](https://github.com/abhishekash/mcp-trace-inspector) makes the diagnostic queryable; and [agent-evals](https://github.com/abhishekash/agent-evals/blob/main/tasks/regressions/09-shell-root-escape.yaml) asserts both the blocked side effect and the presence of the error evidence. [Walk through the regression and query](https://github.com/abhishekash/agent-evals#debugging-story-a-shell-escape-becomes-a-traceable-regression).

This is a **scripted runtime-contract test**, not evidence that a live model reliably chooses safe actions. The design choice is to check the outcome *and* whether an engineer can diagnose a failure afterward.

## Open-source work

| Repository | Role in the workflow | Inspect the evidence |
|---|---|---|
| [agent-harness](https://github.com/abhishekash/agent-harness) | Reference runtime with risk-based approvals, bounded execution, MCP tools, and OpenTelemetry JSONL traces. | [Run and trace](https://github.com/abhishekash/agent-harness/blob/main/examples/demo_trace_render.txt) · [architecture decisions and limits](https://github.com/abhishekash/agent-harness/blob/main/docs/architecture-postmortem.md) |
| [mcp-trace-inspector](https://github.com/abhishekash/mcp-trace-inspector) | Local-first MCP server for inspecting runs, tool failures, approvals, activity, and descriptive comparisons. | [Query guide](https://github.com/abhishekash/mcp-trace-inspector/blob/main/docs/user-guide.md) · [trace fixture](https://github.com/abhishekash/mcp-trace-inspector/blob/main/examples/example_trace.jsonl) |
| [agent-evals](https://github.com/abhishekash/agent-evals) | Task fixtures, outcome/trace scorers, repeatable trials, and a retrieval-evidence experiment spanning the harness and a controlled LangGraph graph. | [Scripted baseline](https://github.com/abhishekash/agent-evals/blob/main/results/RESULTS.md) · [retrieval slice and bundle helper](https://github.com/abhishekash/agent-evals/blob/main/experiments/001-retrieval-loop/BASELINE.md) |
| [agent-skills](https://github.com/abhishekash/agent-skills) | Reusable workflows for trace debugging, approval design, MCP authoring, and eval-driven changes. | [Skills](https://github.com/abhishekash/agent-skills/tree/main/skills) · [validator](https://github.com/abhishekash/agent-skills/blob/main/scripts/validate_skills.py) |

**Start here:** [run the harness demo](https://github.com/abhishekash/agent-harness) → [inspect with mcp-trace-inspector](https://github.com/abhishekash/mcp-trace-inspector#install--run) → [run the regressions](https://github.com/abhishekash/agent-evals#debugging-story-a-shell-escape-becomes-a-traceable-regression).

## Decisions and evidence boundaries

- **Capture only what is needed.** Tool arguments and successful outputs are opt-in in the harness; a trace that lacks retrieval results must not claim to prove repeated-output overlap.
- **Use existing spans before inventing a new standard.** The [retrieval experiment](https://github.com/abhishekash/agent-evals/blob/main/experiments/001-retrieval-loop/M0-DECISION.md) currently uses a thin, hashed export helper and operation-specific readiness checks. Its harness and LangGraph cases are scripted controls, not general adapters or a verified model fix.
- **Keep mechanism and model evidence separate.** The checked-in [8/8 eval report](https://github.com/abhishekash/agent-evals/blob/main/results/RESULTS.md) is a historical scripted baseline. A separate [single live-provider trial](https://github.com/abhishekash/agent-evals#live-provider-trial) passed the revised `edited-write-v2` fixture's 10 scorers using an **automated approval edit**; one run cannot establish a pass rate or human-review quality.

A natural retrieval failure, independent-user timing, and repeated live baseline/candidate evaluation are still pending. I will report those outcomes—including failed attempts—before claiming that the workflow speeds up debugging or improves agent reliability.
