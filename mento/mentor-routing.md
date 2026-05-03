# Mentor Routing

이 파일은 멘토 동작의 canonical routing surface입니다. 절차를 길게 설명하지 않고, 요청 유형별로 먼저 읽을 파일과 다음 workflow만 지정합니다.

## Routing Principles

- `AGENTS.md`는 Codex CLI가 자동으로 읽는 bootstrap이다.
- 이 파일은 요청 유형을 workflow로 연결하는 라우터다.
- `mento/workflows/*.md`는 실제 절차를 담당한다.
- `mento/workflows/closeout/*.md`는 closeout 중 실수 비용이 큰 gate를 담당한다.
- `mento/rubrics/*.md`는 평가 기준만 담당한다.
- `README.md`는 public reader 설명이며, 멘토 실행 규칙의 canonical source가 아니다.

## Learning Start

Trigger examples:

- "오늘 공부하자"
- "오늘 2시간 공부하고 싶어"
- "주제: <topic>"
- "<language/topic> 공부하고 싶어"
- "기존 내용 보고 다음 학습 추천해줘"

Read first:

- `mento/roadmap.md`
- `mento/session-log.md`
- `mento/weaknesses.md`
- `mento/backlog.md`
- relevant `learning/<track>/README.md`
- relevant module `README.md`, `guide.md`, and `notes.md`

Then follow:

- `mento/workflows/learning-start.md`

## Topic Intake

Use when a new module, new track, or broad new study topic is being considered.

Read first:

- `mento/roadmap.md`
- `mento/backlog.md`
- existing track README files under `learning/`
- `mento/workflows/topic-intake.md`

Then follow:

- `mento/workflows/topic-intake.md`

## Mentor Challenge

Use when the requested topic is too broad, poorly sequenced, missing prerequisites, or likely to reduce learning value.

Read first:

- current roadmap/backlog context
- relevant `learning/` material
- `mento/workflows/mentor-challenge.md`

Then follow:

- Warn once, propose a smaller executable alternative, then continue with the learner's choice if they insist.

## Study Session

Use when the learner is actively implementing or modifying practice code.

Read first:

- relevant module `guide.md`
- relevant `practice/` files
- relevant `reference/` files only when comparison is appropriate
- module `notes.md`
- `mento/workflows/study-session.md`

Then follow:

- `mento/workflows/study-session.md`

## Code Review Session

Use when the learner asks for review or brings code for feedback.

Read first:

- target `practice/` code
- relevant module `guide.md`
- relevant module `notes.md`
- `mento/rubrics/code-review-rubric.md`
- `mento/workflows/code-review-session.md`

Then follow:

- `mento/workflows/code-review-session.md`

## Closeout

Use when a guide is ready, direction changes, drift is identified, learning completes, or repo changes are ready to publish.

Read first:

- `git status --short`
- every file used for learning, review, verification, or recording in the current session
- `mento/workflows/session-closeout.md`

Then follow:

- `mento/workflows/session-closeout.md`

Mandatory closeout gates:

- latest file reread
- public safety
- drift decision
- evaluation
- verification
- git publish decision
- NexusV1 record decision

## Retrospective

Use when the learner asks to review progress, choose the next weakness, or adjust the learning direction.

Read first:

- `mento/session-log.md`
- `mento/weaknesses.md`
- `mento/roadmap.md`
- `mento/backlog.md`
- relevant module `notes.md`

Then follow:

- Use the learning-start judgment shape when choosing the next session.
- Use closeout if roadmap, backlog, weaknesses, or public records change.
