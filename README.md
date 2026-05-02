# Learn with Agents

AI-guided software engineering study lab.

This repository is a public learning workspace for practicing software engineering with AI agents as mentors, reviewers, and pair-programming partners. It is not a polished portfolio project. It is a record of deliberate practice: small implementations, review notes, refactoring loops, and follow-up exercises.

## What this repo is

- A coding-first study lab for Python, Java, Go, design patterns, fundamentals, and system design.
- A public trail of learning sessions: what was built, what was reviewed, and what changed next.
- An AI-based mentorship workflow where Codex acts as an instructor and senior-engineer reviewer.
- A place to practice engineering habits: naming, boundaries, tests, tradeoffs, and maintainability.

## What this repo is not

- Not a finished product portfolio.
- Not a diary or private self-evaluation log.
- Not a dump of generated answers.
- Not a place for company, client, credential, or personally sensitive material.

## Public learning policy

Because this repository is intended to be public, records should stay useful but non-private.

Do commit:

- study modules under `learning/`
- practice code and reference implementations
- reproducible notes, guides, rubrics, and workflows
- concise session logs that focus on code, review, and next changes

Do not commit:

- credentials, tokens, account details, or private URLs
- company/client/project-specific details
- personal diary-style reflections
- raw AI runtime logs or local tool state
- IDE and virtual environment files

When in doubt, write learning evidence in this form:

```text
Built: <file or feature>
Reviewed: <specific code or concept>
Next: <one concrete modification>
```

## Structure

```text
.
├── learning/
│   ├── python/
│   │   └── oop/
│   │       ├── 00-legacy-notes/
│   │       └── 01-http-scraper/
│   ├── java/
│   ├── go/
│   ├── design-patterns/
│   └── fundamentals/
├── mento/
│   ├── workflows/
│   ├── prompts/
│   ├── rubrics/
│   ├── templates/
│   └── weekly-retrospectives/
├── AGENTS.md
├── pyproject.toml
└── uv.lock
```

## How study sessions work

1. Pick a topic or ask the agent mentor for the next recommended session.
2. The agent checks `mento/` records and relevant `learning/` material.
3. The session starts with a short prediction, design choice, or explanation prompt.
4. Code is written in `practice/`.
5. Reference code is used only for comparison, not as the first answer.
6. The agent reviews the result against the current rubric.
7. The session ends with one concrete next modification.
8. Meaningful sessions are summarized in `mento/session-log.md`.

## Learning start examples

```text
오늘 공부하자
오늘 2시간 공부하고 싶어
주제: Go 동시성
Java Stream 공부하고 싶어
기존 내용 보고 다음 학습 추천해줘
이 코드 리뷰하면서 학습하고 싶어
```

The agent does not blindly follow the requested topic. It first checks whether the topic is a good next step, too broad, missing prerequisites, or misaligned with the current path. If needed, it proposes a better alternative before moving into coding.

## Current tracks

- [Python](learning/python/README.md)
- [Java](learning/java/README.md)
- [Go](learning/go/README.md)
- [Design Patterns](learning/design-patterns/README.md)
- [Fundamentals](learning/fundamentals/README.md)

Current first module:

- [Python OOP HTTP Scraper](learning/python/oop/01-http-scraper/README.md)

## Agent mentor role

In this repository, the AI agent should act as:

- a veteran instructor
- a senior engineer reviewer
- a pair-programming guide
- a guardrail against shallow practice

The mentor should keep the bar high while keeping the work executable. The default output is not a lecture; it should lead to code, review, verification, and one next improvement.

## Module convention

Each module should usually follow this shape:

```text
learning/<track>/<area>/<NN-name>/
├── README.md          # module goal, run instructions, file map
├── guide.md           # study guide
├── practice/          # learner implementation
├── reference/         # comparison code, not first answer
├── notes.md           # concept notes and retrospective
└── requirements.txt   # only when needed
```

## Success criteria

A meaningful session should leave evidence of:

- code written
- code reviewed
- one next concrete modification

The goal is not to look perfect. The goal is to practice engineering deliberately and make the learning loop visible.
