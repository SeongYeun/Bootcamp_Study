# 예외처리 ㅡ try + except + (else + finally)

# try:
#     x = int(input("숫자를 입력하세요: "))
#     result = 10 / x
# except ZeroDivisionError as e:              # e는 변수임, 보통 e, err, error 로 사용됨
#     print("예외 메시지: ", e)
# except ValueError as e: 
#     print("예외 메시지: ", e)
# else:
#     print(f"result: {result}")
# finally:
#     print("프로그램이 종료됩니다.")


# try:
#     x = int(input("숫자를 입력하세요: "))
#     result = 10 / x
# except (ZeroDivisionError, ValueError) as e:        # 여러 에러코드 출력이 같으면 이렇게 묶어서 처리할 수 있음
#     print("예외 메시지: ", e)
# else:
#     print(f"result: {result}")
# finally:
#     print("프로그램이 종료됩니다.")

# # 강제오류 발생시킴
# raise Exception("예외처리")

def divide(a, b):
    if b == 0 :
        raise ZeroDivisionError("0으로 나눌 수 없습니다.")
    return a / b

try:
    result = divide(10, 2)
except ZeroDivisionError as e:
    print("예외 발생: ", e)         # 예외 발생:  division by zero
                                   # 예외 발생:  0으로 나눌 수 없습니다.  <-- raise 조건문 추가 후
else:
    with open("result_try_except.txt",'w', encoding='utf-8') as file:
        file.write(f"결과: {result}")
