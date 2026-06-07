# Roadmap

목표: 언어와 주제를 넘나들며 소프트웨어 엔지니어링을 실무적 사고와 함께 익힌다.

## 현재 초점

- Python OOP 기본기
- 작은 HTTP 스크래퍼
- `dataclass`, `Protocol`/`ABC`, `pydantic`의 선택 기준
- 코드 리뷰를 통한 책임 분리 훈련

현재 모듈:

- `learning/python/oop/01-http-scraper/`

## Python OOP 진행 계획

1. 값 객체 만들기
   - `Quote`를 직접 구현한다.
   - plain class와 `dataclass(frozen=True, slots=True)`의 차이를 설명한다.
2. 역할 경계 나누기
   - `Fetcher`, `Parser`, `QuoteScraper` 책임을 분리한다.
   - 상속보다 composition을 먼저 선택하는 이유를 설명한다.
3. 테스트 가능한 설계 만들기
   - `FakeFetcher` 또는 fixture HTML로 네트워크 없는 검산을 추가한다.
   - Protocol 기반 대체 가능성을 확인한다.
4. 실패 정책 정리
   - timeout, HTTP error, HTML 구조 변경을 어디에서 처리할지 결정한다.
   - 예외를 삼키는 코드와 드러내는 코드의 tradeoff를 비교한다.
5. 변화 압력 적용
   - pagination, tag filtering, parser strategy 중 하나를 추가한다.
   - 변경이 어느 객체에 집중되는지 리뷰한다.

다음 코딩 목표:

- `learning/python/oop/01-http-scraper/practice/oop_scraper.py`에 `Quote` 값 객체와 `short()` 메서드를 먼저 구현한다.

## 트랙 후보

- Python: OOP, typing, testing, packaging, async, web/backend
- Java: OOP, collections, streams, concurrency, Spring basics
- Go: structs/interfaces, errors, goroutines, HTTP, testing
- Design Patterns: pattern as response to change pressure
- Fundamentals: data structures, algorithms, networking, debugging, tests

## 다음 후보

- Fundamentals networking: Same-Origin Policy 로컬 브라우저 실습 (`learning/fundamentals/networking/01-same-origin-policy/`)
1. Python OOP scraper 1차 구현: `Quote`, `Fetcher`, `Parser`, `QuoteScraper`
2. Python testing: fake fetcher와 fixture HTML로 네트워크 없는 검산
3. Python error handling: 예외 설계와 retry 기준
4. Python typing: `Protocol`, generic, narrowing
5. Design Patterns: Strategy를 scraper parser 선택 문제로 학습

## 원칙

- 한 번에 하나의 작은 기능을 만든다.
- 기능을 만든 뒤 리뷰한다.
- 리뷰에서 나온 다음 수정 하나를 바로 실행한다.
