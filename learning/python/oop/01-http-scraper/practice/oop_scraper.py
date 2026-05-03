"""Hands-on practice file for the OOP HTTP scraper lesson.

Follow `guide.md` and fill this file step by step.
Use `reference/oop_scraper.py` only when you need to compare your work.
"""

# Step 1. Define a Quote value object.
# class Quote:
#     text: str
#     author: str | None
#     tag: list[str]

#     def __init__(
#         self,
#         text: str,
#         author: str | None,
#         tag: list[str]
#     ) -> None:
#         self.text = text
#         self.author = author if author else "unknown"
#         self.tag = tag

#     def short(self) -> str:
#         tag_str = str(self.tag) if self.tag else "no tag"
#         return f"Text: {self.text}\nAuthor: {self.author}\nTag: {tag_str}"


# class Quote:
#     text: str
#     author: str
#     tags: list[str]

#     def __init__(self, text: str, author: str, tags: list[str]) -> None:
#         self.text = text
#         self.author = author
#         self.tags = tags

#     def short(self) -> str:
#         return f"{self.text} - {self.author}"

## dataclass로 값 객체 정리하기
from dataclasses import dataclass


@dataclass(frozen=True)
class Quote:
    text: str
    author: str
    # tags: list[str]
    tags: tuple[str, ...]  # why?

    def short(self) -> str:
        return f"{self.text} - {self.author}"


# Step 2. Define Fetcher and Parser protocols.
from typing import Protocol


class Fetcher(Protocol):
    def fetch(self, url: str) -> str: ...


class Parser(Protocol):
    def parse(self, html: str) -> list[Quote]: ...


# Step 3. Implement RequestsFetcher.
import requests


@dataclass(frozen=True, slots=True)
class RequestsFetcher:
    timeout: float = 5.0
    user_agent: str = "oop-study-scraper/1.0"

    def fetch(self, url: str) -> str:
        response = requests.get(
            url,
            timeout=self.timeout,
            headers={"User-Agent": self.user_agent}
        )
        response.raise_for_status()
        return response.text


# Step 4. Implement QuotesParser.
from parsel import Selector


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

# Step 5. Compose everything with QuoteScraper.

@dataclass(frozen=True, slots=True)
class QuoteScraper:
    fetcher: Fetcher
    parser: Parser

    def scrape(self, url: str) -> list[Quote]:
        html = self.fetcher.fetch(url)
        return self.parser.parse(html)

# FakeFetcher
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

# if __name__ == "__main__":
#     # Build and run your scraper here.
#     pass

# if __name__ == "__main__":
#     quote = Quote("Life is short.", "Someone", ("life", "short"))
#     print(quote)
#     print(quote.short())

# quote = Quote("A", "B", ("x",))
# quote.author = "C" # frozen 관련 에러

# if __name__ == "__main__":
#     fetcher = RequestsFetcher()
#     html = fetcher.fetch("https://quotes.toscrape.com/")
#     print(html[:200])

# if __name__ == "__main__":
#     fetcher = RequestsFetcher()
#     parser = QuotesParser()
#
#     html = fetcher.fetch("https://quotes.toscrape.com/")
#     quotes = parser.parse(html)
#
#     for quote in quotes[:3]:
#         print(quote.short())
#         print("tags:", quote.tags)

# if __name__ == "__main__":
#     scraper = QuoteScraper(fetcher=FakeFetcher(), parser=QuotesParser())
#     quotes = scraper.scrape("unused-url")
#     print(quotes)

if __name__ == "__main__":
    scraper = QuoteScraper(
        fetcher=RequestsFetcher(timeout=5.0),
        parser=QuotesParser(),
    )
    quotes = scraper.scrape("https://quotes.toscrape.com/")

    for index, quote in enumerate(quotes[:5], start=1):
        print(f"{index}. {quote.short()}")
        print(f"   tags: {', '.join(quote.tags)}")