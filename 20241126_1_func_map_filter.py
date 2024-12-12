#======= 변수 =======
# 1) 전역변수
quantity = 10

def get_price(price):
    price = price * quantity
    return price

print(f"{quantity}개의 가격은 {get_price(2000):,}입니다")     # --> 10개의 가격은 20,000입니다
print(f"{quantity}개의 가격은 {get_price(5000):,}입니다")     # --> 10개의 가격은 50,000입니다

# 2) 지역변수
def oneUp():
    x = 0
    x += 1
    return x
print(oneUp())          # --> 1

# 3) 변수의 유효번위
quantity = 10

def price_sum(price):
    # quantity = 7
    return price * quantity
print(price_sum(2000))      # --> 14000  # 똑같은 변수가 있을땐 지역변수가 우선순위가 높음
print(price_sum(2000))      # --> 20000  # 지역변수 quantity가 없을때 전역변수 quantity값이 계산에 적용됨

# 4) global 키워드
x = 0
def oneUp():
    global x
    x += 1
    return x


# 원래 코드
print(oneUp())      # --> 오류 남 : cannot access local variable 'x' where it is not associated with a value
# 함수내 global x 추가시
print(oneUp())      # --> 1 같은 명령어 계속 반속할때마다 전역변수가 값이 변경되기 때문에 결과값이 달라짐

# 5) 함수의 기본 매개변수
def pr_str(txt = "안녕하세요", count=1):
    for _ in range(count):
        print(txt, end=" ")

pr_str()                # --> 안녕하세요  << 기본값이 함수정의에 있기 때문에 매개변수값이 없어도 오류발생 안함
pr_str("hello", 5)        # --> hello hello hello hello hello 
pr_str("hi")            # --> hi 
pr_str(5)              # --> 5 

# 6) 함수 호출키워드 (순서)
def intro(name, age, city):
    print(f"이름은{name}이고 나이는 {age}이고 사는 곳은 {city}입니다.")
intro("홍길동",23,"서울")                   # --> 이름은홍길동이고 나이는 23이고 사는 곳은 서울입니다.
intro(city="서울",name="임꺽정",age=25)     # --> 이름은임꺽정이고 나이는 25이고 사는 곳은 서울입니다.
# 일부만 키워드 사용시 ㅡ 키워드 없는 변수들을 기존 함수정의 순서에 맞게 순서대로 쓴 후 키워드 변수들을 입력하면됨
# 키워드 변수들은 순서 상관 없음
intro("홍길동", city="부산", age=25)        # --> 이름은홍길동이고 나이는 25이고 사는 곳은 부산입니다.

# 7) 가변 매개변수 ㅡ 매개변수 개수가 가변적일때 >> *args 사용
def calc_avg(*args):
    total = 0
    for i in args :  # args는 튜플 형태로 인수를 받고 계산을 진행함
        total += i
    avg = total / len(args)
    return avg
print(calc_avg(1,2,3,4,5,6,7,8))        # --> 4.5

# 가변 위치 매개변수 ㅡ 튜플 형태
def text_def(a, b, *args):
    print("text : ", a)
    print("b : ", b)
    print("args : ", args)
text_def(1,2,3,4,5)                         # --> args :  (1, 2, 3, 4, 5)
text_def("hi", 1,2,3,4,5)                   # 고정위치 매개변수 a와 print("text : ", a) 추가 후
# text :  hi
# args :  (1, 2, 3, 4, 5)
text_def("hi", 1,2,3,4,5)                   # 고정위치 매개변수 b와 print("b : ", b) 추가 후
# text :  hi
# b :  1
# args :  (2, 3, 4, 5)

# 가변 키워드 매개변수 ㅡ 딕셔너리 형태
def intro(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
intro(name="홍길동", age=20, city="서울", gender="남자")
# name : 홍길동
# age : 20
# city : 서울
# gender : 남자


#======= 내장함수 =======
# 절대값 구하는 함수 vs 내장함수 ㅡ abs(값)
def my_abs(x):
    if x < 0:
        return -x
    else :
        return x

print(my_abs(-10))              # --> 10
print(my_abs(5))              # --> 5
print(abs(-25))                 # --> 25

# 거듭제곱 산출 내장함수 ㅡ pow(밑, 지수)
print(pow(2, 3))                # --> 8
print(pow(2, 4))                # --> 16
def my_pow(x, y):
    num = 1
    for i in range(y) :
        print(f"i = {i}, {num*x}={num}x{x}")
        num *= x
    return num
print(my_pow(3, 4))
# i = 0, 3=1x3
# i = 1, 9=3x3
# i = 2, 27=9x3
# i = 3, 81=27x3
# 81


# map(함수, 반복가능 객체) -> 리턴 : list()형태
def square(x):
    return x ** 3
numbers = [2, 4, 6, 8]
squared = map(square, numbers)
print(squared)                          # --> <map object at 0x000001EE0DE76A40>   : 리스트의 주소값 반환
squared = list(squared)
print(squared)                          # --> [8, 64, 216, 512]


filter(함수(T/F), 반복가능 객체) -> 리턴 : list()형태  : 함수가 True일때의 객체내 값만 필터링
def even_number(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(even_number, numbers)))   # --> [2, 4, 6, 8]


# 실습4. 함수 만들기
def get_multiple(start, end, x):
    ranges = list(range(start, end+1))
    def multi(a):
        return a % x == 0
    multiple = list(filter(multi, ranges))
    print(multiple)
    print(f"{x}의 배수의 개수 : {len(multiple)}")
    return multiple, len(multiple)
get_multiple(1,30,3)
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
# 3의 배수의 개수 : 10

# 실습4. 함수 만들기 ㅡ 다른 크루 코드 응용
def get_multiple_1(start, end, x):
    a = range(start, end+1)
    multi = [i for i in a if i%x==0]    # <<< 리스트내포에 반복문과 조건문에서 i 통일
    print(multi)
    print(f"{x}의 배수의 개수 : {len(multi)}")
    return
get_multiple_1(1,50, 7)
# [7, 14, 21, 28, 35, 42, 49]
# 7의 배수의 개수 : 7

# 실습4. 함수 만들기 ㅡ 리더님 코드 _ 1 ㅡ 리스트내포 사용 ㅡ 추천
def count(num):
    lists = [i for i in range(1, 31) if i % num == 0]
    counts = len(lists)
    return lists, counts
num=3
lists, counts = count(num)
print(f"{num}의 배수: ", lists)
print(f"{num}의 배수의 개수: ", counts)
# 3의 배수:  [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
# 3의 배수의 개수:  10

# 실습4. 함수 만들기 ㅡ 리더님 코드 _ 2 ㅡ 중첩함수 x filter() 사용 ㅡ 비추 > 리스트내포 x 람다 사용 추천
def count(num) :
    # 중첩 함수 ㅡ count()함수 내에서만 사용 가능
    def check(x):
        return x % num == 0
    lists = list(filter(check, range(1, 31)))
    return lists, len(lists)
num=4
lists, counts = count(num)
print(f"{num}의 배수: ", lists)
print(f"{num}의 배수의 개수: ", counts)
# 4의 배수:  [4, 8, 12, 16, 20, 24, 28]
# 4의 배수의 개수:  7


#======= 재귀함수 : 반복문제의 단순화 =======   예) 팩토리얼, 피보나치, 하노이 탑
def sos(i):
    print("Hepl me!", i)
    if i==1 :
        return ""
    else:
        return sos(i-1)

sos(3)
# Hepl me! 3
# Hepl me! 2
# Hepl me! 1

# 팩토리얼
def factorial(n):
    print("n의 값 : ", n)
    if n == 1 :
        return 1
    else :
        return n * factorial(n-1)
print(factorial(5))
# n의 값 :  5
# n의 값 :  4
# n의 값 :  3
# n의 값 :  2
# n의 값 :  1
# 120

# 실습5. 피보나치 수열 만들기  ㅡ 오류 있음
def fibonacci(a):
    if a < 0 :
        return 0
    elif a == (0 or 1) :
        return a
    else:
        print(f"a : {a}", end=" ")
        result_1 = fibonacci(a-1)
        result_2 = fibonacci(a-2)
        print(f"result_1 : {result_1},  result_2 : {result_2}")
        return result_1 + result_2
print(fibonacci(6))

# 실습5. 피보나치 수열 만들기 ㅡ 리더님 코드_1  : 시간 복잡도로 따지면 좋은 코드는 아님
# ㄴ> 메모제이션? 이용하면 됨
def fibonacci(n):
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))         # --> 8


#======= 람다식 : 짧은 익명 함수 (=함수명이 없는 임시함수) =======
lambda 매개변수 : 표현식(리턴값 식)
# 1) 매개변수가 1개인 람다 함수
# 1-1) 일반식
def add(x, y):
    return x+y
print(add(3,4))             # --> 7
# 1-2) 람다식
add = lambda x, y: x+y
print(add(4,5))             # --> 9

oneup = lambda x : x+1
print(oneup(1))             # --> 2
print((lambda x : x+1)(1))  # --> 2

square = lambda x: x**2
print(square(4))            # --> 16
print((lambda x: x**2)(4))  # --> 16

minus = lambda x, y : x-y
print(minus(10, 6))         # --> 4
print((lambda x, y : x-y)(10, 3))   # --> 7

# 2) 람다 함수를 매개 변수로 전달하기
# callback함수
def call(func):
    for _ in range(10):
        func()          # <-- ()를 사용해야 함수를 실행하게 됨

def hello():
    print("안녕하세요")

hello2 = lambda: print("반갑습니다.")
call(hello)         # --> 안녕하세요 * 10
call(hello2)         # --> 반갑습니다. * 10

람다식 w/ map()
numbers = [2, 4, 6, 8]
squared = map(lambda x : x**3, numbers)
print(list(squared))        # --> [8, 64, 216, 512]

# 람다식 w/ filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(lambda x: x%2==0, numbers)))      #--> [2, 4, 6, 8]

# 실습4. 함수 만들기 ㅡ 리더님 코드 _ 2 ㅡ 중첩함수 x filter() -> 람다식으로 변경
def count(num) :
    # 중첩 함수 -> 람다식으로 변환
    def check(x):
        return x % num == 0
    lists = list(filter(lambda x : x % num == 0, range(1, 31)))
    return lists, len(lists)
num=4
lists, counts = count(num)
print(f"{num}의 배수: ", lists)
print(f"{num}의 배수의 개수: ", counts)
# 4의 배수:  [4, 8, 12, 16, 20, 24, 28]
# 4의 배수의 개수:  7



# 실습6. 함수 종합 프로그래밍
weather_data = [
    ["2024-11-20", "서울", 15.2, 0.0],
    ["2024-11-20", "부산", 18.4, 0.0],
    ["2024-11-21", "서울", 10.5, 2.3],
    ["2024-11-21", "부산", 14.6, 1.2],
    ["2024-11-22", "서울",  8.3, 0.0],
    ["2024-11-22", "부산", 12.0, 0.0]
]
def get_temp_avg(data, city):
    temp = [data[i][2] for i in range(0, len(data)) if data[i][1]==city]
    temp_avg = sum(temp) / len(temp)
    return temp_avg

def get_min_max_temp(data, city):
    temp_lists=[data[i][2] for i in range(0, len(data)) if data[i][1]==city]
    return min(temp_lists), max(temp_lists)

def get_rainfall(data, city):
    rainfall_lists=[data[i][3] for i in range(0, len(data)) if data[i][1]==city]
    rainfall_days=len([i for i in rainfall_lists if i > 0])
    return sum(rainfall_lists), rainfall_days

def add_weather_data(date, city, temp, rain):
    global weather_data
    weather_data.append([date, city, float(temp), float(rain)])
    return

def print_data_all(data):
    print("현재 저장된 날씨 데이터:")
    for i in range(0, len(data)):
        print(f"날짜: {data[i][0]}, 도시: {data[i][1]}, 일평균 기온 : {data[i][2]}℃, 강수량: {data[i][3]}mm")
    return

while True :
    print("=========================")
    print("[날씨 데이터 분석 프로그램]")
    print("1. 평균 기온 계산")
    print("2. 최고/최저 기온 찾기")
    print("3. 강수량 분석")
    print("4. 날씨 데이터 추가")
    print("5. 전체 데이터 출력")
    print("6. 종료 ㅡ 강성연")
    user_input = input("원하는 기능의 번호를 입력하세요 : ")
    len_wd = len(weather_data)
    # 프로그램 종료
    if user_input == "6" :
        print("분석 프로그램을 종료합니다.")
        break
    # 1:평균기온 계산 ㅡ get_temp_avg()
    elif user_input == "1":
        input_1 = input("도시 이름을 입력하세요 : ")
        celc_avg = get_temp_avg(weather_data, input_1)
        print (f"{input_1}의 평균 기온 : {celc_avg:.2f}℃")
    # 2:최고/최저 기온 ㅡ get_min_max_temp()
    elif user_input == "2":
        input_2 = input("도시 이름을 입력하세요 : ")
        min_t, max_t = get_min_max_temp(weather_data, input_2)
        print(f"{input_2}의 최고 기온 : {max_t}℃, 최저 기온 : {min_t}℃") 
    # 3:강수량 분석 ㅡ get_rainfall()
    elif user_input == "3":
        input_3 = input("도시 이름을 입력하세요 : ")
        sum_rain, days_rain = get_rainfall(weather_data, input_3)
        print(f"{input_3}의 총 강수량 : {sum_rain}mm")
        print(f"{input_3}의 강수량이 있었던 날(수) : {days_rain}일")
    # 4:데이터추가 ㅡ add_weather_data()
    elif user_input == "4":
        input_4_1 = input("날짜를 입력하세요 (YYYY-MM-DD) : ")
        input_4_2 = input("도시 이름을 입력하세요 : ")
        input_4_3 = input("평균 기온을 입력하세요(℃) : ")
        input_4_4 = input("강수량을 입력하세요(mm) : ")
        add_weather_data(input_4_1, input_4_2, input_4_3, input_4_4)
        print(f"{input_4_2}의 날씨 데이터가 추가되었습니다.")    
    # 5:전체 데이터 출력 ㅡ print_data_all()
    elif user_input == "5":
        print_data_all(weather_data)
    else :
        print("잘못 입력하셨습니다. 원하는 기능의 번호를 입력하세요 : ")
