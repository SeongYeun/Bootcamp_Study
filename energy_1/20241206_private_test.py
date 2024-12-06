import matplotlib.pyplot as plt
from IPython.display import display
# %matplotlib inline
# 데이터 준비
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# 그래프 그리기
plt.plot(x, y)

# 타이틀과 레이블 추가
plt.title("Simple Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# 그래프 보이기 (IPython 디스플레이 사용)
display(plt.gcf())
# plt.show()