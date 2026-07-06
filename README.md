# AI Knowledge Agent

A Python CLI agent that answers questions via a local LLM, built as a portfolio
project to demonstrate Python, API integration, and agent-building fundamentals.

## Status

**Phase 1 — Python Fundamentals + API Wrapper.** CLI + LLM provider wrapper are
functional. RAG, tool use, and Docker Compose orchestration are planned next
(see project roadmap).

## Features

- CLI entry point: ask a question, get an answer from a local LLM
- `LLMProvider` class wrapping an OpenAI-compatible chat completions endpoint
- Automatic retry with exponential backoff (3 attempts: 1s / 2s / 4s) on
  connection failures
- Test suite covering the success path and retry-exhaustion path

## Requirements

- Python 3.11+
- LM Studio (or another OpenAI-compatible server) running locally at
  `http://localhost:1234/v1`

## Install

git clone <your-repo-url>
cd ai-knowledge-agent
python3 -m venv .venv
source .venv/bin/activate
pip install -e .

## Usage

Start LM Studio's local server, then:

python -m agent ask "What is a container in one sentence?"

If the LLM server is unreachable, the CLI retries 3 times with exponential
backoff before failing with a clear error message instead of a stack trace.

## Running tests

pytest -v

## Project structure

src/agent/
  __init__.py
  __main__.py     # entry point for `python -m agent`
  cli.py          # argparse CLI (ask subcommand)
  llm.py          # LLMProvider: HTTP calls + retry/backoff
  greeting.py
tests/
  test_llm.py     # success path + retry-exhaustion path (mocked)
pyproject.toml    # src-layout, editable install

## Roadmap

- [ ] RAG layer over a public document corpus (ChromaDB + embeddings)
- [ ] Tool-use agent loop (search, fetch, calculator)
- [ ] Docker Compose (agent + local LLM, no local installs required)
- [ ] CI via GitHub Actions
