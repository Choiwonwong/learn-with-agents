# OOP Track

Python 객체지향을 실습 중심으로 공부하는 트랙입니다.

## 현재 모듈

| 순서 | 모듈 | 목표 |
|---:|---|---|
| 01 | [HTTP Scraper](01-http-scraper/) | OOP 기본 개념을 작은 스크래퍼로 연결 |

## 학습 순서

1. `01-http-scraper/guide.md`를 따라 2시간 실습을 진행한다.
2. `01-http-scraper/practice/oop_scraper.py`에 직접 구현한다.
3. `reference/oop_scraper.py`와 구조를 비교한다.
4. `notes.md`에 `dataclass`, `Protocol`, `pydantic` 선택 기준을 정리한다.

## OOP Python 학습 계획

목표는 문법 암기가 아니라 "객체가 어떤 책임을 가져야 하는가"를 코드로 판단하는 감각을 만드는 것입니다.

### 1단계: 값 객체와 책임 분리

- 실습 파일: `01-http-scraper/practice/oop_scraper.py`
- 구현 대상: `Quote`, `Fetcher`, `Parser`, `QuoteScraper`
- 핵심 질문:
  - `Quote`를 `dict`가 아니라 객체로 두면 무엇이 좋아지는가?
  - `Fetcher`, `Parser`, `Scraper`를 나누면 테스트와 변경이 어떻게 쉬워지는가?
- 성공 기준:
  - `reference/oop_scraper.py`를 보지 않고 최소 동작 버전을 작성한다.
  - 작성 후 reference와 책임 경계를 비교한다.

### 2단계: 테스트 가능한 경계 만들기

- 추가 대상: `FakeFetcher` 또는 고정 HTML fixture
- 핵심 질문:
  - 네트워크 없이 parser와 scraper를 검산할 수 있는가?
  - Protocol을 쓰면 테스트 대역을 어떻게 끼워 넣을 수 있는가?
- 성공 기준:
  - 외부 사이트 접속 없이 quote 파싱 결과를 확인한다.
  - 실패 케이스를 최소 1개 검산한다.

### 3단계: 예외와 실패 정책

- 추가 대상: timeout, HTTP error, HTML 구조 변경 대응
- 핵심 질문:
  - 어디에서 예외를 잡고, 어디에서는 그대로 올려야 하는가?
  - "재시도"는 fetcher 책임인가, scraper 책임인가?
- 성공 기준:
  - 실패 정책을 코드와 `notes.md`에 함께 남긴다.

### 4단계: 타입과 검증 도구 선택

- 비교 대상: plain class, `dataclass`, `Protocol`/`ABC`, `pydantic`
- 핵심 질문:
  - 타입 힌트와 런타임 검증은 각각 어떤 문제를 해결하는가?
  - 이 작은 스크래퍼에서 `pydantic`은 필요한가, 과한가?
- 성공 기준:
  - `notes.md`에 도구 선택 기준을 예시와 함께 정리한다.

### 5단계: 변화 압력으로 디자인 패턴 연결

- 확장 후보: pagination, tag filtering, parser strategy
- 핵심 질문:
  - 기능 추가가 들어올 때 어느 객체가 바뀌어야 하는가?
  - Strategy 패턴이 실제로 단순하게 만드는 지점은 어디인가?
- 성공 기준:
  - 기능 하나를 추가하고, 변경된 책임을 리뷰한다.

## 현재 재검토 결과

- Active curriculum은 `01-http-scraper/` 하나로 유지한다.
- 오래된 OOP 메모는 현재 실습 흐름을 방해하므로 삭제했다.
- 다음 세션의 첫 코딩 목표는 `practice/oop_scraper.py`에서 `Quote` 값 객체와 `short()` 메서드를 직접 구현하는 것이다.
