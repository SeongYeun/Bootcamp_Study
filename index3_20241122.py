#======= 반복문 : for / while =======
#======= while 문 =======
# i=0
# while i<3:
#     print("반복문 ", i)
#     i += 1
# print("종료")

# 합계구하기
# num = 1
# total = 0
# while num <=10 :
#     total += num
#     num += 1
# print(f"1부터 10까지의 합은 {total}입니다.")        # --> 1부터 10까지의 합은 55입니다.

# 입력값 무한 받기
# user_input = ""
# while user_input != "종료" :
#     user_input = input("원하는 값을 입력하세요. 종료하려면 '종료'를 입력하세요 : ")
#     print(f"입력한 값 : {user_input}")
# print("프로그램이 종료되었습니다.")

# 무한루프

# break 문 _1
# while True :
#     dinner = input("오늘 저녁 뭐먹지? ")
#     if dinner=="제육":
#         break
#     print(f"오늘 저녁 메뉴는 {dinner}입니다.")
# print("저녁 메뉴 완료")

# break 문 _2
# count =0
# while True :
#     print(count, end=" ")
#     count += 1
#     if count == 10:
#         break
#  ㄴ--> 0 1 2 3 4 5 6 7 8 9 

# continue 문
# count = 0
# while count <10:
#     count += 1
#     if count % 2 == 0:
#         continue
#     print(count, end=" ")
# # ㄴ--> 1 3 5 7 9 

# 실습. while문 사용하기
while True :
    a = input("양수를 입력하세요  ('종료' 입력 시 프로그램 종료): ")
    
    if str(a).isdecimal() :
        a=int(a)
        if a==0:
            continue
        else :
            count = 1
            total = 0
            while count <= a :
                total += count
                count += 1
            print(f"1부터 {a}까지의 합은 {total}입니다.")
    elif a=="종료":
        print("프로그램을 종료합니다.")
        break
    else :
        print("양수만 입력 하세요")








#======= for 문 =======
