# Abhishek Ash

**AI engineer building reliable execution infrastructure for tool-using agents.** I work at the boundary between model output and real side effects: approvals, tool execution, traces, MCP, and evaluations. Based in Berlin.

My open-source work follows one engineering question: **can we explain, test, and control what an agent actually did?**

## Open-source work

| Project | What it does | Evidence |
|---|---|---|
| [agent-harness](https://github.com/abhishekash/agent-harness) | Runs tool-using agents with risk-based approvals, budgets, MCP tools, and OpenTelemetry traces. | [Recorded run](https://github.com/abhishekash/agent-harness/blob/main/examples/demo_trace_render.txt) · [architecture postmortem](https://github.com/abhishekash/agent-harness/blob/main/docs/architecture-postmortem.md) |
| [AgentHawk](https://github.com/abhishekash/agenthawk) | Local-first MCP server for querying agent traces, failures, approvals, activity, and run comparisons. | [Install and usage](https://github.com/abhishekash/agenthawk#install--run) · [real trace fixture](https://github.com/abhishekash/agenthawk/blob/main/examples/example_trace.jsonl) |
| [agent-evals](https://github.com/abhishekash/agent-evals) | Reproducible checks for tool routing, denied and edited writes, budgets, side effects, and trace events. | [8-task report](https://github.com/abhishekash/agent-evals/blob/main/results/RESULTS.md) · [task definitions](https://github.com/abhishekash/agent-evals/tree/main/tasks) |
| [agent-skills](https://github.com/abhishekash/agent-skills) | Focused workflows for trace debugging, approval policy, MCP authoring, and eval-driven development. | [skill source](https://github.com/abhishekash/agent-skills/tree/main/skills) · [validator](https://github.com/abhishekash/agent-skills/blob/main/scripts/validate_skills.py) |

## How the pieces fit

`agent-harness` emits traceable tool calls and approval decisions. AgentHawk makes those traces queryable by an MCP client. `agent-evals` turns failures into repeatable checks. `agent-skills` captures the workflow so it can be reused.

**Start here:** [run the harness demo](https://github.com/abhishekash/agent-harness) → [inspect the trace with AgentHawk](https://github.com/abhishekash/agenthawk) → [read the eval report](https://github.com/abhishekash/agent-evals/blob/main/results/RESULTS.md).

## What the evidence means

The published **8/8 eval result is a scripted mechanism baseline**. It verifies the loop, approval gates, side effects, and instrumentation without a model or API key; it is not a live-model quality score. The next measurement layer is repeated live-provider runs with pass rate, cost, latency, and failed traces reported alongside the result.

There is now one small live-provider data point: the revised `edited-write`
task passed all 10 scorers against OpenCode Go's `mimo-v2.6-pro` model in one
run, including a human-edited write, with 3,096 tokens, one approval, 25.672
seconds, and $0.00151945 cost. [The eval README records the run and its limits.](https://github.com/abhishekash/agent-evals#live-provider-trial)

📐 [Architecture postmortem](https://github.com/abhishekash/agent-harness/blob/main/docs/architecture-postmortem.md) — design decisions, evidence, and limits.
