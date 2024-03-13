#web1.py
# 웹크롤링을 위한 선언
from bs4 import BeautifulSoup
#페이지를 로딩
page = open("test01.html", "rt", encoding="utf-8").read()

soup = BeautifulSoup(page, "html.parser")
#print(soup.prettify())
#print(soup.find_all("a"))
#print(soup.find("p"))
print(soup.find(id="first"))

for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n","")
    print(title)
#조건이 있는 경우 <p class='outer-text'> 컨텐츠 </p>
#print(soup.find_all("p", class_="outer-text"))
#attrs
#print(soup.find_all("p", attrs={"class"="outer-text"}))
#print(soup.find_all("p", attrs={"class":"outer-text"}))