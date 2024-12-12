# 웹 스크랩핑 ㅡ 정적

from bs4 import BeautifulSoup

# html_str = """
# <html>
#     <body>
#         <div id="content">
#             <ul class="industry">
#                 <li>인공지능</li>
#                 <li>빅데이터</li>
#                 <li>신재생에너지</li>
#             </ul>
#             <ul class="comlang">
#                 <li>Python</li>
#                 <li>C++</li>
#                 <li>Javascript</li>
#             </ul>
#         </div>
#     </body>
# </html>
# """

# soup = BeautifulSoup(html_str, 'html.parser')
# # # print(soup)

# # # 파싱여부 확인
# # # print(soup.li.text)         # --> 인공지능

# #=========== .find 메서드
# # first_ul = soup.find('ul')
# # print(first_ul)
# # # <ul class="industry">
# # # <li>인공지능</li>
# # # <li>빅데이터</li>
# # # <li>신재생에너지</li>
# # # </ul>

# # print(first_ul.text)
# # # 인공지능
# # # 빅데이터
# # # 신재생에너지


# # all_ul = soup.find_all('ul')
# # print(all_ul)
# # # -- 결과 --
# # # [<ul class="industry">
# # # <li>인공지능</li>
# # # <li>빅데이터</li>
# # # <li>신재생에너지</li>
# # # </ul>, <ul class="comlang">
# # # <li>Python</li>
# # # <li>C++</li>
# # # <li>Javascript</li>
# # # </ul>]

# # print(all_ul[1])
# # # -- 결과 --
# # # <ul class="comlang">
# # # <li>Python</li>
# # # <li>C++</li>
# # # <li>Javascript</li>
# # # </ul>


# # print(all_ul[1].text)
# # # -- 결과 --
# # # Python
# # # C++
# # # Javascript


# class_ul = soup.find('ul', attrs={"class":"comlang"})
# # print(class_ul)
# # # -- 결과 --
# # <ul class="comlang">
# # <li>Python</li>
# # <li>C++</li>
# # <li>Javascript</li>
# # </ul>

# # print(class_ul.text)
# # # -- 결과 --
# # Python
# # C++
# # Javascript



# #=========== .select 메서드
# first_ul = soup.select_one("ul.industry")        # ~ 일치 선택자 : 태그명.class명
# print(first_ul)
# # <ul class="industry">
# # <li>인공지능</li>
# # <li>빅데이터</li>
# # <li>신재생에너지</li>
# # </ul>

# all_ul_1 = soup.select("div >ul")
# all_ul_2 = soup.select("#content>ul")
# all_ul_3 = soup.select("#content")
# print(all_ul_1)
# print()
# print(all_ul_2)
# print()
# print(all_ul_3)


# 서울시청 웹스크랩핑
import requests
html_url = "https://www.seoul.go.kr/main/index.jsp"
res = requests.get(html_url)
# print(res)              # --> <Response [200]>
# print(res.text)              # --> url상의 text 모두 출력

soup = BeautifulSoup(res.text, "html.parser")
# print(soup)                     # --> url상의 text가 객체 형태로 모두 출력

all_nav = soup.select("nav > ul > li > a")
# print(all_nav)
# [<a href="/realmnews/in/list.do" onclick="action_logging({tr_code:'gnb_news'});">서울소식</a>, <a href="/citizen/citizen.do" onclick="action_logging({tr_code:'top_menu05'});">시민참여</a>, <a href="https://news.seoul.go.kr" onclick="action_logging({tr_code:'gnb_more'});" target="_blank">분야별정보</a>, <a href="/seoul/seoul.do" onclick="action_logging({tr_code:'top_menu04'});">서울소개</a>, <a href="//org.seoul.go.kr" onclick="action_logging({tr_code:'top_menu06'});">부서안내</a>, <a href="//opengov.seoul.go.kr" onclick="action_logging({tr_code:'gnb_opnegov'});" rel="nosublink" target="_blank" title="새창열림">정보공개</a>, <a href="//eungdapso.seoul.go.kr" onclick="action_logging({tr_code:'gnb_eungdapso'});" rel="nosublink" target="_blank" title="새창열 림">응답소</a>, <a href="/member/userlogin/loginCheck.do" onclick="action_logging({tr_code:'top_menu01'});">로그인</a>, <a href="/member/userlogin/logOut.do" onclick="action_logging({tr_code:'top_menu01'});">로그아웃</a>, <a href="/member/info/mySeoul.do" onclick="action_logging({tr_code:'top_menu02'});">나의서울</a>, <a href="javascript:void(0)" onclick="checkMailUserYn(); return false;" title="새창열림">전자우편</a>]  
# print(all_nav[1].text)              # --> 시민참여

# for i in all_nav:
#     print(i.text)
# # 서울소식
# # 시민참여
# # 분야별정보
# # 서울소개
# # 부서안내
# # 정보공개
# # 응답소
# # 로그인
# # 로그아웃
# # 나의서울
# # 전자우편



# # 실습. 국립중앙박물관의 관람시간과 관람료 스크랩핑
# html_url_1 = "https://www.museum.go.kr/site/main/home"
# res_1 = requests.get(html_url_1)
# soup_1 = BeautifulSoup(res_1.text, "html.parser")
# timetable = [i.text for i in soup_1.select("div.info-txt.info-time > ul > li")]
# charge = [i.text for i in soup_1.select("div.info-txt.info-admission > ul > li")]
# print("관람시간")
# for i in timetable:
#     print(i)
# print("관람료")
# for i in charge:
#     print(i)
# print()

# # 실습. 국립중앙박물관의 관람시간과 관람료 스크랩핑 ㅡ 리더님 코드
# html_url_l = "https://www.museum.go.kr/site/main/home"
# res_l = requests.get(html_url_l)
# soup_l = BeautifulSoup(res_l.text, "html.parser")
# infos = soup_l.select("ul.main-info-area > li")
# times = soup_l.select(".info-time > ul > li")
# for i in times:
#     print("이용시간 : ", i.text.strip())

# pay = soup_l.select(".info-admission > ul > li")
# for i in pay:
#     print("관람료 : ", i.text.strip())
# # 이용시간 :  월/화/목/금/일 10:00 ~ 18:00
# # 이용시간 :  수/토 10:00 ~ 21:00
# # 이용시간 :  * 입장 마감은 폐관30분 전까지
# # 관람료 :  무료 특별전시는 유료


# # KBS 뉴스 스크랩핑
# kbs_news_url = "https://news.kbs.co.kr/news/pc/view/view.do?ncd=8117340"
# kbs_news_url_1 = "https://news.kbs.co.kr/news/pc/view/view.do?ncd=8121478"

# res_news = requests.get(kbs_news_url_1)
# soup_news = BeautifulSoup(res_news.text, "html.parser")
# # print(soup_news)
# title_news = soup_news.select_one(".headline-title")            # 해당 클래스가 1개만 있을때는 태그명 생략 가능
# contents_news = soup_news.select_one(".detail-body")
# print("제목 : ", title_news.text)
# print("내용 : ", contents_news.text.strip())
# # print(title_news.text)

# with open("news.txt", "w", encoding="utf8") as file:
#     file.write(title_news.text.strip())
#     file.write(contents_news.text)


# # 실습2. 전자 신문 메인 기사 크롤링
# html_url_main= "https://m.etnews.com/20241203000250"
# res_main = requests.get(html_url_main)
# soup_main = BeautifulSoup(res_main.text, "html.parser")
# # print(soup_main)

# # 1) 제목 가져오기
# title_main = soup_main.select_one("h2#article_title_h2").text
# print("기사 제목 : ",title_main, "\n")

# # 2) 발행일 가져오기
# pressdate = [i.text for i in soup_main.select("div.timewrap > .time > time")][0]
# print(pressdate, "\n")

# # 3) 본문 내용 가져오기
# content_main = soup_main.select_one("div#articleBody > p")
# print("======================  기사 본문  ======================")
# print(content_main.text)



# 실습2. 전자 신문 메인 기사 크롤링 ㅡ 리더님 코드
# 1) 매일경제 robots.txt 확인
# User-agent: *
# Disallow: /_TP/
# Disallow: /_CP/
# Disallow: /_CT/
# Disallow: /search
# Disallow: /news/inc/mkNewsLogIframe.php
# Disallow: /include/inc_news_cnt.php


# html_url_main= "https://www.mk.co.kr/news/sports/11183644"
# res_main = requests.get(html_url_main)
# soup_main = BeautifulSoup(res_main.text, "html.parser")
# # print(soup_main)

# title = soup_main.select_one(".news_ttl")  #  > div:first-child > div:first-child > div:first-child > p> span
# print("제목: ",title.text)
# time = soup_main.select_one(".time_area > dl > dd")
# print("날짜: ",time.text)
# content = soup_main.select("div.news_cnt_detail_wrap *:not(div)")
# print("기사\n",time.text)


# # 명언 크롤링
# quote_html_url = "https://quotes.toscrape.com/"
# res_quote = requests.get(quote_html_url)
# soup_quote = BeautifulSoup(res_quote.text, "html.parser")
# quote = soup_quote.select(".quote > .text")
# # print(len(quote))
# print()
# text = [ i.text.strip() for i in quote]
# # print(text)
# print()
# speak = soup_quote.select(".author")
# author = [i.text.strip() for i in speak]
# # print(author)
# zipped = list(zip(text, author))            # zip : 두 list의 병렬 합친 튜플 생성
# # print(zipped)
# for text, speak in zipped:
#     print (f"명언 : ", text)
#     print(f"from : {speak} \n")


# # 실습3. 네이버 환율정보 크롤링
# exchange_html_url = "https://m.stock.naver.com/marketindex/home/exchangeRate/exchange"
# res_exchange = requests.get(exchange_html_url)
# soup_exchange = BeautifulSoup(res_exchange.text, "html.parser")
# exchange_type = [ i.text for i in soup_exchange.select("ul.MainList_list__TEOEp > li > a > strong")]
# # print(exchange_type)
# # print()
# exchange_rate = [ i.text for i in soup_exchange.select("ul.MainList_list__TEOEp > li > a > span")]
# exchange_rate = [ exchange_rate[i] for i in range(len(exchange_rate)) if i % 2 == 0]
# # print(exchange_rate)
# # print()
# exchange = list(zip(exchange_type, exchange_rate))
# print("===========  환율 정보  ===========")
# for e_type, e_rate in exchange:
#     print(f"환종 : {e_type} ㅡ 환율 : {e_rate}")

# 실습3. 네이버 환율정보 크롤링 ㅡ 리더님 코드
# 네이버증권 > 시장지표 > 환율
from bs4 import BeautifulSoup
import requests
# html_url = "https://finance.naver.com/marketindex/"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, "html.parser")
# usd = soup.select("#exchangeList .usd .value")
# jpy = soup.select("#exchangeList .jpy .value")
# cny = soup.select("#exchangeList .cny .value")
# print("USD: ", usd.text)
# print("JPY: ", jpy.text)
# print("CNY: ", cny.text)




# # 실습4. 주식정보 크롤링
# stock_html_url = "https://finance.naver.com/item/main.naver?code=005490"
# res_stock = requests.get(stock_html_url)
# soup_stock = BeautifulSoup(res_stock.text, "html.parser")
# # 종목명
# stock_comp_name = soup_stock.select_one("div.wrap_company > h2 > a")
# # 종목코드
# stock_comp_code = soup_stock.select_one("div.description > span.code")
# # 기준일자
# stock_comp_date = soup_stock.select_one("span#time > .date")
# # 기업개요
# stock_comp_desc = [ i.text for i in soup_stock.select("div.summary_info > p")]
# stock_comp_desc = ''.join(stock_comp_desc)
# # 금일 종가
# price_close = [ i.text for i in soup_stock.select("p.no_today > em.no_down > span") if i.text.isdecimal() ]
# price_close = int(''.join(price_close))
# # 기타 정보 (시가/고가/저가/전일종가/거래량/거래대금)
# info_table = [i.text.strip() for i in soup_stock.select(".no_info span") if len(i.text)!=1]
# del info_table[4:6]
# del info_table[10]
# info_type = [i for i in info_table if info_table.index(i)%2==0]
# info_nums = [i for i in info_table if info_table.index(i)%2==1]
# info_tuple = list(zip(info_type, info_nums))

# # 주식 정보 출력
# print(f"종목명(종목코드) :  {stock_comp_name.text} {stock_comp_code.text}\n")  #.text.strip()
# print(f"기업개요 : \n   {stock_comp_desc}\n")
# print(f"주가일자 : {stock_comp_date.text}\n")
# print(f"금일 종가 : {price_close:,d}원\n")
# for i in range(len(info_tuple)):
#     if info_tuple[i][0] =="거래대금":
#         print(f"{info_tuple[i][0]}(백만) : {info_tuple[i][1]}")
#     else:
#         print(f"{info_tuple[i][0]} : {info_tuple[i][1]}")



# 실습4. 주식정보 크롤링 ㅡ 리더님 코드
#  게속 업데이트되면서 html 화면의 Elemnet 확인이 어려울때 > Network 탭에서 정지 아이콘을 클릭한 후 
def stock(code):
    html_url = f"https://finance.naver.com/item/main.naver?code={code}"
    res = requests.get(html_url)
    soup = BeautifulSoup(res.text, "html.parser")
    # print(soup)
    comppany = soup.select_one(".wrap_company > h2 > a")
    print(f"회사명 : {comppany.text}")
    price = soup.select_one(".today > .no_today .blind")
    print(f"종가 : {price.text.strip()}원")
    ex_price = soup.select_one(".today > .no_exday .blind")
    print(f"전일대비 : {ex_price.text.strip()[0]}원")

stock("035720")     # 카카오
stock("005930")     # 삼성전자
stock("294090")     # 카카오


