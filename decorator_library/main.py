import httpx

from decorators import retry

URL = "https://www.scrapethissite.com/pages/"


class Scraper:
    def __init__(self, url: str):
        self.url: str = url
        self.content: str = ""

    def __repr__(self):
        return f"Scrapper for: {self.url}"

    def __len__(self):
        return len(self.content)

    def __getitem__(self, position):
        return self.content[position]


@retry
def scrape(url: str):
    r = httpx.get(url)


def main():
    print(f"Scraping: {URL}")
    scrape(URL)


if __name__ == "__main__":
    main()
