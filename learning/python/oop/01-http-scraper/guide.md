# Python OOP 2시간 실습 가이드: 작은 HTTP 스크래퍼 만들기

목표: `quotes.toscrape.com`에서 quote, author, tag를 가져오는 아주 작은 스크래퍼를 만들며 Python OOP의 실무형 감각을 익힌다.

이 가이드는 완성 코드를 처음부터 복사하는 방식이 아니다. 각 단계에서 먼저 직접 타이핑하고, 막히면 아래의 검산 코드를 확인한다.

## 오늘의 성공 기준

2시간 뒤에 다음 질문에 답할 수 있으면 성공이다.

- 왜 데이터를 그냥 `dict`로 두지 않고 객체로 표현하는가?
- `class`와 `dataclass`의 역할 차이는 무엇인가?
- `Protocol` 또는 `ABC`는 언제 필요한가?
- 외부 HTTP/HTML 데이터처럼 믿을 수 없는 입력에는 왜 `pydantic` 같은 검증 도구가 유용한가?
- 스크래퍼를 `Fetcher`, `Parser`, `Scraper`, `Result` 역할로 나누면 무엇이 좋아지는가?

## 준비

권장 환경:

- Python 3.14+
- 가상환경 사용

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install requests parsel pydantic
```

이미 실습 파일이 준비되어 있다. 이 파일에 직접 작성한다.

```bash
learning/python/oop/01-http-scraper/practice/oop_scraper.py
```

## 120분 진행표

|      시간 | 목표                          | 산출물                       |
| --------: | ----------------------------- | ---------------------------- |
|    0-10분 | OOP를 스크래퍼 문제에 연결    | 역할 후보 4개 정리           |
|   10-25분 | 기본 class로 객체 모델 만들기 | `Quote` class                |
|   25-40분 | `dataclass`로 값 객체 정리    | `Quote` dataclass            |
|   40-60분 | 추상화 경계 만들기            | `Fetcher`, `Parser` Protocol |
|   60-80분 | HTTP 요청 객체 만들기         | `RequestsFetcher`            |
|  80-100분 | HTML 파서 객체 만들기         | `QuotesParser`               |
| 100-110분 | 조립 객체 만들기              | `QuoteScraper`               |
| 110-120분 | `pydantic` 비교와 회고        | 도구 선택 기준               |

## 1단계: OOP를 문제에 붙이기

스크래퍼를 함수 하나로도 만들 수 있다. 하지만 OOP를 연습하려면 "무엇이 책임을 갖는가"를 먼저 나눠야 한다.

이번 프로젝트의 역할은 4개다.

| 역할           | 책임                                       |
| -------------- | ------------------------------------------ |
| `Quote`        | 가져온 quote 하나를 표현하는 값 객체       |
| `Fetcher`      | URL에서 HTML 문자열을 가져오는 역할        |
| `Parser`       | HTML 문자열에서 `Quote` 목록을 뽑는 역할   |
| `QuoteScraper` | fetcher와 parser를 조립해 전체 흐름을 실행 |

핵심은 상속부터 떠올리지 않는 것이다. 먼저 책임을 작게 나누고, 객체끼리 협력하게 만든다. Python OOP에서는 상속보다 composition을 먼저 고려하는 편이 보통 더 단순하다.

### 실습 1

`oop_scraper.py`에 아래 주석을 직접 쓰고, 각 역할이 어떤 메서드를 가져야 할지 한 줄씩 적어보자.

```python
# Quote: 데이터를 조회, 수정하는 메소드
# Fetcher: HTTP 응답을 요청한다.
# Parser: HTTP 응답을 Quote에 맞게 추출한다.
# QuoteScraper: HTTP 요청, 응답 추출, Quote 데이터 생성을 진행한다.
```

#### 보완 답변

```python
# Quote : quote 하나의 text, author, tag를 가진 값 객체이며, short로 짧은 표현을 한다.
# Fetcher : URL을 받아 HTML 문자열을 가져온다. fetch(url) -> str
# Parser : HTML 문자열을 Quote 목록으로 변환한다. parse(str) -> list[Quote]
# QuoteScraper : Fetcher과 Parser를 조합해서 scrape(url) -> list[Quote] 흐름을 실행한다.
```

## 2단계: 기본 class로 값 객체 만들기

먼저 `dataclass` 없이 평범한 class로 시작한다. 그래야 `dataclass`가 무엇을 줄여주는지 보인다.

직접 작성:

```python
class Quote:
    def __init__(self, text: str, author: str, tags: list[str]) -> None:
        self.text = text
        self.author = author
        self.tags = tags

    def short(self) -> str:
        return f"{self.text} - {self.author}"
```

아래 코드를 맨 아래에 붙여 실행해보자.

```python
if __name__ == "__main__":
    quote = Quote("Life is short.", "Someone", ["life", "short"])
    print(quote.short())
```

생각할 점:

- `__init__`은 객체가 어떤 데이터를 가져야 하는지 정한다.
- `self`는 현재 객체 자신이다.
- `short()`는 quote와 관련된 행동이므로 `Quote` 안에 두는 것이 자연스럽다.

하지만 단점도 있다.

- 값만 담는 객체인데 작성량이 많다.
- `repr`, 비교, 불변성 같은 기본 기능을 직접 챙겨야 한다.
- `tags`가 외부에서 바뀔 수 있다.

## 3단계: `dataclass`로 값 객체 정리하기

`dataclass`는 "데이터를 담는 클래스"를 간결하게 만든다. 특히 스크래핑 결과처럼 구조가 있는 값을 표현할 때 좋다.

방금 만든 `Quote` class를 지우고 아래처럼 바꿔보자.

```python
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Quote:
    text: str
    author: str
    tags: tuple[str, ...]

    def short(self) -> str:
        return f"{self.text} - {self.author}"
```

검산:

```python
if __name__ == "__main__":
    quote = Quote("Life is short.", "Someone", ("life", "short"))
    print(quote)
    print(quote.short())
```

여기서 선택한 옵션:

- `frozen=True`: 만든 뒤 값을 바꾸지 못하게 한다.
- `slots=True`: 객체가 가질 속성을 고정해 메모리 사용과 오타 실수를 줄인다.
- `tuple[str, ...]`: tag 목록도 불변에 가깝게 다룬다.

### 실습 2

아래 코드를 실행해보고 에러가 왜 나는지 설명해보자.

```python
quote = Quote("A", "B", ("x",))
quote.author = "C"
```

답: `frozen=True`인 dataclass는 생성 후 필드 재할당을 막는다. 스크래핑 결과는 "이미 관측된 값"이므로 불변으로 다루는 편이 안전하다.

## 4단계: `Protocol`로 역할의 모양 정하기

이제 Fetcher와 Parser의 "모양"을 정한다. 중요한 점은 아직 구현하지 않는다는 것이다. 먼저 이 프로젝트에서 필요한 경계를 선언한다.

```python
from typing import Protocol


class Fetcher(Protocol):
    def fetch(self, url: str) -> str:
        ...


class Parser(Protocol):
    def parse(self, html: str) -> list[Quote]:
        ...
```

`Protocol`은 "이 메서드를 가진 객체라면 이 역할로 쓸 수 있다"는 구조적 타입이다. 즉, 꼭 `Fetcher`를 상속하지 않아도 `fetch(url) -> str` 메서드가 있으면 Fetcher처럼 다룰 수 있다.

비교:

```python
class MyFetcher:
    def fetch(self, url: str) -> str:
        return "<html></html>"
```

`MyFetcher`는 `Fetcher`를 상속하지 않았지만, 모양이 맞기 때문에 타입 관점에서는 Fetcher 역할을 할 수 있다.

### `ABC`는 언제 쓰나?

`abc.ABC`와 `@abstractmethod`는 런타임에서 "반드시 구현해야 한다"는 상속 기반 계약을 강제하고 싶을 때 쓴다.

```python
from abc import ABC, abstractmethod


class BaseFetcher(ABC):
    @abstractmethod
    def fetch(self, url: str) -> str:
        raise NotImplementedError
```

이번 작은 프로젝트에서는 `Protocol`이 더 가볍다. 라이브러리나 프레임워크처럼 상속 계층을 강제해야 한다면 `ABC`를 고려한다.

## 5단계: HTTP 요청 객체 만들기

이제 실제 HTTP 요청을 담당하는 객체를 만든다.

파일 상단 import를 정리한다.

```python
from dataclasses import dataclass
from typing import Protocol

import requests
```

그 다음 `RequestsFetcher`를 작성한다.

```python
@dataclass(frozen=True, slots=True)
class RequestsFetcher:
    timeout: float = 5.0
    user_agent: str = "oop-study-scraper/1.0"

    def fetch(self, url: str) -> str:
        response = requests.get(
            url,
            timeout=self.timeout,
            headers={"User-Agent": self.user_agent},
        )
        response.raise_for_status()
        return response.text
```

여기서 OOP 포인트:

- `timeout`, `user_agent`는 fetcher의 설정이다.
- HTTP 요청 세부 사항은 `RequestsFetcher` 안으로 숨긴다.
- 다른 코드에서는 `fetch(url)`만 알면 된다.

### 실습 3

아래 코드를 실행해 HTML 앞부분이 출력되는지 확인한다.

```python
if __name__ == "__main__":
    fetcher = RequestsFetcher()
    html = fetcher.fetch("https://quotes.toscrape.com/")
    print(html[:200])
```

## 6단계: HTML 파서 객체 만들기

`parsel`로 HTML에서 quote 데이터를 뽑는다. `parsel`은 Scrapy 생태계에서 쓰는 selector 라이브러리이며, HTML/XML 문서에서 CSS selector와 XPath를 둘 다 사용할 수 있다.

표준 라이브러리의 `html.parser`도 사용할 수는 있다. 하지만 `HTMLParser`를 상속하고 `handle_starttag`, `handle_data` 같은 이벤트 메서드를 직접 관리해야 해서, 이번 목표인 "HTML 구조에서 데이터를 선택해 값 객체로 바꾸기"에는 `parsel`이 더 좋은 학습 재료다.

import를 추가한다.

```python
from parsel import Selector
```

파서 구현:

```python
class QuotesParser:
    def parse(self, html: str) -> list[Quote]:
        selector = Selector(text=html)
        quotes: list[Quote] = []

        for item in selector.css(".quote"):
            text = item.css(".text::text").get()
            author = item.css(".author::text").get()

            if text is None or author is None:
                continue

            quote = Quote(
                text=text.strip(),
                author=author.strip(),
                tags=tuple(tag.strip() for tag in item.css(".tags .tag::text").getall()),
            )
            quotes.append(quote)

        return quotes
```

여기서 selector 포인트:

- `Selector(text=html)`: HTML 문자열을 선택 가능한 문서 객체로 감싼다.
- `.css(".quote")`: quote 블록들을 고른다.
- `.css(".text::text").get()`: 첫 번째 텍스트 결과 하나를 가져온다. 없으면 `None`이다.
- `.css(".tags .tag::text").getall()`: 매칭된 텍스트 결과 전체를 `list[str]`로 가져온다.
- `.strip()`: HTML에서 가져온 앞뒤 공백을 값 객체에 넣기 전에 제거한다.

여기서 OOP 포인트:

- HTML 구조를 아는 코드는 `QuotesParser` 안에만 둔다.
- `RequestsFetcher`는 `.quote` CSS selector를 모른다.
- `QuoteScraper`는 나중에 fetch와 parse를 조립만 한다.

### 실습 4

아래 코드를 실행한다.

```python
if __name__ == "__main__":
    fetcher = RequestsFetcher()
    parser = QuotesParser()

    html = fetcher.fetch("https://quotes.toscrape.com/")
    quotes = parser.parse(html)

    for quote in quotes[:3]:
        print(quote.short())
        print("tags:", quote.tags)
```

## 7단계: 조립 객체 만들기

이제 전체 흐름을 담당하는 객체를 만든다.

```python
@dataclass(frozen=True, slots=True)
class QuoteScraper:
    fetcher: Fetcher
    parser: Parser

    def scrape(self, url: str) -> list[Quote]:
        html = self.fetcher.fetch(url)
        return self.parser.parse(html)
```

이 객체의 책임은 아주 작다.

1. fetcher로 HTML을 가져온다.
2. parser로 Quote 목록을 만든다.
3. 결과를 반환한다.

이 구조가 좋은 이유:

- HTTP 요청 구현을 바꿔도 `QuoteScraper`는 그대로 둔다.
- HTML 파싱 방식을 바꿔도 `QuoteScraper`는 그대로 둔다.
- 테스트할 때 가짜 fetcher를 넣을 수 있다.

### 실습 5: 가짜 Fetcher로 테스트 감각 익히기

진짜 네트워크 없이도 scraper를 확인할 수 있다.

```python
class FakeFetcher:
    def fetch(self, url: str) -> str:
        return """
        <html>
          <div class="quote">
            <span class="text">"Test quote"</span>
            <small class="author">Tester</small>
            <div class="tags">
              <a class="tag">unit</a>
              <a class="tag">oop</a>
            </div>
          </div>
        </html>
        """
```

실행:

```python
if __name__ == "__main__":
    scraper = QuoteScraper(fetcher=FakeFetcher(), parser=QuotesParser())
    quotes = scraper.scrape("unused-url")
    print(quotes)
```

핵심: `FakeFetcher`는 `Fetcher`를 상속하지 않았지만 `fetch()` 메서드가 있으므로 조립 가능하다. 이것이 `Protocol`이 주는 실용적인 유연성이다.

## 8단계: 최종 실행 코드

맨 아래 실행부를 하나만 남긴다.

```python
if __name__ == "__main__":
    scraper = QuoteScraper(
        fetcher=RequestsFetcher(timeout=5.0),
        parser=QuotesParser(),
    )
    quotes = scraper.scrape("https://quotes.toscrape.com/")

    for index, quote in enumerate(quotes[:5], start=1):
        print(f"{index}. {quote.short()}")
        print(f"   tags: {', '.join(quote.tags)}")
```

## 9단계: `pydantic`은 어디에 쓰나?

`dataclass`는 Python 내부에서 다루는 값 객체에 좋다. 하지만 외부 입력이 믿을 수 없고, 타입 변환/검증/직렬화가 중요하면 `pydantic`이 더 적합할 수 있다.

예를 들어, HTML에서 뽑은 데이터가 비어 있으면 막고 싶다고 하자.

```python
from pydantic import BaseModel, Field


class QuoteModel(BaseModel):
    text: str = Field(min_length=1)
    author: str = Field(min_length=1)
    tags: tuple[str, ...] = ()
```

사용:

```python
model = QuoteModel(
    text="A quote",
    author="Author",
    tags=("life", "truth"),
)
print(model.model_dump())
```

실패 확인:

```python
QuoteModel(text="", author="", tags=("x",))
```

### `dataclass` vs `pydantic`

| 기준               | `dataclass`     | `pydantic`                   |
| ------------------ | --------------- | ---------------------------- |
| 주 용도            | 내부 값 객체    | 외부 입력 검증, 파싱, 직렬화 |
| 런타임 검증        | 거의 직접 구현  | 강함                         |
| 작성량             | 적음            | 적음                         |
| 의존성             | 표준 라이브러리 | 외부 라이브러리              |
| 이번 프로젝트 추천 | 기본 결과 객체  | 옵션: HTML/JSON 경계 검증    |

이번 2시간 학습에서는 최종 `Quote`는 `dataclass`로 유지하고, `pydantic`은 "외부 데이터 경계에서 검증이 필요할 때 쓰는 도구"로 이해하면 충분하다.

## 최종 파일 예시

막히면 아래 코드와 비교하되, 먼저 직접 작성한 코드가 왜 다른지 확인하자.

```python
from dataclasses import dataclass
from typing import Protocol

import requests
from parsel import Selector


@dataclass(frozen=True, slots=True)
class Quote:
    text: str
    author: str
    tags: tuple[str, ...]

    def short(self) -> str:
        return f"{self.text} - {self.author}"


class Fetcher(Protocol):
    def fetch(self, url: str) -> str:
        ...


class Parser(Protocol):
    def parse(self, html: str) -> list[Quote]:
        ...


@dataclass(frozen=True, slots=True)
class RequestsFetcher:
    timeout: float = 5.0
    user_agent: str = "oop-study-scraper/1.0"

    def fetch(self, url: str) -> str:
        response = requests.get(
            url,
            timeout=self.timeout,
            headers={"User-Agent": self.user_agent},
        )
        response.raise_for_status()
        return response.text


class QuotesParser:
    def parse(self, html: str) -> list[Quote]:
        selector = Selector(text=html)
        quotes: list[Quote] = []

        for item in selector.css(".quote"):
            text = item.css(".text::text").get()
            author = item.css(".author::text").get()

            if text is None or author is None:
                continue

            quote = Quote(
                text=text.strip(),
                author=author.strip(),
                tags=tuple(tag.strip() for tag in item.css(".tags .tag::text").getall()),
            )
            quotes.append(quote)

        return quotes


@dataclass(frozen=True, slots=True)
class QuoteScraper:
    fetcher: Fetcher
    parser: Parser

    def scrape(self, url: str) -> list[Quote]:
        html = self.fetcher.fetch(url)
        return self.parser.parse(html)


if __name__ == "__main__":
    scraper = QuoteScraper(
        fetcher=RequestsFetcher(timeout=5.0),
        parser=QuotesParser(),
    )
    quotes = scraper.scrape("https://quotes.toscrape.com/")

    for index, quote in enumerate(quotes[:5], start=1):
        print(f"{index}. {quote.short()}")
        print(f"   tags: {', '.join(quote.tags)}")
```

## 개념 정리

### Encapsulation

HTTP 요청 세부 사항은 `RequestsFetcher` 안에 숨긴다. HTML selector 세부 사항은 `QuotesParser` 안에 숨긴다.

### Abstraction

`Fetcher`와 `Parser`는 구체 구현이 아니라 필요한 메서드의 모양만 말한다.

### Polymorphism

`RequestsFetcher`와 `FakeFetcher`는 서로 다른 객체지만 둘 다 `fetch(url) -> str`를 제공하므로 `QuoteScraper` 입장에서는 교체 가능하다.

### Composition

`QuoteScraper`는 fetcher와 parser를 상속하지 않는다. 두 객체를 받아서 조립한다.

### Inheritance

이번 프로젝트에서는 상속이 거의 필요 없다. 상속은 "is-a" 관계와 공통 구현이 뚜렷할 때만 선택한다.

## 자기 점검 질문

1. `Quote`를 왜 `dict` 대신 객체로 만들었는가?
2. `Quote`가 `frozen=True`이면 어떤 장점과 불편함이 있는가?
3. `QuoteScraper`가 직접 `requests.get()`을 호출하지 않는 이유는 무엇인가?
4. `Protocol`과 `ABC`의 차이를 한 문장으로 설명하면?
5. `pydantic`을 이 프로젝트에 반드시 넣지 않아도 되는 이유는?
6. 그래도 `pydantic`이 유용해지는 순간은 언제인가?
7. `parsel`에서 `.get()`과 `.getall()`은 각각 언제 쓰는가?
8. 표준 `html.parser`가 이번 selector 중심 실습에는 덜 적합한 이유는?

## 다음 확장 과제

시간이 남으면 하나만 고른다.

- 페이지 2까지 가져오도록 URL을 조립한다.
- author별 quote 개수를 집계한다.
- tag 하나를 입력받아 해당 tag의 quote만 출력한다.
- `QuoteModel`을 도입해 빈 문자열을 검증한다.
- `FakeFetcher`를 이용해 `assert len(quotes) == 1` 같은 간단한 검산 코드를 추가한다.

## 참고 자료

- Python `dataclasses`: https://docs.python.org/3/library/dataclasses.html
- Python `abc`: https://docs.python.org/3/library/abc.html
- Python typing `Protocol`: https://typing.python.org/en/latest/reference/protocols.html
- Requests documentation: https://requests.readthedocs.io/
- Parsel documentation: https://parsel.readthedocs.io/
- Python `html.parser`: https://docs.python.org/3/library/html.parser.html
- Pydantic models: https://docs.pydantic.dev/latest/concepts/models/
