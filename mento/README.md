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
├── mentor-routing.md
├── backlog.md
├── roadmap.md
├── session-log.md
├── weaknesses.md
├── workflows/
│   ├── learning-start.md
│   ├── topic-intake.md
│   ├── mentor-challenge.md
│   ├── study-session.md
│   ├── code-review-session.md
│   ├── session-closeout.md
│   └── closeout/
│       ├── public-safety.md
│       ├── verification.md
│       ├── git-publish.md
│       └── nexus-record.md
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

## Routing rule

`mentor-routing.md` is the canonical routing surface for mentor requests. It maps request types to the files that must be read first and the workflow that should run next.

Keep detailed workflow rules out of `AGENTS.md` and this README. Use:

- `mentor-routing.md` for routing
- `workflows/*.md` for procedures
- `workflows/closeout/*.md` for high-risk closeout gates
- `rubrics/*.md` for evaluation criteria

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

Closeout details are split by risk gate:

- [public-safety.md](workflows/closeout/public-safety.md)
- [verification.md](workflows/closeout/verification.md)
- [git-publish.md](workflows/closeout/git-publish.md)
- [nexus-record.md](workflows/closeout/nexus-record.md)

NexusV1 is treated as the learner's private environment. It is not a dependency for public readers of this repository, and public repo records should remain useful without access to it.

## Learning start rule

When the learner says things like "오늘 공부하자", "주제: ...", or "기존 내용 보고 추천해줘", follow [workflows/learning-start.md](workflows/learning-start.md).

Before starting, use [mentor-routing.md](mentor-routing.md) to identify the required read targets. If the requested topic is too broad or poorly sequenced, challenge it once and propose a smaller executable alternative.
