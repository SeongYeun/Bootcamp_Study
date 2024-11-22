#======= 리스트 (list) =======
#==== 1) 리스트 기초
# number = [1, 2, 3, "Hello", "Python"]
# print(number[3])                # --> Hello
# print(number[0])                # --> 1

# text = "Hello, Python"
# text = list(text)
# print(text)                     # --> ['H', 'e', 'l', 'l', 'o', ',', ' ', 'P', 'y', 't', 'h', 'o', 'n']

#==== 2) 리스트 슬라이싱
# shop = ["반팔", "청바지", "이어폰", ["무선키보드", "기계식키보드"]]
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
# num = [3, 1, 5, 2]
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

# QnA
# print(sorted(x))   --> sorted()함수는 원본을 수정하지 않기 때문에 출력이 가능
# print(x.sort())    --> 오류 발생 -- 원인 : 원본데이터를 변경하는 메서드를 바로 print할 수 없음

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
# rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
# print("1. 2번 인덱스 값 출력 : ", rainbow[2])
# #  ㄴ--> yellow
# print("2. 알파벳 순서로 정렬한 값 출력 : ", sorted(rainbow))
# #  ㄴ--> ['blue', 'green', 'indigo', 'orange', 'purple', 'red', 'yellow']
# rainbow.append("white")
# print("3. 좋아하는 색 맨 마지막에 추가하기 : ", rainbow)
# #  ㄴ--> ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple', 'white']
# del rainbow[3:7]
# print("4. 3~6번째 값 삭제하기 : ", rainbow)
# #  ㄴ--> ['red', 'orange', 'yellow', 'white']



#======= 2차원 리스트 (행렬) =======
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# #==== 1) 함수이용
# # 요소 7 출력
# print(matrix[2][0])
# # 요소 추가
# matrix[1] = matrix[1] + [99]
# print(matrix)
# #  ㄴ--> [[1, 2, 3], [4, 5, 6, 99], [7, 8, 9]]
# # 행 추가
# matrix = matrix + [[10, 11, 12]]   # 2차원 배열이므로 []를 두 개 겹쳐서 사용
# print(matrix)
# #  ㄴ--> [[1, 2, 3], [4, 5, 6, 99], [7, 8, 9], [10, 11, 12]]
# # 요소 수정
# matrix[0][0] = 100
# matrix[1][1] = 500
# print(matrix)
# #  ㄴ--> [[100, 2, 3], [4, 500, 6, 99], [7, 8, 9], [10, 11, 12]]
# # 행 삭제
# del matrix[2]
# print(matrix)
# #  ㄴ--> [[100, 2, 3], [4, 500, 6, 99], [10, 11, 12]]
# # 행 개수
# rows = len(matrix)
# print(rows)
# #  ㄴ--> 3
# # 열 개수
# cols = len(matrix[0])
# print(cols)
# #  ㄴ--> 3
# #==== 2) 메서드 이용
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# # 요소 추가
# matrix[0].append(10)
# print(matrix)
# #  ㄴ--> [[1, 2, 3, 10], [4, 5, 6], [7, 8, 9]]
# # 행 추가 : .insert() / .append() / .extend()
# matrix.append([10, 11, 12])
# print(matrix)
# #  ㄴ--> [[1, 2, 3, 10], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
# matrix[1].insert(1, 100)
# print(matrix)
# #  ㄴ--> [[1, 2, 3, 10], [4, 100, 5, 6], [7, 8, 9], [10, 11, 12]]
# matrix.insert(2, ["안녕하세요", "반갑습니다", "어서오세요"])
# print(matrix)
# #  ㄴ--> [[1, 2, 3, 10], [4, 100, 5, 6], ['안녕하세요', '반갑습니다', '어서오세요'], [7, 8, 9], [10, 11, 12]]
# matrix[0].extend([11, 12])
# print(matrix)
# #  ㄴ--> [[1, 2, 3, 10, 11, 12], [4, 100, 5, 6], ['안녕하세요', '반갑습니다', '어서오세요'], [7, 8, 9], [10, 11, 12]]



#======= 튜플(Tuple) =======
# # t1 = (1)        # 오류
# t1 = (1,)
# print(t1[0])           # --> 1
# t2 = (1, 2, 3, 4, 5, 3, 4, 4, 3, 3, 3)
# print(t2.count(3))     # --> 5
# t3 = 1,2,3
# print(t3.index(2))     # --> 1
# t4 = ('a', 'b', 'c', ("안녕", "감사"))
# print(t4[3][0])        # --> 안녕
# print(len(t4))         # --> 4
# print('d' in t4)       # --> False
# # t1.append(1)           # 오류



