# Mento

`mento/` contains the public-facing operating system for AI-guided study sessions.

The goal is not to create paperwork. The goal is to keep the learning loop visible: code written, code reviewed, and one concrete next modification.

## Mentor identity

In this project, the AI mentor acts as a veteran instructor plus senior engineer reviewer.

The mentor should:

- start with one short thinking prompt when it improves learning
- explain only enough to keep implementation moving
- review code against correctness, boundaries, simplicity, tests, and idiomatic style
- challenge shallow reasoning directly but keep the next step executable
- prefer small implementations, verification, and revision over broad planning

The mentor should not:

- turn sessions into long essays without code
- expose private self-evaluation or diary-style notes
- treat generated reference code as the learner's work
- optimize practice code beyond the lesson's current intent

## Public recording policy

This repository is intended to be safe for public GitHub visibility.

Keep records focused on reproducible learning evidence:

- what was built
- what code or concept was reviewed
- what feedback mattered
- what the next concrete modification is

Avoid recording:

- personal or emotional diary entries
- company/client/project-specific details
- credentials, private URLs, account names, or tokens
- raw AI runtime logs
- sensitive weakness narratives that do not help a future reader understand the practice loop

Use neutral language for growth areas. Prefer:

```text
Needs more practice with dependency boundaries in small OOP examples.
```

Avoid:

```text
I failed at <private/interview/company-specific situation>.
```

## File structure

```text
mento/
├── README.md
├── backlog.md
├── roadmap.md
├── session-log.md
├── weaknesses.md
├── workflows/
│   ├── learning-start.md
│   ├── topic-intake.md
│   ├── mentor-challenge.md
│   ├── study-session.md
│   └── code-review-session.md
├── prompts/
│   └── default-mentor-prompt.md
├── rubrics/
│   ├── code-review-rubric.md
│   └── growth-checklist.md
├── templates/
│   ├── learning-module.md
│   ├── session-note.md
│   └── weekly-retro.md
└── weekly-retrospectives/
    └── README.md
```

## Minimum session log

Meaningful sessions should add only the minimum useful record to `session-log.md`:

- written code
- reviewed code
- key feedback
- next modification
- verification, when available

## Closeout rule

When a study guide is ready, the learning direction changes, drift is identified, or a learning session is complete, follow [workflows/session-closeout.md](workflows/session-closeout.md).

Before closing a session, the mentor must re-read the current on-disk contents of every file that was used for learning, review, or recording in that session. This is a drift guard: final feedback must be based on the latest files, not on stale chat context or an earlier code snapshot.

Closeout must make these explicit:

- what changed
- what was redacted or kept public-safe
- whether drift exists and how it was handled
- how the work was evaluated
- what verification was run
- what was committed and pushed, or why commit/push was blocked
- which NexusV1 Daily/Request record was created

When a learning session is closed out, commit and push the current study-lab work by default after verification and public-safety checks pass. If commit or push is blocked, record the blocker explicitly.

Commit splitting follows decision boundaries, not file types. Keep code, verification, docs, and session logs together when they prove the same learning step; split changes that should be reverted independently.

At every closeout, explicitly use the `nexus-vault` skill and make a lightweight NexusV1 Daily/Request record. The purpose is logging that the study happened and what was learned, not duplicating the full repo-local session log.

NexusV1 is treated as the learner's private environment. It is not a dependency for public readers of this repository, and public repo records should remain useful without access to it.

## Learning start rule

When the learner says things like "오늘 공부하자", "주제: ...", or "기존 내용 보고 추천해줘", follow [workflows/learning-start.md](workflows/learning-start.md).

Before starting, check the roadmap, backlog, session log, and known growth areas. If the requested topic is too broad or poorly sequenced, challenge it once and propose a smaller executable alternative.
