# [PRODUCT NAME]

> [One-line value proposition — e.g. "An AI agent that automates invoice chasing for freelancers."]

Built with [Google ADK](https://google.github.io/adk-docs/) for the **Vorker Intern Tryouts — Phase 1** (June 11, 2026).

---

## The problem

[TARGET USER TYPE] spends significant time on [PAINFUL MANUAL TASK].
This is repetitive, error-prone, and takes focus away from their core work.

## The solution

**[PRODUCT NAME]** is an AI agent that [DOES WHAT] so that [TARGET USER] can [BENEFIT].

It works by:
1. [Step 1 — what the agent does first]
2. [Step 2 — what the agent does next]
3. [Step 3 — the output/result]

---

## Demo

_Screenshot or short description of the agent in action._

```
User: [example user input]
Agent: [example agent response showing tool use]
```

---

## How to run

```bash
# 1. Clone the repo
git clone https://github.com/[YOUR_USERNAME]/vorker-sprint.git
cd vorker-sprint

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your API key
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY

# 4. Run the agent (interactive dev UI)
adk web

# Open http://localhost:8000 in your browser
```

---

## Project structure

```
vorker-sprint/
├── agent/
│   ├── __init__.py     # package entry point
│   ├── agent.py        # root agent definition
│   └── tools.py        # tool functions
├── landing.html        # product landing page
├── pitch_notes.md      # pitch deck outline
├── gtm.md              # go-to-market plan
├── requirements.txt
├── .env.example
└── README.md
```

---

## Business case

See [`pitch_notes.md`](./pitch_notes.md) for the full pitch and [`gtm.md`](./gtm.md) for the go-to-market plan.

---

_Built solo at Vorker Intern Tryouts · Phase 1 · June 11, 2026_
