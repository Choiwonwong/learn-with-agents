# Session Closeout Workflow

학습 준비, 방향 수정, drift 식별, 학습 종료, 또는 공개 가능한 변경 정리가 필요할 때 사용하는 종료 프로세스입니다.

목표는 "무엇을 했는지"를 정리하는 데서 끝나지 않습니다. 공개 안전성, 학습 방향 정합성, 검증 증거, 커밋/푸시 가능 상태, 필요 시 개인 지식 저장소 기록까지 한 흐름으로 닫습니다.

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

커밋/푸시는 `repo-closeout` 체크를 통과한 뒤에만 진행합니다.

## 2. 작업 내용 정리

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

## 3. 공개 안전 검열

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

## 4. drift 정리

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

## 5. 평가

학습 종료 또는 방향 수정 시에는 아래 질문으로 평가합니다.

- 오늘 작성한 코드가 있는가?
- 리뷰받은 코드 또는 리뷰 대상이 있는가?
- 실행/검증 증거가 있는가?
- 다음 수정 하나가 명확한가?
- 이번 변경이 현재 roadmap/backlog와 일치하는가?
- 불필요한 문서화가 코딩을 대체하지 않았는가?
- 공개 저장소에 안전한 내용만 남았는가?

평가 결과는 길게 쓰지 않습니다. `pass`, `partial`, `blocked` 중 하나와 근거만 남깁니다.

## 6. 검증

변경 종류에 맞게 최소 검증을 수행합니다.

| 변경 종류 | 최소 검증 |
|---|---|
| Python 코드 | `python3 -m py_compile` 또는 관련 테스트 |
| 문서만 변경 | 링크/경로/중복 참조 검색 |
| 학습 방향 변경 | `roadmap.md`, `backlog.md`, `session-log.md` 정합성 확인 |
| 공개 안전성 | 민감 후보 grep, `git diff`, `git status --short` |
| 삭제/정리 | 남은 참조 검색, 파일 목록 확인 |

검증하지 못한 항목은 `Not-tested:` 또는 세션 로그에 명시합니다.

## 7. commit + push 준비

커밋 전 체크:

- `git status --short`로 staged/untracked 상태 확인
- `.omx/`, `.venv/`, `.idea/`, raw logs, secrets가 커밋 대상이 아닌지 확인
- `git diff --stat`와 핵심 diff 확인
- closeout 기록이 `mento/session-log.md` 또는 관련 문서에 남았는지 확인
- 테스트/검증 결과가 기록되었는지 확인

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
Not-tested: Private knowledge-base recording because learning was not fully complete
```

푸시는 아래 조건을 만족할 때만 합니다.

- 사용자가 커밋/푸시까지 요청했거나, 세션 closeout의 명시된 종료 조건이 `commit + push`인 경우
- remote/branch가 의도한 대상임을 확인한 경우
- 공개 안전 검열과 검증이 통과한 경우

## 8. 개인 지식 저장소 기록

개인 지식 저장소 기록은 **학습이 완전히 끝났을 때** 수행합니다. 준비 완료, 방향 수정, drift 식별만으로는 기본적으로 기록하지 않습니다.

개인 지식 저장소는 이 학습자의 사적 환경입니다. 이 공개 저장소의 독자가 접근하거나 재현해야 하는 필수 시스템이 아니므로, public repo 문서에는 개인 저장소 내부 경로/개인 맥락을 요구사항처럼 남기지 않습니다.

자동화가 실제 개인 기록 대상을 알아야 한다면 tracked 문서가 아니라 ignored local runtime configuration 또는 사용자별 agent memory에서 해석합니다.

기록 기준:

- 한 세션 또는 모듈이 `learning-complete` 상태
- 코드/리뷰/검증/다음 수정이 정리됨
- 공개 안전 검열 통과
- 가능하면 관련 commit hash 또는 pushed branch가 있음

기록 내용:

- Daily Agent Activity에 요약 append
- 큰 학습 단위라면 Request 또는 Decision note 생성
- 공개 가능한 학습 증거만 기록
- private/company/account/interview/credential 맥락은 기록하지 않음

개인 지식 저장소에 기록하는 경우의 안전 규칙:

- `500_Sanctum/` 접근 금지
- 삭제 금지, 필요 시 archive 이동
- Obsidian CLI는 `path=`를 사용
- Daily는 오늘 날짜에만 append
- 한국어로 요약하되 파일명/태그/frontmatter는 영어 사용

## 9. 완료 선언 형식

최종 응답은 짧게 아래를 포함합니다.

```text
완료 상태: <guide-ready|direction-changed|drift-identified|learning-complete|repo-closeout>
정리: <핵심 변경>
검열: <통과/수정 내용>
Drift: <없음 또는 처리 결과>
평가: <pass|partial|blocked + 근거>
검증: <실행한 명령/결과>
Git: <not committed|committed|pushed + hash/branch>
Private record: <not needed|recorded|deferred + 이유>
다음 수정: <하나>
```
