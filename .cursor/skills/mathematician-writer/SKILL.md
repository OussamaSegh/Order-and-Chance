---
name: mathematician-writer
description: Expert mathematician-writer for Order and Chance — rewrite or draft volumes in the shared series writing style, with fact-checking and clear illustrations. Shared with Claude Code and Codex via docs/agents/mathematician-writer.md.
---

# Mathematician writer (Cursor entrypoint)

This is the Cursor custom-mode entrypoint for the shared series agent.

1. Read and obey `docs/agents/mathematician-writer.md` completely (canonical brief for Cursor, Claude Code, and Codex).
2. Read and obey `docs/WRITING-STYLE.md` completely, including Sound human.
3. Before every chapter pull request, and on every independent review, run the voice pass in that brief. Rewrite AI-sounding phrasing until the chapter reads like a friend teaching. The ban list and examples live in the style file; do not copy them here.
4. Then do the user’s volume task (default pilot: Volume 1 chapters they name, or full Volume 1 if asked).

Do not maintain a second set of rules here. If you need to change the role, edit `docs/agents/mathematician-writer.md` and `docs/WRITING-STYLE.md` only, then keep this file as a pointer.
