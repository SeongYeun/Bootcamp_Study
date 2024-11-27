#####   전처리
from sklearn.preprocessing import MinMaxScaler      # 
from sklearn.preprocessing import RobustScaler      # 
from sklearn.preprocessing import StandardScaler    # 
from sklearn.preprocessing import LabelEncoder      # train['컬럼명']=le.fit_transform(train['컬럼명'])  /  test['컬럼명']=le.transform(test['컬럼명'])
from sklearn.model_selection import train_test_split  # (train, target, test_size=0.2, random_state=0)
#####   범주형분석
from sklearn.ensemble import RandomForestClassifier # (random_state=0, max_depth=3~10, n_estimators=100~500)
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression # 범주형 분류에만 사용
from statsmodels.formula.api import logit
import xgboost as xgb       # XGBClassifier         --> target 범주가 0부터 시작해야 함 (예: 0, 1, 2, 3)
import lightgbm as lgb      # LGBMClassifier (random_state=0)
from sklearn.metrics import roc_auc_score           # roc_auc_score(y_val, pred)
from sklearn.metrics import f1_score                # f1_score(y_val, pred, average='macro')
from scipy.stats import chi2_contingency
#####   연속형분석
from sklearn.ensemble import RandomForestRegressor  # (random_state=0, max_depth=3~10, n_estimators=100~500)
from sklearn.linear_model import LinearRegression
import xgboost as xgb       # XGBRegressor (random_state=0)
import lightgbm as lgb      # LGBMRegressor (random_state=0)
from sklearn.metrics import mean_squared_error      # RMSE = mean_squared_error(y_val, pred) ** 0.5
from sklearn.metrics import r2_score                # f2 = r2_score(y_val, pred)


##### ==================  help 사용
1st : 해당 패키지 import
2nd : help(패키지명)            # --> 패키지내 서브패키지/모듈/함수 목록 출력
2nd : help(패키지명.함수명)     # --> 함수의 매개변수 및 디폴트값과 사용예시 출력


##### ==================  불러오기 w/ 컬럼별 자료형 지정
df = pd.read_csv("파일명.csv", index_col='컬럼명')      # 인덱스 컬럼 지정
df = pd.read_csv("파일명.csv", index=False)            # 인덱스 제거

##### ==================  날짜 설정/추출
df['컬럼명'] = pd.to_datetime(df['컬럼명'])     # date타입으로 타입변경
df['year'] = df['날짜컬럼명'].dt.year           # year 추출 후 별도 변수 생성
df['month'] = df['날짜컬럼명'].dt.month         # month 추출 후 별도 변수 생성
df['month'] = df['날짜컬럼명'].dt.total_seconds()/60         # 시간을 초단위로 환산 후 분으로 환산


##### ==================  출력 옵션 설정
pd.options.display.float_format = '{:.4f}'.format
pd.set_option('display.float_format', lambda x: f'{x:.2f}') 
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)


##### ==================  EDA
df.describe(include="O")


##### ==================  테이블 병합 / Join
combined = pd.concat([train, test])         # append 효과
combined = pd.merge(left=train, right=test, how="inner/left/right/outer", on='컬럼명')      # Join



##### ==================  슬라이싱
df.pop('분리할컬럼명')
df.drop('버릴컬럼명', axis=1/0, inplace=T/F)        # axis=1 : 컬럼(↓)
df.idxmax()                                         # 가장 큰 값의 인덱스명(값) 반환


##### ==================  그룹집계 ㅡ groupby + .집계매서드()






##### ==================  행 합계 / 열 합계
열 집계값 ㅡ .mean() / .sum() / .std()
행 집계값 ㅡ df.T + .mean() / .sum() / .std()
sum(기본값 : axis=0 (방향:↓))

##### ==================  표준편차
표본 표준편차(ddof=1)   : pandas >> df.std()
# 모 표준편차  (ddof=0)   : numpy  >> np.std(df)


##### ==================  정렬
df.sort_values('컬럼명', ascending=T/F, inplace=T/F)
df=sorted(columns=['컬럼명'], data=df)


##### ==================  상위 / 하위 n개
min_value = df['컬럼명'][:10].min()


##### ==================  연속형변수 도수분포표 ~ 히스토그램
import numpy as np
# 히스토그램의 구간 설정 및 빈도 계산
hist, bin_edges = np.histogram(df['연속변수명'], bins=10)
# 구간별 빈도표 생성
bin_labels = [f"{round(bin_edges[i],2)} - {round(bin_edges[i+1],2)}" for i in range(len(bin_edges)-1)]
frequency_table = pd.DataFrame({'Bin':bin_labes, 'Freq':hist})


##### ==================  연속형변수 도수분포표 ~ 줄기-잎 그래프
import numpy as np
# 줄기, 입 추출
df['stem'] = df['values'] // 10
df['leaf'] = df['values'] % 10
# 줄기-잎 도표 생성
stem_leaf = df.groupby('stem')['leaf'].apply(list).reset_index()
# 줄기-잎 도표 출력
for index, row in stem_leaf.iterrows():
	print(f"{row['stem']} | {' '.join(map(str, sorted(row['leaf'])))}")


##### ==================  스케일링 ㅡ Min-Max
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
cols = ['Customer_care_calls', 'Customer_rating', 'Cost_of_the_Product']
X_tr[cols] = scaler.fit_transform(X_tr[cols])
X_test[cols] = scaler.transform(X_test[cols])


##### ==================  스케일링 ㅡ Robust
from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
cols = ['Customer_care_calls', 'Customer_rating', 'Cost_of_the_Product']
X_tr[cols] = scaler.fit_transform(X_tr[cols])
X_test[cols] = scaler.transform(X_test[cols])


##### ==================  레이블 인코딩
from sklearn.preprocessing import LabelEncoder
cols = X_tr.select_dtypes(include='O').columns
for col in cols:
    le = LabelEncoder()
    train[col] = le.fit_transform(train[col])
    test[col] = le.transform(test[col])

le.inverse_transform()                          # 레이블인코딩 취소 (원래 데이터로 복원)

##### ==================  원핫 인코딩
dummies = df.get_dummies(df['대상컬럼명'])                            # 대상 컬럼만 원핫 인코딩
dummies = df.get_dummies(df, columns=['대상컬럼1', '대상컬럼2'])       # 대상 컬럼만 원핫 인코딩
dummies = df.get_dummies(df)                                         # df 저체를 대상으로 원핫 인코딩




##### ==================  검증데이터 분할
from sklearn.preprocessing import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(train, target, test_size = 0.2, random_state=0)


##### ==================  랜덤포레스트
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
depth = [3, 5, 7, 9, 10]
n_est = [100, 200, 300, 400, 500]
for i in depth :
	for j in n_est :
		rf_0 = RandomForestClassifier(random_state=0, max_depth=i, n_estimators=j)
		rf_0.fit(X_tr, y_tr)
		pred_0 = rf_0.predict(X_val)
		roc_auc_0 = roc_auc_score(y_val, pred_0)
		print("rf(depth : ",i, ", n_esti : ",j,")의 ROC_AUC : ", roc_auc_0) 


##### ==================  test 예측 및 csv 파일 제출
# >>> 튜닝 결과증 best 조건값으로 학습 후 test 예측
rf_0 = RandomForestClassifier(random_state=0, max_depth=5, n_estimators=400)
rf_0.fit(X_tr, y_tr)
pred = pd.DataFrame({'pred' : rf_0.predict(test)})              # 값 예측
pred = pd.DataFrame({'pred' : rf_0.predict_proba(test)})        # 확률 예측

# print(pred.head())

pred.to_csv("result.csv", index=False)
check = pd.read_csv("result.csv")
print(check)






##### ==================  로지스틱회귀 _1
from statsmodels.formula.api import logit
X = df[['Gender', 'SibSp', 'Parch', 'Fare']].copy()
Y = ['Survived']
model = logit(formula="Survived ~ Gender + SibSp + Parch + Fare", data=df).fit()
print("===========================\n")
print(model.summary())
print("===========================\n")
print(round(-0.2007, 3))   # -0.201

##### ==================  로지스틱회귀 _2
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(rnadom_state=0)
lr.fit(X_tr, y_tr)
pred = lr.predict(X_val)
print(roc_auc_score(y_val, pred[:,1]))


##### ==================  의사결정나무 DT ㅡ DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(random_state=0)
dt.fit(X_tr, y_tr)
pred = dt.predict(X_val)
print(roc_auc_score(y_val, pred[:,1]))


##### ==================  Xgboost 모델 ㅡ XGBClassifier
# ㄴ target 범주가 0부터 시작해야 함 (예: 0, 1, 2, 3)
import xgboost as xgb
xg = xgb.XGBClassifier(random_state=0)
xg.fit(X_tr, y_tr)
pred = xg.predict(X_val)
print(roc_auc_score(y_val, pred[:,1]))


##### ==================  LightGBM 모델
import lightgbm as lgb
lg = lgb.LGBMClassifier(random_state=0, verbose=-1)
lg.fit(X_tr, y_tr)
pred = lg.predict(X_val)
print(roc_auc_score(y_val, pred[:,1]))




##### ==================  교차검증 (Cross Validation)
##### ==================  교차검증 ㅡ 1) K-fold
from sklearn.model_selection import cross_val_score
score = cross_val_score(rf, train, target, cv=5, scoring='f1_macro')        # 랜덤포레스트에 대해 K=5인 교차검증 후 f1_macro 점수 리턴
print(score.mean())                                                         # 교차검증 후 K개의 점수에 대한 평균으로 성능 평가

##### ==================  변수간 독립성 검정  >  교차테이블 (관찰빈도)  > 카이제곱 검정
from scipy.stats import chi2_contingency
crosstab = pd.crosstab(df['Gender'], df['Survived'])
print("===========================\n")
print(crosstab)
# print("===========================\n")
# print(chi2_contingency(crosstab))
chi2_stats, p_chi2, dof_chi2, expe_freq = chi2_contingency(crosstab)
print("===========================\n")
print(round(chi2_stats, 3))  # 260.717


##### ==================  변수간 독립성 검정  >  교차테이블 (관찰빈도비율)  > 카이제곱 검정
# 관찰빈도표 --(비율환산)--> 상대빈도표
# 기대빈도표 --(비율환산)--> 기대비율표

# 감기약(위약) 관찰빈도 / 상대빈도표
# 1 :   아픔    : 10% = 0.1
# 2 : 조금 아픔 :  5% = 0.05
# 3 :  속쓰림   : 15% = 0.15
# 4 : 이상 없음 : 70% = 0.7
# 상대빈도(비율)을 리스트로 생성 (레이블 순서대로)
prob = [0.1, 0.05, 0.15, 0.7]
# 항암약 기대빈도 = 감기약 관찰빈도(비율) * 항암표본수(20)
expected_counts = [(0.1*20), (0.05*20), (0.15*20), (0.7*20)]            # 방법_1
expected_counts = [ x*len(df) for x in prob]                            # 방법_2


# 항암약(위약)의 관찰빈도표 산출
observed_counts = df['항암약'].value_counts().sort_index().to_list()
# 항암약(위약)의 상대빈도표 산출
print(df['항암약'].value_counts(normalize=True))            # 관찰빈도(.value_counts)를 비율(normalize=True)로 환산

# 카이제곱 검정
from scipy.stats import chisquare
chi2chisquare(f_obs=observed_counts, f_exp = expected_counts)




##### ==================  Survived / SibSp 오즈비
import numpy as np
odds_ratio = np.exp(model.params["SibSp"])
print("===========================\n")
print(odds_ratio)
print(round(odds_ratio,3))    # 0.702




##### ==================  ttest_ind : 독립 2표본 검정






##### ==================  다중 선형 회귀
