# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository will hold Star Island this and that.

## Working Rules

- **Git**: The user will perform all git commands (commit, push, etc.). Read-only git (`status`, `diff`, `log`) is fine; do not run anything that changes repository state.
- **Calculations**: If you do any calculation, generate it as a Python script and write it to disk so that it can be added to the repository.
- **Python environment**: If you need to run Python, use the `ocean14` conda environment (e.g., `conda run -n ocean14 python script.py`).

## Prompts

Task instructions live in `claude_prompts/`. Start with `claude_prompts/start_up.md` and do the numbered task you are pointed at. Log completed work under that file's `## Logs` section.
