# Session Closeout Workflow

학습 준비, 방향 수정, drift 식별, 학습 종료, 또는 공개 가능한 변경 정리가 필요할 때 사용하는 종료 프로세스입니다.

목표는 "무엇을 했는지"를 정리하는 데서 끝나지 않습니다. 공개 안전성, 학습 방향 정합성, 검증 증거, 기본 commit + push, 필수 NexusV1 기록까지 한 흐름으로 닫습니다.

## 1. closeout 이벤트 분류

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

학습 마무리에서는 검증과 공개 안전 검열을 통과한 뒤 현재 study-lab 변경을 commit + push하는 것이 기본입니다. `repo-closeout`은 별도 공개 저장소 정리까지 포함하는 강한 closeout이지만, 일반 `learning-complete`도 commit + push 기본 규칙을 따른다.

## 2. 최신 파일 재읽기

closeout 전에 이번 학습에서 사용한 파일을 현재 디스크에서 다시 읽습니다.

목적은 drift 식별입니다. 리뷰 중간에 코드나 문서가 바뀌었을 수 있으므로, 최종 피드백과 기록은 반드시 최신 파일 상태를 기준으로 합니다.

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

## 4. 공개 안전 검열

이 저장소는 public learning lab이므로 커밋 전 반드시 검열합니다.

### 제거하거나 일반화할 것

- 개인 신상, 감정적/일기식 서술
- 회사, 고객, 계정, 인터뷰, 사내 프로젝트 맥락
- 토큰, 키, 비밀번호, 쿠키, private URL
- raw AI runtime state, local logs, IDE metadata, virtualenv
- 민감한 약점 서사

### 남겨도 되는 것

- 학습 목표
- 작성한 코드와 리뷰 포인트
- 검증 결과
- 다음 수정
- 공개 가능한 기술적 tradeoff

권장 표현:

```text
Needs more practice with dependency boundaries in small OOP examples.
```

피할 표현:

```text
I struggled because of <private/company/interview-specific context>.
```

검열 후에는 `git diff` 기준으로 실제 커밋될 내용만 다시 확인합니다.

## 5. drift 정리

Drift는 "계획과 실제가 다르다"는 사실 자체가 문제가 아니라, 기록 없이 누적되는 것이 문제입니다.

### Drift 유형

- `scope-drift`: 오늘 범위보다 커짐
- `sequence-drift`: 로드맵 순서와 달라짐
- `artifact-drift`: README, roadmap, backlog, notes가 서로 다름
- `quality-drift`: 검증/리뷰 없이 문서만 늘어남
- `privacy-drift`: 공개 저장소에 부적절한 맥락이 들어감

### 처리 방식

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

## 7. 검증

변경 종류에 맞게 최소 검증을 수행합니다.

| 변경 종류 | 최소 검증 |
|---|---|
| Python 코드 | `python3 -m py_compile` 또는 관련 테스트 |
| 문서만 변경 | 링크/경로/중복 참조 검색 |
| 학습 방향 변경 | `roadmap.md`, `backlog.md`, `session-log.md` 정합성 확인 |
| closeout / 리뷰 마무리 | 이번 학습에 사용한 파일 재읽기, 최신 코드 기준 검증 명령 재실행 |
| 공개 안전성 | 민감 후보 grep, `git diff`, `git status --short` |
| 삭제/정리 | 남은 참조 검색, 파일 목록 확인 |

검증하지 못한 항목은 `Not-tested:` 또는 세션 로그에 명시합니다.

## 8. commit + push

학습 마무리 시 commit + push는 기본 수행입니다. 사용자가 명시적으로 멈추라고 했거나, 검증 실패, 공개 안전 문제, remote/branch 불명확, destructive risk 같은 blocker가 있을 때만 보류합니다.

커밋 전 체크:

- `git status --short`로 staged/untracked 상태 확인
- `.omx/`, `.venv/`, `.idea/`, raw logs, secrets가 커밋 대상이 아닌지 확인
- `git diff --stat`와 핵심 diff 확인
- closeout 기록이 `mento/session-log.md` 또는 관련 문서에 남았는지 확인
- 테스트/검증 결과가 기록되었는지 확인
- commit/push를 보류한다면 blocker를 `mento/session-log.md`와 최종 응답에 남긴다.

커밋 메시지는 AGENTS.md의 Lore Commit Protocol을 따릅니다.

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

푸시는 아래 조건을 만족하면 진행합니다.

- 학습 마무리 또는 repo closeout 상태인 경우
- remote/branch가 의도한 대상임을 확인한 경우
- 공개 안전 검열과 검증이 통과한 경우

## 9. NexusV1 기록

작업 마무리 시에는 `nexus-vault` 스킬을 명시적으로 사용해 NexusV1 기록을 반드시 남깁니다.

NexusV1 기록은 상세한 중복 문서가 아니라 "오늘 이런 공부를 했다"는 가벼운 로깅이 기본 목적입니다. 이 공개 저장소의 독자가 접근하거나 재현해야 하는 필수 시스템이 아니므로, public repo 문서에는 NexusV1 내부 경로/개인 맥락을 요구사항처럼 남기지 않습니다.

자동화가 실제 NexusV1 기록 대상을 알아야 한다면 tracked 문서가 아니라 `nexus-vault` 스킬, ignored local runtime configuration, 또는 사용자별 agent memory에서 해석합니다.

기록 기준:

- 한 세션 또는 모듈이 `learning-complete` 상태
- 작업 마무리, 방향 전환, 운영 규칙 변경처럼 closeout이 발생함
- 코드/리뷰/검증/다음 수정이 정리됨
- 공개 안전 검열 통과

기록 내용:

- Daily Agent Activity에 요약 append
- 큰 학습 단위라면 Request 또는 Decision note 생성
- 공개 가능한 학습 증거만 기록
- private/company/account/interview/credential 맥락은 기록하지 않음

NexusV1에 기록하는 경우의 안전 규칙:

- `500_Sanctum/` 접근 금지
- 삭제 금지, 필요 시 archive 이동
- Obsidian CLI는 `path=`를 사용
- Daily는 오늘 날짜에만 append
- 한국어로 요약하되 파일명/태그/frontmatter는 영어 사용
- Obsidian CLI 사용 전 가능한 범위에서 target vault가 NexusV1인지 확인

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
