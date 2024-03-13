
import urllib.request
from bs4 import BeautifulSoup
Goods = "24000829"
url = "hhttps://tickets.interpark.com/goods/"
page = urllib.request.urlopen(url).read()

soup = BeautifulSoup(page, "html.parser")
f = open("dangn.txt","wt",encoding="utf-8")
posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
    titleElem = post.find("h2", attrs={"class":"card-title"})
    priceElem = post.find("div", attrs={"class":"card-price"})
    addrElem = post.find("div", attrs={"class":"card-region-name"})
    title = titleElem.text.replace("\n","").strip()
    price = priceElem.text.replace("\n","").strip()
    addr = addrElem.text.replace("\n","").strip()
    print(f"{title}, {price},{addr}")
    f.write(f"{title}, {price},{addr}\n")

f.close()