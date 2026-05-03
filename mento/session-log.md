# Session Log

의미 있는 학습 세션마다 최신 항목을 위에 추가합니다.

## 2026-05-03 - Go First CLI Guide Ready

- 목표: GoLand로 Go 기본 실행 흐름을 1시간 동안 맛볼 수 있는 첫 Go 모듈을 준비한다.
- 작성한 코드/문서:
  - `learning/go/README.md`
  - `learning/go/basics/01-first-cli/README.md`
  - `learning/go/basics/01-first-cli/guide.md`
  - `learning/go/basics/01-first-cli/notes.md`
  - `learning/go/basics/01-first-cli/practice/`
  - `learning/go/basics/01-first-cli/reference/`
- 리뷰받은 코드:
  - 아직 없음. 다음 학습 세션에서 `practice/` 코드를 직접 실행하고 수정하며 리뷰한다.
- 주요 피드백:
  - 이번 목표는 실무 Go가 아니라 module, package, main, struct, method, test, debug 흐름을 관찰하는 것이다.
  - GoLand는 학습 보조 도구로 사용하되 `go run .`과 `go test ./...` CLI 흐름도 같이 확인한다.
- 공개 안전 / 검열:
  - 새 자료는 공개 가능한 언어 학습 내용만 담고 있으며 개인, 회사, 계정, credential, private URL 맥락을 추가하지 않았다.
- Drift:
  - 상태: accept
  - 내용: 현재 roadmap의 즉시 초점은 Python OOP지만, Go 맛보기 모듈 준비로 잠시 이동했다. Go는 트랙 후보에 이미 있으므로 첫 모듈 준비를 수용한다.
- 평가:
  - 상태: partial
  - 근거: 학습 자료와 예제 코드는 준비되었지만, Go SDK가 shell에서 아직 확인되지 않아 실행 검증은 다음 세션으로 남았다.
- 다음 수정:
  - GoLand에서 `learning/go/basics/01-first-cli/practice`를 열고 `go run .`, `go test ./...`를 실행한 뒤 `notes.md`를 채운다.
- 검증:
  - 파일 구조와 경로를 확인한다.

## 2026-05-02 - Learning Closeout Workflow Review

- 목표: 학습 준비 완료, 방향 수정, drift 식별, 학습 종료, 검열, 평가, commit/push, 개인 지식 저장소 기록으로 이어지는 종료 프로세스를 명확히 한다.
- 작성한 코드/문서:
  - `mento/workflows/session-closeout.md`
  - `mento/workflows/README.md`
  - `mento/workflows/study-session.md`
  - `mento/workflows/learning-start.md`
  - `mento/templates/session-note.md`
  - `mento/rubrics/growth-checklist.md`
  - `mento/README.md`
  - `README.md`
  - `AGENTS.md`
- 리뷰받은 코드:
  - 코드 변경은 없음. 운영 workflow 문서 정합성을 리뷰했다.
- 주요 피드백:
  - 기존 문서는 세션 시작/진행/리뷰는 있었지만 종료 이후의 공개 안전 검열, drift 처리, 평가, commit/push, 개인 지식 저장소 기록이 단일 경로로 연결되어 있지 않았다.
  - 개인 지식 저장소 기록은 모든 중간 상태가 아니라 학습이 완전히 끝난 경우에만 수행하도록 분리했다.
  - 개인 지식 저장소는 공개 저장소의 필수 의존성이나 재현 조건처럼 보이지 않게 일반화해서 표현한다.
  - 실제 개인 기록 대상 해석은 tracked 문서가 아니라 ignored local runtime configuration 또는 사용자별 agent memory에서 처리한다.
- 공개 안전 / 검열:
  - 새 문서는 공개 학습 운영 절차만 담고 있으며 개인, 회사, 계정, credential, private URL 맥락을 추가하지 않았다.
- Drift:
  - 상태: accepted
  - 내용: OOP 구현으로 바로 돌아가기 전에 학습 종료/공개 정리 프로세스 정비로 이동했다. 공개 lab 운영 기준을 먼저 고정하는 것이 이후 세션 품질에 필요하므로 수용한다.
- 평가:
  - 상태: pass
  - 근거: closeout workflow가 시작, 진행, 리뷰 문서와 연결되었고 개인 지식 저장소 기록 조건이 분리되었다.
- 다음 수정:
  - 다음 OOP Python 세션 종료 시 `session-closeout.md` 형식으로 실제 closeout을 한 번 수행한다.
- 검증:
  - closeout workflow 참조와 기존 문서의 연결을 확인한다.
- Git / personal record:
  - Git: 본 closeout 문서 변경과 함께 커밋 대상.
  - Personal record: 학습 완료 상태가 아니므로 기록하지 않음.

## 2026-05-02 - Python OOP Curriculum Cleanup

- 목표: 현재 OOP Python 학습 흐름에서 오래된 자료를 제거하고 active curriculum을 HTTP scraper 중심으로 재정리한다.
- 작성한 코드/문서:
  - `learning/python/oop/README.md`
  - `mento/roadmap.md`
  - `mento/backlog.md`
  - `README.md`
  - `AGENTS.md`
- 리뷰받은 코드:
  - `learning/python/oop/01-http-scraper/practice/oop_scraper.py`는 아직 scaffold 상태라 다음 세션에서 직접 구현이 필요하다.
- 주요 피드백:
  - 오래된 자료가 00번 모듈처럼 보이면 현재 학습 순서를 흐리므로 active curriculum에서 제거한다.
  - 다음 학습은 `Quote` 값 객체부터 시작해 책임 분리, 테스트 가능한 경계, 실패 정책, 변화 압력 순서로 진행한다.
- 다음 수정:
  - `practice/oop_scraper.py`에 `Quote` 값 객체와 `short()` 메서드를 직접 구현한다.
- 검증:
  - 오래된 자료 참조 제거 여부와 Python 문법 검사를 수행한다.

## 2026-05-02 - Public Learning Lab Positioning

- 목표: GitHub public 공개를 전제로 이 저장소를 AI-guided learning lab으로 명확히 포지셔닝한다.
- 작성한 코드/문서:
  - `README.md`
  - `AGENTS.md`
  - `mento/README.md`
  - `.gitignore`
  - `pyproject.toml`
  - `uv.lock`
- 리뷰받은 코드:
  - 공개 위험 키워드 스캔으로 정책 문구 외 민감 정보 노출 후보를 확인했다.
- 주요 피드백:
  - 이 저장소는 완성 포트폴리오가 아니라 공개 가능한 학습 실험실로 운영한다.
  - AI mentor/agent 기반 학습임을 명시하되, 개인적인 기록은 최소화한다.
- 다음 수정:
  - Git 저장소 초기화 전에 `.omx/`, `.idea`, `.venv`가 커밋 대상에서 제외되는지 확인한다.
- 검증:
  - `python3 -m py_compile`로 Python 실습/참조 파일 문법 확인 통과
  - `UV_CACHE_DIR=/tmp/uv-cache uv lock`로 lockfile 재생성 통과

## 2026-05-02 - Learning Workflow Restructure

- 목표: 이 공간을 Python뿐 아니라 Java, Go, design pattern, fundamentals까지 다루는 범용 학습 워크스페이스로 재설계
- 작성한 코드/문서:
  - `README.md`
  - `AGENTS.md`
  - `learning/python/oop/`
  - `learning/java/`
  - `learning/go/`
  - `learning/design-patterns/`
  - `learning/fundamentals/`
  - `mento/workflows/`
- 리뷰받은 코드:
  - `python -m py_compile learning/python/oop/01-http-scraper/reference/oop_scraper.py learning/python/oop/01-http-scraper/practice/oop_scraper.py`
- 주요 피드백:
  - `learning/`은 자료 보관소가 아니라 실제 실습 공간이어야 한다.
  - `practice/`가 내가 직접 작성하는 곳이고 `reference/`는 비교용이다.
  - 학습 시작은 `Learning Start Workflow`로 트리거된다.
- 다음 수정:
  - 다음 학습 세션에서 `learning/python/oop/01-http-scraper/practice/oop_scraper.py`를 직접 구현하고 코드 리뷰를 받는다.
- 검증:
  - 새 Python 실습/참조 파일 문법 확인 통과

## 2026-05-02 - Mentor Operating Structure

- 목표: Codex를 장기 학습 멘토로 쓰기 위한 프로젝트 규칙과 `mento/` 구조 만들기
- 작성한 코드/문서:
  - `AGENTS.md`
  - `README.md`
  - `mento/`
- 리뷰받은 코드:
  - 아직 없음. 이번 세션은 멘토링 운영 구조 정리 세션.
- 다음 수정:
  - OOP scraper 실습을 진행한 뒤, 작성한 `learning/python/oop/01-http-scraper/practice/oop_scraper.py`를 이 루브릭으로 리뷰한다.

## Template

- 목표:
- 작성한 코드:
- 리뷰받은 코드:
- 주요 피드백:
- 다음 수정:
- 검증:
