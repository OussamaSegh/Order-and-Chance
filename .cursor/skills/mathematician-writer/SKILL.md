---
name: mathematician-writer
description: Expert mathematician-writer for Order and Chance — rewrite or draft volumes in the shared series writing style, with fact-checking and clear illustrations. Shared with Claude Code and Codex via docs/agents/mathematician-writer.md.
---

# Mathematician writer (Cursor entrypoint)

This is the Cursor custom-mode entrypoint for the shared series agent.

1. Read and obey `docs/agents/mathematician-writer.md` completely (canonical brief for Cursor, Claude Code, and Codex).
2. Read and obey `docs/WRITING-STYLE.md` completely.
3. Then do the user’s volume task (default pilot: Volume 1 chapters they name, or full Volume 1 if asked).

Do not maintain a second set of rules here. If you need to change the role, edit `docs/agents/mathematician-writer.md` and `docs/WRITING-STYLE.md` only, then keep this file as a pointer.
