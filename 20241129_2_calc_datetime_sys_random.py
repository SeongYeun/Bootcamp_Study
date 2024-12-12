#### ===============  모듈 =============== ####

# 1) 모듈 불러오는 방식
# import calc
# import calc as a
# from calc import add, sub
# from calc import add as a, sub as b
# from calc import *



# 모듈명.함수명
# print(calc.add(10,4))               # --> 14
# print(calc.sub(10,4))               # --> 6
# print(calc.multiply(10,4))          # --> 40
# print(calc.divide(10,4))            # --> 2.5

# 모듈 별칭 사용 후
# print(a.add(10,4))                      # --> 14
# print(a.sub(10,4))                      # --> 6
# print(a.multiply(10,4))                 # --> 40
# print(a.divide(10,4))                   # --> 2.5

# from calc import add, sub 경우
# print(calc.add(10,4))                      # --> 14
# print(calc.sub(10,4))                      # --> 6

# from calc import add as a, sub as b 경우
# print(a(10,4))                      # --> 14
# print(b(10,4))                      # --> 6

# from calc import * 경우
# print(add(10,4))               # --> 14
# print(sub(10,4))               # --> 6
# print(multiply(10,4))          # --> 40
# print(divide(10,4))            # --> 2.5



# 2) .today()ㅡ 타임존값X, .now()ㅡ타임존값O
from datetime import datetime, timedelta, timezone

# now = datetime.today()          # .today() : 현재시간
# print(now)                      # --> 2024-11-29 16:15:17.117610
# print(now.year)                 # --> 연도 추출
# print(now.month)                # --> 월 추출
# print(now.day)                  # --> 일 추출
# print(now.hour)                 # --> 시간 추출
# print(now.minute)               # --> 분 추출
# print(now.second)               # --> 초 추출

# print(f"{now.year}년 {now.month}월 {now.day}일")            # --> 2024년 11월 29일


# now = datetime.now()            # .now() : 현재시간, 타임존을 이용한 계산 가능
# print(now)                      # --> 2024-11-29 16:18:43.007254


# 3) 특정날짜 계산
# next_week = now + timedelta(weeks=1)
# print(next_week)                # --> 2024-12-06 16:24:40.908093
# next_week = now + timedelta(weeks=1, hours=1)
# print(next_week)                # --> 2024-12-06 17:25:33.092768


# 4) 타임존 계산
# print(timezone.utc)                 # --> UTC
# print(datetime.now(timezone.utc))   # --> 현재 UTC 타임존값(+00:00) : 2024-11-29 07:30:15.516962+00:00 

# print(datetime.now(timezone(timedelta(hours=9))))
# # 2024-11-29 16:31:28.716026+09:00  #--> 뒤에 +09:00이 타임존값


# 4) 남짜, 요일 추출
# from datetime import date
# open_day = date(year=2024, month=11, day=18)
# print(date.today())                         # --> 2024-11-29
# print(date.today().weekday())               # --> 4 (금요일 의미)
# week = ["월", "화", "수", "목", "금", "토", "일"]
# print(week[date.today().weekday()])         # --> 금

# pass_day = date.today() - open_day
# print(pass_day)                             # --> 11 days, 0:00:00
# print(pass_day.days)                        # --> 11


# 5) 시간 추출, 잠시 멈춤(대기)
# import time
# print(time.time())                          # --> 1732866566.9799538
# print(time.localtime())                     # --> time.struct_time(tm_year=2024, tm_mon=11, tm_mday=29, tm_hour=16, tm_min=49, tm_sec=26, tm_wday=4, tm_yday=334, tm_isdst=0)
# print("2초 대기")
# time.sleep(2)                   # 프로그램 잠시 멈춤
# print("대기완료")
# start = time.perf_counter()     # 시간측정
# time.sleep(1)                   # 프로그램 잠시 멈춤
# end = time.perf_counter()
# print(end-start)                            # --> 1.0004861000925303

# 6) 올림/반올림/내림 / 제곱근/팩토리얼
# import math
# print(math.pi)                              # --> 3.141592653589793
# print(math.sqrt(25))                        # --> 5.0
# print(math.factorial(5))                    # --> 120
# print(math.ceil(2.43))                      # --> 3
# print(math.floor(4.88))                     # --> 4
# print(round(2.5))                           # --> 2
# print(round(2.5, 0))                        # --> 2.0
# print(round(2.5000001))                     # --> 3


# 7) 난수 생성
# import random, math
# print(random.randint(1,10))                 # 끝값 포함한 정수의 난수 발생
# # --> 7
# print(random.uniform(1.1,5.5))              # 실수의 난수 발생
# # --> 1.2834394443752437
# print(random.random())                       # 0~1 사이 난수 발생
# print(random.randrange(1000, 10000))         # 끝값 미포함하여 난수 발생

# choices = [1, 2, 3, 4, 5, 6, 7, 8]
# print(random.choice(choices))               # 특정 목록내에서 임의 선택
# # --> 8

# rand = 1000 + math.floor(random.random() * 9000)
# print(rand)                             # --> 3986


# # 실습. 로또 번호 뽑기
# import random, math
# numbers = list(range(1, 46))
# set_num = set()
# while True :
#     if len(set_num) == 6 :
#         print(sorted(set_num))
#         break
#     else :
#         set_num.add(random.choice(numbers))

# # 실습. 로또 번호 뽑기 ㅡ 리더님 코드
# import random, math
# lotto = set()
# while len(lotto)<6 :
#     lotto.add(random.randint(1, 45))

# print(sorted(lotto))

# # 실습. 로또 번호 뽑기 ㅡ 다른 크루 코드
# # 1) random.sample() 이용
# lotto = sorted(random.sample(numbers, 6))
# print(lotto)


# 8) sys
import sys

# print(sys.argv)
# # --> ['c:/Users/praye/Documents/Bootcamp/index2_20241129.py']
# print(sys.argv[1:])
# # --> []

# git bash에서 python index2_20241129.py a b c d 입력후  ㅡ 외부에서 파이썬 파일에 입력
# print(sys.argv[1:])
# ['a', 'b', 'c', 'd']

# git bash(터미널)에서 출력화면 설정
if "-h" in sys.argv or "--help" in sys.argv:
    print("사용법 : python main.py [옵션]")
    print("-h, --help         도움말 표시")
    print("-v, --version     버전정보표시")
    sys.exit(0)         # 프로그램 종료

if "-v" in sys.argv or "--version" in sys.argv:
    print("버전 : 1.0.0")
    sys.exit(0)         # 프로그램 종료

# git bach에서 : python index2_20241129.py -h
# -->
# 사용법 : python main.py [옵션]
# -h, --help         도움말 표시
# -v, --version     버전정보표시

# git bach에서 : python index2_20241129.py -v
# --> 버전 : 1.0.0


# 9) os
# import os

# dir_current = os.getcwd()               # 현재 파일 주소(위치) 반환
# print(dir_current)
# file_path = os.chdir(dir_current)       # ()안 경로로 이동
# dir = os.popen('ls')                    # ()안 명령어를 터미널에 입력
# print(dir.read())                       # 터미널 결과를 읽어와서 출력

# os.mkdir("os_mkdir_test")                   # 현재 위치에 신규 폴더 생성
# os.rmdir("os_mkdir_test")                   # 현재 위치 해당 폴더 삭제

# print(os.environ.get('PATH'))               # 환경변수 내용을 출력
# C:\Users\praye\bin;C:\Program Files\Git\mingw64\bin;C:\Program Files\Git\usr\local\bin;C:\Program Files\Git\usr\bin;C:\Program Files\Git\usr\bin;C:\Program Files\Git\mingw64\bin;C:\Program Files\Git\usr\bin;C:\Users\praye\bin;C:\Program Files (x86)\Intel\iCLS Client;C:\Program Files\Intel\iCLS Client;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\IPT;C:\Program Files\Intel\Intel(R) Management Engine Components\IPT;C:\Program Files\Intel\WiFi\bin;C:\Program Files\Common Files\Intel\WirelessCommon;C:\WINDOWS\System32\OpenSSH;C:\Users\praye\AppData\Local\Programs\Python\Python37-32;C:\Program Files\dotnet;C:\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit;C:\Program Files\Git\cmd;C:\Users\praye\AppData\Local\Programs\Python\Python312\Scripts;C:\Users\praye\AppData\Local\Programs\Python\Python312;C:\Program Files\MySQL\MySQL Shell 8.0\bin;C:\Users\praye\AppData\Local\Programs\Python\Python39\Scripts;C:\Users\praye\AppData\Local\Programs\Python\Python39;C:\Ruby26-x64\bin;C:\Users\praye\AppData\Local\Microsoft\WindowsApps;C:\Users\praye\AppData\Local\atom\bin;C:\Users\praye\AppData\Local\Microsoft\WindowsApps;C:\Users\praye\.dotnet\tools;C:\Users\praye\AppData\Local\Programs\Microsoft VS Code\bin;C:\Program Files\Graphviz\bin;C:\Program Files\Git\usr\bin\vendor_perl;C:\Program Files\Git\usr\bin\core_perl



# 10) json  : 자바스크립트 <-> 파이썬 문법 변환
# import json

# # 파이썬 객체
# data = {
#     "name":"홍길동",
#     "age":20,
#     "city":"서울"
# }

# # 자바스크립트 객체로 변환
# json_str = json.dumps(data)         # 딕셔너리(키:값)을 하나의 문자열로 변환
# print(json_str)                     # json 객체
# # --> {"name": "\ud64d\uae38\ub3d9", "age": 20, "city": "\uc11c\uc6b8"}

# py_obj = json.loads(json_str)
# print(py_obj)                       # 파이썬 객체 (딕셔너리)
# # --> {'name': '홍길동', 'age': 20, 'city': '서울'}


# 실습. 타자연습 게임
import random
from datetime import datetime

words = ["mountain", "river", "forest", "ocean", 
         "desert", "tree", "flower", "cloud", 
         "rain", "sunlight"]
start_time = datetime.today()
counts = 0
print("[=====영어 타자 연습=====]")
while True:
    test_word = random.sample(words, 1)[0]
    counts += 1 
    print(f"단어 : {test_word}")
    user_input = input("입력 : ")
    print()
    if user_input == "exit":
        print("[=====게임 종료=====]")
        end_time = datetime.today()
        break
    while user_input != test_word:
        print("오답! 다시 시도하세요\n")
        user_input = input("입력 : ")
    print("통과!\n")
    
total_time = end_time - start_time
total_seconds = total_time.total_seconds()
print(f"총 {counts}개의 단어를 입력하셨습니다.")
print(f"총 걸린 시간: {total_seconds:.2f}초")
print(f"평균 단어당 입력 시간: {total_seconds/counts:.2f}초")


# 실습. 타자연습 게임 ㅡ 리더님 코드  w/반복문
import random, time


def game():
    print("영어 타자 연습 게임")
    print("게임종료를 원하시면 exit를 입력하세요")
    total_words = 0
    start_time = time.time()        # 현재 시간 기록 (최소단위 : 초)

    while True:
        word = random.choice(words)
        print(f"단어: {word}")

        while True:
            user_input = input("입력 : ")

            if user_input == "exit":
                end_time = time.time()
                total_time = end_time - start_time
                print("\n게임종료")
                print(f"총 입력한 단어는 {total_words}개 입니다.")
                print(f"총 걸린 시간은 {total_time:.2f}초")
                print(f"단어당 평균시간은 {total_time / total_words:.2f}초")
                return                      # --> game()함수가 종료됨
            
            if user_input == word:
                print("통과!")
                total_words += 1
                break
            else:
                print("오타! 다시입력")





        
    
