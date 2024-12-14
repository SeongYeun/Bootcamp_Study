# 변수 사이즈 확인
# from sys import getsizeof
# print(getsizeof(1))    # --> 28
# print(getsizeof("1"))  # --> 42


# 변수 자료형 확인
# print(type(1111))         # --> int
# print(type(11.11))        # --> float
# print(type("11.11"))      # --> str
# print(type("안녕하세요"))  # --> str
# print(type(True))         # --> bool
# print(type(None))         # --> NoneType


# 자료형 변환
# num = int(input("숫자를 입력하세요 >>>  "))   # ****입력받은 값은 모두 문자형****
# b = num%2 == 0
# print(num, "이/가 True면 짝수, False면 홀수 -> 결과 : ", b)
# print(int(5.5))        # --> 5
# print(int("30"), type(int("30")))     # --> 30, 'int'
# a = "10"
# print(type(int(a)))    # --> int
# print(type(a))         # --> str
# num = 10
# print(type(str(num)))  # --> str


# 문자열 연산 ㅡ  +:연결  *:반복
# print("안녕하세요 " + "반갑습니다")       # 안녕하세요 반갑습니다
# print("안녕하세요 ", "반갑습니다")        # 안녕하세요  반갑습니다
# a = "파이썬"
# print("안녕하세요 "+a+"반갑습니다")       # 안녕하세요 파이썬반갑습니다
# print("안녕하세요 " + a + "반갑습니다")   # 안녕하세요 파이썬반갑습니다
# # print("안녕하세요 " + 10)              # 오류
# print("hey! " * 10)                     # hey! hey! hey! hey! hey! hey! hey! hey! hey! hey!


# 여러줄 문자열 출력   ㅡ """ : 독스트링  1) 주석처리 2) 여러줄 출력
korea_song = """
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산
대한사람 대한으로 길이 보전하세
"""
# print(korea_song)


# 따옴표 출력
# print('"오늘 저녁 뭐먹지?"라고 말했다.')           # --> "오늘 저녁 뭐먹지?"라고 말했다.
# print("'오늘 저녁 뭐먹지?'라고 생각하는 중이다.")   # --> '오늘 저녁 뭐먹지?'라고 생각하는 중이다.
# print("Hello\nWorld")              
# # --> Hello
# #     World
# print("Hello\tWorld")              # --> Hello   World
# print("This is a backslash : \\")  # --> This is a backslash : \
# print('It\'s a book')              # --> It's a book
# print("He sid \"Hello\"")          # --> He sid "Hello"


# 문자열 포매팅 : 다양한 타입을 포함한 문자열 출력
# 1) 포맷코드 사용 ㅡ 많이 사용하진 않음
# year = "올해는 %d년 %s의 해이다" % (2024, "용띠")
# print(year)                         # --> 올해는 2024년 용띠의 해이다
# year = "올해는 %d년 %s의 해이다" % (2025, "뱀띠")
# print(year)                         # --> 올해는 2025년 뱀띠의 해이다

# number = "저는 올해 %d살 입니다" % 20
# print(number)                       # --> 저는 올해 20살 입니다
# calc = "20 나누기 3은 %f" % 6.66
# print(calc)                         # --> 20 나누기 3은 6.660000
# calc = "20 나누기 3은 %.10f" % 6.66
# print(calc)                         # --> 20 나누기 3은 6.6600000000
# text = "저는 %10s에서 살고 있습니다." % "서울"
# print(text)                         # --> 저는         서울에서 살고 있습니다.
# text = "저는 %-10s에서 살고 있습니다." % "서울"
# print(text)                         # --> 저는 서울        에서 살고 있습니다.
# char = "이모티콘은 %c 이것으로 할께요" % "😊"    # --> Win+. : 이모티콘창 팝업
# print(char)                         # --> 이모티콘은 😊 이것으로 할께요

# 2) 포멧 매서드(format()) 사용
# country = "대한민국"
# city = "서울"
# people = "한국인"
# text = "저는 올해 {0}살입니다.".format(20)
# print(text)                   # --> 저는 올해 20살입니다.
# text = "저는 {0}사람이며 {1}에 살고있습니다.".format(country, city)
# print(text)                   # --> 저는 대한민국사람이며 서울에 살고있습니다.
# # text = "제가 사는 {a}은 {0}에 있습니다.".format(a="한국", city)     # 오류
# # print(text)                   # --> 오류
# text = "제가 사는 {0}은 {a}에 있습니다.".format(city, a="한국")
# print(text)                   # --> 제가 사는 서울은 한국에 있습니다.
# text = "나는 {1}이다. {{ 그리고 }} {0}에 산다.".format(city, people)
# print(text)                   # --> 나는 한국인이다. { 그리고 } 서울에 산다.
# text = "{}점수: {}점, {}점수: {}점".format("영어", 100, "수학", 90)
# print(text)                   # --> 영어점수: 100점, 수학점수: 90점

# a ="[{0:<10}]".format("hey")  # > :왼쪽정렬
# print(a)                      # --> [hey       ]
# a ="[{0:>10}]".format("hey")  # < :오른쪽정렬
# print(a)                      # --> [       hey]
# a ="[{0:^10}]".format("hey")  # ^ :가운데정렬
# print(a)                      # --> [   hey    ]
# a ="[{0:!<10}]".format("hey") # !< : 좌측정렬 & !로 공백채움
# print(a)                      # --> [hey!!!!!!!]
# a ="[{0:^20.7f}]".format(1 / 3) # 가운데정렬(^) & 총 20자리(20) & 소수점7자리(.7) 실수형(f)
# print(a)                      # --> [     0.3333333      ]
# a ="[{0:,}]".format(123456789) # 정수부분 3자리마다 , 표기
# print(a)                      # --> [123,456,789]

# # 3) f문자열 사용 ㅡ 가장 많이 사용 (파이썬 3.6버전부터 가능)
# name = "홍길동"
# age = 20
# print(f"내 이름은 {name}입니다. 나이는 {age +1}입니다.")     # --> 내 이름은 홍길동입니다. 나이는 21입니다.
# print(f"내 이름은 [{name:-^20}]")                          # --> 내 이름은 [--------홍길동---------]

# 실습. 이스케이프(\) 연습
# print("| \\_/ |")
# print("| q p |\t  /}")
# print("(  Θ  )\"\"\"\\")
# print("| \"^\"`\t   |")
# print("| |_/=\\ \\__|")
# print("\n\n\n")

# 실습. f문자열 포매팅 실습
# name = "강성연"
# print(f"1) {name:=^20}")
# print(f"2) 문자열 실습입니다. {{ 중괄호 }}를 출력해보세요")



#  문자열 인덱싱 / 슬라이싱
# a = "Hello, Python"
# print(a[7]+a[8]+a[9]+a[10]+a[11]+a[12])   # --> Python
# print(a[7:])                              # --> Python
# print(a[-6:])                             # --> Python
# print(a[7:12])                             # --> Pytho
# print(a[7:13])                             # --> Python


# date = "20240930"
# print("년 : ", date[:4])     # -->년 :  2024
# print("월 : ", date[4:6])    # -->월 :  09
# print("일 : ", date[6:])     # -->일 :  30
# print(date[:4]+"년 "+date[4:6]+"월 "+date[6:]+"일")    # --> 2024년 09월 30일

# 길이구하기 : len()함수
# print(len(a))                  # --> 13
# print(len(date))               # --> 8

# 개수 세기 : .count(찾을문자) 메서드
# print(a.count('l'))            # --> 2

# 위치 찾기
#  : .find(찾을문자) 메서드 ~> 있는지 여부  (없을때 -1 반환)
#  : .index(찾을문자) 메서드 ~> index값을 반환 (없을때 오류)
# a = "Hello, Python"
# print(a.find('P'))               # --> 7
# print(a.find('o'))               # --> 4
# print(a.index('o'))              # --> 4
# print(a.find('s'))               # --> -1
# print(a.index('s'))            # --> 오류

# first_o = a.find('o')
# print(first_o)                   # --> 4
# second_o = a.find('o', first_o + 1)
# print(second_o)                  # --> 11


# 문자열
# 바꾸기 : .replace("기존문자", "바꿀문자")
# 나누기 : .split("나누는문자")
# a = "Hello, Python"
# print(a.replace("Python", "파이썬"))   # --> Hello, 파이썬
# print(a.split("l"))                   # --> ['He', '', 'o, Python']
# print(a.split(" "))                   # --> ['Hello,', 'Python']


# 대소문자 변환
# a = "Hello, World"
# print(a.upper())                        # --> HELLO, WORLD
# print(a.lower())                        # --> hello, world

# 공백 삭제
# a = "     H e  l l     o   "
# print(f"[{a.rstrip()}]")                # --> [     H e  l l     o]
# print(f"[{a.lstrip()}]")                # --> [H e  l l     o   ]
# print(f"[{a.strip()}]")                 # --> [H e  l l     o]
# print(f"[{a.replace(" ", "")}]")        # --> [Hello]

# 숫자판별
# print("1234".isdecimal())               # --> True
# print("1234".isdigit())                 # --> True
# print("1234".isnumeric())               # --> True
# print("-1234".isnumeric())              # --> False  *** 음수는 항상 False
# print("12.34".isnumeric())              # --> False  *** 소수점 포함한 실수는 False

# print("Hello".islower())                # --> False
# print("HELLO".isupper())                # --> True


# 실습. 종합실습
# 1번)
# name = input("이름을 입력하세요. ")
# age = int(input("나이를 입력하세요. "))
# print(f"안녕하세요! {name}님 ({age}세)\n")
# 2번)
# name = input("이름을 입력하세요. ")
# year_birth = int(input("태어난 년도를 입력하세요. "))
# year_current = int(input("올해 년도를 입력하세요. "))
# print(f"올해는 {year_current}년, {name}님의 나이는 {year_current - year_birth}세 입니다.")