"""Small runtime demo for ABC vs Protocol.

Run from the project root:

    python learning/python/oop/01-http-scraper/practice/abc_protocol_demo.py
"""

from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable


class AbstractFetcher(ABC):
    @abstractmethod
    def fetch(self, url: str) -> str:
        """Return HTML for the given URL."""
        raise NotImplementedError


class MissingFetchMethod(AbstractFetcher):
    pass


class RequestsFetcher(AbstractFetcher):
    def fetch(self, url: str) -> str:
        return f"<html>real response from {url}</html>"


class FetcherProtocol(Protocol):
    def fetch(self, url: str) -> str:
        """Return HTML for the given URL."""
        ...


class FakeFetcher:
    def fetch(self, url: str) -> str:
        return f"<html>fake response for {url}</html>"


class WrongShapeFetcher:
    def download(self, url: str) -> str:
        return f"<html>downloaded {url}</html>"


@runtime_checkable
class RuntimeCheckableFetcher(Protocol):
    def fetch(self, url: str) -> str:
        ...


def scrape_with_abc(fetcher: AbstractFetcher, url: str) -> None:
    html = fetcher.fetch(url)
    print(f"ABC consumer received: {html}")


def scrape_with_protocol(fetcher: FetcherProtocol, url: str) -> None:
    html = fetcher.fetch(url)
    print(f"Protocol consumer received: {html}")


def show_abc_runtime_check() -> None:
    print("\n1. ABC + @abstractmethod")

    try:
        MissingFetchMethod()
    except TypeError as error:
        print("MissingFetchMethod() failed at runtime:")
        print(f"  {error}")

    fetcher = RequestsFetcher()
    print("RequestsFetcher() succeeded.")
    scrape_with_abc(fetcher, "https://example.com")


def show_protocol_runtime_behavior() -> None:
    print("\n2. Protocol")

    fake_fetcher = FakeFetcher()
    scrape_with_protocol(fake_fetcher, "https://example.com")
    print("FakeFetcher did not inherit FetcherProtocol, but it has fetch().")

    wrong_fetcher = WrongShapeFetcher()
    print("WrongShapeFetcher can still be instantiated.")

    try:
        scrape_with_protocol(wrong_fetcher, "https://example.com")  # type: ignore[arg-type]
    except AttributeError as error:
        print("Calling through the Protocol-shaped function failed at runtime:")
        print(f"  {error}")


def show_runtime_checkable_protocol_limit() -> None:
    print("\n3. @runtime_checkable Protocol")

    print(
        "isinstance(FakeFetcher(), RuntimeCheckableFetcher):",
        isinstance(FakeFetcher(), RuntimeCheckableFetcher),
    )
    print(
        "isinstance(WrongShapeFetcher(), RuntimeCheckableFetcher):",
        isinstance(WrongShapeFetcher(), RuntimeCheckableFetcher),
    )
    print("This checks attribute presence at runtime, not full type signatures.")


if __name__ == "__main__":
    show_abc_runtime_check()
    show_protocol_runtime_behavior()
    show_runtime_checkable_protocol_limit()
