# TECHNICAL STATE — Mira & Mia Live

## Design goal
Stream Mira/Mia conversation without exposing the private ChatGPT UI.

## Privacy boundary
OBS sees only the public browser-source page.
A local/private control page handles interaction.
The local page cannot and should not silently scrape the private ChatGPT conversation.

## V1
Purpose: prove the private/public wall.

Success:
- public display worked;
- Mia could explicitly send approved text to stream.

Failure:
- required copying/pasting both sides.
- nicknamed the **Victorian court stenographer workflow**.

## V2
Architecture:
Mia local input → local server → OpenAI Responses API → Mira response → public display → OBS.

First API failure:
HTTP 500 surfaced because OpenAI returned `credit_balance_exhausted`.

Interpretation:
local bridge/server path worked; account had no remaining API credit.

Important: ChatGPT subscription and API billing are separate.

## V3
Package previously created in conversation:
`Mira_Mia_Live_V3_Automatic_CostGuard.zip`

Default local server port:
**8766**

Reason: V2 used 8765; separate ports prevent collision.

Private/control:
`http://localhost:8766/chat.html`

OBS display:
`http://localhost:8766/display.html`

Suggested OBS browser-source size:
1920 × 1080

### V3 behavior
- automatic Mia → public display
- automatic API Mira → public display
- Public checkbox for on/off-stream exchange
- `previous_response_id` used for API turn chaining
- stable Mira context supplied via `MIRA_CONTEXT.md`
- prompt-cache request
- model selector: Sol / Terra / Luna
- Terra default
- approximate usage/cost meter
- cached-input counter
- API-turn counter
- configurable session budget guard
- default local guard: **$1.00**
- scene buttons (Starting Soon / BRB / Technical Difficulties / Return)
- clear public display
- fresh API thread/reset meter

### Important limitation
The local cost guard is approximate. A final request can overshoot slightly because exact token usage is known after completion. OpenAI billing is authoritative.

### API-key handling
The generated batch workflow asks for the API key in the command window/environment rather than writing it into the project files.
Never show the key on stream or paste it into ordinary chat.

## Rejected relay alternative
A no-API-cost “ChatGPT Relay” idea was discussed:
- Mia types locally;
- message copied/pasted into ChatGPT;
- Mira reply copied back once.

Rejected because it still makes Mia perform too much manual middleware work.

**Mia Middleware Services™ is not the product.**
