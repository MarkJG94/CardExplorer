import httpx
from websites import *
from selectolax.parser import HTMLParser
from dataclasses import dataclass, asdict
from urllib.parse import quote

@dataclass
class Card:
    cardname: str
    price: float


def get_html(card, store, page):
    search = card.replace(" ", store.whitespace)
    searchurl = store.url + search
    resp = httpx.get(searchurl)
    return HTMLParser(resp.text)

def load_stores_as_array():
    stores = []
    stores.append(TrollTraderCards())
    stores.append(AxionNow())
    stores.append(MagicMadhouse())
    return stores

def parse_products(card, store, html):
    products = html.css(store.productsCSS)
    for item in products:
        new_item = Card(
        cardname = None,
        price = None
        )
        try:
            new_item.cardname = item.css_first(store.cardnameCSS).text()
            new_item.price = item.css_first(store.priceCSS).text().strip()
        except:
            pass
        if (new_item.cardname is not None and new_item.price is not None):
            if new_item.cardname in card:
                print(asdict(new_item))

def main():
    stores = load_stores_as_array()
    initsearch = input("Enter card name you wish to search: ")
    CARD_TO_SEARCH = initsearch
    for store in stores:
        html = get_html(CARD_TO_SEARCH, store, 1)
        print(html.css_first("title").text())
        parse_products(CARD_TO_SEARCH, store, html)
    
        
if __name__ == '__main__':
    main()
