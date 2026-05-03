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
