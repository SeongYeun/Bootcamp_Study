#======= 셋(Set) =======
# s1 = {1,1,1,1,1,1,1,1, 2}
# print(s1)               # --> {1, 2}
# s2 = ['안녕', '잘가', 'Hi', 'Hi', '안녕']
# print(set(s2))          # --> {'Hi', '안녕', '잘가'}


# s1 = {1, 2, 3, 3, 4}
# print(s1)                 # --> {1, 2, 3, 4}
# s1.add(5)
# print(s1)                 # --> {1, 2, 3, 4, 5}
# s1.update([6,7,8,9,10])
# print(s1)                 # --> {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# s1.remove(3)
# print(s1)                 # --> {1, 2, 4, 5, 6, 7, 8, 9, 10}
# s1.discard(9)
# print(s1)                 # --> {1, 2, 4, 5, 6, 7, 8, 10}
# # s1.remove(11)
# # print(s1)                 # --> 오류 (없는 원소 삭제 명령문이라서 오류)
# s1.discard(11)
# print(s1)                 # --> {1, 2, 4, 5, 6, 7, 8, 10}
#                           # --> 아무 오류도 발생하지 않음
# s1.clear()
# print(s1)                 # --> set()  ㅡ 빈 set을 의미함


# # set 연산 
# # 1) 합집합 : | / .union()
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# s3_1 = s1 | s2
# s3_2 = s1.union(s2)
# print(s3_1)                 # --> {1, 2, 3, 4, 5, 6, 7, 8}
# print(s3_2)                 # --> {1, 2, 3, 4, 5, 6, 7, 8}

# # 2) 교집합 : & / .intersection()
# s4_1 = s1 & s2
# s4_2 = s1.intersection(s2)
# print(s4_1)                 # --> {4, 5}
# print(s4_2)                 # --> {4, 5}

# # 3) 차집합 : - / .difference()
# s5_1 = s1 - s2
# s5_2 = s1.difference(s2)
# print(s5_1)                 # --> {1, 2, 3}
# print(s5_2)                 # --> {1, 2, 3}
# s5_3 = s2 - s1
# s5_4 = s2.difference(s1)
# print(s5_3)                 # --> {8, 6, 7}
# print(s5_4)                 # --> {8, 6, 7}


#======= 딕셔너리(Dictionary) =======
# # 1) 딕셔너리 생성
# dict1 = {}
# dict2 = dict()
# dict1 = {
#     "name" : "홍길동", 
#     "age" : 20,
#     "city" : "서울",
#     "hobby" : ["런닝", "등산", "헬스"]
# }
# print(dict1)                # --> {'name': '홍길동', 'age': 20, 'city': '서울', 'hobby': ['런닝', '등산', '헬스']}
# dict2 = dict(name="홍길동", age=20)
# print(dict2)                # --> {'name': '홍길동', 'age': 20}
# print(dict1['name'])        # --> 홍길동
# print(dict1['hobby'][2])        # --> 헬스

# # 2) 값 수정
# dict1["age"]=21
# print(dict1)                # --> {'name': '홍길동', 'age': 21, 'city': '서울', 'hobby': ['런닝', '등산', '헬스']}  

# # 3) 값 추가
# dict1["birthday"]=20001011
# print(dict1)                # --> {'name': '홍길동', 'age': 21, 'city': '서울', 'hobby': ['런닝', '등산', '헬스'], 'birthday': 20001011}
# dict1['hobby'] = "캠핑"     # 기존 값들이 제거되고 '캠핑'만 대입됨
# dict1['hobby'] = ['런닝', '등산', '헬스', "캠핑"]     # --> {'name': '홍길동', 'age': 21, 'city': '서울', 'hobby': ['런닝', '등산', '헬스', '캠핑'], 'birthday': 20001011}
# print(dict1)                # --> 
# del dict1['birthday']
# print(dict1)                # --> {'name': '홍길동', 'age': 21, 'city': '서울', 'hobby': ['런닝', '등산', '헬스', '캠핑']}

# # 4) 딕셔너리 메서드
# # : .get('key')  -> 해당 key의 value 반환
# fruits = {
#     "apple" : "사과",
#     "banana" : "바나나"
# }
# print(fruits.get('apple'))      # --> 사과
# print(fruits.get('peach'))      # --> None
# print(fruits.get('peach', '복숭아'))      # --> 복숭아

# # : 여러요소 추가/키조회/값조회/전체조회/삭제
# fruits.update({
#     'grapes' : '포도',
#     'melon' : '멜론'
# })
# print(fruits)                   # --> {'apple': '사과', 'banana': '바나나', 'grapes': '포도', 'melon': '멜론'}
# print(fruits.items())           # --> dict_items([('apple', '사과'), ('banana', '바나나'), ('grapes', '포도'), ('melon', '멜 론')])
# print(fruits.keys())            # --> dict_keys(['apple', 'banana', 'grapes', 'melon'])
# print(fruits.values())          # --> dict_values(['사과', '바나나', '포도', '멜론'])
# fruits.clear()
# print(fruits)                   # --> {}


# # 실습. 성적관리
# # 1) 학생 딕셔너리 생성
# student = {}
# # 2) 학생 딕셔너리 데이터 추가
# student = {
#     "Alice" : 85,
#     "Bob" : 90,
#     "Charlie" : 95
# }
# # 3) "David" 학생의 점수로 80을 추가
# student['David'] = 80
# # 4) "Alice" 학생의 점수를 88로 수정
# student['Alice'] = 88
# # 5) "Bob" 학생을 딕셔너리에서 삭제
# del student['Bob']


#======= 내장함수 =======
# # sum()
# numbers = [1,2,3,4,5]
# print(sum(numbers))             # --> 15
# score = {"A" : 90, "B" : 80, "C" : 85}
# print(sum(score.values()))      # --> 255

# range()

# max() / min()

# len()

# zip() : 병렬의 튜플(변경불가)을 리스트 묶어주는 함수
# names = ['Alice', 'Bob', 'Charlie', 'David']
# scores = [85, 90, 88, 95]
# zipped = zip(names, scores)
# print(zipped)                   # --> <zip object at 0x00000227093736C0>
# zipped = list(zip(names, scores))
# print(zipped)                   # --> [('Alice', 85), ('Bob', 90), ('Charlie', 88), ('David', 95)]

