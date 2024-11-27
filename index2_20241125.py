#======= 함수 =======
# 1) 매개변수 O, 리턴값 X
# def say_hello(born, name):
#     age = 2024 - born
#     print(f"{name}님의 나이는 {age}세 입니다.")

# say_hello(2000, "하린")             # --> 하린님의 나이는 24세 입니다.
# say_hello(2001, "민지")             # --> 민지님의 나이는 23세 입니다.

# # 곱셈함수
# def gugudan(dan, end):
#     print(f"[ {dan}단 ]")
#     for i in range(1, end+1):
#         print(f"{dan} x {i} = {dan * i}")

# gugudan(4, 3)
# # [ 4단 ]
# # 4 x 1 = 4
# # 4 x 2 = 8
# # 4 x 3 = 12


# 2) 결과값이 있는 함수 (리턴값 O)
# def calc_sum(num1, num2):
#     total = 0
#     for i in range(num1, num2+1):
#         total += i
#     return total
# result = calc_sum(4, 37)
# print(result)                       # --> 697

# 
# def fruits():
#     return ["사과", "바나나", "복숭아"]
# print(fruits())                         # --> ['사과', '바나나', '복숭아']

# def students():
#     return {
#         "name" : "홍길동",
#         "age" : 20,
#         "major" : "컴퓨터공학"
#     }
# print(students())                       # --> {'name': '홍길동', 'age': 20, 'major': '컴퓨터공학'}


# # 여러 개의 리턴값이 있는 함수정의
# def get_return():
#     arr = ["사과", "바나나"]
#     dic = {
#         "name" : "홍길동",
#         "age" : 20
#     }
#     num = 30
#     return arr, dic, num
# arrs, dicts, nums = get_return()
# print(arrs)         # --> ['사과', '바나나']
# print(dicts)        # --> {'name': '홍길동', 'age': 20}
# print(nums)         # --> 30

# 실습1
# def sum_product (num1, num2):
#     if num1 == num2 :
#         result = num1 * num2
#         print(f"결과(곱) : {result}")
#     else :
#         result = num1 * num2
#         print(f"결과(합) : {result}")

# sum_product(2,5)                        # --> 결과(합) : 10
# sum_product(4,4)                        # --> 결과(곱) : 16


# 실습2
# def delivery_charge(name, price):
#     total = 0
#     if price < 20000 :
#         total = price + 2500
#     else :
#         total = price
#     print(f"{name} 가격: {total:,}원")

# delivery_charge("상품1", 30000)         # --> 상품1 가격: 30,000원
# delivery_charge("상품2", 15000)         # --> 상품2 가격: 17,500원

# 매개변수로 리스트 전달
# def times(num):
#     return [i ** 2 for i in num]
# arr = [1,2,3,4,5]
# print(times(arr))                         # --> [1, 4, 9, 16, 25]


# 실습3
# 1) check_machine : 남은 음료수를 확인할 수 있는 함수
def check_machine(drink_list) :
    return drink_list
# 2) is_drink : 음료수가 있는지 확인하는 함수
def is_drink(drink_list, drink_name):
    if drink_name in drink_list:
        return True
    else :
        return False
# 3) add_drink : 음료수를 추가하는 함수
def add_drink(drink_list, drink_name):
    result = drink_list.append(drink_name)
    print(f"{drink_name} 음료수 추가 완료")
    result.sort()
    return result
# 4) remove_drink : 음료수를 제거하는 함수
def remove_drink(drink_list, drink_name):
    result = drink_list
    if drink_name not in drink_list:
        print(f"{drink_name}가 없습니다.")
    else : 
        result = drink_list.remove(drink_name)
        print(f"{drink_name} 음료수 삭제 완료")
    return result

# 5) 함수 이용한 자판기 프로그램 - 리더님 코드
vm = ["게토레이", "게토레이", "레쓰비", "레쓰비", "생수", "생수", "생수", "이프로"]

def check_machine():
    print("남은 음료수: ", vm)
def is_drink(drink):
    return drink in vm
def add_drink(drink):
    vm.append(drink)
    vm.sort()
    print("추가 완료")
def remove_drink(drink, user):
    vm.remove(drink)
    if user == ("1" or "소비자") :
        print(f"{drink} 드릴게요")
    else :
        print("삭제 완료")


while True:
    user_input=input("사용자를 선택하세요. (1. 소비자, 2. 주인, 3. 종료): ")
    # 1. 소비자
    if user_input == ("1" or "소비자") :
        drink = input("마시고 싶은 음료는? ")
        if is_drink(drink):     # drink in vm:    # 있으면 제거
            remove_drink(drink, user_input)
        else:
            print("음료수가 없습니다.")
        check_machine() # print("남은 음료수: ", vm)
    # 2. 주인
    elif user_input == ("2" or "주인") :
        move = input("할 일을 선택하세요 (1. 추가, 2. 삭제) : ")
        if move == ("1" or "추가"):
            drink = input("추가할 음료수는? ")
            add_drink(drink)
        elif move == ("2" or "삭제"):
            drink = input("삭제할 음료수는? ")
            if is_drink(drink):      # drink in vm :
                remove_drink(drink, user_input)
            else :
                print(f"{drink}는 현재 없습니다.")        
        else:
            print("값을 잘못 입력하셨습니다..")
        check_machine() # print("남은 음료수: ", vm)
    # 3. 종료
    elif user_input == ("3" or "종료") :
        print("자판기 프로그램을 종료합니다.")
        break
    # 입력값 오류
    else:
        print("값을 잘못 입력하셨습니다..")