import requests
from bs4 import BeautifulSoup

r=requests.get("https://search.naver.com/search.naver?sm=tab_sug.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EC%98%A4%EB%8A%98%EC%9D%98+%EB%82%A0%EC%94%A8&oquery=%EC%98%A4%EB%8A%98%EC%9D%98%EB%82%A0%EC%94%A8&tqi=hWQJLlp0J14ssB%2BTkNRssssstNG-453951&acq=%EC%98%A4%EB%8A%98%EC%9D%98%EB%82%A0%EC%94%A8&acr=1&qdt=0")
bs=BeautifulSoup(r.content,"html.parser")

weather=  bs.select_one("div.temperature_info>dl.summary_list>dd.desc")

print("오늘의 체감온도는:{}도 입니다.".format(weather.text))