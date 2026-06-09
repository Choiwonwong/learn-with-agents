# Learning Backlog

## Ready

- Same-Origin Policy Session C: `practice/sop_lab.py`에서 preflight가 필요한 CORS 요청을 추가하고 브라우저 Network 탭에서 `OPTIONS` 요청을 관찰한다.
- `learning/python/oop/01-http-scraper/practice/oop_scraper.py`에 `Quote` 값 객체와 `short()` 메서드를 직접 구현한다.
- `Fetcher`, `Parser` Protocol을 추가하고 각 역할의 책임을 주석으로 설명한다.
- `RequestsFetcher`, `QuotesParser`, `QuoteScraper`를 최소 동작 버전으로 연결한다.
- 구현 후 `learning/python/oop/01-http-scraper/reference/oop_scraper.py`와 책임 경계를 비교한다.
- `mento/rubrics/code-review-rubric.md` 기준으로 리뷰한다.

## Later

- `FakeFetcher`로 네트워크 없는 검산 추가
- fixture HTML 기반 parser 검산 추가
- timeout / HTTP error 처리 기준 정리
- pagination 지원
- tag filter 기능
- parser Strategy 적용 여부 검토
- `pydantic` 검증 모델 적용
- `pytest` 도입
- Java 첫 모듈 설계
- Go 첫 모듈 설계
- Design Patterns 첫 모듈 설계
