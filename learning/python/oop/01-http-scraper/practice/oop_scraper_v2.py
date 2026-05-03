"""Hands-on practice file for the OOP HTTP scraper lesson.

Follow `guide.md` and fill this file step by step.
Use `reference/oop_scraper.py` only when you need to compare your work.
"""

## dataclass로 값 객체 정리하기
from dataclasses import dataclass
from typing import override

from pydantic import BaseModel

class QuoteModel(BaseModel):
    text: str
    author: str
    tags: tuple[str, ...]
    page_idx: int

    def short(self) -> str:
        return f"{self.text} - {self.author}"


# Step 2. Define Fetcher and Parser
from abc import ABC, abstractmethod


class Fetcher(ABC):
    @abstractmethod
    def fetch(self, url: str) -> str:
        pass


class Parser(ABC):
    @abstractmethod
    def parse(self, html: str, page_idx: int) -> list[QuoteModel]:
        pass


# Step 3. Implement RequestsFetcher.
import requests


@dataclass(frozen=True, slots=True)
class RequestsFetcher(Fetcher):
    timeout: float = 5.0
    user_agent: str = "oop-study-scraper/1.0"

    @override
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


class QuotesParser(Parser):
    @override
    def parse(self, html: str, page_idx: int) -> list[QuoteModel]:
        selector = Selector(text=html)
        quotes: list[QuoteModel] = []

        for item in selector.css(".quote"):
            text = item.css(".text::text").get()
            author = item.css(".author::text").get()

            if text is None or author is None:
                continue

            q = QuoteModel(
                text=text.strip(),
                author=author.strip(),
                tags=tuple(tag.strip() for tag in item.css(".tags .tag::text").getall()),
                page_idx=page_idx,
            )
            quotes.append(q)

        return quotes

# Step 5. Compose everything with QuoteScraper.

@dataclass(frozen=True, slots=True)
class QuoteScraper:
    fetcher: Fetcher
    parser: Parser

    def scrape(self, url: str, page_count: int = 1) -> QuoteCollection:
        quotes: list[QuoteModel] = []
        for page_idx in range(1, page_count + 1, 1):
            html = self.fetcher.fetch(url.format(page_idx=page_idx))
            result = self.parser.parse(html, page_idx)
            quotes.extend(result)
        return QuoteCollection(tuple(quotes))

@dataclass(frozen=True, slots=True)
class QuoteCollection:
    quotes: tuple[QuoteModel, ...]

    def count(self) -> int:
        return len(self.quotes)

    def find_by_tag(self, tag: str) -> QuoteModel | None:
        for q in self.quotes:
            if tag in q.tags:
                return q
        return None

class FakeFetcher(Fetcher):
    @override
    def fetch(self, url: str) -> str: # noqa
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

if __name__ == "__main__":
    scraper = QuoteScraper(
        fetcher=RequestsFetcher(timeout=5.0),
        parser=QuotesParser(),
    )
    # quoteCollection = scraper.scrape("https://quotes.toscrape.com/page/{page_idx}/")
    quote_collection = scraper.scrape("https://quotes.toscrape.com/page/{page_idx}/", page_count=2)


    for index, quote in enumerate(quote_collection.quotes, start=1):
        print(f"{index}. {quote.short()}")
        print(f"   tags: {', '.join(quote.tags)}")

    print(f"quotes count : {quote_collection.count()}")

    search_tag = "simile"
    print(f"{search_tag} tag quote : {quote_collection.find_by_tag(search_tag)}")
