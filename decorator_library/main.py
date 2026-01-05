import httpx
from decorators import retry

URL = "https://www.scrapethissite.com/pages/"


@retry
def scrape(url: str):
    r = httpx.get(url)


def main():
    print(f"Scraping: {URL}")
    scrape(URL)


if __name__ == "__main__":
    main()
