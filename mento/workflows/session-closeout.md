# Session Closeout Workflow

학습 준비, 방향 수정, drift 식별, 학습 종료, 또는 공개 가능한 변경 정리가 필요할 때 사용하는 closeout orchestrator입니다.

목표는 closeout 절차 전체를 한 파일에 쌓는 것이 아니라, 종료 순서와 필수 gate를 안정적으로 라우팅하는 것입니다. 세부 위험 gate는 `mento/workflows/closeout/` 아래 문서가 canonical source입니다.

## 1. Closeout 이벤트 분류

먼저 이번 종료가 무엇인지 하나로 분류합니다.

| 이벤트 | 의미 | 필수 산출물 |
|---|---|---|
| `guide-ready` | 학습 가이드/준비가 완료됨 | 사용할 파일, 성공 기준, 첫 실습 목표 |
| `direction-changed` | 학습 방향 또는 우선순위가 바뀜 | 바뀐 이유, 새 순서, 밀린 항목 |
| `drift-identified` | 계획과 실제 진행이 어긋남 | drift 내용, 원인, 복구/수용 결정 |
| `learning-complete` | 한 세션 또는 모듈 학습이 끝남 | 코드, 리뷰, 검증, 다음 수정 |
| `repo-closeout` | 공개 저장소 변경을 커밋/푸시할 준비 | diff 요약, 검열 결과, 검증, 커밋 메시지 |

하나의 작업이 여러 이벤트에 해당하면 가장 강한 이벤트를 기준으로 닫습니다.

```text
learning-complete > drift-identified > direction-changed > guide-ready
```

`repo-closeout`은 별도 공개 저장소 정리까지 포함하는 강한 closeout입니다. 일반 `learning-complete`도 검증과 공개 안전 검열을 통과하면 commit + push 기본 규칙을 따릅니다.

## 2. 최신 파일 재읽기

closeout 전에 이번 학습에서 사용한 파일을 현재 디스크에서 다시 읽습니다.

목적은 stale context로 인한 drift를 막는 것입니다. 리뷰 중간에 코드나 문서가 바뀌었을 수 있으므로, 최종 피드백과 기록은 반드시 최신 파일 상태를 기준으로 합니다.

재읽기 대상:

- 사용자가 작성하거나 수정한 `practice/` 코드
- 리뷰에 사용한 reference 코드, guide, notes
- closeout에 기록할 `mento/` 문서
- 검증 대상 파일과 untracked 학습 파일

절차:

1. `git status --short`와 필요한 파일 목록을 확인한다.
2. 이번 학습 판단에 사용한 파일을 `sed`, `rg`, `nl` 등으로 다시 읽는다.
3. 사용자가 "이미 바꿨다"고 말한 내용은 이전 대화가 아니라 현재 파일을 기준으로 확인한다.
4. 최신 파일 상태와 기존 피드백/기록이 다르면 기록과 검증 명령을 갱신한다.

## 3. 작업 내용 정리

아래 순서로 현재 상태를 요약합니다.

1. 의도: 원래 무엇을 하려 했는가?
2. 실제 변경: 어떤 파일과 코드/문서를 바꿨는가?
3. 학습 증거: 작성한 코드, 리뷰한 코드, 검증 결과는 무엇인가?
4. 남은 일: 다음 한 가지 수정은 무엇인가?
5. 보류한 일: 지금 하지 않은 이유는 무엇인가?

기록 위치:

- 세션/모듈 진행: `mento/session-log.md`
- 다음 작업: `mento/backlog.md`
- 장기 방향: `mento/roadmap.md`
- 반복 약점: `mento/weaknesses.md`
- 모듈별 회고: 해당 `learning/.../notes.md`

## 4. Public Safety Gate

공개 저장소에 안전한 내용만 남기는지 확인합니다.

Canonical gate:

- `mento/workflows/closeout/public-safety.md`

이 gate가 통과하기 전에는 commit/push를 진행하지 않습니다.

## 5. Drift 정리

Drift는 "계획과 실제가 다르다"는 사실 자체가 문제가 아니라, 기록 없이 누적되는 것이 문제입니다.

Drift 유형:

- `scope-drift`: 오늘 범위보다 커짐
- `sequence-drift`: 로드맵 순서와 달라짐
- `artifact-drift`: README, roadmap, backlog, notes가 서로 다름
- `quality-drift`: 검증/리뷰 없이 문서만 늘어남
- `privacy-drift`: 공개 저장소에 부적절한 맥락이 들어감

처리 방식:

1. Drift를 한 문장으로 적습니다.
2. `accept`, `correct`, `defer` 중 하나를 고릅니다.
3. 선택 이유와 다음 조치를 남깁니다.

예:

```text
Drift: OOP 학습이 구현보다 운영 문서 정리로 이동했다.
Decision: accept.
Reason: 공개 학습 lab 운영 기준이 먼저 필요했다.
Next: 다음 세션은 practice/oop_scraper.py 구현으로 되돌린다.
```

## 6. 평가

학습 종료 또는 방향 수정 시에는 아래 질문으로 평가합니다.

- 오늘 작성한 코드가 있는가?
- 리뷰받은 코드 또는 리뷰 대상이 있는가?
- 실행/검증 증거가 있는가?
- 다음 수정 하나가 명확한가?
- 이번 변경이 현재 roadmap/backlog와 일치하는가?
- 불필요한 문서화가 코딩을 대체하지 않았는가?
- 공개 저장소에 안전한 내용만 남았는가?

평가 결과는 길게 쓰지 않습니다. `pass`, `partial`, `blocked` 중 하나와 근거만 남깁니다.

## 7. Verification Gate

변경 종류에 맞게 최소 검증을 수행합니다.

Canonical gate:

- `mento/workflows/closeout/verification.md`

검증하지 못한 항목은 `Not-tested:` 또는 세션 로그에 명시합니다.

## 8. Git Publish Gate

학습 마무리 시 commit + push는 기본 수행입니다. 단, 검증 실패, 공개 안전 문제, remote/branch 불명확, destructive risk 같은 blocker가 있으면 보류하고 blocker를 기록합니다.

학습 플래닝과 실제 학습은 PR을 분리합니다. 계획, 커리큘럼, workflow, module scaffold, `learning-plan.md`는 planning PR에 담고, 실제 학습 중 채운 notes, practice code, 리뷰 피드백, 다음 수정은 별도 learning PR에 담습니다. 실제 학습 과정에서 학습 문서를 수정하는 것은 세션 증거와 다음 수정 기록을 남기기 위한 경우 허용합니다.

Canonical gate:

- `mento/workflows/closeout/git-publish.md`

## 9. NexusV1 Record Gate

작업 마무리 시에는 `nexus-vault` 스킬을 명시적으로 사용해 NexusV1 기록을 반드시 남깁니다. NexusV1은 사적 환경이며 public repo 독자의 재현 요구사항이 아닙니다.

Canonical gate:

- `mento/workflows/closeout/nexus-record.md`

## 10. 완료 선언 형식

최종 응답은 짧게 아래를 포함합니다.

```text
완료 상태: <guide-ready|direction-changed|drift-identified|learning-complete|repo-closeout>
정리: <핵심 변경>
검열: <통과/수정 내용>
Drift: <없음 또는 처리 결과>
평가: <pass|partial|blocked + 근거>
검증: <실행한 명령/결과>
Git: <pushed|blocked + hash/branch 또는 blocker>
NexusV1: <recorded|blocked + Request/Daily 또는 blocker>
다음 수정: <하나>
```
