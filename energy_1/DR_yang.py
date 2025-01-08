



# 데이터 전처리 : 일시, 휴일 

# # 새 파일 경로 설정
# file_path = r"C:\Users\didrj\documents\workspace\python\1224\제주도 시간별 기상자료 및 발전수요량(20230101_20240930) (1).csv"
# # 데이터 불러오기
# data = pd.read_csv(file_path, encoding='EUC-KR')

# # '일시' 컬럼을 datetime 형식으로 변환 (형식 지정)
# data['일시'] = pd.to_datetime(data['일시'].astype(str))

# # 공휴일 데이터 추가 (예시로 설정)
# public_holidays = pd.to_datetime([
#     '2023-01-01', '2023-01-21', '2023-01-22', '2023-01-23', '2023-03-01', '2023-05-05', '2023-06-06', '2023-08-15',
#     '2023-09-28', '2023-09-29', '2023-09-30', '2023-10-03', '2023-12-25'
# ])
# # 공휴일을 datetime.date 형식으로 변환
# public_holidays = public_holidays.date
# # 먼저 공휴일 처리: 공휴일은 'O'로 설정
# data['휴일'] = data['일시'].dt.date.apply(
#     lambda x: 'O' if x in public_holidays else 'X')
# # 주말 처리: 주말(토요일, 일요일)을 'O'로 설정 (공휴일이 이미 'O'로 설정된 경우는 그대로 두고, 아닌 경우만 'O'로 설정)
# for index, row in data.iterrows():
#     if row['휴일'] == 'X':  # 공휴일이 아닌 경우만
#         if row['일시'].weekday() in [5, 6]:  # 토요일(5), 일요일(6)
#             data.at[index, '휴일'] = 'O'
# # 결과 확인
# print(data[['일시', '휴일']].head())
# # 수정된 DataFrame을 다시 CSV 파일로 저장
# output_file_path = 'C:/Users/didrj/documents/workspace/python/1224/휴일포함_수정.csv'
# data.to_csv(output_file_path, index=False, encoding='EUC-KR')
# # 컬럼 순서를 변경: '일시', '휴일', '발전수요량' 순으로 정렬
# columns_order = ['일시', '휴일'] + \
#     [col for col in data.columns if col not in ['일시', '휴일']]
# # 데이터프레임의 컬럼 순서를 재정렬
# data = data[columns_order]
# # 결과 확인
# print(data[['일시', '휴일', '발전수요량']].head())
# # 수정된 DataFrame을 다시 CSV 파일로 저장
# output_file_path = 'C:/Users/didrj/documents/workspace/python/1224/휴일포함_수정_재정렬.csv'
# data.to_csv(output_file_path, index=False, encoding='EUC-KR')


##################################################################################################

"""월별 휴일 vs 비휴일 발전 수요량 비교"""
import pandas as pd
import matplotlib.pyplot as plt
# '휴일포함.csv' 파일 경로 설정
# file_path = ".\\raw data\\holiday.csv"
# CSV 파일 읽기
data = pd.read_csv(r'C:\Users\praye\Documents\Bootcamp\energy_1\raw data\holiday.csv', encoding='EUC-KR')
# '일시' 컬럼을 datetime 형식으로 변환
data['일시'] = pd.to_datetime(data['일시'], errors='coerce')
# '년', '월' 컬럼 생성 (월별 그룹화를 위해)
data['년'] = data['일시'].dt.year
data['월'] = data['일시'].dt.month

# 결측값 처리 후 데이터 확인
print("\n결측값 처리 후 데이터:")
print(data[['일시', '발전수요량', '기온(°C)']].head())
# 피어슨 상관계수 계산
correlation_pearson = data["발전수요량"].corr(data["기온(°C)"])
# 결과 출력
print(
    f"\n2023-06부터 2023-08까지 발전수요량과 기온(°C)의 피어슨 상관계수: {correlation_pearson:.2f}")

# 각 월별로 그룹화하여 휴일과 비휴일의 발전 수요량 비교
monthly_comparison = []
for year in data['년'].unique():  # 연도별로 처리
    for month in data[data['년'] == year]['월'].unique():  # 월별로 처리
        # 해당 년월의 데이터 추출
        monthly_data = data[(data['년'] == year) & (data['월'] == month)]
        # 휴일과 비휴일 데이터 분리
        holiday_data = monthly_data[monthly_data['휴일'] == 'O']  # 휴일인 데이터
        # 휴일이 아닌 데이터
        non_holiday_data = monthly_data[monthly_data['휴일'] == 'X']
        # 발전 수요량의 평균값 계산
        holiday_demand_avg = holiday_data['발전수요량'].mean(
        ) if not holiday_data.empty else 0
        non_holiday_demand_avg = non_holiday_data['발전수요량'].mean(
        ) if not non_holiday_data.empty else 0
        # 발전 수요량 차이 계산
        demand_diff = holiday_demand_avg - non_holiday_demand_avg
        # 결과 저장
        monthly_comparison.append({
            '년': year,
            '월': month,
            '일시': pd.to_datetime(f"{year}-{month:02d}-01"),  # 날짜 형식으로 저장
            '휴일 평균 발전 수요량': holiday_demand_avg,
            '비휴일 평균 발전 수요량': non_holiday_demand_avg,
            '발전 수요량 차이': demand_diff  # 발전 수요량 차이 컬럼 추가
        })
# 결과를 DataFrame으로 변환
comparison_df = pd.DataFrame(monthly_comparison)
# 출력
print(comparison_df)
# 그래프 시각화 (하나의 그래프에 두 선을 겹쳐서 표시)
plt.figure(figsize=(12, 6))
# 휴일 평균 발전 수요량 그래프
plt.plot(comparison_df['일시'], comparison_df['휴일 평균 발전 수요량'],
         marker='o', color='b', label='Holiday Avg Demand')
# 비휴일 평균 발전 수요량 그래프
plt.plot(comparison_df['일시'], comparison_df['비휴일 평균 발전 수요량'],
         marker='o', color='r', label='Non-Holiday Avg Demand')
# 제목과 라벨 설정 (영어로 변경)
plt.title(
    'Holiday vs Non-Holiday Average Power Demand (2023-01 to 2024-09)', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Power Demand', fontsize=12)
# x축 날짜 포맷
plt.xticks(rotation=45)
# 그리드 추가
plt.grid(True)
# 범례 추가
plt.legend()
# 레이아웃 조정
plt.tight_layout()
# 그래프 출력
plt.show()
