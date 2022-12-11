class TrollTraderCards:
    def __init__(self):
        self.url = "https://www.trolltradercards.com/products/search?q="
        self.whitespace = "+"
        self.productsCSS = "div.meta"
        self.cardnameCSS = "h4.name"
        self.priceCSS = "span.price"

class AxionNow:
    def __init__(self):
        self.url = "https://www.axionnow.com/products/search?q="
        self.whitespace = "+"
        self.productsCSS = "div.meta"
        self.cardnameCSS = "h4.name"
        self.priceCSS = "span.price"

class MagicMadhouse:
    def __init__(self):
        self.url = "https://magicmadhouse.co.uk/search.php?search_query="
        self.whitespace = "%20"
        self.productsCSS = "#kuLandingProductsListUl"
        self.cardnameCSS = "#kuLandingProductsListUl > li:nth-child(1) > div.kuNameDesc > div.kuName > a"
        self.priceCSS = "#kuLandingProductsListUl > li:nth-child(1) > div.kuPrice > div"