"""
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

print((lambda x : x+1)(1))
print()
print((lambda x: x*3)(2))
print()
print((lambda x: x*x*x)(4))
print()

print((lambda x, y: x+y)(3, 4))
print()

print((lambda x, y: x-y)(3, 4))
print()

print((lambda x, y: x*y)(3, 4))
print()

print((lambda x, y: x/y)(3, 4))
print()

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

print("콜백(callback) 함수")

def call_10(func):
    for _ in range(10):
        func()

def hello():
    print("안녕하세요")

hello2 = lambda: print("반갑습니다.")

# 호출
call_10(hello)
print()

print()
call_10(hello2)
"""
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# map(함수명, 시퀀스)
numbers = [1, 2, 3, 4]
squared = (lambda x: x**2)(4)
print(squared)
# 16
squared = map(lambda x: x**2, numbers)
print(squared)
# <map object at 0x000001C9BA0E6B00>        <-- 결과값들의 주소값을 리턴
print(list(squared))
# [1, 4, 9, 16]

squared = map(lambda x: x**2, [2,5,7])
print(list(squared))
# [4, 25, 49]

result = list(map(lambda x: x * 2 if x % 2 != 0 else x, [1,2,3,4,5]))
print(result)
# [2, 2, 6, 4, 10]

def even_or_odd(number):
    return "짝수" if number % 2 == 0 else "홀수"
print(even_or_odd(10))      # --> 짝수
print(even_or_odd(7))       # --> 홀수

even_numbers = list(filter(lambda x : True if x%2==0 else False, [1,2,3,4,5,6]))
print(even_numbers)
# [2, 4, 6]

words = ['apple', 'banana', 'cherry']
print([(lambda x : len(x))(x) for x in words])
# [5, 6, 6]


