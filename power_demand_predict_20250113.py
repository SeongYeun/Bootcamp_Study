import pandas as pd
import numpy as np
# 숫자 표현법 변경 (1e6 -> 소수점 2자리 실수형)
pd.set_option('display.float_format', '{:,.2f}'.format)

# min-max로 스케일링한 컬럼 기준 패턴 분석
# 주기별 주요 영향요인 확인
# 월별 : 기온갭(19도대비) + 일사량
# 요일 : 평일과 주말(토~일)간 차이 확인
# 휴일 : 휴일여부간 차이 확인
# 시간 : 기온갭(19도대비) + 지면온도갭(19도초과분)

# 발전수요량 : 전력시장에 참여하는 태양광발전량은 포함됨 (자가용 태양광 발전량은 미집계)
# 태양광 발전량 ~ 일사량(발전량 생산성 관련) & 일조량(태양광 모듈 실제 작동시간 결정)
# 태양광 발전 시스템 출력(P) = 시스템 효율(η) * 일사량(G) * 태양광 패널 면적(m2)
# 태양광은 일사량의 즉각적 변화와 일조 시간의 누적효과 모두 영향을 받음
# 지면온도(T) = a*일사량(I) + b*일조량(S) + c   (a,b,c : 상수)
# 지면온도(Tm) = 일사량(I)*(1-표면반사율(α))*cos(일사각도(θ))

# 1. 발전수요량 취합
# 출처 : 공공데이터포털(data.go.kr) > 한국거래소_시간별 제주전력수요
demand_1 = pd.read_csv(r"C:/Users/praye/Documents/Bootcamp/energy_1/raw data/한국전력거래소_시간별 제주전력수요_2017_2023.2.csv", encoding="EUC-KR")           # 2017~2023.2.
demand_2 = pd.read_csv(r"C:/Users/praye/Documents/Bootcamp/energy_1/raw data/한국전력거래소_시간별 제주전력수요_20230301-20230930.csv", encoding="EUC-KR")     # 2023.3.~2023.9.
demand_3 = pd.read_csv(r"C:/Users/praye/Documents/Bootcamp/energy_1/raw data/시간별 제주전력수요_240331.csv", encoding="EUC-KR")                              # 2023.9.~2024.3.
demand_4 = pd.read_csv(r"C:/Users/praye/Documents/Bootcamp/energy_1/raw data/시간별 제주전력수요_240630.csv", encoding="EUC-KR")                              # 2024.4.~2024.6.
demand_5 = pd.read_csv(r"C:/Users/praye/Documents/Bootcamp/energy_1/raw data/한국전력거래소_시간별 제주전력수요_20240930.csv", encoding="utf-8")               # 2024.7.~2024.9.
# demand_1.shape,     # (2250,26)     : 마지막 불필요한 컬럼 삭제필요, 단위:kWh
# demand_2.shape,     # (214,25)      : 2023.9.(1개월분 기간 겹침),   단위:kWh
# demand_3.shape,     # (213,25)      : 2023.9.(1개월분 기간 겹침),   단위:MWh
# demand_4.shape,     # (91,25)       : 단위:MWh
# demand_5.shape      # (92,25)       : 단위:MWh

# 1) 불필요 컬럼 제거 (demand_1의 마지막 컬럼) 및 컬럼명 변경
demand_1 = demand_1.iloc[:, :-1]
demand_1 = demand_1.rename(columns={'거래일자' : '날짜'})
demand_2 = demand_2.rename(columns={'거래일자' : '날짜'})

# 2) 단위 통일(kWh, Mwh -> kWh)
for col in demand_3.columns[1:]:
    demand_3[col] = demand_3[col]*1000
    demand_4[col] = demand_4[col]*1000
    demand_5[col] = demand_5[col]*1000


# 3) 발전수요량 전체기간 합치기
demand = pd.concat([demand_1, demand_2, demand_3, demand_4, demand_5])

# 4) 컬럼명 변경 (기상자료의 시간 표시형식과 일치)
demand.columns = demand.columns.str.replace("시", ":00")
demand.columns = demand.columns.str.replace("24", "0")

# 5) 데이터 형태 변환 (melt)
value_var = demand.columns[1:]
demand_melted = pd.melt(demand, id_vars=['날짜'], value_vars=value_var, 
                        var_name="시간", value_name="발전수요량")

# 6) 컬럼 합치기, 시간순 정렬 및 중복 제거
demand_melted['일시']=demand_melted['날짜']+" "+demand_melted['시간']
demand_melted['일시']=pd.to_datetime(demand_melted['일시'])
demand_melted = demand_melted.sort_values('일시')
demand_melted = demand_melted.drop_duplicates('일시')

# 7) '일시' 및 '발전수요량' 컬럼만 추출
demand_result =pd.concat([demand_melted['일시'], demand_melted['발전수요량']], axis=1)

# 2. 기상자료 취합
# 출처 : 기상청 기상자료개방포털 > 데이터 > 기상관측 > 지상 > 자료
# 검색조건 : 지점 - 제주특별자치도 > 제주(184)
#           기간 - 20230101 00시 ~ 20231231 23시
#           기간 - 20240101 00시 ~ 20241222 23시
temp_23 = pd.read_csv(r"C:/Users/praye/Documents/Bootcamp/energy_1/raw data/OBS_ASOS_TIM_20241223162335.csv", encoding="EUC-KR")
temp_24 = pd.read_csv(r"C:/Users/praye/Documents/Bootcamp/energy_1/raw data/OBS_ASOS_TIM_20241223162031.csv", encoding="EUC-KR")

# 1) '일시' 자료형 변환 (object->datetime)
temp_23['일시'] = pd.to_datetime(temp_23['일시'])
temp_24['일시'] = pd.to_datetime(temp_24['일시'])

# 2) 기온데이터 병합
temperature = pd.concat([temp_23, temp_24])

# 3) 불필요 컬럼 제거
drop_col = [x for x in temperature.columns if ('지점' in x) or ('플래그' in x )  or ('약어' in x ) ]
temperature = temperature.drop(columns=drop_col)

# 3. 데이터 병합 (1.기상자료 x 2.발전수요량)
temp_demand = pd.merge(left=demand_result, right=temperature, how='inner', on='일시')
# temp_demand.info()


# 3-1) 결측치 처리 ㅡ '지면상태'컬럼 삭제 및 0으로 대체
temp_demand = temp_demand.drop(columns=['지면상태(지면상태코드)'])
na_0_col = ['강수량(mm)', '일조(hr)', '일사(MJ/m2)', '적설(cm)','3시간신적설(cm)',
            '전운량(10분위)', '최저운고(100m )', '현상번호(국내식)']
for col in na_0_col:
    temp_demand[col] = temp_demand[col].fillna(0)

# 3-2) 나머지 컬럼 결측치 데이터 삭제
lists_dropna = list(temp_demand.isna().sum()[lambda x : x > 0].index)
temp_demand.dropna(subset=lists_dropna, how='any', inplace=True)

# len(temp_demand), temp_demand.isna().sum()
# [temp_demand.isna().sum()[lambda x : x > 0].index]

# 4. 컬럼 추가 : 휴일, 요일, 월, 시간
holidays = ['2023-01-01', '2023-01-21', '2023-01-22', '2023-01-23', '2023-01-24', 
            '2023-03-01', '2023-05-01', '2023-05-05', '2023-05-27', '2023-05-29', 
            '2023-06-06', '2023-08-15', '2023-09-28', '2023-09-29', '2023-09-30', 
            '2023-10-03', '2023-10-09', '2023-12-25', '2024-01-01', '2024-02-09', 
            '2024-02-10', '2024-02-11', '2024-02-12', '2024-03-01', '2024-04-10', 
            '2024-05-01', '2024-05-05', '2024-05-06', '2024-05-15', '2024-06-06', 
            '2024-08-15', '2024-09-16', '2024-09-17', '2024-09-18', '2024-10-03', 
            '2024-10-09', '2024-12-25']
temp_demand['day_of_week']=temp_demand['일시'].dt.dayofweek                                         # (5:토요일, 6:일요일)
temp_demand['holiday'] = np.where(temp_demand['일시'].dt.date.astype(str).isin(holidays), 1, 0)     # (1:휴일,  0:비휴일)
temp_demand['month'] = temp_demand['일시'].dt.month
temp_demand['hour'] = temp_demand['일시'].dt.hour

# temp_demand.head(3).T
# temp_demand.info()



# #   기온 - 정수값 컬럼 생성
# temp_demand['temp_int'] = temp_demand['기온(°C)'].astype(int)
# #   같은 정수 기온값들의 평균값 산출 
# temp_demand['demand_mean'] = temp_demand.groupby('temp_int')['발전수요량'].transform('mean')
# temp_demand.head(3)
# 5. 컬럼추가 : abs(기온 - 변곡점 온도)
temp_gap_base = 19
temp_demand['기온편차'] = abs(temp_demand['기온(°C)']-temp_gap_base)
surface_gap_base = 5
temp_demand['temp_surface_gap'] = abs(temp_demand['지면온도(°C)']-surface_gap_base)
temp_demand['over_surface_gap_base'] = np.where(temp_demand['지면온도(°C)']>surface_gap_base, 
                                                temp_demand['지면온도(°C)']-surface_gap_base, 0)
temp_demand['shifted_insolation'] = temp_demand['일사(MJ/m2)'].shift(3)
temp_demand['gaps_temp_surface'] = temp_demand['기온편차'] + temp_demand['over_surface_gap_base']*0.3


# 6. 스케일 조정 : Min-Max
def min_max (df, col) : 
    return (df[col] - df[col].min())  /  (df[col].max() - df[col].min())

#   발전수요량, 기온(°C), 지면온도(°C), 일사(MJ/m2)   
# ['s_기온', 's_지면온도', 's_일사량', 's_발전수요량', 's_기온편차']
temp_demand['s_발전수요량']  = min_max(temp_demand, '발전수요량')
temp_demand['s_기온']  = min_max(temp_demand, '기온(°C)')
temp_demand['s_기온편차']             = min_max(temp_demand, '기온편차')
temp_demand['s_지면온도'] = min_max(temp_demand, '지면온도(°C)')
temp_demand['s_일사량']   = min_max(temp_demand, '일사(MJ/m2)')
temp_demand['s_일조량']   = min_max(temp_demand, '일조(hr)')
temp_demand['s_시정']   = min_max(temp_demand, '시정(10m)')

temp_demand['일사x일조'] = temp_demand['일사(MJ/m2)'] * temp_demand['일조(hr)']
temp_demand['s_일사x일조']   = min_max(temp_demand, '일사x일조')

#   기온갭(temp_gap), 지면온도갭(temp_surface_gap), 지면온도초과갭(over_surface_gap_base))
temp_demand['s_발전수요량-기온편차'] = temp_demand['s_발전수요량'] - temp_demand['s_기온편차']
temp_demand['s_temp_surface_gap']     = (temp_demand['temp_surface_gap'] - temp_demand['temp_surface_gap'].min())/(temp_demand['temp_surface_gap'].max() - temp_demand['temp_surface_gap'].min())
temp_demand['s_temp_surface_overgap'] = (temp_demand['over_surface_gap_base'] - temp_demand['over_surface_gap_base'].min())/(temp_demand['over_surface_gap_base'].max() - temp_demand['over_surface_gap_base'].min())
temp_demand['s_shifted_insolation']   = (temp_demand['shifted_insolation'] - temp_demand['shifted_insolation'].min())/(temp_demand['shifted_insolation'].max() - temp_demand['shifted_insolation'].min())

# 시각화 설정
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager
path =  'C:\\Windows\\Fonts\\H2GTRM.TTF'
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)
sns.set_theme(style='darkgrid')

# 모든 컬럼이 출력되도록 설정
pd.set_option('display.max_columns', None)

# 업무시간 여부 컬럼 추가 (월~금 중 휴일이 아니면서 5시부터 20시까지)
cond_1 = temp_demand['holiday']==0
cond_2 = temp_demand['day_of_week'].isin(list(range(0,5)))
cond_3 = temp_demand['hour'].isin(list(range(5,21)))
temp_demand['working_hour'] = cond_1 & cond_2 & cond_3

###############
# 시계열분석
###############


import warnings
from statsmodels.tsa.seasonal import seasonal_decompose
cols=['일시', '발전수요량'] #, '일사(MJ/m2)', '일조(hr)', '기온편차', '풍속(m/s)',  '지면온도(°C)', 'month', 'day_of_week', 'hour', 'working_hour']
ts = temp_demand[cols].set_index('일시')
# ts.info()

# 발전수요량의 시계열분해 (statsmodels의 seasonal_decompose)
period_ = len(ts) * 24
result = seasonal_decompose(ts, model='multiplicative', period=720)
# plt.rcParams['figure.figsize']=[12,8]
# result.plot()
# plt.show()

# 발전수요량의 시계열분해 (statsmodels의 seasonal_decompose)
period_ = len(ts) * 24
result = seasonal_decompose(ts, model='multiplicative', period=24)
# plt.rcParams['figure.figsize']=[12,8]
# result.plot()
# plt.show()


# 정상성 검정 (H0 : 데이터가 정상성을 갖지 않는다)
from statsmodels.tsa.stattools import adfuller

# 데이터셋 분리 (train vs test)
training = ts[:24*365]
test = ts[24*365:]
adf = adfuller(training, regression='ct')
print(f"정상성 검정(ct) 통계량 : {adf[0]:.6f}, 정상성 검정(ct) p-value : {adf[1]:.6f}")
# (np.float64(-4.01833396172674), np.float64(0.008280251969175787))
# ㄴ> p-value가 0.05보다 현저히 작으므로 H0 기각 ( = 정상성 만족)


# 정상성 검정 (H0 : 데이터가 정상성을 갖지 않는다)
from statsmodels.tsa.stattools import adfuller

# 데이터셋 분리 (train vs test)
training = ts[:24*365]
test = ts[24*365:]
adf_tt = adfuller(training, regression='ctt')
print(f"정상성 검정(ctt) 통계량 : {adf_tt[0]:.6f}, 정상성 검정(ctt) p-value : {adf_tt[1]:.6f}")

# (np.float64(-4.112103226524976), np.float64(0.02269369580223671))
# ㄴ> p-value가 0.05보다 작으므로 H0 기각 ( = 정상성 만족)


# MA 모형 q값 찾기
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# # PACF 차트
# plot_pacf(ts)
# plt.show()

# # ACF 차트
# plot_acf(ts)
# plt.show()


# ARIMA 분석
from statsmodels.tsa.arima.model import ARIMA

model = ARIMA(training, order=(1,0,2))
res = model.fit()
print(f"ARIMA(1,0,2) 분석 결과 : \n{res.summary()}")

# Auto-ARIMA
from statsmodels.tsa.arima.model import ARIMA

model = ARIMA(training, order=(2,0,2))
res = model.fit()
print(f"ARIMA(2,0,2) 분석 결과 : \n{res.summary()}")


# 예측
pred_y = res.forecast(steps=len(test), alpha=0.5)
test_y = test
pred_y.index = test_y.index


# Auto-ARIMA
from pmdarima import auto_arima
import numpy as np

# auto_model = auto_arima(training, start_p=0, d=1, start_q=0,
#                         max_p=3, max_q=3,
#                         start_P=0, start_Q=0,
#                         max_P=3, max_Q=3, m=7,
#                         seasonal=True, information_criterion='aic',
#                         trace=True)

# ARIMA(0,1,0)(0,0,0)[7] intercept   : AIC=207876.244, Time=0.23 sec
# ARIMA(1,1,0)(1,0,0)[7] intercept   : AIC=203252.037, Time=1.80 sec
# ARIMA(0,1,1)(0,0,1)[7] intercept   : AIC=204190.587, Time=1.62 sec
# ARIMA(0,1,0)(0,0,0)[7]             : AIC=207874.244, Time=0.12 sec
# ARIMA(1,1,0)(0,0,0)[7] intercept   : AIC=203518.286, Time=0.46 sec
# ARIMA(1,1,0)(2,0,0)[7] intercept   : AIC=203241.471, Time=3.77 sec
# ARIMA(1,1,0)(3,0,0)[7] intercept   : AIC=203228.201, Time=10.20 sec
# ARIMA(1,1,0)(3,0,1)[7] intercept   : AIC=203049.501, Time=23.59 sec
# ARIMA(1,1,0)(2,0,1)[7] intercept   : AIC=203059.677, Time=9.26 sec
# ARIMA(1,1,0)(3,0,2)[7] intercept   : AIC=inf, Time=56.86 sec

# ARIMA(1,1,0)(2,0,2)[7] intercept   : AIC=inf, Time=31.04 sec
# ARIMA(0,1,0)(3,0,1)[7] intercept   : AIC=205952.231, Time=24.42 sec
# ARIMA(2,1,0)(3,0,1)[7] intercept   : AIC=203050.978, Time=26.24 sec
# ARIMA(1,1,1)(3,0,1)[7] intercept   : AIC=203051.140, Time=27.95 sec
# ARIMA(0,1,1)(3,0,1)[7] intercept   : AIC=203908.278, Time=22.84 sec
# ARIMA(2,1,1)(3,0,1)[7] intercept   : AIC=203045.072, Time=40.30 sec
# ARIMA(2,1,1)(2,0,1)[7] intercept   : AIC=203056.800, Time=15.55 sec
# ARIMA(2,1,0)(3,0,1)[7] intercept   : AIC=203050.978, Time=26.24 sec
# ARIMA(1,1,1)(3,0,1)[7] intercept   : AIC=203051.140, Time=27.95 sec
# ARIMA(0,1,1)(3,0,1)[7] intercept   : AIC=203908.278, Time=22.84 sec

# ARIMA(2,1,1)(3,0,1)[7] intercept   : AIC=203045.072, Time=40.30 sec
# ARIMA(2,1,1)(2,0,1)[7] intercept   : AIC=203056.800, Time=15.55 sec
# ARIMA(1,1,1)(3,0,1)[7] intercept   : AIC=203051.140, Time=27.95 sec
# ARIMA(0,1,1)(3,0,1)[7] intercept   : AIC=203908.278, Time=22.84 sec
# ARIMA(2,1,1)(3,0,1)[7] intercept   : AIC=203045.072, Time=40.30 sec
# ARIMA(2,1,1)(2,0,1)[7] intercept   : AIC=203056.800, Time=15.55 sec
# ARIMA(2,1,1)(3,0,1)[7] intercept   : AIC=203045.072, Time=40.30 sec
# ARIMA(2,1,1)(2,0,1)[7] intercept   : AIC=203056.800, Time=15.55 sec
# ARIMA(2,1,1)(3,0,1)[7] intercept   : AIC=203045.072, Time=40.30 sec
# ARIMA(2,1,1)(2,0,1)[7] intercept   : AIC=203056.800, Time=15.55 sec

# ARIMA(2,1,1)(2,0,1)[7] intercept   : AIC=203056.800, Time=15.55 sec
# ARIMA(2,1,1)(3,0,0)[7] intercept   : AIC=203232.752, Time=22.66 sec
# ARIMA(2,1,1)(3,0,2)[7] intercept   : AIC=inf, Time=70.72 sec
# ARIMA(2,1,1)(2,0,0)[7] intercept   : AIC=203245.408, Time=18.10 sec
# ARIMA(2,1,1)(2,0,2)[7] intercept   : AIC=inf, Time=48.75 sec
# ARIMA(3,1,1)(3,0,1)[7] intercept   : AIC=202014.325, Time=73.66 sec
# ARIMA(3,1,1)(2,0,1)[7] intercept   : AIC=202027.569, Time=24.37 sec
# ARIMA(3,1,1)(3,0,0)[7] intercept   : AIC=202099.548, Time=36.89 sec
# ARIMA(3,1,1)(3,0,2)[7] intercept   : AIC=inf, Time=93.55 sec
# ARIMA(3,1,1)(2,0,0)[7] intercept   : AIC=202101.387, Time=27.92 sec

# ARIMA(3,1,1)(2,0,2)[7] intercept   : AIC=202105.483, Time=41.43 sec
# ARIMA(3,1,0)(3,0,1)[7] intercept   : AIC=202976.529, Time=40.22 sec
# ARIMA(3,1,2)(3,0,1)[7] intercept   : AIC=201972.680, Time=93.30 sec
# ARIMA(3,1,2)(2,0,1)[7] intercept   : AIC=201963.228, Time=39.48 sec
# ARIMA(3,1,2)(1,0,1)[7] intercept   : AIC=202051.295, Time=39.45 sec
# ARIMA(3,1,2)(2,0,0)[7] intercept   : AIC=202040.445, Time=47.82 sec
# ARIMA(3,1,2)(2,0,2)[7] intercept   : AIC=201954.921, Time=48.68 sec
# ARIMA(3,1,2)(1,0,2)[7] intercept   : AIC=201980.933, Time=42.91 sec
# ARIMA(3,1,2)(3,0,2)[7] intercept   : AIC=201963.077, Time=80.53 sec
# ARIMA(3,1,2)(2,0,3)[7] intercept   : AIC=inf, Time=79.88 sec

# ARIMA(3,1,2)(1,0,3)[7] intercept   : AIC=201970.590, Time=79.74 sec
# ARIMA(3,1,2)(3,0,3)[7] intercept   : AIC=inf, Time=101.96 sec
# ARIMA(2,1,2)(2,0,2)[7] intercept   : AIC=201963.267, Time=46.42 sec
# ARIMA(3,1,3)(2,0,2)[7] intercept   : AIC=201947.014, Time=51.55 sec
# ARIMA(3,1,3)(1,0,2)[7] intercept   : AIC=201974.127, Time=49.92 sec
# ARIMA(3,1,3)(2,0,1)[7] intercept   : AIC=202042.713, Time=16.29 sec
# ARIMA(3,1,3)(3,0,2)[7] intercept   : AIC=inf, Time=93.69 sec
# ARIMA(3,1,3)(2,0,3)[7] intercept   : AIC=inf, Time=99.05 sec
# ARIMA(3,1,3)(1,0,1)[7] intercept   : AIC=202040.623, Time=8.82 sec
# ARIMA(3,1,3)(1,0,3)[7] intercept   : AIC=201952.321, Time=82.28 sec

# ARIMA(3,1,3)(3,0,1)[7] intercept   : AIC=201937.780, Time=79.51 sec
# ARIMA(3,1,3)(3,0,0)[7] intercept   : AIC=202041.218, Time=26.43 sec
# ARIMA(3,1,3)(2,0,0)[7] intercept   : AIC=202040.533, Time=14.87 sec
# ARIMA(2,1,3)(3,0,1)[7] intercept   : AIC=201651.597, Time=65.43 sec
# ARIMA(2,1,3)(2,0,1)[7] intercept   : AIC=201962.519, Time=38.98 sec
# ARIMA(2,1,3)(3,0,0)[7] intercept   : AIC=202044.369, Time=29.06 sec
# ARIMA(2,1,3)(3,0,2)[7] intercept   : AIC=inf, Time=71.07 sec
# ARIMA(2,1,3)(2,0,0)[7] intercept   : AIC=202044.162, Time=17.56 sec
# ARIMA(2,1,3)(2,0,2)[7] intercept   : AIC=inf, Time=54.72 sec
# ARIMA(1,1,3)(3,0,1)[7] intercept   : AIC=inf, Time=42.12 sec

# ARIMA(2,1,2)(3,0,1)[7] intercept   : AIC=201953.944, Time=46.81 sec
# ARIMA(1,1,2)(3,0,1)[7] intercept   : AIC=203005.902, Time=35.83 sec
# ARIMA(2,1,3)(3,0,1)[7]             : AIC=201649.445, Time=64.13 sec   << Best model
# ARIMA(2,1,3)(2,0,1)[7]             : AIC=201960.724, Time=37.47 sec
# ARIMA(2,1,3)(3,0,0)[7]             : AIC=202042.374, Time=29.31 sec
# ARIMA(2,1,3)(3,0,2)[7]             : AIC=inf, Time=62.47 sec
# ARIMA(2,1,3)(2,0,0)[7]             : AIC=202042.168, Time=15.36 sec
# ARIMA(2,1,3)(2,0,2)[7]             : AIC=inf, Time=46.94 sec
# ARIMA(1,1,3)(3,0,1)[7]             : AIC=inf, Time=40.11 sec
# ARIMA(2,1,2)(3,0,1)[7]             : AIC=201951.569, Time=43.07 sec

# ARIMA(3,1,3)(3,0,1)[7]             : AIC=201935.472, Time=75.85 sec
# ARIMA(1,1,2)(3,0,1)[7]             : AIC=203003.902, Time=30.21 sec
# ARIMA(3,1,2)(3,0,1)[7]             : AIC=201965.840, Time=70.86 sec

# Best model:  ARIMA(2,1,3)(3,0,1)[7]
# Total fit time: 2934.663 seconds


# print(f'Auto_ARIMA (m=21)\n')  # m=21은 계절성까지 고려하면서 메모리 부족으로 분석 중단됨됨
# auto_model = auto_arima(training, start_p=0, d=1, start_q=0,
#                         max_p=3, max_q=3,
#                         start_P=0, start_Q=0,
#                         max_P=3, max_Q=3, m=21,
#                         seasonal=True, information_criterion='aic',
#                         trace=True)

# ARIMA(0,1,0)(0,0,0)[21] intercept   : AIC=207876.244, Time=0.22 sec
# ARIMA(1,1,0)(1,0,0)[21] intercept   : AIC=203506.980, Time=10.80 sec
# ARIMA(0,1,1)(0,0,1)[21] intercept   : AIC=204579.276, Time=7.33 sec
# ARIMA(0,1,0)(0,0,0)[21]             : AIC=207874.244, Time=0.18 sec
# ARIMA(1,1,0)(0,0,0)[21] intercept   : AIC=203518.286, Time=0.82 sec
# ARIMA(1,1,0)(2,0,0)[21] intercept   : AIC=203353.330, Time=78.50 sec
# ARIMA(1,1,0)(3,0,0)[21] intercept   : AIC=203347.117, Time=120.01 sec
# ARIMA(1,1,0)(3,0,1)[21] intercept   : AIC=203348.370, Time=473.08 sec
# ARIMA(1,1,0)(2,0,1)[21] intercept   : AIC=203348.428, Time=105.15 sec
# ARIMA(0,1,0)(3,0,0)[21] intercept   : AIC=206745.354, Time=99.65 sec
# ARIMA(2,1,0)(3,0,0)[21] intercept   : AIC=203346.322, Time=343.40 sec
# ARIMA(2,1,0)(2,0,0)[21] intercept   : AIC=203352.601, Time=96.92 sec
# ARIMA(2,1,0)(3,0,1)[21] intercept   : AIC=203347.094, Time=232.40 sec
# ARIMA(2,1,0)(2,0,1)[21] intercept   : AIC=203347.370, Time=135.39 sec
# ARIMA(3,1,0)(3,0,0)[21] intercept   : AIC=203231.143, Time=170.39 sec <<< 나온 결과중 best
# ARIMA(3,1,0)(2,0,0)[21] intercept   : AIC=203237.821, Time=84.23 sec
# ARIMA(3,1,0)(3,0,1)[21] intercept   : AIC=203227.404, Time=402.57 sec
# 메모리 부족으로 이하 분석 중단


a=10
print(f'a<<2 : {a<<2}')         # 40  = 10 * (2**2) = 10 * 4
print(f'a<<4 : {a<<4}')         # 160 = 10 * (2**4) = 10 * 16
print(f'a>>2 : {a>>2:.5f}')         # 2 = 10 * (1/2**2) = 10 / 4 = 2
print(f'a>>4 : {a>>4:.5f}')         # 0 = 10 * (1/2**4) = 10 / 16 = 0