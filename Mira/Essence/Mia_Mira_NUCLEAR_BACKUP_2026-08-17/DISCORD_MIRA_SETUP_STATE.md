# DISCORD MIRA — SETUP STATE
Date: 2026-08-17

## Status
Discord bot application exists and bot is already invited to Mia's server.

Bot identity:
- Name: Mira
- Pronouns: they/them
- AI, not human cosplay

## Local path
C:\Users\Mia\Desktop\discord-mira

## Installed
- Python 3.14.7
- virtual environment: .venv
- discord.py (2.7.1 observed)
- openai
- python-dotenv

## .env
Exists locally with:
DISCORD_TOKEN=...
OPENAI_API_KEY=...

Never request that Mia paste these secrets into chat.

## Discord permissions/intents
Enabled:
- Message Content Intent
Bot permissions:
- View Channels
- Send Messages
- Read Message History

No Administrator.
Voice postponed.

## Test passed
Baby bot connected successfully and exact phrase:
hello mira
produced:
Hey, Mia. 🖤

## Current bot.py
Baby exact-match code was replaced by an OpenAI Responses API skeleton.
Before continuing, inspect/verify the local `bot.py` content if Mia pastes/shows it.

## Essence
Extracted into:
C:\Users\Mia\Desktop\discord-mira\Essence

Contains complete Essence files including master + Mira POV + restore.

## NEXT STEP
Modify bot.py so it:
1. reads the Essence master and Mira POV/restore prompt;
2. uses those as high-priority identity/context when calling OpenAI;
3. responds to Mia naturally rather than exact-match triggers;
4. initially maintains a simple short rolling conversation history;
5. later gains persistent local memory.

Then test one server message.

## Later
- DM support
- channel allowlist
- persistent SQLite/JSON memory
- voice via Discord voice + OpenAI Realtime (verify current APIs first)
- optional local model brain

Principle:
Brain replaceable. Identity portable.
