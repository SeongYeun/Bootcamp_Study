import matplotlib.pyplot as plt
import seaborn as sns
from pydataset import data
from matplotlib import font_manager

#path = "C:\\Users\\shg02\\AppData\\Local\\Microsoft\\Windows\\Fonts\\Pretendard-Medium.ttf"
path = "Pretendard-Medium.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)

mtcars = data('mtcars')

print(mtcars.head())

#실린더수에 따른 평균연비를 계산
#방법1
# cyl_mpg = mtcars.groupby('cyl')['mpg'].mean().reset_index()
# plt.bar(cyl_mpg["cyl"], cyl_mpg["mpg"])
#방법2
# cyl_mpg = mtcars.groupby('cyl')['mpg'].mean()
# print(cyl_mpg)
# cyl_mpg.plot(kind="bar")
# plt.xticks(rotation=0)

#변속기 유형별 평균마력
# am_hp = mtcars.groupby('am')['hp'].mean()
# print(am_hp)
# am_hp.plot(kind="bar", color="green")
# plt.xticks(rotation=0)

# #실린더를 기준으로 기어에 따른평균 연비
# cyl_gear = mtcars.pivot_table(index="cyl", columns="gear", values="mpg")
# print(cyl_gear)
# sns.heatmap(cyl_gear, annot=True, fmt=".2f")

# #pivot() 중복된 조합이 있을경우 오류 발생, 고유한 값이 보장될때 사용
# #pivot_table() 중복된 조합이 있는 경우에도 동작, 실무에 더 적합


#corr(method="pearson") #피어슨 상관계수(기본값)
#corr(method="spreaman") #스피어만 상관계수
#corr(method="kendall") #켄달의 타우 상관계수
corr_cars = mtcars[ ['mpg', 'hp', 'wt'] ].corr()
sns.heatmap(corr_cars, annot=True)


plt.show()


# ===========================================================================
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager


#path = "C:\\Users\\shg02\\AppData\\Local\\Microsoft\\Windows\\Fonts\\Pretendard-Medium.ttf"
path = "Pretendard-Medium.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)

file_name = "./1211/연령별인구현황.csv"
data = pd.read_csv(file_name, encoding="EUC-KR")


region_name = input("검색하고 싶은 지역명을 입력하세요: ")
data = data.rename(columns={"행정구역": "지역명"})
age_columns = [ col for col in data.columns if "세" in col ]

#숫자로 변환
for col in age_columns:
    data[col] = data[col].str.replace(",", "").astype(int)

#필터링
# contains() :문자열 데이터 필터링, 특정 패턴을 찾을때
# na : 결측값을 포함할지 결정. 기본값 True
# case : 영문의 대소문자 구분. 기본값 True
region_data = data[ data["지역명"].str.contains(region_name, na=False) ]

if region_data.empty:
    print(f"{region_name}의 지역은 존재하지 않습니다.")

#2024년11월_계_80~89세 [2024년11월, 80~89세]
#데이터 추출
age_groups = [ col.split("_계_")[1] for col in age_columns ]
result = region_data[age_columns].iloc[0].values

#그래프 그리기
plt.figure(figsize=(10, 8))
plt.plot(age_groups, result, marker="o", label=region_name)
plt.title(f"{region_name}의 연령별 인구 수", fontsize=16, pad=10)
plt.xlabel("연령대")
plt.ylabel("인구수")
plt.grid(True, linestyle="--", alpha=0.6)
plt.xticks(rotation=45)
plt.legend()
plt.show()
# print(age_groups)
# print(region_data[age_columns].iloc[0].values)

# ===========================================================================

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager


#path = "C:\\Users\\shg02\\AppData\\Local\\Microsoft\\Windows\\Fonts\\Pretendard-Medium.ttf"
path = "Pretendard-Medium.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)

file_name = "./1211/성별_연령별인구현황.csv"
data = pd.read_csv(file_name, encoding="EUC-KR")
region_name = input("검색하고 싶은 지역명을 입력하세요: ")

# 지역검색
region_data = data[data["행정구역"].str.contains(region_name, na=False)]
if region_data.empty:
    print(f"{region_name}의 지역은 존재하지 않습니다.")

# male_columns = [ col for col in region_data.columns if "남" in col and "세" in col ]
female_columns = [ col for col in region_data.columns if "여" in col and "세" in col ]
male_columns = [ col for col in region_data.filter(like="남_").columns if "총인구수" not in col and "연령구간인구수" not in col  ]
#filter() items=["2024년11월_남_40~49세", "2024년11월_남_70~79세"]

# for col in male_columns:
#     region_data[col] = region_data[col].astype(str).str.replace(",", "").astype(int)

# for col in female_columns:
#     region_data[col] = region_data[col].astype(str).str.replace(",", "").astype(int)

male_result = region_data[male_columns].iloc[0].astype(str).str.replace(",", "").astype(int)
#female_result =  region_data[female_columns].iloc[0].astype(str).str.replace(",", "").astype(int)
female_result = region_data[female_columns].iloc[0].apply(lambda x : int(str(x).replace(",", "")) )
#apply(): 사용자 함수 정의

age_groups = [col.split("_남_")[1] for col in male_columns]


plt.figure(figsize=(10, 8))
plt.plot(age_groups, male_result, marker='o', label="남성", color="blue")
plt.plot(age_groups, female_result, marker='o', label="여성", color="red")


plt.title(f"{region_name}의 연령별 인구 수", fontsize=16, pad=10)
plt.xlabel("연령대")
plt.ylabel("인구수")
plt.grid(True, linestyle="--", alpha=0.6)
plt.xticks(rotation=45)
plt.legend()
plt.show()


print(age_groups)
