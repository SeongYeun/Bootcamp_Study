##### ==================  레이블 인코딩
from sklearn.preprocessing import LabelEncoder
cols = X_tr.select_dtypes(include='O').columns






##### ==================  머신러닝 학습 및 튜닝
from sklearn.preprocessing import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
X_tr, X_val, y_tr, y_val = train_test_split(train, target, test_size = 0.2, random_state=0)
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
pred = pd.DataFrame({'pred' : rf_0.predict(test)})
# print(pred.head())

pred.to_csv("result.csv", index=False)
check = pd.read_csv("result.csv")
print(check)


##### ==================  표준편차
# 모 표준편차  (ddof=0)   : numpy  >> np.std(df)
# 표본 표준편차(ddof=1)   : pandas >> df.std()




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



##### ==================  로지스틱회귀
from statsmodels.formula.api import logit
X = df[['Gender', 'SibSp', 'Parch', 'Fare']].copy()
Y = ['Survived']
model = logit(formula="Survived ~ Gender + SibSp + Parch + Fare", data=df).fit()
print("===========================\n")
print(model.summary())
print("===========================\n")
print(round(-0.2007, 3))   # -0.201



##### ==================  Survived / SibSp 오즈비
import numpy as np
odds_ratio = np.exp(model.params["SibSp"])
print("===========================\n")
print(odds_ratio)
print(round(odds_ratio,3))    # 0.702






