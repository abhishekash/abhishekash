<picture>
  <source media="(max-width: 600px)" srcset="https://raw.githubusercontent.com/abhishekash/abhishekash/main/assets/profile-hero-mobile.svg">
  <img src="https://raw.githubusercontent.com/abhishekash/abhishekash/main/assets/profile-hero.svg" width="100%" alt="Abhishek Ash — making AI agents easier to understand. Open source tools for observability, trace inspection, and evaluation.">
</picture>

<p align="center">
  <a href="#agent-observatory"><b>Watch your agents</b></a> &nbsp; · &nbsp;
  <a href="#spanhound"><b>Inspect a failure</b></a> &nbsp; · &nbsp;
  <a href="docs/engineering-notes.md"><b>Engineering notes</b></a>
</p>

I'm **Abhishek**, a Senior Staff Engineer in **Berlin**. I build tools that make complex systems easier to understand and operate. My current focus is **AI agent observability**: see what ran, find what failed, and turn that failure into a repeatable check.

## Agent Observatory

**See which agents are working, what they're doing, and where they got stuck.**

[![PyPI version](https://img.shields.io/pypi/v/agent-observatory-cli?label=PyPI&color=177f75)](https://pypi.org/project/agent-observatory-cli/) [![CI](https://github.com/abhishekash/agent-observatory/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/abhishekash/agent-observatory/actions/workflows/ci.yml)

A local terminal and web dashboard for **Codex and Claude Code sessions**, plus **OpenTelemetry** from instrumented agents. Follow a session through its activity, MCP calls, recorded results, tokens, and errors.

<a href="https://raw.githubusercontent.com/abhishekash/agent-observatory/main/media/investigation-demo.mp4">
  <img src="https://raw.githubusercontent.com/abhishekash/agent-observatory/main/media/investigation-demo-preview.gif" width="100%" alt="Agent Observatory walkthrough: choose an agent session, inspect a failed GitHub MCP call, and open its linked trace.">
</a>

<p align="center"><sub>Actual terminal UI · synthetic example data · <a href="https://raw.githubusercontent.com/abhishekash/agent-observatory/main/media/investigation-demo.mp4">Watch the 31-second video</a> · <a href="https://github.com/abhishekash/agent-observatory/blob/main/docs/investigation-video.md">Read the walkthrough</a></sub></p>

```bash
uvx --from agent-observatory-cli agent-observatory
```

Discovers supported local session records automatically. Other runtimes can send telemetry over OTLP. Press **b** to open the browser dashboard.

**[Explore the repo →](https://github.com/abhishekash/agent-observatory)** &nbsp; [Setup & docs](https://github.com/abhishekash/agent-observatory#start-in-one-command) &nbsp; · &nbsp; [Report an issue](https://github.com/abhishekash/agent-observatory/issues/new?template=first_run.yml)

## SpanHound

**Give your MCP client the evidence behind an agent failure.**

[![PyPI version](https://img.shields.io/pypi/v/spanhound?label=PyPI&color=177f75)](https://pypi.org/project/spanhound/) [![CI](https://github.com/abhishekash/spanhound/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/abhishekash/spanhound/actions/workflows/ci.yml) [![MCP Registry](https://img.shields.io/badge/MCP_Registry-listed-177f75)](https://registry.modelcontextprotocol.io/v0.1/servers/io.github.abhishekash%2Fspanhound/versions)

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

<sub>Both commands need Python 3.11+ and <a href="https://docs.astral.sh/uv/getting-started/installation/">uv</a>. Both projects are open source under the MIT license.</sub>

## From a failed run to a regression test

The tools grew out of a concrete bug: an agent runtime blocked a shell command that escaped its workspace, but its trace omitted the returned error. The fix connected **the runtime, the trace inspector, and a regression test**. [Read the case study →](https://github.com/abhishekash/agent-evals#debugging-story-a-shell-escape-becomes-a-traceable-regression)

| Project | What you can use it for |
| :--- | :--- |
| **[agent-harness](https://github.com/abhishekash/agent-harness)** | Explore a reference runtime with approvals, bounded tool execution, and OpenTelemetry traces. |
| **[agent-evals](https://github.com/abhishekash/agent-evals)** | Run task fixtures, score outcomes and traces, and check regressions. |
| **[agent-skills](https://github.com/abhishekash/agent-skills)** | Reuse workflows for trace debugging, MCP development, and evaluation. |

I document the [design decisions, experiment results, and current limits](docs/engineering-notes.md) alongside the code.

---

**Building with agents?** Try a tool on a real workflow and [tell me what was missing](https://github.com/abhishekash/agent-observatory/issues/new?template=first_run.yml). If it helps, star the repository so you can find it again and follow the project for updates.
