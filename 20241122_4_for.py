#======= for 문 =======
# 1) for 문 w/ range()함수
# for i in range(10) :
#     print(i, end=" ")           # --> 0 1 2 3 4 5 6 7 8 9 
# print()
# for i in range(3, 9) :
#     print(i, end=" ")           # --> 3 4 5 6 7 8
# print()
# for i in range(1, 100, 12) :
#     print(i, end=" ")           # --> 1 13 25 37 49 61 73 85 97
# print()


# 2) for 문 w/ list
# fruits = ["사과","바나나","포도","체리"]
# for fruit in fruits:
#     print(fruit, end=" | ")         # --> 사과 | 바나나 | 포도 | 체리 | 

# 합계 구하기
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# total = 0
# for num in numbers :
#     total += num
# print(f"합계는 {total}입니다.")         # --> 합계는 55입니다.

# for문 + 조건문
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 != 0 :
        print(num, end=" ")             # --> 1 3 5 7 9 

 


