# 출력 : print()
"""
print("안녕하세요")
print("Hello", "Python")
print("Hello", "Python", sep="")
print("Hello", "Python", sep="__")
print("안녕하세요", end=" ! ")
print("저는 OOO입니다.")
print(1234567)
"""

# 입력 : input() ㅡ 입력받은 값=문자열
# singer = input("좋아하는 가수는? ")
# print("좋아하는 가수는 ", singer, "입니다.")


# 주석
# 라인 1줄 : #  = Ctrl+/
# 한 줄 주석에 사용, 코드 뒤에서도 사용가능
# 라인 2+줄 : """ 여러라인 주석 """


# 들여쓰기 ㅡ 문법 강제사항


# 객체 ㅡ 숫자, 문자(열), 리스트, 딕셔너리 / 매서드 묶음 등등
# 가변성 : list, dict, set > 값 수정O
# qnfqustjd : 숫자, 문자열, tuple > 값 수정X & 값 변경시 새로운 객체 생성


# 변수 값 할당 = RAM에 값 저장 w/ index
# x = 10
# print("x : ", x)
# y, z = 3.14, "안녕하세요"
# print("y : ", y)
# print("z : ", z)
# # 재할당
# x = "반값습니다"
# print("before x : ", x, id(x))
# x = 10
# print("after x : ", x, id(x))

# a = [1, 2, 3]
# print("before a : ", a, id(a))
# a.append(4)
# print("after a : ", a, id(a))


# 키워드
# import keyword
# print(keyword.kwlist)  # 식별자(변수명) 사용불가


# 산술연산자
# x = 48/2(9+3)   # * 연산자가 없어서 오류 발생함
# print("x : ", x)
# // : 몫
# % : 나머지


# 연산자 우선순위 퀴즈
# x = 100 -2 / 7  + 9 *3   # 126.71428571428571
# print(x)
# x = (100 -2) / 7  + 9 *3  # 41.0
# print(x)


# 복합대입연산자 : 일반연산자= : +=, -=, *=, /=, //=, %=, **=
# num = 5
# print("num >>> ", num)
# num += 5
# print("num+=5 >>> ",num)
# num -= 2
# print("num-=2 >>> ",num)
# num *= 6
# print("num*=6 >>> ",num)
# num /= 2
# print("num/=2 >>> ",num)
# num //= 5
# print("num//=5 >>> ",num)
# num %= 3
# print("num%=3 >>> ",num)
# num = 4
# num **= 4
# print("num**=4 >>> ",num)


# 비교연산자
# num1 = 10
# num2 = 20
# num3 = "10"
# print(num1 > num2)   # F
# print(num1 < num2)   # T
# print(num1 == num3)  # F
# print(num1 >= 10)    # T
# print(num2 <= 19)    # F
# print(num1 != num3)  # T


# 논리연산자

# in 연산자
# a = "Hello World"
# print("H" in a)  # T
# print('h' in a)  # F
# print('a' in a)  # F
# print('l' in a)  # T
# a = ['q', 'w', 'e', 'r', 'w']
# print('a' in a)  # F
# print('q' in a)  # T
# print('w' in a)  # T
# print('j' in a)  # F


# 실습 - 연산자 연습
# a = 27
# b = a%2 == 0
# print(a, "이/가 True면 짝수, False면 홀수 -> 결과 : ", b)

