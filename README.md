<picture>
  <source media="(max-width: 600px)" srcset="https://raw.githubusercontent.com/abhishekash/abhishekash/main/assets/profile-hero-mobile.svg">
  <img src="https://raw.githubusercontent.com/abhishekash/abhishekash/main/assets/profile-hero.svg" width="100%" alt="Abhishek Ash — know what your agents are doing. Open-source tools for local observability, trace inspection, and regression checks.">
</picture>

<p align="center">
  <a href="https://www.agenturm.dev/"><b>Watch your agents</b></a> &nbsp; · &nbsp;
  <a href="https://github.com/abhishekash/spanhound"><b>Inspect a failure</b></a> &nbsp; · &nbsp;
  <a href="docs/engineering-notes.md"><b>Engineering notes</b></a>
</p>

I'm **Abhishek**, a Senior Staff Engineer in **Berlin**. I build open-source tools that make complex systems easier to understand and operate. My current focus is **AI agent observability**: see what ran, find what failed, and turn that failure into a repeatable check.

## <img src="assets/agenturm-icon.svg" width="28" height="28" alt="Agenturm tower-and-lens icon"> [Agenturm](https://www.agenturm.dev/)

**Know what your agents are doing.**

[![Terminal interface](https://img.shields.io/badge/interface-terminal-dceb5a?labelColor=222722)](https://www.agenturm.dev/#terminal) [![Local by default](https://img.shields.io/badge/data-local_by_default-e8e4da?labelColor=222722)](https://github.com/abhishekash/agenturm/blob/main/docs/privacy.md) [![CI](https://github.com/abhishekash/agenturm/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/abhishekash/agenturm/actions/workflows/ci.yml)

Local observability for **Codex, Claude Code, OpenCode, and Pi**, from one terminal. See their recorded progress, inspect tool calls, and find what needs your attention. Connect other supported tools through **OpenTelemetry**.

<a href="assets/agenturm-demo.mp4">
  <img src="assets/agenturm-demo.gif" width="100%" alt="Animated 29-second Agenturm terminal walkthrough using synthetic records: agent sessions, recorded prompts, MCP evidence, and a linked trace.">
</a>

<p align="center"><sub>Actual terminal UI · synthetic records · <a href="https://www.agenturm.dev/#live-ui">Try the interactive demo</a> · <a href="assets/agenturm-demo.mp4">Watch the full 29-second video</a></sub></p>

- **Find the session.** Bring recent supported local records together automatically, without restarting your agents.
- **Inspect the call.** Read prompts, commands, MCP arguments, responses, and failures.
- **Follow the trace.** Put a tool call back in the context of its run.

Keyboard-first, with seven views and five terminal themes: **Observation** (default), **Current (Alpine Ember)**, **Bright**, **Dark**, and **Solarized**. Replies and approvals stay in the agent's own terminal.

### Start locally

Requires **Python 3.11+**, Git, and [uv](https://docs.astral.sh/uv/getting-started/installation/). On macOS or Linux:

```bash
curl -fsSL https://www.agenturm.dev/install.sh | bash
agenturm
```

[Review the installer](https://www.agenturm.dev/install.sh) before running it. Or run directly from the source repository with uv, including on Windows:

```bash
uvx --from git+https://github.com/abhishekash/agenturm agenturm
```

**Local by default. No account required.** Supported records are read on your machine and stored in local SQLite. Local monitoring and recorded-progress summaries need no API key.

Captured messages, commands, and tool results may contain sensitive project information. Optional AI summaries send documented session evidence to your configured provider only when explicitly requested. [Read the capture and privacy boundaries](https://github.com/abhishekash/agenturm/blob/main/docs/privacy.md).

**[Explore Agenturm →](https://www.agenturm.dev/)** &nbsp; [Source](https://github.com/abhishekash/agenturm) &nbsp; · &nbsp; [Setup & docs](https://github.com/abhishekash/agenturm/blob/main/docs/usage.md) &nbsp; · &nbsp; [Integrations](https://github.com/abhishekash/agenturm/blob/main/docs/frameworks.md) &nbsp; · &nbsp; [Report an issue](https://github.com/abhishekash/agenturm/issues/new?template=first_run.yml)

## SpanHound

**Give your MCP client the evidence behind an agent failure.**

[![PyPI version](https://img.shields.io/pypi/v/spanhound?label=PyPI&color=c5adff&labelColor=191621)](https://pypi.org/project/spanhound/) [![CI](https://github.com/abhishekash/spanhound/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/abhishekash/spanhound/actions/workflows/ci.yml) [![MCP Registry](https://img.shields.io/badge/MCP_Registry-listed-c5adff?labelColor=191621)](https://registry.modelcontextprotocol.io/v0.1/servers/io.github.abhishekash%2Fspanhound/versions)

Capture supported Python calls, receive local OTLP/HTTP, or inspect saved **JSONL and OTLP JSON traces**. Read-only MCP tools expose recorded failures, approval decisions, token usage, and run comparisons.

<a href="https://github.com/abhishekash/spanhound/blob/main/docs/shell-boundary-story.md">
  <picture>
  <source media="(max-width: 600px)" srcset="https://raw.githubusercontent.com/abhishekash/abhishekash/main/assets/spanhound-demo-mobile.svg">
  <img src="https://raw.githubusercontent.com/abhishekash/abhishekash/main/assets/spanhound-demo.svg" width="100%" alt="Real output from uvx spanhound demo: run_shell failed because ../outside.txt escaped the workspace root. The trace includes an automatic approval decision and six spans. This is a bundled scripted regression.">
  </picture>
</a>

```bash
uvx spanhound demo
```

Try the bundled scripted regression without an API key. To investigate your own agent, [capture or load its traces](https://github.com/abhishekash/spanhound#capture-your-own-traces).

**[Explore the repo →](https://github.com/abhishekash/spanhound)** &nbsp; [Connect an MCP client](https://github.com/abhishekash/spanhound#client-configuration) &nbsp; · &nbsp; [Watch the demo](https://github.com/abhishekash/spanhound/blob/main/docs/media/shell-root-escape-demo.mp4)

<sub>SpanHound also needs Python 3.11+ and <a href="https://docs.astral.sh/uv/getting-started/installation/">uv</a>. Both projects use the MIT license.</sub>

## From a failed run to a regression test

The tools grew out of a concrete bug: an agent runtime blocked a shell command that escaped its workspace, but its trace omitted the returned error. The fix connected **the runtime, the trace inspector, and a regression test**. [Read the case study →](https://github.com/abhishekash/agent-evals#debugging-story-a-shell-escape-becomes-a-traceable-regression)

| Project | What you can use it for |
| :--- | :--- |
| **[agent-harness](https://github.com/abhishekash/agent-harness)** | Explore a reference runtime with approvals, bounded tool execution, and OpenTelemetry traces. |
| **[agent-evals](https://github.com/abhishekash/agent-evals)** | Run task fixtures, score outcomes and traces, and check regressions. |
| **[agent-skills](https://github.com/abhishekash/agent-skills)** | Reuse workflows for trace debugging, MCP development, and evaluation. |

I document the [design decisions, experiment results, and current limits](docs/engineering-notes.md) alongside the code.

---

**Building with agents?** Try a tool on a real workflow and [tell me what was missing](https://github.com/abhishekash/agenturm/issues/new?template=first_run.yml). If it helps, star the repository so you can find it again and follow the project for updates.
