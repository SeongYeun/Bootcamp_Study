# 웹크롤링 ㅡ 제주 하루전시장 시간별 SMP 단가

# 1. 라이브러리 및 기본 설정
import pandas as pd
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

url = "https://www.kpx.or.kr/bidSmpLfdDataDa.es?mid=a10406020100&device=pc&division=smpDataDa&gubun=today"
rs = requests.get(url)
soup = BeautifulSoup(rs.text, 'html.parser')
# 2. hour
hour=["0:00", "1:00", "2:00", "3:00", "4:00", "5:00", "6:00", "7:00", "8:00", "9:00", "10:00", "11:00",
     "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00",
      "22:00", "23:00"]

# 3. 오늘 날짜
today = datetime.today().strftime("%Y-%m-%d")
tommarow = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")


# 4. SMP 웹크롤링
if rs.status_code != 200:
    print('웹페이지 정보 가져오기 실패')
else:
    # print('웹페이지 정보 가져오기 성공\n')
    raw = soup.find_all('td')
    n = len(raw)

    # 오늘, 내일 hourly SMP -> list에 저장
    today_smp, tmr_smp = [], []
    a=1
    for i in range(n) : 
        if i == 189:
            today_smp.insert(0, raw[i].text)
            a+=1
        elif (i==190):
            tmr_smp.insert(0, raw[i].text)
            a+=1
        elif a==7:
            today_smp.append(raw[i].text)
            a+=1
        elif a==8:
            tmr_smp.append(raw[i].text)
            a=1
        else:
            a+=1
    # print("오늘 : ", len(today_smp), today_smp)
    # print("내일 : ", len(tmr_smp), tmr_smp)
    today_smp = [float(i) for i in today_smp[:-3]]
    tmr_smp = [float(i) for i in tmr_smp[:-4]]


    # text graph
    def graph_hourlysmp(hour, smp):
        sp, ch_m, ch_p = " ", "-", "+"
        file.write(f"{'hour':^6s}   {'SMP':^8s}\n")
        file.write(f"{'='*6:6s}   {'='*8:8s}  {'-'*10} 0 {'-'*40}\n")
        for i, smp_v in enumerate(smp):
            n_sp, n_ch_m, n_ch_p = 10, 0, 0
            if smp_v<=0:
                n_ch_m = int(smp_v*0.1)
                n_sp = 10-n_ch_m
            else:
                n_ch_p = int(smp_v*0.1)
            file.write(f"{hour[i]+"~":>6s}   {smp_v:>8.2f}  {sp*n_sp}{ch_m*n_ch_m} 0 {ch_p*n_ch_p}\n")            

# 5. 오늘 & 내일 SMP 그래프 (CSV 파일 생성)
with open("hourly_smp.csv", "w", encoding="utf-8") as file:
    file.write(f"[   오늘({today}) 시간별 SMP(원/kWh) 예측 그래프   ]\n")
    graph_hourlysmp(hour, today_smp)
    file.write("\n")
    file.write(f"[   내일({tommarow}) 시간별 SMP(원/kWh) 예측 그래프   ]\n")
    graph_hourlysmp(hour, tmr_smp)



