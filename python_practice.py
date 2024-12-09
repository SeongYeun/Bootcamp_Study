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



"""


# ※  리스트  vs  배열(numpy)  vs  데이터프레임(pandas) ㅡ 2차원 배열 기준

# 2차원 배열 정의 (변수 할당)
# 1) 리스트 (2차원)
list_table = [[1, "a", True], 
              ["b", "4", 10],
              [False, [7, "c"], 0]]

# >>> 출력결과 ㅡ 모든 요소가 한 줄로 나열 (각 요소간 ,로 구분됨)
# [[1, 'a', True], ['b', '4', 10], [False, [7, 'c'], 0]] 


# 2) 배열(numpy) ㅡ 모든 요소의 자료형이 동일해야 함
import numpy as np
np_array = np.array([[2, 10, 5<=7],
                     [1.2, 5, 7],
                     [3, np.pi, 0]])

# >>> 출력결과 ㅡ 행과 열에 맞춰 요소가 출력됨 (각 요소간 탭으로 구분됨)
# [[ 2.         10.          1.        ]
#  [ 1.2         5.          7.        ]
#  [ 3.          3.14159265  0.        ]]


# 3) 데이터프레임(pandas)
import pandas as pd
pd_df = pd.DataFrame({
    "name" : ["Alice","Bob", "Charlie"],
    "age" : [34, 27, 42],
    "country" : ["USA", "Spain", "Canada"]},
    index=["A", "B", "C"])
# print(pd_df)
# #       name  age country
# # A    Alice   34     USA
# # B      Bob   27   Spain
# # C  Charlie   42  Canada
data = {
    "name" : ["Alice","Bob", "Charlie"],
    "age" : [34, 27, 42],
    "country" : ["USA", "Spain", "Canada"]}
data_1 = pd.DataFrame({
    "name" : ["Alice","Bob", "Charlie"],
    "age" : [34, 27, 42],
    "country" : ["USA", "Spain", "Canada"]})

df_wo_index = pd.DataFrame(data)
# print(df_wo_index)        # 오류코드 : ValueError: If using all scalar values, you must pass an index  --> DataFrame으로 정의시 index를 지정해줘야 함
# print("data_1 : \n",data_1)
# # data_1 : 
# #        name  age country
# # 0    Alice   34     USA
# # 1      Bob   27   Spain
# # 2  Charlie   42  Canada
# df_with_index = pd.DataFrame(data, index=[0, 1, 2])
# print(df_with_index)
# #       name  age country
# # 0    Alice   34     USA
# # 1      Bob   27   Spain
# # 2  Charlie   42  Canada


# >>> 출력결과 ㅡ 행과 열에 맞춰 요소가 출력됨
#               (각 요소간 탭으로 구분되고 대괄호[]가 없음, index 번호가 자동부여됨)
#       name  age country
# A    Alice   34     USA
# B      Bob   27   Spain
# C  Charlie   42  Canada


# 출력물 비교 
# print(list_table,"\n")
# print(np_array,"\n")
# print(pd_df,"\n")




############################ 요소 접근 ############################
# 1. 객체(변수명)에 대괄호[ ]를 열면 요소에 접근하는 것
#       (예외 : 데이터프레임은 컬럼 접근 방식이 됨)
# 2. 대괄호 안에 index 번호로 접근하는 것이 기본
# 3. index는 왼쪽에서는 0부터 시작, 오른쪽에서는 -1부터 시작
##################################################################

# 1) 행 전체 / 열 전체
list_table = [[1,    "a",       True],  # <-- list_table[0]  /  list_table[-3]
              ["b",  "4",       10],    # <-- list_table[1]  /  list_table[-2]
              [False, [7, "c"], 0]]     # <-- list_table[2]  /  list_table[-1]
#                               ㄴ> [i[2] for i in list_table]
#                      ㄴ> [i[1] for i in list_table]
#              ㄴ> [i[0] for i in list_table]

# print([i[0] for i in list_table])

np_array = np.array([[2,    10,     5<=7],     # <-- np_array[0]  /  np_array[-3]
                     [1.2,  5,      7],        # <-- np_array[1]  /  np_array[-2] 
                     [3,    np.pi,  0]])       # <-- np_array[2]  /  np_array[-1] 
#                                   ㄴ> [i[2] for i in np_array]
#                            ㄴ> [i[1] for i in np_array]
#                     ㄴ> [i[0] for i in np_array]
# print(np_array[2])

# pd_df 
#       name  age country
# A    Alice   34     USA     # <-- pd_df.iloc[0]  /  pd_df.loc["A"]
# B      Bob   27   Spain     # <-- pd_df.iloc[1]  /  pd_df.loc["B"]
# C  Charlie   42  Canada     # <-- pd_df.iloc[2]  /  pd_df.loc["C"]
#                 ㄴ> pd_df["country"]  / pd_df.iloc[:, 2]  /  pd_df.loc[:, "country"]
#            ㄴ> pd_df["age"]           / pd_df.iloc[:, 1]  /  pd_df.loc[:, "age"]
#     ㄴ> pd_df["name"]                 / pd_df.iloc[:, 0]  /  pd_df.loc[:, "name"]

# tip) .iloc와 .loc는 행기반 접근방식이라 행 인덱싱값이 필수로 포함되어야 함




# 2) 일부 요소에 접근(추출)
# 방법 1) 리스트, 베열 ㅡ 주로 행 전체 또는 열 전체 접근 후 내부 요소 인덱싱을 한번 더 하는 방식
# 방법 2) 데이터프레임 ㅡ 주로 행과 열의 인덱싱의 교차점으로 지정하는 방식 (.iloc 또는 .loc 사용)

# (1) 3행 2열 요소 접근
list_table = [[1,    "a",       True],
              ["b",  "4",       10],
              [False, [7, "c"], 0]]     # <-- list_table[2][1]  /  list_table[-1][-2]
#                      ㄴ> [i[1] for i in list_table][2]

np_array = np.array([[2,    10,     5<=7],
                     [1.2,  5,      7],
                     [3,    np.pi,  0]])       # <-- np_array[2][1]  /  np_array[-1][-2] 
#                            ㄴ> [i[1] for i in np_array]

# pd_df 
#       name  age country
# A    Alice   34     USA
# B      Bob   27   Spain
# C  Charlie   42  Canada         # <-- pd_df.iloc[2,1]  /  pd_df.loc["C", "age"]
# #            ㄴ> pd_df["age"][2] 
# 현재에는 pd_df["age"][2] 방식으로 출력이 되지만 향후에는 [2]대신 .loc["C"]방식으로 변경된다는 경고문구도 출력됨

import pandas as pd
index = ["A", "B", "C"]
name = pd.Series(["Alice","Bob", "Charlie"], index=index)
age = pd.Series([34, 27, 42], index=index)
country = pd.Series(["USA", "Spain", "Canada"], index=index)
# print("name : \n", name)
# # name :
# #  A      Alice
# # B        Bob
# # C    Charlie
# print(name.iloc[2])         # Charlie
# print(name.iloc[-2])        # Bob
# print(name.loc["A"])        # Alice
pd_df = pd.DataFrame({
    "name" : name,
    "age" : age,
    "country" : country})

# print("series로 만든 df : \n", pd_df)
# # series로 만든 df : 
# #        name  age country
# # A    Alice   34     USA
# # B      Bob   27   Spain
# # C  Charlie   42  Canada

############################ 객체별 + / * 연산  ############################
# 리스트 / 문자열     : 나란히 나열(+), 반복 나열(*)
# 배열 / 데이터프레임 : 같은 위치 요소간 덧셈(+), 같은 위치 요소간 곱셈(*)



# # # 1) 문자열
# str_1 = "water"
# str_2 = "melon"
# print("water " + "melon ")            # water melon 
# print("water "*2 + "melon "*3)        # water water melon melon melon 
# # print(str_1 - "ter")    # 오류
# # # print(str_1 + 2)    # 오류
# # # print(str_1 * str_2)    # 오류

# # # 2) 리스트
list_1 = [1, 5, 6]
list_2 = [0.1, 2, 8]
# print(list_1 + list_2)      # [1, 5, 6, 0.1, 2, 8]
# # print(list_1 * list_2)      # 오류
# # print(list_1 + 3)           # 오류
# print(list_1 * 3)           # [1, 5, 6, 1, 5, 6, 1, 5, 6]
# list_1.append(list_2)
# print(list_1)               # [1, 5, 6, [0.1, 2, 8]]

# # 두 리스트의 같은 위치 요소마다 더하거나 곱할 때
# # 1) 반복문 사용
# list_sum = [i+j for i, j in zip(list_1, list_2)]
# list_multiple = [x*y for x, y in zip(list_1, list_2)]
# print("list_sum : ", list_sum)              # list_sum :  [1.1, 7, 14]
# print("list_multiple : ", list_multiple)    # list_multiple :  [0.1, 10, 48]
# # 2) 배열이나 데이터프레임으로 형변환 후 연산
# array_li_1 = np.array(list_1)
# array_li_2 = np.array(list_2)
# print("array sum : ", array_li_1 + array_li_2)          # array sum :  [ 1.1  7.  14. ]
# print("array multiple : ", array_li_1 * array_li_2)     # array multiple :  [ 0.1 10.  48. ]
# print(list_1.append(list_2))
# print(list_1)               # [1, 5, 6, [0.1, 2, 8]]


# # list_1 = [[1, 5, 6]]
# # list_2 = [[0.1, 2, 8]]
# # print(list_1 + list_2)
# # # [[1, 5, 6], [0.1, 2, 8]]
# # print(3 * list_1)
# # # [[1, 5, 6], [1, 5, 6], [1, 5, 6]]
# # # print(list_1+3)       # 오류
# # # print(list_1 * list_2)  # 오류

# # 3) 배열
# array_1 = np.array([1, 5, 6])
# array_2 = np.array([0.1, 2, 8])
# print(array_1 + array_2)        # [ 1.1  7.  14. ]
# print(array_1 * array_2)        # [ 0.1 10.  48. ]
# print(array_1*3)                # [ 3 15 18]
# print(array_1+3)                # [4 8 9]

# # array_1 = np.array([[1, 5, 6]])
# # array_2 = np.array([[0.1, 2, 8]])
# # print(array_1 + array_2)        # [[ 1.1  7.  14. ]]
# # print(array_1 * array_2)        # [[ 0.1 10.  48. ]]
# # print(array_1*3)                # [[ 3 15 18]]
# # print(array_1+3)                # [[4 8 9]]

# # 4) 시리즈
# series_1 = pd.Series([1, 5, 6])
# series_2 = pd.Series([0.1, 2, 8])
# print(series_1 + series_2)
# # 0     1.1
# # 1     7.0
# # 2    14.0
# # dtype: float64
# print(series_1 * series_2)
# # 0     0.1
# # 1    10.0
# # 2    48.0
# # dtype: float64
# print(series_1 *3)
# # 0     3
# # 1    15
# # 2    18
# # dtype: int64
# print(series_1 +3)
# # 0    4
# # 1    8
# # 2    9
# # dtype: int64


# # 5) 데이터프레임
# df_1 = pd.DataFrame([1, 5, 6])
# df_2 = pd.DataFrame([0.1, 2, 8])
# print(df_1 + df_2)
# # #       0
# # # 0   1.1
# # # 1   7.0
# # # 2  14.0
# print(df_1 * df_2)
# # #       0
# # # 0   0.1
# # # 1  10.0
# # # 2  48.0
# print(df_1*3)
# # #     0
# # # 0   3
# # # 1  15
# # # 2  18
# print(df_1 + 3)
# # #    0
# # # 0  4
# # # 1  8
# # # 2  9

# list_1 = [1, 5, 6]
# array_1 = np.array([1, 5, 6])
# # df_1 = pd.DataFrame({"a":1, "b":5, "c":6})
# se_1 = pd.Series([1, 5, 6])
# se_2 = pd.Series([0.1, 2, 8])
# # print(array_1 + df_1.iloc[0])
# print(array_1 + se_1)
# # 0     2
# # 1    10
# # 2    12
# # dtype: int64
# print(list_1 + se_1)


"""
############################ 객체별 요소 필터링 및 값변환############################
# 1) 문자열
string = "Hi, World! 123" 
# 알파벳만 필터링하고 대문자로 변환 
print(                [char for char in string]                   )     # ['H', 'i', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!', ' ', '1', '2', '3']
print(                [char for char in string if char.isalpha()] )     # ['H', 'I', 'W', 'o', 'r', 'l', 'd']
print(        [char.upper() for char in string if char.isalpha()] )     # ['H', 'I', 'W', 'O', 'R', 'L', 'D']
print(''.join([char.upper() for char in string if char.isalpha()]))     # HIWORLD

print(    list(                                filter(lambda char : char.isalpha(), string) ))     # ['H', 'i', 'W', 'o', 'r', 'l', 'd']
print(    list(map(lambda char : char.upper(), filter(lambda char : char.isalpha(), string))))     # ['H', 'I', 'W', 'O', 'R', 'L', 'D']
print('_'.join(map(lambda char : char.upper(), filter(lambda char : char.isalpha(), string))))     # H_I_W_O_R_L_D

# 숫자는 '*'로 변환 
print(        [char                                for char in string] )    # ['H', 'i', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!', ' ', '1', '2', '3']
print(        [char if not char.isdigit() else '*' for char in string] )    # ['H', 'i', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!', ' ', '*', '*', '*']
print(''.join([char if not char.isdigit() else '*' for char in string]))    # Hi, World! ***

# # 빈칸을 '-'로 변환
# print(string.replace(" ", "-"))
# print(string)


# 2) 리스트
nums = [1, 5, 6, 8, 10, 12, 15]

# 짝수를 제곱으로 변환
print(list(                      filter(lambda x: x % 2 == 0, nums) ))      # [6, 8, 10, 12]
print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nums))))      # [36, 64, 100, 144]

# 짝수는 제곱, 홀수는 두 배로 변환
print([   x                            for x in nums ])     # [1, 5, 6, 8, 10, 12, 15]
print([x ** 2 if x % 2 == 0 else x * 2 for x in nums ])     # [2, 10, 36, 64, 100, 144, 30]
# print(nums)

# 10미만은 2를 곱하고 10이상은 5를 더하기
print([  x                        for x in nums ])     # [1, 5, 6, 8, 10, 12, 15]
print([x * 2 if x < 10 else x + 5 for x in nums ])     # [2, 10, 12, 16, 15, 17, 20]


# 3) 배열(numpy)
import numpy as np
arr = np.array([1, 5, 6, 8, 9, 10, 12, 15])

# 3-1) 10보다 큰 값만 필터링하고, 그 값을 로그 변환
print(       arr[arr>10] )           # [12 15]
print(np.log(arr[arr>10]))           # [2.48490665 2.7080502 ]

print(         list(                         filter(lambda x: x > 10, arr) ) )       # [np.int64(12), np.int64(15)]
print(         list(map(lambda x: np.log(x), filter(lambda x: x > 10, arr))) )       # [np.float64(2.4849066497880004), np.float64(2.70805020110221)] 
print(np.array(list(map(lambda x: np.log(x), filter(lambda x: x > 10, arr)))))       # [2.48490665 2.7080502 ]

# 3-2) 5미만 값은 자연 지수로 변환, 5이상 값은 1.5 곱한 값으로 변환
print(np.where(arr < 5, np.exp(arr), arr * 1.5))    # [  2.71828183 2.0794415    9.          12.          13.5         15.          18.          22.5       ]


# 4) 시리즈
import pandas as pd
series_ = pd.Series([1, 5, 6, 8, 9, 10, 12, 15])

# 10보다 큰 값만 필터링하고, 그 값을 제곱으로 변환
print("1) : \n",series_),           print("2) : \n",series_[series_ > 10]),     print("3) : \n",series_[series_ > 10].apply(lambda x: x ** 2))
# 1) :                              # 2) :                                      # 3) :
# 0     1                           # 6    12                                   # 6    144
# 1     5                           # 7    15                                   # 7    225
# 2     6                           # dtype: int64                              # dtype: int64
# 3     8
# 4     9
# 5    10
# 6    12
# 7    15
# dtype: int64


# 5이하 값은 세 배로 변환

print("1) : \n", pd.Series( (lambda x: x * 3)(series_) )),      print("2) : \n", series_.apply(lambda x: x * 3 if x <= 5 else x))   
# 1) :                                                          # 2) :
#  0     3                                                      #  0     3
# 1    15                                                       # 1    15
# 2    18                                                       # 2     6
# 3    24                                                       # 3     8
# 4    27                                                       # 4     9
# 5    30                                                       # 5    10
# 6    36                                                       # 6    12
# 7    45                                                       # 7    15
# dtype: int64                                                  # dtype: int64

                                                                        # dtype: int64
print("1] : \n", pd.Series([ x for x in series_])),             print("2] : \n", pd.Series([x * 3 if x <= 5 else x for x in series_]))             # 0     3
# 1] :                                                          # 2] :
#  0     1                                                      #  0     3
# 1     5                                                       # 1    15
# 2     6                                                       # 2     6
# 3     8                                                       # 3     8
# 4     9                                                       # 4     9
# 5    10                                                       # 5    10
# 6    12                                                       # 6    12
# 7    15                                                       # 7    15
# dtype: int64                                                  # dtype: int64


"""

# 5) 데이터프레임
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Edward'],
    'Age': [24, 27, 22, 32, 29],
    'Score': [85, 78, 90, 88, 76]
}

df = pd.DataFrame(data)
df_1 = df.copy()
df_2 = df.copy()
df_3 = df.copy()
"""
print("data.keys() : ", data.keys())
print("df.keys() : ", df.keys())
print("df.columns : ", df.columns)
print()
print("data.values() : ", data.values())
# print("df.values() : ", df.values())        # 오류
print("df.values : ", df.values)
print()
print("data.items() : ", data.items())
print("df.items() : \n", pd.DataFrame(df.items()))
print()
print("df.index : ", df.index)
print()
print("df.sort_columns : ", df.sort_columns()) # 오류
print()
"""

# 나이가 25 이상인 행만 필터링하고, 'Score' 열의 값을 1.1배로 변환
print("방법 1 : \n", df[df['Age'] >= 25].assign(Score=lambda x: x['Score'] * 1.1))
        # 방법 1 : 
        #       Name  Age  Score
        # 1     Bob   27   85.8
        # 3   David   32   96.8
        # 4  Edward   29   83.6

print("방법 2  : \n",df_2.query("Age>=25").assign(Score=lambda x: x['Score'] * 1.1))
        # 방법 2 :
        #       Name  Age  Score
        # 1     Bob   27   85.8
        # 3   David   32   96.8
        # 4  Edward   29   83.6

print("방법 3 중간 필터결과: \n",df_3.loc[df_3['Age']>=25])
        # 방법 3 중간 필터결과:
        #       Name  Age  Score
        # 1     Bob   27     78
        # 3   David   32     88
        # 4  Edward   29     76
df_3['Score'] = df_3['Score'].astype(float)
df_3.loc[df_3['Age']>=25, 'Score'] *= 1.1
print("방법 3 : \n",df_3)
        # 방법 3 :     
        #        Name  Age  Score
        # 0    Alice   24   85.0
        # 1      Bob   27   85.8
        # 2  Charlie   22   90.0
        # 3    David   32   96.8
        # 4   Edward   29   83.6










