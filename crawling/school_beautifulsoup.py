from bs4 import BeautifulSoup
from bs4.element import Tag
import requests

webpage = requests.get("https://sadang.sen.ms.kr")
soup = BeautifulSoup(webpage.content, "html.parser")
a = soup.find(attrs={'class':'main_small_list'})
for i in a:
    if type(i) is Tag:
        print(i.find(attrs={'class' : 'ellipsis'}).get_text())
        print(i.find(attrs={'class' : 'date'}).get_text())
# for i in a:
#     print(i.find_all(attr={'class' : "ellipsis"}))
#     print(i.select('.ellipsis')[0].get_text())