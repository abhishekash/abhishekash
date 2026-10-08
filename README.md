# Abhishek Ash

I build infrastructure for AI agents — **harnesses, MCP servers, evaluations, and the skills that extend them**.

### Current focus

- 🔐 Human-in-the-loop agent execution: risk-tiered approvals, denials, and human-edited tool calls
- 🔭 Agent observability: OpenTelemetry spans, trace-backed debugging, token/cost accounting
- 🧪 Deterministic evals before live-model claims — measure the loop, side effects, and safety contracts

### Projects

| Project | What it demonstrates |
|---|---|
| [agent-harness](https://github.com/abhishekash/agent-harness) | Agent runtime with pluggable providers, HITL approval gates, OTel JSONL traces, MCP client, and `SKILL.md` loading |
| [mcp-trace](https://github.com/abhishekash/mcp-trace) | MCP server that lets agents query their own runs, span trees, slow spans, approvals, and token/cost usage |
| [agent-skills](https://github.com/abhishekash/agent-skills) | Opinionated skills for trace debugging, HITL policy design, MCP authoring, and eval-driven development |
| [agent-evals](https://github.com/abhishekash/agent-evals) | YAML task suite with deterministic scorers, safety checks, isolated workspaces, and trace-backed reports |

These projects share a trace contract: **the harness emits spans → `mcp-trace` makes them queryable → `agent-evals` scores the behavior → skills teach the workflow**.

📐 [Architecture postmortem](https://github.com/abhishekash/agent-harness/blob/main/docs/architecture-postmortem.md) — decisions, evidence, and honest limits.

### Stack & ecosystem

`Model Context Protocol` · `OpenTelemetry` · `agent harnesses` · `Agent Skills` · `Python` · `Go` · `TypeScript`

### Elsewhere

- 📫 ash.abhishek@gmail.com
- 🌍 Berlin, Germany

<!--
Next proof to add:
- merged contributions to pi-mono / modelcontextprotocol / anthropics/skills
- more postmortems from real runs
- the live [MCP Registry listing](https://registry.modelcontextprotocol.io/v0.1/servers/io.github.abhishekash%2Fmcp-trace/versions/0.1.0)
-->
