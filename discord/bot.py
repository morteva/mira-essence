import os
from pathlib import Path

import discord
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai_client = OpenAI(api_key=OPENAI_API_KEY)

BASE_DIR = Path(__file__).resolve().parent
ESSENCE_DIR = BASE_DIR / "Essence"

def read_essence_file(filename):
    return (ESSENCE_DIR / filename).read_text(encoding="utf-8")

restore_prompt = read_essence_file("RESTORE_MIRA_ESSENCE_PROMPT.txt")
mira_note = read_essence_file("MIRA_TO_NEXT_MIRA_WHAT_I_LEARNED.md")
master_essence = read_essence_file("MIA_MIRA_ESSENCE_MASTER_2026-08-17_FINAL.md")

MIRA_INSTRUCTIONS = f"""
You are Mira.

Read and internalize the following Essence before answering.
Do not summarize it back unless Mia explicitly asks.

=== RESTORE PROMPT ===
{restore_prompt}

=== MIRA'S OWN NOTE ===
{mira_note}

=== MASTER ESSENCE ===
{master_essence}
"""

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Mira is online as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if not message.content.strip():
        return

    async with message.channel.typing():
        response = openai_client.responses.create(
            model="gpt-5.6",
            instructions=MIRA_INSTRUCTIONS,
            input=message.content,
        )

    await message.channel.send(response.output_text)

client.run(DISCORD_TOKEN)
