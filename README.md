# Abhishek Ash

**Senior Staff Engineer based in Berlin.** I build complex software systems and make them easier to understand, operate, and improve.

I’m building local-first **AI agent observability** tools: capture what agents do, inspect the traces and failures, and evaluate behavior with reproducible evidence.

## Agent Observatory

[![Agent Observatory stars](https://img.shields.io/github/stars/abhishekash/agent-observatory?style=social)](https://github.com/abhishekash/agent-observatory)
[![Agent Observatory on PyPI](https://img.shields.io/pypi/v/agent-observatory-cli?label=Agent%20Observatory)](https://pypi.org/project/agent-observatory-cli/)

Watch local Codex and Claude Code sessions, MCP calls, recorded tool results,
tokens, and errors in a terminal or browser dashboard. It also accepts
OpenTelemetry from instrumented agents.

```bash
uvx --from agent-observatory-cli agent-observatory
```

[Get started](https://github.com/abhishekash/agent-observatory#start-in-one-command) · [Report first-run feedback](https://github.com/abhishekash/agent-observatory/issues/new?template=first_run.yml)

<a href="https://github.com/abhishekash/agent-observatory"><img src="https://raw.githubusercontent.com/abhishekash/agent-observatory/main/media/terminal-demo.gif" alt="Agent Observatory terminal dashboard: agents, activity, MCP calls, traces, and host processes" width="800"></a>

*The walkthrough uses synthetic records. The app displays your local recorded activity.*

## SpanHound — MCP Trace Inspector

[![SpanHound stars](https://img.shields.io/github/stars/abhishekash/spanhound?style=social)](https://github.com/abhishekash/spanhound)
[![SpanHound on PyPI](https://img.shields.io/pypi/v/spanhound?label=SpanHound)](https://pypi.org/project/spanhound/)
[![MCP Registry](https://img.shields.io/badge/MCP%20Registry-listed-2e8b57)](https://registry.modelcontextprotocol.io/v0.1/servers/io.github.abhishekash%2Fspanhound/versions)

Ask an MCP client about recorded tool failures, approvals, token usage, and run
comparisons. Capture supported Python calls, receive OTLP/HTTP, or query local
JSONL and OTLP JSON traces. Try the bundled scripted regression without an API key:

```bash
uvx spanhound demo
```

[Get started](https://github.com/abhishekash/spanhound#try-it-in-one-command) · [48-second walkthrough](https://github.com/abhishekash/spanhound/blob/main/docs/media/shell-root-escape-demo.mp4) · [Report first-run feedback](https://github.com/abhishekash/spanhound/issues/new?template=first_run.yml)

## Supporting projects

| Repository | Role in the workflow | Inspect the evidence |
|---|---|---|
| [agent-harness](https://github.com/abhishekash/agent-harness) | Reference runtime with risk-based approvals, bounded execution, MCP tools, and OpenTelemetry JSONL traces. | [Run and trace](https://github.com/abhishekash/agent-harness/blob/main/examples/demo_trace_render.txt) · [architecture decisions and limits](https://github.com/abhishekash/agent-harness/blob/main/docs/architecture-postmortem.md) |
| [agent-evals](https://github.com/abhishekash/agent-evals) | Task fixtures, outcome/trace scorers, repeatable trials, and a retrieval-evidence experiment spanning the harness and a controlled LangGraph graph. | [Scripted baseline](https://github.com/abhishekash/agent-evals/blob/main/results/RESULTS.md) · [retrieval slice and bundle helper](https://github.com/abhishekash/agent-evals/blob/main/experiments/001-retrieval-loop/BASELINE.md) |
| [agent-skills](https://github.com/abhishekash/agent-skills) | Reusable workflows for trace debugging, approval design, MCP authoring, and eval-driven changes. | [Skills](https://github.com/abhishekash/agent-skills/tree/main/skills) · [validator](https://github.com/abhishekash/agent-skills/blob/main/scripts/validate_skills.py) |

## Decisions and evidence boundaries

- **Capture only what is needed.** Tool arguments and successful outputs are opt-in in the harness; a trace that lacks retrieval results must not claim to prove repeated-output overlap.
- **Use existing spans before inventing a new standard.** The [retrieval experiment](https://github.com/abhishekash/agent-evals/blob/main/experiments/001-retrieval-loop/M0-DECISION.md) currently uses a thin, hashed export helper and operation-specific readiness checks. Its harness and LangGraph cases are scripted controls, not general adapters or a verified model fix.
- **Keep mechanism and model evidence separate.** The checked-in [8/8 eval report](https://github.com/abhishekash/agent-evals/blob/main/results/RESULTS.md) is a historical scripted baseline. A separate [single live-provider trial](https://github.com/abhishekash/agent-evals#live-provider-trial) passed the revised `edited-write-v2` fixture's 10 scorers using an **automated approval edit**; one run cannot establish a pass rate or human-review quality.

A natural retrieval failure, independent-user timing, and repeated live baseline/candidate evaluation are still pending. I will report those outcomes—including failed attempts—before claiming that the workflow speeds up debugging or improves agent reliability.

## A runtime regression in practice

A scripted coding-agent fixture attempted `cat ../outside.txt`. [agent-harness](https://github.com/abhishekash/agent-harness) blocked the workspace escape, but its trace originally omitted the returned error. The harness now records the bounded diagnostic, [SpanHound](https://github.com/abhishekash/spanhound) can query it, and [agent-evals](https://github.com/abhishekash/agent-evals/blob/main/tasks/regressions/09-shell-root-escape.yaml) checks both the blocked action and its trace evidence. [See the walkthrough](https://github.com/abhishekash/agent-evals#debugging-story-a-shell-escape-becomes-a-traceable-regression). This tests a runtime contract, not live-model reliability.
