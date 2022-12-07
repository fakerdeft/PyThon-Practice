# requests //요청하기 위한 라이브러리
# BeautifulSoup //파싱(필요한 데이터 추출)하기 위한 라이브러리

import requests
from bs4 import BeautifulSoup

r=requests.get("https://www.naver.com")
bs=BeautifulSoup(r.content,"html.parser")


# h3=bs.select_one("h3>a")
# print(h3)

# h3=bs.select("h3")
# print(h3[0].text) # 해당 태그에서 텍스트
# print(h3[0].name) # 해당 태그의 이름
# print(h3[0].attrs) # 해당 태그의 속성

# selecter=bs.select_one("div.current_box")
# selecter=bs.select(".title")
# selecter=bs.select("#u_skip")
# selecter=bs.find_all("div",{"class":"partner_box"})
selecter=bs.find("div",{"class":"partner_box"})
print(selecter.text)