# Session Log

의미 있는 학습 세션마다 최신 항목을 위에 추가합니다.

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
