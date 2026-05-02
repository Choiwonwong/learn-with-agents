from dataclasses import dataclass
from typing import Protocol

import requests
from bs4 import BeautifulSoup


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
        soup = BeautifulSoup(html, "html.parser")
        quotes: list[Quote] = []

        for item in soup.select(".quote"):
            text_node = item.select_one(".text")
            author_node = item.select_one(".author")
            tag_nodes = item.select(".tags .tag")

            if text_node is None or author_node is None:
                continue

            quote = Quote(
                text=text_node.get_text(strip=True),
                author=author_node.get_text(strip=True),
                tags=tuple(tag.get_text(strip=True) for tag in tag_nodes),
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
