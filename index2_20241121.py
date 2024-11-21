#======= 리스트 (list) =======
#==== 1) 리스트 기초
# number = [1, 2, 3, "Hello", "Python"]
# print(number[3])                # --> Hello
# print(number[0])                # --> 1

# text = "Hello, Python"
# text = list(text)
# print(text)                     # --> ['H', 'e', 'l', 'l', 'o', ',', ' ', 'P', 'y', 't', 'h', 'o', 'n']

#==== 2) 리스트 슬라이싱
shop = ["반팔", "청바지", "이어폰", ["무선키보드", "기계식키보드"]]
# print(shop[:2])                 # --> ['반팔', '청바지']
# print(shop[3])                  # --> ['무선키보드', '기계식키보드']
# print(shop[-2])                 # --> 이어폰
# print(shop[3][0])               # --> 무선키보드

#==== 3) 리스트 값 수정
# shop[0]="긴팔"
# print(shop)                      # --> ['긴팔', '청바지', '이어폰', ['무선키보드', '기계식키보드']]
# # shop[100] = "신발"                 # --> 오류
# del shop[0]
# print(shop)                      # --> ['청바지', '이어폰', ['무선키보드', '기계식키보드']]
# del shop[2:]
# print(shop)                      # --> ['청바지', '이어폰']
# # 리스트 연산
# a = [1, 2, 3]
# b = ["안녕하세요", "반갑습니다"]
# print(a + b)                    # --> [1, 2, 3, '안녕하세요', '반갑습니다']
# print(b * 3)                    # --> ['안녕하세요', '반갑습니다', '안녕하세요', '반갑습니다', '안녕하세요', '반갑습니다']

#==== 4) 리스트 값 정렬
#  : sorted(list, reverse=T/F)
num = [3, 1, 5, 2]
# num_asc = sorted(num)
# print(num_asc)                      # --> [1, 2, 3, 5]
# num_desc = sorted(num, reverse=True)
# print(num_desc)                     # --> [5, 3, 2, 1]
# print(num)                          # --> [3, 1, 5, 2]

#  : list.sort(reverse=T/F)   /  list.reverse()
# num.sort()
# print(num)                          # --> [1, 2, 3, 5]
# korean = ["강", "이", "박", "최", "김"]
# korean.sort(reverse=True)
# print(korean)                        # --> ['최', '이', '박', '김', '강']
# korean.sort()
# print(korean)                        # --> ['강', '김', '박', '이', '최']
# alphabet = ['b', 'c', 'a', 'd']
# alphabet.reverse()
# print(alphabet)                      # --> ['d', 'a', 'c', 'b']

#==== 5) 리스트 위치(index) 찾기
# : .index("찾는값")
# alphabet = ['d', 'a', 'c', 'b']
# print(alphabet.index('c'))              # --> 2


#==== 6) 리스트 요소 추가/삭제 메서드
# a = ['a', 'b', 'c', "안녕", "Hi"]
# a.append("Good")
# print(a)                                # --> ['a', 'b', 'c', '안녕', 'Hi', 'Good']
# a.pop()
# print(a)                                # --> ['a', 'b', 'c', '안녕', 'Hi']
# a.pop(2)
# print(a)                                # --> ['a', 'b', '안녕', 'Hi']
# a.remove("안녕")
# print(a)                                # --> ['a', 'b', 'Hi']
# a.insert(2, "잘가")
# print(a)                                # --> ['a', 'b', '잘가', 'Hi']
# a.clear()
# print(a)                                # --> []

# : .count('찾는값')
# x = ['q', 'w', 'e', 'e', 'r', 'w']
# print(x.count('w'))                     # --> 2


# 실습. 리스트 연습문제
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
print("1. 2번 인덱스 값 출력 : ", rainbow[2])
print("2. 알파벳 순서로 정렬한 값 출력 : ", sorted(rainbow))
rainbow.append("white")
print("3. 좋아하는 색 맨 마지막에 추가하기 : ", rainbow)
rainbow.pop(6)
rainbow.pop(5)
rainbow.pop(4)
rainbow.pop(3)
print("4. 3~6번째 값 삭제하기 : ", rainbow)