# Abhishek Ash

**AI engineer building observable, testable agents.** I work on the execution layer around models: tool use, human approvals, MCP integrations, traces, and evaluations. Based in Berlin.

My current public work connects four small projects around one question: **Can we explain and test what an agent actually did, including its side effects?**

| Project | AI-native use case | Proof you can inspect |
|---|---|---|
| [agent-harness](https://github.com/abhishekash/agent-harness) | Run a tool-using assistant with risk-based approvals, budgets, and traceable decisions. | [Recorded run](https://github.com/abhishekash/agent-harness/blob/main/examples/demo_trace_render.txt) · [architecture decisions](https://github.com/abhishekash/agent-harness/blob/main/docs/architecture-postmortem.md) |
| [mcp-trace](https://github.com/abhishekash/mcp-trace) | Let an agent query prior runs for slow spans, token use, and approval history through MCP. | [Real trace fixture](https://github.com/abhishekash/mcp-trace/blob/main/examples/example_trace.jsonl) · [PyPI package](https://pypi.org/project/abhishekash-mcp-trace/0.1.1/) |
| [agent-evals](https://github.com/abhishekash/agent-evals) | Catch regressions in tool routing, denied writes, edited approvals, and budget stops. | [Eight task baseline](https://github.com/abhishekash/agent-evals/blob/main/results/RESULTS.md) · [task definitions](https://github.com/abhishekash/agent-evals/tree/main/tasks) |
| [agent-skills](https://github.com/abhishekash/agent-skills) | Give coding agents focused workflows for trace debugging, approval policy, MCP authoring, and eval design. | [Skill source](https://github.com/abhishekash/agent-skills/tree/main/skills) · [validator](https://github.com/abhishekash/agent-skills/blob/main/scripts/validate_skills.py) |

### How the pieces fit

`agent-harness` records tool calls and approval decisions as JSONL traces. `mcp-trace` exposes those traces to an MCP client. `agent-evals` runs repeatable tasks through the harness and checks the result, side effects, and trace. `agent-skills` documents the engineering workflow.

The published **8/8 eval baseline is scripted**: it verifies runtime mechanisms without a model or API key. It is not a live-model quality score. Live-model comparisons, with repeated runs and cost and latency reporting, are the next measurement step.

**Start here:** [Run the harness demo](https://github.com/abhishekash/agent-harness) → [inspect the trace with MCP](https://github.com/abhishekash/mcp-trace) → [read the eval results](https://github.com/abhishekash/agent-evals/blob/main/results/RESULTS.md).
