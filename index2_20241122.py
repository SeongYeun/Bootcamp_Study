#======= 조건문 : if / else / elif =======
# age = 21
# if age <20 :
#     print("미성년자 입니다")           # --> False로 출력없음

# print(f"나이는 {age}입니다")           # --> 나이는 21입니다


# # 실습. if문
# # 1) 비밀번호
# pwd = input("비밀번호를 입력하세요 : ")
# if pwd == "abc123" :
#     print("비밀번호가 맞습니다.\n")

# # 2) 짝수
# a = int(input("숫자를 입력하세요 : "))
# if ((a % 2) == 0)  :
#     print("짝수입니다.\n")


# # 실습. if ~ else
# # 1) 비밀번호
# pwd = input("비밀번호를 입력하세요 : ")
# if pwd == "abc123" :
#     print("비밀번호가 맞습니다.\n")
# else :
#     print("비밀번호가 틀렸습니다.\n")

# # 2) 짝수
# a = int(input("숫자를 입력하세요 : "))
# if a % 2 == 0  :
#     print("짝수입니다.\n")
# else :
#     print("홀수입니다.\n")

# if ~ elif ~ else
# age = int(input("나이를 입력하세요 : "))

# if age < 20 :
#     print("10대 입니다.")
# elif age < 30 :
#     print("20대 입니다.")
# elif age < 40 :
#     print("30대 입니다.")
# elif age < 40 :
#     print("30대 입니다.")
# elif age < 50 :
#     print("40대 입니다.")
# else :
#     print("50대 이상 입니다.")


# # 실습. elif
# score = int(input("점수를 입력하세요 : "))
# if score >= 90 :
#     print("학점 : A")
# elif score >= 80 :
#     print("학점 : B")
# elif score >= 70 :
#     print("학점 : C")
# elif score >= 60 :
#     print("학점 : D")
# else :
    # print("학점 : F")


#======= 중첩조건문 =======
# # 실습. 중첩 조건문
# age = int(input("나이를 숫자로 입력해주세요 : "))
# pay = input("결제방법을 입력해주세요 (현금 또는 카드): ")
# if age <0 :
#     print("0 이상의 나이 값을 입력하세요")
# elif age >= 75 | age <8:
#     print(f"{age}세의 요금은 무료 입니다.")
# elif age < 14 :
#     print(f"{age}세의 요금은 450원 입니다.")
# elif age < 20 :
#     if pay == "카드" :
#         print(f"{age}세의 {pay}요금은 720원 입니다.")
#     else :
#         print(f"{age}세의 {pay}요금은 1000원 입니다.")
# else :
#     if pay == "카드" :
#         print(f"{age}세의 {pay}요금은 1200원 입니다.")
#     else :
#         print(f"{age}세의 {pay}요금은 1300원 입니다.")

# 
# age = int(input("나이를 숫자로 입력해주세요 : "))
# if age >0 :
#     method = input("결제방법을 입력해주세요 (현금 또는 카드): ")
#     if method == "카드" :
#         if age <8:
#             price = "무료"
#         elif age <14:
#             price = "450원"
#         elif age <20:
#             price = "720원"
#         elif age <75:
#             price = "1200원"
#         else:
#             price = "무료"
#     elif method == "현금" :
#         if age <8:
#             price = "무료"
#         elif age <14:
#             price = "450원"
#         elif age <20:
#             price = "1000원"
#         elif age <75:
#             price = "1300원"
#         else:
#             price = "무료"
# else :
#     price = None
#     print("카드 또는 현금만 입력하세요.")
# if price :
#     print(f"{age}세의 {method}요금은 {price}입니다.")

# 삼항연산자
# age = int(input("나이를 입력하세요 : "))
# message = "20대입니다." if age < 30 & age >=20 else "20대가 아닙니다."
# print(message)
# message = "20대입니다." if age < 30 & age >=20 else "30대가 아닙니다." if age < 40 & age >=30 else "20대도 30대도 아닙니다." 
# print(message)



# 조건문 + in 연산자
fruit = input("과일을 한글로 입력하세요 : ")
if fruit in ["사과", "바나나", "복숭아"] :
    print(f"{fruit}은(는) 과일에 포함되어 있습니다.")
else :
    print("존재하지 않는 과일입니다.")



# 실습. in 연산자 활용
