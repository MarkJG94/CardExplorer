import httpx
from trolltrader import TrollTraderCards
from axionnow import AxionNow
from selectolax.parser import HTMLParser
from dataclasses import dataclass, asdict

@dataclass
class Card:
    cardname: str
    price: float
  
def get_html(page):
    website = AxionNow()
    search = input("Enter card name you wish to search: ")
    searchurl = website.url + search
    resp = httpx.get(searchurl)
    return HTMLParser(resp.text)

def parse_products(html):
    products = html.css("div.meta")
    results = []
    for item in products:
        new_item = Card(
        cardname = None,
        price = None
        )
        try:
            new_item.cardname = item.css_first("h4.name").text()
            new_item.price = item.css_first("span.price").text().strip()
        except:
            pass
        if (new_item.cardname is not None and new_item.price is not None):
            print(asdict(new_item))

def main():
    html = get_html(1)
    print(html.css_first("title").text())
    parse_products(html)
        
if __name__ == '__main__':
    main()

