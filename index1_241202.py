


import requests, json

url = "https://koreanjson.com/posts"
res = requests.get(url)

# print(res)              # res 코드 출력 (200 : 성공 의미)
# <Response [200]>

# print(res.json())       # JSON값으로 처리해서 출력
# --> 장문의 법조문이 출력됨

if res.status_code == 200 : 
    data = res.json()
    for i in data :
        print(f"ID: {i['id']}, 제목: {i['title']}")
else:
    print("요청 실패")
# ID: 1, 제목: 정당의 목적이나 활동이 민주적 기본질서에 위배될 때에는 정부는 헌법재판소에 
# 그 해산을 제소할 수 있고, 정당은 헌법재판소의 심판에 의하여 해산된다.
# ID: 2, 제목: 누구든지 법률에 의하지 아니하고는 체포·구속·압수·수색 또는 심문을 받지 아니 하며, 법률과 적법한 절차에 의하지 아니하고는 처벌·보안처분 또는 강제노역을 받지 아니한다.
# ID: 3, 제목: 누구든지 성별·종교 또는 사회적 신분에 의하여 정치적·경제적·사회적·문화적 생 활의 모든 영역에 있어서 차별을 받지 아니한다.
# ID: 4, 제목: 모든 국민은 주거의 자유를 침해받지 아니한다.
# ....

# ** 뷰티플숲(웹크롤링)모듈과 같이 자주 사용할 코드
with open("data.json", 'w', encoding='utf-8') as file :
    json.dump(data, file, ensure_ascii=False, indent=4)           # data, file은 필수이고 맨 처음 와야 함  / ensure_ascii가 아닌 한글로 출력하겠다는 의미
# JSON 파일에 저장된 내용
# [
#     {
#         "id": 1,
#         "title": "정당의 목적이나 활동이 민주적 기본질서에 위배될 때에는 정부는 헌법재판소에 그 해산을 제소할 수 있고, 정당은 헌법재판소의 심판에 의하여 해산된다.",
#         "content": "모든 국민은 인간으로서의 존엄과 가치를 가지며, 행복을 추구할 권리를 가진다. 모든 국민은 종교의 자유를 가진다. 국가는 농·어민과 중소기업의 자조조직을 육성하여야 하며, 그 자율적 활동과 발전을 보장한다. 모든 국민은 양심의 자유를 가진다. 누구든지 체포 또는 구속을 당한 때에는 즉시 변호인의 조력을 받을 권리를 가진다.",
#         "createdAt": "2019-02-24T16:17:47.000Z",
#         "updatedAt": "2019-02-24T16:17:47.000Z",
#         "UserId": 1
#     },
#     {
#         "id": 2,
#         "title": "누구든지 법률에 의하지 아니하고는 체포·구속·압수·수색 또는 심문을 받지 아니하며, 법률과 적법한 절차에 의하지 아니하고는 처벌·보안처분 또는 강제노역을 받지 아니한다.",
#         "content": "형사피고인은 유죄의 판결이 확정될 때까지는 무죄로 추정된다. 형사피고인은 유죄의 판결이 확정될 때까지는 무죄로 추정된다. 모든 국민은 행위시의 법률에 의하여 범죄를 구성하지 아니하는 행위로 소추되지 아니하며, 동일한 범죄에 대하여 거듭 처벌받지 아니한다. 모든 국민은 행위시의 법률에 의하여 범죄를 구성하지 아니하는 행위로 소추되지 아니하며, 동일한 범죄에 대하여 거듭 처벌받지 아니한다. 모든 국민은 고문을 받지 아니하며, 형사상 자기에게 불리한 진술을 강요당하지 아니한다.",
#         "createdAt": "2019-02-24T16:17:47.000Z",
#         "updatedAt": "2019-02-24T16:17:47.000Z",
#         "UserId": 1
#     },




