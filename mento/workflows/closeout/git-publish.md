# Git Publish Gate

학습 마무리 시 commit + push는 기본 수행입니다. 사용자가 명시적으로 멈추라고 했거나, 검증 실패, 공개 안전 문제, remote/branch 불명확, destructive risk 같은 blocker가 있을 때만 보류합니다.

## 커밋 전 체크

- `git status --short`로 staged/untracked 상태를 확인한다.
- `.omx/`, `.venv/`, `.idea/`, raw logs, secrets가 커밋 대상이 아닌지 확인한다.
- `git diff --stat`와 핵심 diff를 확인한다.
- commit splitting rule에 따라 commit 단위가 의사결정 경계와 맞는지 확인한다.
- closeout 기록이 `mento/session-log.md` 또는 관련 문서에 남았는지 확인한다.
- 테스트/검증 결과가 기록되었는지 확인한다.
- commit/push를 보류한다면 blocker를 `mento/session-log.md`와 최종 응답에 남긴다.

## Commit Splitting Rule

커밋은 파일 종류가 아니라 의사결정 경계로 나눕니다.

기본 질문:

```text
이 커밋을 나중에 되돌릴 때, 포함된 변경을 모두 함께 되돌려도 되는가?
```

대답이 "아니오"라면 커밋을 나눕니다.

원칙:

- `1 commit = 하나의 학습/운영 의사결정 단위`
- 같은 학습 단계의 code, tests/checks, guide, notes, session-log는 함께 커밋할 수 있다.
- 운영 규칙 변경은 practice code 변경과 분리한다. 단, 그 규칙 변경이 해당 세션 closeout 자체를 완성하기 위한 직접 변경이면 같은 closeout 묶음으로 허용한다.
- parser 선택, Python version policy, dependency/lockfile 변경처럼 되돌림 영향이 큰 결정은 별도 커밋을 우선한다.
- 서로 다른 learning track, unrelated cleanup, formatting-only churn은 별도 커밋으로 분리한다.
- 실험 코드와 안정화/검증 코드는 되돌림 경계가 다르면 분리한다.

작은 세션에서는 과도하게 쪼개지 않습니다. 기준은 "미래의 내가 커밋 하나만 읽고 의사결정과 검증을 이해할 수 있는가"입니다.

## Commit Message

커밋 메시지는 이 gate의 Lore Commit Protocol을 따릅니다.

### Lore Commit Protocol

모든 커밋 메시지는 git-native trailer를 사용한 짧은 decision record여야 합니다.

Format:

```text
<intent line: why the change was made, not what changed>

<optional concise body: constraints and approach rationale>

Constraint: <external constraint that shaped the decision>
Rejected: <alternative considered> | <reason for rejection>
Confidence: <low|medium|high>
Scope-risk: <narrow|moderate|broad>
Directive: <forward-looking warning for future modifiers>
Tested: <what was verified>
Not-tested: <known gaps in verification>
```

Rules:

- Intent line first; describe why, not what.
- Use trailers only when they add decision context.
- Use `Rejected:` for alternatives future agents should not re-explore.
- Use `Directive:` for warnings.
- Use `Constraint:` for external forces.
- Use `Not-tested:` for known verification gaps.

예:

```text
Keep OOP learning closeout safe and reproducible

Constraint: Public learning lab records must avoid private context and raw runtime state
Rejected: Ad-hoc end-of-session summaries | They do not reliably cover drift, redaction, verification, and push readiness
Confidence: high
Scope-risk: narrow
Directive: Run session closeout before committing learning direction or completion changes
Tested: documentation reference search and Python syntax checks
Tested: NexusV1 Daily/Request record created and read back
```

## Push 조건

푸시는 아래 조건을 만족하면 진행합니다.

- 학습 마무리 또는 repo closeout 상태인 경우
- remote/branch가 의도한 대상임을 확인한 경우
- 공개 안전 검열과 검증이 통과한 경우
