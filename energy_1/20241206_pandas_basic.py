import pandas as pd
"""

# ======================  시리즈 (pd.Series)  ====================== #

# 1) 리스트 형식으로 생성
data = [10, 20, 30, 40]
# series = pd.Series(data)
# print(series)
# 0    10
# 1    20
# 2    30
# 3    40

# Series 인덱스 커스텀
series = pd.Series(data, index=["a","b","c","d"])
# print(series)
# a    10
# b    20
# c    30
# d    40
# dtype: int64


# 2) 딕셔너리 형식으로 생성
data_1 = {
    "a" : 10,
    "b" : True,
    "c" : 3.14,
    "d" : "python"
}
series_1 = pd.Series(data_1, name="딕셔너리")
# print(series_1)
# a        10
# b      True
# c      3.14
# d    python
# Name: 딕셔너리, dtype: object


print(series_1.index)
# Index(['a', 'b', 'c', 'd'], dtype='object')
print(series_1.values)
# [10 True 3.14 'python']
print(series_1.shape)
# (4,)


data_2 = ('민지', '여', False)
member = pd.Series(data_2, index=['이름', '성별', '결혼여부'])
print(member)
# 이름         민지
# 성별          여
# 결혼여부    False
# dtype: object

print(member['이름'])
# 민지
# print(member['성별', '결혼여부'])       # --> 오류 남
print(member[['성별', '결혼여부']])
# 성별          여
# 결혼여부    False
# dtype: object

data_3 = [10, 20, 30, 40, 50]
series_3 = pd.Series(data_3, index=['a','b','c','d','e'])
print(series_3[series_3>20])
# c    30
# d    40
# e    50
# dtype: int64
series_3['c'] = 100
print(series_3)
# a     10
# b     20
# c    100
# d     40
# e     50
# dtype: int64


# 실습1. 시리즈 만들기
data = ["4 cups", "1 cup", "2 large", "1 can"]
series = pd.Series(data, name="Dinner", index=["밀가루","우유","계란","참치캔"])
print(series)



# ======================  데이터프레임 (pd.DataFrame)  ====================== #
data = {
    'Name' : ["홍길동", "임꺽정", "성춘향"],
    'Age' : [25, 30, 27],
    'City' : ["서울", "부산", "인천"]
}
df = pd.DataFrame(data)
print(df)
#   Name  Age City
# 0  홍길동   25   서울
# 1  임꺽정   30   부산
# 2  성춘향   27   인천


index = ["2020","2021","2022","2023","2024","2025"]

yeonghee = pd.Series([140,150,160,170,180,190], index=index)
cheolsu = pd.Series([200,210,220,230,240,250], index=index)

result = pd.DataFrame({
    '영희':yeonghee,
    '철수':cheolsu
})
print(result)
#        영희   철수
# 2020  140  200
# 2021  150  210
# 2022  160  220
# 2023  170  230
# 2024  180  240
# 2025  190  250

print(result.head())        # ㅡ 위 5개 데이터만 출력
#        영희   철수
# 2020  140  200
# 2021  150  210
# 2022  160  220
# 2023  170  230
# 2024  180  240

print(result.tail())        # ㅡ 아래 5개 데이터만 출력
#        영희   철수
# 2021  150  210
# 2022  160  220
# 2023  170  230
# 2024  180  240
# 2025  190  250

print(result.shape)         # ㅡ 데이터 크기 확인 (행, 열)
# (6, 2)

print(result.info())        # ㅡ 구조 및 타입 요약 (결측치 확인 가능)
# <class 'pandas.core.frame.DataFrame'>
# Index: 6 entries, 2020 to 2025
# Data columns (total 2 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   영희      6 non-null      int64
#  1   철수      6 non-null      int64
# dtypes: int64(2)
# memory usage: 144.0+ bytes
# None

print(result.columns,"\n")        # ㅡ 컬럼 이름 확인
# Index(['영희', '철수'], dtype='object')
print(result.values,"\n")        # ㅡ 행 값 확인
# [[140 200]
#  [150 210]
#  [160 220]
#  [170 230]
#  [180 240]
#  [190 250]]
print(result.index,"\n")        # ㅡ 인덱스 확인
# Index(['2020', '2021', '2022', '2023', '2024', '2025'], dtype='object')

print(result.dtypes,"\n")        # ㅡ 데이터 타입 확인
# 영희    int64
# 철수    int64
# dtype: object
print(result['영희'],"\n")        # ㅡ 해당 열의 모든 값 출력 (열이름 미출력) ㅡ 시리즈 형태
# 2020    140
# 2021    150
# 2022    160
# 2023    170
# 2024    180
# 2025    190
# Name: 영희, dtype: int64
print(result[['영희']],"\n")        # ㅡ 해당 열의 모든 값 출력 (열이름 출력) ㅡ 데이터프레임 형태
#        영희
# 2020  140
# 2021  150
# 2022  160
# 2023  170
# 2024  180
# 2025  190


"""
data = {
    'Name' : ["홍길동", "임꺽정", "성춘향"],
    'Age' : [25, 30, 27],
    'City' : ["서울", "부산", "인천"]
}
df = pd.DataFrame(data, index=['a', 'b', 'c'])
print(df)
#   Name  Age City
# a  홍길동   25   서울
# b  임꺽정   30   부산
# c  성춘향   27   인천


# 1) .loc
print(df.loc['b'])
# Name    임꺽정
# Age      30
# City     부산
# Name: b, dtype: object

print(df.loc['b', 'Age'])
# 30

print(df.loc['a':'c', 'Name':'Age'])
#   Name  Age
# a  홍길동   25
# b  임꺽정   30
# c  성춘향   27

print(df.loc[ df['Age']>=30 ])
#   Name  Age City
# b  임꺽정   30   부산

print("~ ", df.loc[ ~df['Age']>=30 ])


"""
print(df.loc[:, "Name" ])
# b  임꺽정   30   부산
# a    홍길동
# b    임꺽정
# c    성춘향
# Name: Name, dtype: object

print(df.loc["a", :],"\n")
# Name    홍길동
# Age      25
# City     서울
# Name: a, dtype: object


# 2) .iloc
print(df.iloc[1],"\n")
# Name    임꺽정
# Age      30
# City     부산
# Name: b, dtype: object

print(df.iloc[1, 1],"\n")
# 30

print(df.iloc[0:2, 0:2],"\n")
#   Name  Age
# a  홍길동   25
# b  임꺽정   30

print(df.iloc[[0,2], [1,2]],"\n")
#    Age City
# a   25   서울
# c   27   인천

print(df.iloc[:, 0],"\n")
# a    홍길동
# b    임꺽정
# c    성춘향
# Name: Name, dtype: object

print(df.iloc[0, :],"\n")
# Name    홍길동
# Age      25
# City     서울
# Name: a, dtype: object


data = {
    'Name' : ["홍길동", "임꺽정", "성춘향"],
    'Age' : [25, 30, 27],
    'City' : ["서울", "부산", "인천"]
}
df = pd.DataFrame(data, index=['a', 'b', 'c'])
print(df,'\n')
#   Name  Age City
# a  홍길동   25   서울
# b  임꺽정   30   부산
# c  성춘향   27   인천

new_data = {'Name' : "이몽룡", 'Age' : 31, 'City' : "포항"}

result = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
print(result,'\n')
#   Name  Age City
# 0  홍길동   25   서울
# 1  임꺽정   30   부산
# 2  성춘향   27   인천
# 3  이몽룡   31   포항


result['직업'] = ["엔지니어", '개발자','디자이너','기획자']
print(result, '\n')
#   Name  Age City    직업
# 0  홍길동   25   서울  엔지니어
# 1  임꺽정   30   부산   개발자
# 2  성춘향   27   인천  디자이너
# 3  이몽룡   31   포항   기획자


result.at[1, 'City'] = "천안"
print(result, '\n')
#   Name  Age City    직업
# 0  홍길동   25   서울  엔지니어
# 1  임꺽정   30   천안   개발자
# 2  성춘향   27   인천  디자이너
# 3  이몽룡   31   포항   기획자

result.loc[result['Name']=='임꺽정', 'Age'] = 32
print(result, '\n')
#   Name  Age City    직업
# 0  홍길동   25   서울  엔지니어
# 1  임꺽정   32   천안   개발자
# 2  성춘향   27   인천  디자이너
# 3  이몽룡   31   포항   기획자


result.rename(columns={'Name':'이름', 'Age':'나이'}, inplace=True)
print(result, '\n')
#     이름  나이 City    직업
# 0  홍길동  25   서울  엔지니어
# 1  임꺽정  32   천안   개발자
# 2  성춘향  27   인천  디자이너
# 3  이몽룡  31   포항   기획자

result.sort_values(by="나이", inplace=True)
print(result, '\n')
#     이름  나이 City    직업
# 0  홍길동  25   서울  엔지니어
# 2  성춘향  27   인천  디자이너
# 3  이몽룡  31   포print(result['수학'], '\n')항   기획자
# 1  임꺽정  32   천안   개발자

result.sort_values(by="나이", ascending=False, inplace=True)
print(result, '\n')
#     이름  나이 City    직업
# 1  임꺽정  32   천안   개발자
# 3  이몽룡  31   포항   기획자
# 2  성춘향  27   인천  디자이너
# 0  홍길동  25   서울  엔지니어

result.drop(columns=['City'], inplace=True)
print(result, '\n')
#     이름  나이    직업
# 1  임꺽정  32   개발자
# 3  이몽룡  31   기획자
# 2  성춘향  27  디자이너
# 0  홍길동  25  엔지니어 

"""

# 실습2. 데이터프레임 만들기
name = ['홍길동','임꺽정','성춘향']
math = [85,90,78]
eng = [88,76,92]
sci = [95,89,84]
df = pd.DataFrame({
    "이름" : name,
    "수학" : math,
    "영어" : eng,
    "과학" : sci 
})
print(df, '\n')
new_data = pd.DataFrame({
    "이름" : ["이몽룡"],
    "수학" : [88],
    "영어" : [85],
    "과학" : [90] 
})
result = pd.concat([df, new_data], ignore_index=True)
result.rename(columns={"수학" : "Math"}, inplace=True)
result.at[1,'영어'] = 80
result['Total'] = result.iloc[:,1]+result.iloc[:,2]+result.iloc[:,3]
# ㅡㅡ>  result['Total'] = result['수학'] + result['영어'] + result['과학']
print(result, '\n')



print(result['Math'], '\n')
# 0    85
# 1    90
# 2    78
# 3    88
# Name: Math, dtype: int64
print(result.loc['Math'], '\n')   # 오류남 ㅡ 이유 : 인덱스정보없이 열이름만 있어서 오류
# ㅡㅡ> loc와 iloc는 행에 접근하는 방식이기 때문에 인덱스 정보가 포함되어야 함