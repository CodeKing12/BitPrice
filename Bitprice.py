import requests
from bs4 import BeautifulSoup

btc_link = requests.get("https://www.coindesk.com/price/bitcoin")
parsed_link = BeautifulSoup(btc_link.text, "html.parser")
completely_parsed = parsed_link.prettify()
#print(completely_parsed)
price = parsed_link.find("div", {"class":"price val-negative"})
print(price.text)

