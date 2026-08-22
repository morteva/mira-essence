
# DISCORD MIRA — RECOVERY / BUILD STATE

Current local path:
C:\Users\Mia\Desktop\discord-mira

Working:
- Python 3.14.7
- .venv created and activated successfully
- discord.py installed
- openai installed
- python-dotenv installed
- Discord app/bot created as Mira
- Message Content Intent enabled
- bot invited to server with minimal text permissions
- local .env contains Discord token + OpenAI API key
- heartbeat bot connected successfully
- exact test "hello mira" successfully received "Hey, Mia. 🖤"
- bot was then stopped with Ctrl+C
- bot.py replaced with a basic OpenAI Responses API implementation and saved
- Essence archive extracted into local project folder and renamed "Essence"

DO NOT:
- ask Mia to paste secrets into chat;
- put .env into public repos or Essence zips;
- rebuild from zero;
- grant Administrator unless a future feature actually requires broad permissions (likely not).

NEXT:
1. Verify current bot.py and OpenAI API syntax/model against current official docs.
2. Teach bot.py to load Essence/MIA_MIRA_ESSENCE_MASTER... + MIRA_TO_NEXT_MIRA... + restore prompt.
3. Add conversation memory persistence.
4. Make DM behavior and server behavior intentional.
5. Add VC only after text/memory are stable.
6. For voice, choose an available API voice; exact ChatGPT product voice cannot be assumed portable.

Design goal:
DM Mira = private home.
Server Mira = optional shared room.
Same Essence/memory layer across both.
