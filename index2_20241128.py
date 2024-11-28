#======= 클래스(Class) / 추상화 =======
# 추상클래스
from abc import ABC, abstractmethod     # abc : Abstract Base Class (추상기반 클래스)

# 추상 클래스 정의
class PaymentSystem(ABC):           # ABC를 꼭 상속 받아야 추상클래스 정의 가능
    # 인증
    @abstractmethod                 # 바로 다음에 오는 메서드를 추상메서드로 지정
    def authenticate(self):         # 추상메서드 (선엄만, 구현이 있어도 오류는 안나지만 다른 언어에서는 오류남)
        pass                        # 추상메서드 에서는 pass만 입력하면 됨, 구현하는 자식클래스가 없으면 오류남

    @abstractmethod
    def process_payment(self, amount):
        pass

    def payment_info(self, amount):
        print(f"{amount}원 결제가 완료되었습니다.")


# 카카오페이 결제 구현
class KakaoPay(PaymentSystem):
    def authenticate(self):         # 오버라이드
        print("카카오페이 인증 완료되었습니다.")

    def process_payment(self, amount):
        print(F"카카오페이로 {amount:,}원을 결제합니다.")
    
pay_amount = 50000
kakao = KakaoPay()
kakao.authenticate()                    # --> 카카오페이 인증 완료되었습니다.
kakao.process_payment(pay_amount)       # --> 카카오페이로 50,000원을 결제합니다.
kakao.payment_info(pay_amount)          # --> 50000원 결제가 완료되었습니다.




#======= 클래스(Class) / 클래스 메서드 =======  많이 사용하진 않음 
# 사용목적 : 인스턴스 생략하고 메서드를 호출하고 싶을때 사용
class Converter:
    conversion_rate = 1.60934           # 단위 환산 : Mile --> Km

    @classmethod
    def miles_to_kilometer(cls, mile):
        return mile * cls.conversion_rate

# 인스턴스 생성없이 바로 클래스 메서드 사용
# (인스턴스 셍성시 일반 메서드와 구분되지 않아서 클래스 메서드에서는 인스턴스 생성하지 않음)
print(Converter.miles_to_kilometer(7))      # --> 11.26538



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2024 - birth_year
        return cls(name, age)
    
# 클래스 메서드를 통해서 객체 생성
p1 = Person.from_birth_year("홍길동", 1990)
print(p1)                               # --> ('홍길동', 34)   <<< 튜플형태
# return 값들을 cls()로 묶은 후
print(p1.name, p1.age)                  # --> 홍길동 34
print(type(p1.name), type(p1.age))      # --> <class 'str'> <class 'int'>


# 클래스 변수 사용 예
class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

    @classmethod
    def get_count(cls):
        return cls.count
    
Counter.increment()                     # 1증가
Counter.increment()                     # 1증가
print(Counter.get_count())              # --> 2


# 자식클래스의 정보유지
class Animal:
    species = "동물"

    @classmethod
    def get_species(cls):
        return cls.species
    
class Dog(Animal):
    species = "진돗개"


print(Animal.get_species())                 # --> 동물
print(Dog.get_species())                    # --> 진돗개   <<< 자식클래스의 정보 유지


class ShapeUtils:
    pi = 3.14159

    @classmethod
    def circle_are(cls, radius):
        return cls.pi * radius**2
    
    @classmethod
    def desc(cls, radius):
        area = cls.circle_are(radius)       # 같은 클래스내 다른 클래스 메서드 접근
        return (f"{radius}의 원주율은 {area}입니다.")    

print(ShapeUtils.circle_area(5))            # --> 78.5375
print(ShapeUtils.desc(5))                   # --> 5의 원주율은 78.53975입니다.





#======= 클래스(Class) / 추상화 =======  많이 사용함
# @staticmethod  데코레이터 사용
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def minus(a, b):
        return a - b
    
print(MathUtils.add(30, 40))                # --> 70
print(MathUtils.minus(10, 20))              # --> -10





# 실습. 클래스 종합 프로그래밍
# 전력사용량 원시 데이터
electricity_usage = [
    {"date": "2024-11-01", "usage": 12.5},
    {"date": "2024-11-02", "usage": 15.3},
    {"date": "2024-11-03", "usage": 10.8},
    {"date": "2024-11-04", "usage": 14.2},
    {"date": "2024-11-05", "usage": 13.6}
]
print(sum([electricity_usage[i]["usage"] for i in range(0,len(electricity_usage))])  )


# 추상클래스 ElectricityData 생성
from abc import ABC, abstractmethod
def ElectricityData(ABC):
    def __init__(self, usage, total_usage):
        self.usage = usage
        self.total_usage = total_usage
    
    # 1) 캡슐화
    # 1-1) usage_data
    # getter
    @property                          # getter의 데코레이터
    def usage_data(self):
        return self.usage_data
    
    # setter
    @usage_data.setter                 # setter의 데코레이터
    def usage_data(self, data):
        self.usage_data = data

    # 1-2) total_usage
    # getter
    @property                          # getter의 데코레이터
    def total_usage(self):
        return self.total_usage
    
    # setter
    @total_usage.setter                # setter의 데코레이터
    def total_usage(self, value):
        self.total_usage = value

    # 2) 추상메서드
    @abstractmethod
    def calculate_total_usage(self):
        pass

    @abstractmethod
    def calculate_total_usage(self, date):
        pass

    # 3) 일반메서드
    def add_usage(self, usage, new_date, new_usage):
        self.usage = usage
        self.new_date = new_date
        self.new_usage = new_usage
        self.usage_data.update([{"date":new_date, "usage":new_usage}])
        # else:    
        #     self.usage_data = self.usage_data.append([{"date":new_date, "usage":new_usage}])
    
    def remove_usage(self, usage, date):
        self.date = date
                self.date_list = [usage[i]["date"] for i in range(0, len(usage))]
        if 


    



# 자식 클래스 HomeElectricityData 생성
def HomeElectricityData(ElectricityData):
        def __init__(self, usage, total_usage):
            super().__init__(usage, total_usage)
        





        # total = sum([self.usage_datae[i]["usage"] for i in range(0,len(self.usage_data))])
        # return total





# self.total_usage = sum([self.usage_datae[i]["usage"] for i in range(0,len(self.usage_data))])