# 웹페이지에 들어가지 않고
# 뉴스 검색, 기사 제목, 링크, 본문, 게시날짜를 엑셀에 담아서 출력

import requests
from bs4 import BeautifulSoup
import pandas as pd # 데이터 테이블(표)형식으로 관리
# 웹페이지 들어가지 않고 검색

keyword=input("검색하고자 하는 키워드를 입력해주세요:")

r=requests.get("https://news.google.com/search?q="+keyword+"&hl=ko&gl=KR&ceid=KR%3Ako")
bs=BeautifulSoup(r.text,"html.parser")

# 기사제목, 링크
# titles=bs.select("div.xrnccd > article > h3 > a")
titles=bs.find_all("div",{"class":"xrnccd"})

news=[]

for i in titles:
    title=i.find("h3").text
    links="https://news.google.com"+i.find("a")["href"][1:]
    # date=i.find("time").text

    news.append([title, links])
    google_news_df=pd.DataFrame(news,columns=["기사제목","링크주소"])

google_news_df.to_excel("뉴스크롤링 결과_v2.xlsx")
print("저장성공!!!")


# for i in titles:
#     title=i.text
#     links="https://news.google.com"+i.get("href")[1:]

#     news.append([title,links])
#     google_news_df=pd.DataFrame(news,columns=["기사제목","링크주소"])

# print(google_news_df)
# google_news_df.to_excel("뉴스크롤링 결과.xlsx")
# print("저장성공!!!")