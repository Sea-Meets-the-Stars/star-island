# Getting started

## Goals

This repository will hold Star Island this and that.

## Prompts

1. Read this file.  Execute the 1st task under "Claude/CLAUDE.md file"
2. Read this file.  Execute the 1st task under "Claude/Skills"
3. Read this file.  Execute the 1st task under "Claude/Settings"
4. Read this file.  Execute the 1st task under "Basic start up"

## Claude

### CLAUDE.md file

Generate a basic CLAUDE.md file for this repository.  Include the following:

- I will perform git commands.
- If you do any calculation, generate it as a python script and write it to disk so that I can add it to the Repository.
- If you need to run Python, use the `ocean14` conda environment.

### Skills

Copy over the skills/ files from the `IOPtics` repository
(`~/Oceanography/python/IOPtics/.claude/skills/`).

### Settings

Copy over the settings.json file from the `IOPtics` repository
(`~/Oceanography/python/IOPtics/.claude/settings.json`).  Copy the policy,
not the accumulated path-specific allow entries that reference IOPtics' own
files and scratchpad paths.

## Basic start up

Generate the basic files that one needs for a Python GitHub repository, e.g.
a file for dependencies.  Examine the other Repositories in
`Oceanography/python` to see how I tend to organize things.  Also, make a
suggestion of which of their settings.json files to copy into this one.

## Logging

The "Logs" section will record Claude's work.  Please use the following format:

### <Date> (Short summary of the work)

<Detailed description of the work and what you learned>

...

## Logs

### 2026-10-04 (Run start-up prompts 1-4)

**1. CLAUDE.md file** — Generated `CLAUDE.md` with the three working rules
(user runs git; calculations become scripts on disk; Python via `ocean14`),
modelled on `victor-class/CLAUDE.md`.  Added a pointer to `claude_prompts/`.
The Project Overview repeats the placeholder Goals line and should be
rewritten once the purpose of the repo is settled.

**2. Skills** — Copied `critical-partner` and `grill-me` from
`IOPtics/.claude/skills/` into `.claude/skills/` unchanged.

**3. Settings** — Built `.claude/settings.json` from IOPtics' file, keeping
the house policy (37 allow entries: read-only shell, benign file ops,
read-only git, conda/pip/pytest/jupyter, publisher WebFetch domains) plus the
full deny list (`sudo`, `rm -rf` of `/` and `~`, `git push/commit/reset/rebase`)
and `ask` on `rm`.  Dropped 28 IOPtics-specific entries (one-off Crossref
lookups, absolute paths into IOPtics and its scratchpads).

**4. Basic start up** — Added `setup.py`, `requirements.txt`, `pytest.ini`,
`.gitignore` and a `star_island/` package with `tests/` and an import smoke
test, following `victor-class` (the most recent, cleanest sibling): `setup.py`
+ `requirements.txt` rather than `pyproject.toml`, tests under
`<package>/tests/`.  `.gitignore` is copied from `victor-class`.  Dependencies
are the generic science stack only; the oceanography extras (xarray, netcdf)
were left out until the repo's purpose is known.  `pytest` passes in `ocean14`.

*settings.json suggestion:* of the siblings, `cugn-climatology` has the
cleanest file — it is the IOPtics policy plus a few Crossref one-offs and
nothing else.  OETHER, PAB and retrieve-or-bust have picked up
repo-specific cruft.  The file written here is effectively
`cugn-climatology`'s minus the Crossref entries.

*Learned:* the repo lives in `~/Projects`, not `~/Oceanography/python`, and
its remote is `Sea-Meets-the-Stars/star-island` (the LICENSE is BSD-3,
Sea-Meets-the-Stars).  The Goals line is still a placeholder.

No git commands that change the repository were run.
