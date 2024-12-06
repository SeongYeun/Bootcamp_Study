import numpy as np


# a1 = np.array([1, 2, 3, 4, 5])
# a2 = np.array([[1, 2, 3], [4, 5, 6]])
# a3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print(a1)
# print(a2)
# print(a3)
# print(a1.shape)     # (5,)
# print(a2.shape)     # (2, 3)
# print(a3.shape)     # (2, 2, 2)
# print(a2.ndim)      # 2  ㅡ 배열의 차원 리턴
# print(a2.dtype)     # int64 ㅡ 데이터형 리턴
# print(a2.itemsize)  # 8  ㅡ 
# print(a2.size)      # 6  ㅡ 전체 요소 개수 반환


# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr[1,2])     # 6  ㅡ [행idx, 열idx]로 요소 리턴
# row=[0,2]
# col=[2,2]
# print(arr[row, col])    # [3 9] ㅡ 각 idx에 해당하는 요소를 배열로 리턴


# arr = np.array([10, 20, 30, 40, 50])
# print(arr[arr>20])          # [30 40 50]
# print(arr[arr%20==0])       # [20 40]

# arr[arr>20]=0
# print(arr)                  # [10 20  0  0  0]

# lists = [1, 2]
# print(arr[lists])           # [20  0]


# zero = np.zeros((3, 3))
# one = np.ones((4,5))
# print(zero)                # 3 x 3 배열에 0으로 채워짐
# print(one)                 # 4 x 5 배열에 1으로 채워짐

# # arange ㅡ 값의 간격이 정해졌을때 사용
# ranges = np.arange(1,20, 3)
# print(ranges)               # [ 1  4  7 10 13 16 19]

# # linspace ㅡ 값의 개수가 정해졌을때 사용
# linspaces = np.linspace(0, 2, 10)
# print(linspaces)            # [0.         0.22222222 0.44444444 0.66666667 0.88888889 1.11111111 1.33333333 1.55555556 1.77777778 2.        ]


# arr = np.array(np.arange(1, 10))
# reshapeed = np.reshape(arr, (3,3))
# print(reshapeed)
# # [[1 2 3]
# #  [4 5 6]
# #  [7 8 9]]

# resized = np.resize(arr, (4,4))
# print(resized)
# # [[1 2 3 4]
# #  [5 6 7 8]
# #  [9 1 2 3]
# #  [4 5 6 7]]

# # 리스트 연산 vs Numpy배열 연산
# list_a = [1, 2, 3, 4]
# list_b = [5, 6, 7, 8]

# arr_a = np.array(list_a)
# arr_b = np.array(list_b)

# print(list_a + list_b)      # [1, 2, 3, 4, 5, 6, 7, 8]
# print(arr_a + arr_b)        # [ 6  8 10 12]

# # print(list_a * list_b)    # 오류
# print(arr_a * arr_b)        # [ 5 12 21 32]

# arr_c = np.array([1, 4, 9, 16, 25, 36])
# print(np.sqrt(arr_c))       # [1. 2. 3. 4. 5. 6.]
# print(np.exp(arr_c))        # 지수값 ㅡ [2.71828183e+00 5.45981500e+01 8.10308393e+03 8.88611052e+06 7.20048993e+10 4.31123155e+15]
# print(np.log(arr_c))        # 자연로그 ㅡ [0.         1.38629436 2.19722458 2.77258872 3.21887582 3.58351894]
# print(np.pi)                # 3.141592653589793

# # 라디안값과 삼각함수 
# angles = np.array([ 0, np.pi/6, np.pi/4, np.pi/3, np.pi/2 ])  # 0도, 30도, 45도, 60도, 90도
# print(np.sin(angles))               # [0.         0.5        0.70710678 0.8660254  1.        ]
# print(np.cos(angles))               # [1.00000000e+00 8.66025404e-01 7.07106781e-01 5.00000000e-01 6.12323400e-17]
# print(np.tan(angles))               # [0.00000000e+00 5.77350269e-01 1.00000000e+00 1.73205081e+00 1.63312394e+16]


# # 배열 합치기 ㅡ hstack / vstack  / (column_stack)
# list_a = [1, 2, 3]
# list_b = [4, 5, 6]
# list_c = [7, 8]

# arr_a = np.array(list_a)
# arr_b = np.array(list_b)
# arr_c = np.array(list_c)

# hstacked = np.hstack( (arr_a, arr_b) )
# vstacked = np.vstack( (arr_a, arr_b) )
# c_stacked = np.column_stack( (arr_a, arr_b) )
# # vstacked = np.vstack( (arr_b, arr_c) )      # 두 배열 크기가 달라서 오류 발생함
# print(hstacked)             # [1 2 3 4 5 6]
# print(vstacked)
# # [[1 2 3]
# #  [4 5 6]]
# print(c_stacked)
# # [[1 4]
# #  [2 5]
# #  [3 6]]


# # 배열 나누기 ㅡ hsplit / vsplit
# print(vstacked)
# # [[1 2 3]
# #  [4 5 6]]
# print(np.hsplit(vstacked, 3))       # 가로(h)축을 분할
# # [array([[1], [4]]), 
# #  array([[2], [5]]), 
# #  array([[3], [6]])]
# print(np.vsplit(vstacked, 2))       # 세로(v)축을 분할
# # [array([[1, 2, 3]]), array([[4, 5, 6]])]

# l_a = [1, 2, 3, 4, 5]
# a = np.array([1, 2, 3, 4, 5])
# num = 10
# # print(num + l_a)        # 자료형이 int(num)와 list(l_a)로 달라서 오류 남
# print(num + a)              # [11 12 13 14 15]


# # 브로드캐스팅 ㅡ shape이 달라도 알아서 맞춰서 계산이 되어짐
# a2 = np.array([[1, 2, 3], [4, 5, 6]])
# a4 = np.array([10, 20, 30])
# combine = a2 + a4
# print(combine)
# # [[11 22 33]
# #  [14 25 36]]


# # 실습. 야구기록 데이터 정렬
# from bs4 import BeautifulSoup
# import requests, time
# import numpy as np

# # 1) 웹 크롤링
# kbo_url = "https://www.koreabaseball.com/Record/TeamRank/TeamRankDaily.aspx"
# res = requests.get(kbo_url)
# soup = BeautifulSoup(res.text, 'html.parser')

# kbo_data = [ i.text for i in soup.select("table.tData td")]
# lists = [0, 1, 3, 4, 5, 6]
# kbo_data = [value for idx, value in enumerate(kbo_data) if idx%12 in lists][:60]
# # print(kbo_data)

# kbo_ranks = np.array(kbo_data).reshape((10,6))
# head = np.array(['순위', '팀', '승', '패', '무', '승률'])
# result = np.vstack((head, kbo_ranks))
# # print(result)
            
# with open ("2024kbo.txt", "w", encoding="utf-8") as file : 
#     file.write("========== 2024 한국 프로야구 성적표 ==========\n")
#     for row in range(len(result)) :
#         for col in range(result.shape[1]):
#             file.write(f"{result[row][col]:<5}\t")
#         file.write("\n")

# with open ("2024kbo.txt", "r", encoding="utf-8") as f : 
#     data = f.read()
#     print(data)



# # 실습. 야구기록 데이터 정렬 ㅡ 리더님 코드
# from bs4 import BeautifulSoup
# import requests
# import numpy as np

# # url
# url = "https://www.koreabaseball.com/Record/TeamRank/TeamRankDaily.aspx"
# res = requests.get(url)
# soup = BeautifulSoup(res.text, "html.parser")
# table = soup.find("table", attrs={"class": "tData"})
# values = table.find_all("tr")[1:]

# lists = []
# # 순위 정렬
# for val in values:
#     tds = val.find_all("td")
#     tds = [ i.text.strip() for i in tds ]
#     lists.append([tds[0], tds[1], tds[3], tds[4], tds[5], tds[6]])
# print(lists)
# arr = np.array(lists)
# print(arr)

# file_name = "kbo_2024_ranking.txt"
# header = "순위\t팀\t승\t패\t무\t승률"

# with open(file_name, 'w', encoding='utf-8') as file:
#     # 헤더쓰기
#     file.write(header + "\n")
#     for data in arr:
#         file.write("\t".join(data) +"\n")

# with open(file_name, 'r', encoding='utf-8') as file:
#     print(file.read())

