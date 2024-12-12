# 실습. 클래스 종합 프로그래밍 ㅡ 리더님 코드
# 전력사용량 원시 데이터
electricity_usage = [
    {"date": "2024-11-01", "usage": 12.5},
    {"date": "2024-11-02", "usage": 15.3},
    {"date": "2024-11-03", "usage": 10.8},
    {"date": "2024-11-04", "usage": 14.2},
    {"date": "2024-11-05", "usage": 13.6}
]

# 추상클래스
from abc import ABC, abstractmethod
class ElectricityData(ABC):
    def __init__(self, usage_data, total_usage=0):
        self._usage_data = usage_data
        self._total_usage = total_usage

    # 캡슐화(getter, setter) ㅡ 정보 은닉
    @property
    def usage_data(self):
        return self._usage_data
    
    @usage_data.setter                      # getter, setter 만들때 init에서의 매개변수를 그대로 메서드명으로 사용하는 것이 좋음
    def usage_data(self, new_data):
        self._usage_data = new_data
    
    @property
    def total_usage(self):
        return self._total_usage

    @total_usage.setter    
    def total_usage(self, new_total):
        self._total_usage = new_total

    # 추상메서드
    @abstractmethod
    def calculate_total_usage(self):
        pass

    @abstractmethod
    def get_usage_on_date(self, date):
        pass

    # 일반메서드
    def add_usage(self, date, usage):
        self._usage_data.append({"date":date, "usage":usage})

    def remove_usage(self, date):
        self._usage_data = [ i for i in self._usage_data if i['date']!=date]


# **** 자식 클래스내에서 부모 클래스이 생성자를 필요시 입력
#      입력하지 않아도 되고, 생성자 생략하면 자동으로 부모 클래스내 생성자를 확인


# 자식클래스
class HomeElectricityData(ElectricityData):

    # 추상메서드 구현
    def calculate_total_usage(self):        # 총 전력사용량 반환
        self.total_usage = sum( i['usage'] for i in self.usage_data)             # 부모 추상 클래스내 getter/setter를 super(). 또는 self.로 호출 가능

    def get_usage_on_date(self, date):
        for i in self.usage_data:
            if i['date'] == date :
                return i['usage']

    # 클래스메서드
    @classmethod
    def filter_date(cls, usage_data, start_date, end_date):
        filter_data = [ i for i in usage_data if start_date<= i['date'] <= end_date ]
        return cls(filter_data)

    # 정적메서드
    @staticmethod
    def max_usage(usage_data):
        return max(usage_data, key= lambda x: x["usage"])
        # 람다대신 usage_data["usage"] 사용해도 되는지?  ->  안됨
        # 람다는 해당 객체의 각 요소단위로 접근
        # x = 각 딕셔너리 1행
        # key = x['usage']

home = HomeElectricityData(electricity_usage)
home.calculate_total_usage()
print("총 전력 사용량", home.total_usage)
# --> 총 전력 사용량 66.4
print("특정날짜", home.get_usage_on_date("2024-11-05"))
# --> 특정날짜 13.6
home.add_usage("2024-11-29", 11.0)
print(home.usage_data)
# --> [{'date': '2024-11-01', 'usage': 12.5}, {'date': '2024-11-02', 'usage': 15.3}, {'date': '2024-11-03', 'usage': 10.8}, {'date': '2024-11-04', 'usage': 14.2}, {'date': '2024-11-05', 'usage': 13.6}, {'date': '2024-11-29', 'usage': 11.0}]
home.remove_usage("2024-11-02")
print(home.usage_data)
# --> [{'date': '2024-11-01', 'usage': 12.5}, {'date': '2024-11-03', 'usage': 10.8}, {'date': '2024-11-04', 'usage': 14.2}, {'date': '2024-11-05', 'usage': 13.6}, {'date': '2024-11-29', 'usage': 11.0}]

result = HomeElectricityData.filter_date(electricity_usage, "2024-11-03", "2024-11-05")
print(result.usage_data)
# --> [{'date': '2024-11-03', 'usage': 10.8}, {'date': '2024-11-04', 'usage': 14.2}, {'date': '2024-11-05', 'usage': 13.6}]
max_result = HomeElectricityData.max_usage(electricity_usage)
print(max_result)
# --> {'date': '2024-11-02', 'usage': 15.3}

