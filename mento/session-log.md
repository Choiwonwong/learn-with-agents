# Session Log

의미 있는 학습 세션마다 최신 항목을 위에 추가합니다.

## 2026-06-09 - SOP Session B Site Isolation Closeout

- 목표: Same-Origin Policy Session B에서 renderer process, Site Isolation, SiteInstance/process model을 SOP와 같은 계층으로 혼동하지 않도록 정리한다.
- 작성한 코드/문서:
  - `learning/fundamentals/networking/01-same-origin-policy/notes.md`
  - `mento/backlog.md`
- 리뷰받은 코드:
  - 코드 변경은 없음. Session A의 SOP/CORS 설명과 Session B의 Site Isolation 설명을 개념 경계 기준으로 리뷰했다.
- 주요 피드백:
  - SOP는 정상적인 JavaScript/Web API 접근에서 cross-origin 응답, DOM, storage를 읽을 수 있는지 정하는 웹 플랫폼 접근 제어다.
  - Site Isolation은 renderer compromise를 가정하고 cross-site 민감 데이터가 공격자 renderer process에 섞이지 않도록 하는 브라우저 내부 프로세스 격리 전략이다.
  - 같은 URL을 여러 탭에서 열었을 때 탭별 별도 renderer process가 생길 수 있으며, 이는 Site Isolation과 모순되지 않는다. `site = process`가 아니라 process 배치는 SiteInstance, browsing relationship, process reuse, 안정성, 성능, process limit의 영향을 받는다.
- 공개 안전 / 검열:
  - 기록은 공개 가능한 브라우저 보안 학습 내용과 로컬 관찰만 포함한다. 개인, 회사, 계정, credential, private URL 맥락은 추가하지 않았다.
- Drift:
  - 상태: accept
  - 내용: 코드 작성 대신 이론 중심 Session B closeout으로 진행했다. 해당 모듈은 theory-first 보조 경로이고 `notes.md`의 빈 섹션을 닫는 것이 목표였으므로 수용한다.
- 평가:
  - 상태: pass
  - 근거: `notes.md`의 Renderer Process / Site Isolation 섹션을 완성했고, backlog의 완료 항목을 제거했으며, 다음 실험 범위를 preflight와 SameSite로 분리했다.
- 다음 수정:
  - `practice/sop_lab.py`에서 preflight가 필요한 CORS 요청을 추가하고 브라우저 Network 탭에서 `OPTIONS` 요청을 관찰한다.
- 검증:
  - `rg`로 Session B 빈칸 제거, 완료 체크, 다음 수정 정합성을 확인한다.
  - `git diff --check`, `git diff --stat`, `git status --short`로 문서 변경 범위와 whitespace 상태를 확인한다.

## 2026-05-04 - Mentor Routing SRP Refactor

- 목표: Codex CLI가 안정적으로 읽는 `AGENTS.md`는 얇은 bootstrap으로 유지하고, 멘토 요청 라우팅과 closeout 위험 gate를 책임별 문서로 분리한다.
- 작성한 코드/문서:
  - `AGENTS.md`
  - `README.md`
  - `mento/README.md`
  - `mento/mentor-routing.md`
  - `mento/workflows/session-closeout.md`
  - `mento/workflows/closeout/public-safety.md`
  - `mento/workflows/closeout/verification.md`
  - `mento/workflows/closeout/git-publish.md`
  - `mento/workflows/closeout/nexus-record.md`
  - `mento/workflows/README.md`
  - `mento/workflows/study-session.md`
  - `mento/prompts/default-mentor-prompt.md`
  - `mento/rubrics/growth-checklist.md`
- 리뷰받은 코드:
  - 코드 변경은 없음. 멘토 운영 문서의 SRP와 라우팅 구조를 리뷰했다.
- 주요 피드백:
  - `AGENTS.md`는 Codex CLI bootstrap으로 두고 상세 절차를 반복하지 않는다.
  - `mento/mentor-routing.md`가 요청 유형별 read target과 workflow를 고르는 canonical routing surface가 된다.
  - `session-closeout.md`는 종료 순서와 필수 gate를 조율하고, public safety / verification / git publish / NexusV1 record 세부 규칙은 `mento/workflows/closeout/`가 담당한다.
- 공개 안전 / 검열:
  - 변경 내용은 공개 가능한 멘토 운영 구조와 학습 workflow 문서만 포함한다.
  - NexusV1은 멘토 closeout gate로 유지하되, public repo 독자의 재현 요구사항처럼 설명하지 않는다.
- Drift:
  - 상태: accept
  - 내용: Python OOP 구현 세션이 아니라 멘토 운영 구조 개선으로 진행했다. 사용자가 명시적으로 현재 mento workflow/context 구조 개선을 요청했으므로 수용한다.
- 평가:
  - 상태: pass
  - 근거: 라우팅, workflow, closeout gate, checklist 문서의 canonical owner가 더 분명해졌다.
- 다음 수정:
  - 다음 실제 학습 세션에서 `mento/mentor-routing.md`를 시작점으로 사용하고 closeout gate가 누락 없이 실행되는지 확인한다.
- 검증:
  - `rg`로 routing/closeout/NexusV1/git/verification 참조 위치를 확인한다.
  - `find mento/workflows/closeout -maxdepth 1 -type f`로 gate 문서 4개 생성을 확인한다.
  - `git diff --stat`, `git diff`, `git status --short`로 변경 범위와 `.omx/` 제외 상태를 확인한다.

## 2026-05-04 - Mento Closeout Guardrails Updated

- 목표: 학습 마무리 시 stale context로 인한 drift를 막고, NexusV1 로깅을 필수 closeout 절차로 명시한다.
- 작성한 코드/문서:
  - `AGENTS.md`
  - `mento/README.md`
  - `mento/workflows/session-closeout.md`
  - `mento/workflows/study-session.md`
  - `mento/workflows/README.md`
  - `mento/rubrics/growth-checklist.md`
- 리뷰받은 코드:
  - 코드 변경은 없음. 멘토 운영 규칙과 closeout 절차를 리뷰했다.
- 주요 피드백:
  - closeout 전에는 이번 학습에서 사용한 파일을 최신 디스크 상태로 다시 읽어야 한다.
  - 사용자가 이미 코드를 수정한 경우 이전 대화가 아니라 현재 파일을 기준으로 최종 피드백과 기록을 갱신한다.
  - 작업 마무리 시에는 `nexus-vault` 스킬을 명시적으로 사용해 NexusV1 Daily/Request에 가벼운 학습 로그를 반드시 남긴다.
- 공개 안전 / 검열:
  - 변경 내용은 공개 가능한 멘토 운영 규칙만 포함한다. NexusV1은 사적 환경으로 취급하되 공개 repo의 필수 의존성처럼 설명하지 않는다.
- Drift:
  - 상태: correct
  - 내용: 이전 closeout에서 최신 파일 재읽기와 NexusV1 필수 기록이 누락되었다. 운영 규칙에 두 절차를 명시해 재발을 줄인다.
- 평가:
  - 상태: pass
  - 근거: 관련 mentor/workflow/checklist 문서에 같은 기준을 반영했다.
- 다음 수정:
  - 다음 학습 closeout에서 최신 파일 재읽기와 NexusV1 필수 기록이 실제로 수행되는지 확인한다.
- 검증:
  - 문서 참조 검색으로 closeout, NexusV1, 최신 파일 재읽기 규칙의 반영 위치를 확인한다.

### 2026-05-04 Correction

- 내용: 선택적으로 읽히던 NexusV1 문구를 `작업 마무리 시 NexusV1 기록을 반드시 남긴다`로 강화했다.
- 내용: 학습 마무리의 기본 종료 조건을 `검증 + 공개 안전 검열 + commit + push + NexusV1 기록`으로 명시했다.
- 근거: 사용자가 학습 마무리라고 말한 경우 repo-local 기록에서 멈추지 않고 현재 study-lab 변경을 commit/push까지 진행해야 한다.

### 2026-05-04 Commit Splitting Guidance

- 내용: 커밋 단위는 파일 종류가 아니라 의사결정/되돌림 경계 기준으로 나누도록 명시했다.
- 내용: 같은 학습 단계의 code, 검증, guide, notes, session-log는 함께 커밋할 수 있지만, 운영 규칙 변경, dependency/version policy, unrelated cleanup은 별도 커밋을 우선하도록 정리했다.
- 근거: 학습 기록과 운영 규칙이 함께 커지면 미래 리뷰와 되돌림이 어려워지므로 commit history 자체도 학습 증거로 관리한다.

## 2026-05-04 - Python OOP Scraper V2 Responsibility Review

- 목표: HTTP scraper V2에서 pagination, quote count, tag lookup을 추가하며 `QuoteScraper`와 결과 컬렉션의 책임 경계를 검토한다.
- 작성한 코드/문서:
  - `learning/python/oop/01-http-scraper/practice/oop_scraper_v2.py`
  - `learning/python/oop/01-http-scraper/notes.md`
  - `pyproject.toml`
  - `uv.lock`
- 리뷰받은 코드:
  - `QuoteModel`, `Fetcher`/`Parser` ABC, `RequestsFetcher`, `QuotesParser`, `QuoteScraper`, `QuoteCollection`, `FakeFetcher`
- 주요 피드백:
  - `QuoteScraper`가 fetch와 parse 조립 및 간단한 pagination을 맡는 것은 V2 기준에서 허용 가능하다.
  - quote 개수 집계와 tag lookup을 `QuoteCollection`으로 분리한 판단은 OOP 책임 분리 관점에서 적절하다.
  - `tuple[QuoteModel, ...]`는 여러 quote를 담는 불변 컬렉션 타입으로 맞고, `tuple[QuoteModel]`은 quote 1개짜리 tuple 의미라 부적절하다.
  - Python 3.14+로 프로젝트 버전 약속을 맞추면 `typing.override` 사용은 괜찮다.
  - `get_counts()`를 `count()`, `get_quote_by_tag()`를 `find_by_tag()`로 정리해 컬렉션 API 이름이 더 Pythonic해졌다.
- 공개 안전 / 검열:
  - 기록은 공개 가능한 Python OOP 학습 내용, 코드 리뷰 포인트, 검증 결과만 포함한다.
- Drift:
  - 상태: accept
  - 내용: 원래 V1 scraper 실습에서 V2 확장 과제로 이동했다. 현재 roadmap의 변화 압력 적용 단계와 맞으므로 수용한다.
- 평가:
  - 상태: pass
  - 근거: V2 코드가 문법 검사를 통과했고, `FakeFetcher` 기반 검산으로 2페이지 수집, tuple 저장, count, tag lookup 동작을 확인했다.
- 다음 수정:
  - 다음 세션에서 `QuoteScraper` 안의 `url.format(page_idx=...)`를 그대로 둘지, URL 생성 책임을 작은 객체나 함수로 분리할지 판단한다.
- 검증:
  - `uv run python -m py_compile learning/python/oop/01-http-scraper/practice/oop_scraper_v2.py`
  - `FakeFetcher + QuotesParser + QuoteScraper(page_count=2)`로 quote count `2`, `"oop"` tag lookup 성공, missing tag `None` 반환 확인

## 2026-05-03 - Python OOP Parser Direction Updated

- 목표: HTTP scraper 실습의 HTML parser 학습 방향을 Beautiful Soup 중심에서 `parsel` selector 중심으로 바꾼다.
- 작성한 코드/문서:
  - `learning/python/oop/01-http-scraper/guide.md`
  - `learning/python/oop/01-http-scraper/reference/oop_scraper.py`
  - `learning/python/oop/01-http-scraper/requirements.txt`
  - `pyproject.toml`
  - `uv.lock`
- 리뷰받은 코드:
  - `QuotesParser` reference 구현을 `parsel.Selector`, `.css()`, `.get()`, `.getall()` 흐름으로 검산했다.
- 주요 피드백:
  - 표준 `html.parser`는 콜백 기반이라 selector 중심 scraping 학습에는 덜 적합하다.
  - `parsel`은 CSS selector와 XPath를 함께 다룰 수 있어 parser 역할 경계와 selector 사고를 배우기에 더 직접적이다.
  - 실습 파일의 깨진 `from bs4` import는 `from parsel import Selector`로 맞췄지만, `QuotesParser` 구현은 학습자가 직접 채우는 상태로 남겼다.
- 공개 안전 / 검열:
  - 변경 내용은 공개 가능한 Python OOP/parser 학습 자료만 포함한다.
- 평가:
  - 상태: pass
  - 근거: `uv lock`, Python 문법 검사, fixture HTML 기반 `QuotesParser` 검산을 통과했다.
- 다음 수정:
  - `practice/oop_scraper.py`에서 `QuotesParser.parse()`를 `parsel` selector로 직접 구현한다.
- 검증:
  - `uv run python -m py_compile learning/python/oop/01-http-scraper/practice/oop_scraper.py learning/python/oop/01-http-scraper/reference/oop_scraper.py learning/python/oop/01-http-scraper/practice/abc_protocol_demo.py`
  - fixture HTML로 `QuotesParser().parse()` 결과가 quote 1개, author `Tester`, tags `("unit", "oop")`인지 확인

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

## 2026-06-07 - Same-Origin Policy Topic Intake

- 목표: Same-Origin Policy를 이론과 코드 관찰이 함께 있는 fundamentals networking 모듈로 학습할 수 있게 준비한다.
- 작성한 코드/문서:
  - `learning/fundamentals/networking/01-same-origin-policy/README.md`
  - `learning/fundamentals/networking/01-same-origin-policy/guide.md`
  - `learning/fundamentals/networking/01-same-origin-policy/practice/sop_lab.py`
  - `learning/fundamentals/networking/01-same-origin-policy/notes.md`
  - `learning/fundamentals/networking/01-same-origin-policy/reference/README.md`
  - `learning/fundamentals/README.md`
  - `mento/roadmap.md`
  - `mento/backlog.md`
- 리뷰받은 코드:
  - 아직 없음. 다음 세션에서 `practice/sop_lab.py`를 실행하고 관찰 결과를 리뷰한다.
- 주요 피드백:
  - SOP는 브라우저 JavaScript의 cross-origin 응답 읽기 제한으로 학습해야 하며, 서버 간 통신 규칙이나 인증/인가 대체물로 설명하면 안 된다.
  - CORS, CSRF, XSS, SameSite Cookie를 한꺼번에 섞지 말고 책임 경계를 분리한다.
- 다음 수정:
  - `practice/sop_lab.py`를 실행해 same-origin, cross-origin without CORS, cross-origin with CORS 결과를 `notes.md`에 기록한다.
- 검증:
  - `practice/sop_lab.py` 문법 검사를 통과했다.

## 2026-06-07 - SOP Final Study Plan with Renderer Process Layer

- 목표: Same-Origin Policy 학습 계획을 SOP/CORS 논리 경계에서 renderer process와 Site Isolation 구현 관점까지 확장한다.
- 작성한 코드/문서:
  - `learning/fundamentals/networking/01-same-origin-policy/learning-plan.md`
  - `learning/fundamentals/networking/01-same-origin-policy/README.md`
  - `learning/fundamentals/networking/01-same-origin-policy/notes.md`
- 리뷰받은 코드:
  - 코드 구현은 변경하지 않았다. `practice/sop_lab.py`는 관찰 도구로 유지했다.
- 주요 피드백:
  - SOP는 웹 플랫폼 접근 규칙이고, Site Isolation은 renderer compromise를 고려한 브라우저 내부 격리 전략으로 분리해 학습한다.
  - origin 기준 접근 제어와 site 기준 process isolation을 같은 개념으로 합치지 않는다.
  - Chrome Task Manager, `chrome://process-internals`, iframe 실험은 정답 판정이 아니라 레이어 구분 관찰 도구로 둔다.
- 다음 수정:
  - 실제 학습 세션에서 `notes.md`의 위협 모델, CORS 관찰 결과, renderer process / Site Isolation 설명을 채운다.
- 검증:
  - `practice/sop_lab.py` 문법 검사와 `git diff --check`를 통과했다.

## 2026-06-07 - Study Planning and Learning PR Boundary Rule

- 목표: 학습 플래닝 PR과 실제 학습 PR을 분리하는 hard rule을 학습 레포 운영 절차에 반영한다.
- 작성한 코드/문서:
  - `AGENTS.md`
  - `mento/workflows/session-closeout.md`
  - `mento/workflows/closeout/git-publish.md`
- 리뷰받은 코드:
  - 코드 변경은 없음. 운영 규칙 변경만 수행했다.
- 주요 피드백:
  - 학습 계획, 커리큘럼, workflow, module scaffold, `learning-plan.md`는 planning PR에 담는다.
  - 실제 학습 중 채운 notes, practice code, 관찰 결과, 리뷰 피드백, 다음 수정은 별도 learning PR에 담는다.
  - 실제 학습 과정에서 학습 문서를 수정하는 것은 허용하되, 세션 증거와 다음 수정 기록 목적이어야 한다.
- 다음 수정:
  - Same-Origin Policy 실제 학습은 planning PR과 분리된 새 learning PR에서 `notes.md`를 채우며 진행한다.
- 검증:
  - 운영 규칙 문서 diff와 PR boundary 문구 검색을 확인한다.

## 2026-06-07 - Same-Origin Policy Session A

- 목표: SOP/CORS를 “요청 차단”이 아니라 브라우저의 cross-origin 응답/객체 읽기 제한으로 이해한다.
- 작성한 코드/문서:
  - `learning/fundamentals/networking/01-same-origin-policy/notes.md`
  - `mento/backlog.md`
- 리뷰받은 코드:
  - 코드 구현 변경은 없음. `practice/sop_lab.py`를 실행해 브라우저 관찰 도구로 사용했다.
- 주요 피드백:
  - origin은 `scheme + host + port`의 엄격한 튜플 비교다. port, scheme, subdomain이 다르면 cross-origin이다.
  - SOP는 cross-origin 요청/로드를 모두 막는 정책이 아니라 현재 origin의 JavaScript가 다른 origin 응답/객체를 읽는 것을 제한하는 브라우저 보안 정책이다.
  - CORS는 Cross-Origin Resource Sharing이며, 받는 서버/API 서버가 응답 헤더로 특정 origin에 응답 읽기를 허용하는 정책이다.
  - form submit은 나갈 수 있으므로 SOP만으로 CSRF를 막을 수 없다. XSS는 공격자 코드가 피해 origin 내부에서 실행되는 별도 문제다.
- 공개 안전 / 검열:
  - 예시는 `example.*`, `localhost`만 사용했고 개인/회사/계정/credential/private URL 맥락을 추가하지 않았다.
- Drift:
  - 상태: accept
  - 내용: 학습 중 renderer process 배치가 SOP origin 판정과 1:1 대응하지 않는다는 nuance를 학습 플랜에 정정했다. 실제 학습 이해를 바로잡는 문서 수정이므로 learning PR에 포함한다.
- 평가:
  - 상태: pass
  - 근거: 위협 모델, origin 판정, SOP/CORS 경계, 로컬 관찰 결과, 다음 수정(Session B)이 남았다.
- 다음 수정:
  - Session B에서 renderer process, SiteInstance, Site Isolation을 SOP와 다른 계층으로 분리해 학습한다.
- 검증:
  - `practice/sop_lab.py` 로컬 실행으로 same-origin / no-cors / with-cors 결과를 관찰했다.
  - Session closeout에서 Python 문법 검사와 `git diff --check`를 수행한다.
