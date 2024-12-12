#======= for 문 =======
# # 리스트와 for문
# fruits = ["사과", "포도", "바나나", "복숭아"]
# for fruit in fruits:
#     print("과일은 : ",fruit)
# # 과일은 :  사과
# # 과일은 :  포도
# # 과일은 :  바나나
# # 과일은 :  복숭아

# # 합계 구하기
# numbers = [10,20,30,40,50]
# total = 0
# for num in numbers :
#     total += num
# print(f"리스트 값의 합계는 {total}입니다.")     # --> 리스트 값의 합계는 150입니다.

# # 조건문 사용
# number = [1,2,3,4,5,6,7,8,9]
# for num in number :
#     if num % 2 == 0:
#         print(num, end=" ")             # --> 2 4 6 8

# 리스트 내포
# sqaures = [ i**2 for i in range(1,20)]
# print(sqaures)                          # --> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]

# if문과 함께 사용
# even_squares = [ i ** 2 for i in range(1, 10) if i % 2 == 0 ]
# print(even_squares)                       # --> [4, 16, 36, 64]
# even = [ i for i in range(1, 10) if i % 2 == 0 ]
# print(even)                               # --> [2, 4, 6, 8]

# 딕셔너리와 for문
# my_dic = {
#     "name" : "홍길동",
#     "address" : "서울시 은평구",
#     "gender" : "남자",
#     "hobby" : ["런닝","헬스","낚시"]
# } 
# JSON 형태 = 딕셔너리

# key값만 순회
# for i in my_dic :
#     print(i, end=" ")           # --> name address gender hobby 
# print()
# for i in my_dic.keys() :
#     print(i, end=" ")           # --> name address gender hobby
# print()
# for i in my_dic.values() :
#     print(i, end=", ")           # --> 홍길동, 서울시 은평구, 남자, ['런닝', '헬스', '낚시'],
# print()
# for i in my_dic.items() :
#     print(i, end=", ")           # --> 튜플형태 : ('name', '홍길동'), ('address', '서울시 은평구'), ('gender', '남자'), ('hobby', ['런닝', '헬스', '낚시']),
# print()
# for key, value in my_dic.items() :
#     # print(key, value, end=", ")           # --> name 홍길동, address 서울시 은평구, gender 남자, hobby ['런닝', '헬스', '낚시'],
#     print(f"{key} : {value}", end="  /  ")  # --> name : 홍길동  /  address : 서울시 은평구  /  gender : 남자  /  hobby : ['런닝', '헬스', '낚시']  /


# # 실슴. 구구단 만들기
# num = int(input("몇 단을 출력할까요? : "))
# numbers = list(range(1,10))
# for i in numbers :
#     print(f"{num} x {i} = ", num*i)

# print()

# # # 실습. 정수 합 계산
# num = int(input("어디까지 계산할까요? : "))
# total = 0
# sum_num = [total+i   for i in range(1, num+1)   if i % 2 != 0]
# print(f"1부터 {num}까지의 홀수 합 : ", sum(sum_num))


# print()

# # 실습. 평균값 구하기 _ 내 코드
# scores = {
#     "학생1" : [83, 92, 88],
#     "학생2" : [90, 79, 86],
#     "학생3" : [88, 86, 94]
# }
# for key, value in scores.items():
#     mean = sum(value) / len(value)
#     print(f"{key}의 전체과목 평균은 {mean:.3}점 입니다.")

# # 실습. 평균값 구하기 _ 리더님 코드
# students = {
#     "학생1" : {"국어":83, "영어":92, "수학":88},
#     "학생2" : {"국어":90, "영어":79, "수학":86},
#     "학생3" : {"국어":88, "영어":86, "수학":94}
# }
# for student, score in students.items():
#     total = sum(score.values())      #  <---- 세 과목의합계
#     avg = total / len(score)
#     print(f"{student}의 평균은 {avg:.2f}") 
# # 학생1의 평균은 87.67
# # 학생2의 평균은 85.00
# # 학생3의 평균은 89.33


# # 딕셔너리 안에 딕셔너리가 포함될 수 있음
# scores = {
#     "학생1" : {"국어":83, "영어":92, "수학":88},
#     "학생2" : {"국어":90, "영어":79, "수학":86},
#     "학생3" : {"국어":88, "영어":86, "수학":94}
# }
# print(scores.keys())                # --> dict_keys(['학생1', '학생2', '학생3'])
# print(scores.values())              # --> dict_values([{'국어': 83, '영어': 92, '수학': 88}, {'국어': 90, '영어': 79, '수학': 86}, {'국어': 88, '영어': 86, '수학': 94}])
# print(scores.items())               # --> dict_items([('학생1', {'국어': 83, '영어': 92, '수학': 88}), ('학생2', {'국어': 90, '영어': 79, '수학': 86}), ('학생3', {'국어': 88, '영어': 86, '수학': 94})])

# print()
# print(scores['학생1'].keys())                  # --> dict_keys(['국어', '영어', '수학'])
# print(scores['학생1'].values())                # --> dict_values([83, 92, 88])


#======= 이중 for 문 =======
# for i in range(5):
#     for j in range(3):
#         print(f"i : {i}, j : {j}")
#     print()

# 2차원리스트와 이중 for문
# matrix = [
#     [7,2,8,6],
#     [10,4,3,2],
#     [1,12,5,20],
#     [17,13,18,19]
# ]
# for row in matrix:
#     for elem in row : 
#         if elem % 3 == 0 :
#             print(elem, end=" ")            # --> 6 3 12 18 

# 실습. 이중for문 구구단 만들기
# for i in range(2, 10):
#     print(f"[ {i} 단 ]")
#     for j in range(1, 10):
#         print(f"{i} x {j} = {i*j}")
#     print()

# 과제. 자판기 프로그램
# vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']

# while True : 
#     print("사용자 종류를 입력하세요: ")
#     print("1. 소비자")
#     print("2. 주인")
#     print("3. 종료")
#     a = input(" ")
#     # 예외처리
#     if a.isdecimal():
#         if int(a)==1 :
#             a = "소비자"
#         elif int(a)==2 :
#             a = "주인"
#         elif int(a)==3 :
#             a = "종료"
#         else :
#             print("잘 못 입력하셨습니다.")
#     elif a == "종료":
#         break
#     elif a!="소비자" and a!="주인":
#         print("잘 못 입력하셨습니다.")
#     # 소비자인 경우
#     if a == "소비자":
#         b = input('마시고 싶은 음료? ')
#         if vending_machine.count(b)==0:
#             print(f"{b}는 지금 없네요")
#         else :
#             print(f"{b} 드릴게요")
#             vending_machine.pop(vending_machine.index(b))
#             print("남은 음료수: ",vending_machine)
#     # 주인인 경우
#     elif a == "주인":
#         while True :
#             print("할 일 선택")
#             print("1. 추가")
#             print("2. 삭제")
#             c = input(" ")
#             # 예외처리
#             if c.isdecimal():
#                 if int(c)==1 :
#                     c = "추가"
#                 elif int(c)==2 :
#                     c = "삭제"
#                 else :
#                     print("잘 못 입력하셨습니다.")
#             elif c!="추가" and c!="삭제":
#                 print("잘 못 입력하셨습니다.")
#             print("남은 음료수: ",vending_machine)
#             print()
#             # 추가인 경우
#             if c=="추가" :
#                 add = input("추가할 음료수? ")
#                 vending_machine.append(add)
#                 vending_machine.sort()
#                 print("추가 완료")
#                 print("남은 음료수: ",vending_machine)
#                 break
#             # 삭제인 경우
#             elif c=="삭제" :
#                 while True :
#                     d = input("삭제할 음료수? ")
#                     if vending_machine.count(d)==0:
#                         print(f"{d} 은/는 지금 없네요." )
#                         break
#                     else :
#                         vending_machine.remove(d)
#                         print("삭제 완료")
#                         print("남은 음료수: ",vending_machine)
#                         break
#             break
#     print("=====================================")


# 과제. 리더님 코드
# vm = ["게토레이", "게토레이", "레쓰비", "레쓰비", "생수", "생수", "생수", "이프로"]

# while True:
#     user_input=input("사용자를 선택하세요. (1. 소비자, 2. 주인, 3. 종료): ")
#     # 1. 소비자
#     if user_input == ("1" or "소비자") :
#         drink = input("마시고 싶은 음료는? ")
#         if drink in vm: # 있으면 제거
#             vm.remove(drink)
#             print(f"{drink} 드릴게요")
#         else:
#             print("음료수가 없습니다.")
#         print("남은 음료수: ", vm)
#     # 2. 주인
#     elif user_input == ("2" or "주인") :
#         move = input("할 일을 선택하세요 (1. 추가, 2. 삭제) : ")
#         if move == ("1" or "추가"):
#             drink = input("추가할 음료수는? ")
#             vm.append(drink)
#             vm.sort()
#             print("추가 완료")
#         elif move == ("2" or "삭제"):
#             drink = input("삭제할 음료수는? ")
#             if drink in vm :
#                 vm.remove(drink)
#                 print("삭제 완료")
#             else :
#                 print(f"{drink}는 현재 없습니다.")        
#         else:
#             print("값을 잘못 입력하셨습니다..")
#         print("남은 음료수: ", vm)
#     # 3. 종료
#     elif user_input == ("3" or "종료") :
#         print("자판기 프로그램을 종료합니다.")
#         break
#     # 입력값 오류
#     else:
#         print("값을 잘못 입력하셨습니다..")
        
