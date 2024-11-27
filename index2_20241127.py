#======= 클래스(Class) / 메서드(Method) =======
# # 1) 클래스 (생성자 없는 경우)
# # 1st : 클래스 정의
# class Car:
#     model = ""
#     cc = 0

#     # 함수추가
#     def info(self):
#         print(f"모델명 : {self.model}, 배기량 : {self.cc:,}cc")


# # 2nd : 클래스 사용
# car1 = Car()        # 인스턴스(car1)=객체 생성
# car1.model = "싼타페"
# car1.cc = 2000
# # print(f"모델명 : {car1.model}")         # --> 모델명 : 싼타페
# # print(f"배기량 : {car1.cc}cc")          # --> 배기량 : 2000cc

# car1.info()                             # --> 모델명 : 싼타페, 배기량 : 2,000cc


# # 2) 클래스 (생성자 있는 경우)
# class Car:
#     # 생성자(constructor) : 초기화 함수
#     def __init__(self, model, cc):
#         self.model = model
#         self.cc = cc

#     # 문자열 리턴 특수 메서드
#     def __str__(self):
#         return f"모델명 : {self.model}, 배기량 : {self.cc:,}cc"
    

#     def info(self):
#         print(f"모델명 : {self.model}, 배기량 : {self.cc:,}cc")

    


# car1 = Car("아반떼", 2000)
# car2 = Car("BMW", 2200)
# car1.info()                                 # --> 모델명 : 아반떼, 배기량 : 2,000cc
# car2.info()                                 # --> 모델명 : BMW, 배기량 : 2,200cc
# print(car1)                                 # --> 모델명 : 아반떼, 배기량 : 2,000cc
# print(car2)                                 # --> 모델명 : BMW, 배기량 : 2,200cc
# print("========== 승용차 리스트 ==========")
# cars = [
#     Car("소나타", 2000),
#     Car("쏘렌토", 3000),
#     Car("아반떼", 1600)
# ]
# print(cars[0])                              # --> 모델명 : 소나타, 배기량 : 2,000cc


# # 실습1. 사칙연산 클래스 만들기
# class Calculator:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
    
#     # 덧셈 메서드
#     def add(self):
#         return self.num1 + self.num2
    
#     # 뺄셈 메서드
#     def sub(self):
#         return self.num1 - self.num2

#     # 곱셈 메서드
#     def mul(self):
#         return self.num1 * self.num2

#     # 나눗셈 메서드
#     def div(self):
#         if self.num2 == 0 :
#             print("분모값이 0이므로 나눗셈을 할 수 없습니다.")
#             return None
#         else : 
#             return self.num1 / self.num2

# print(Calculator(5, 3).add())
# print(Calculator(5, 3).sub())
# print(Calculator(5, 3).mul())
# print(f"{Calculator(5, 3).div():.2f}")


# # 실습1. 사칙연산 클래스 만들기 ㅡ 리더님 코드
# class Calculator:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
    
#     def add(self, num):
#         return self.num1 + self.num2 + num          # num은 생성자가 아니기 때문에 self.없이 바로 변수로 받을 수 있음
    
#     def sub(self):
#         return self.num1 - self.num2

#     def mul(self):
#         return self.num1 * self.num2

#     def div(self):
#         if self.num2 == 0:
#             return "분모가 0이 될 수 없습니다."       # 오류 조건을 먼저 작성하는 것이 좋음
#         return self.num1 / self.num2                # else 안 써도 else 쓴것과 같은 순서로 실행되므로 else 생략가능 


# calc = Calculator(10, 7)
# print(calc.add(3))                   # --> 20
# print(calc.sub())                   # --> 3
# print(calc.mul())                   # --> 70
# print(calc.div())                   # --> 1.4285714285714286
# calc = Calculator(10, 0)
# print(calc.div())                   # --> 분모가 0이 될 수 없습니다.


# 클래스변수 vs 인스턴스변수
# 1)
# class Dog:
#     kind = "진돗개"                     # 클래스 변수

#     def __init__ (self, name):
#         self.name = name               # 인스턴스 변수

# # 인스턴스 변수 접근
# dog1 = Dog("백구")
# dog2 = Dog("초코")
# print(dog1.name)                        # --> 백구
# print(dog2.name)                        # --> 초코

# # 클래스 변수 접근
# # print(dog1.kind)                        # --> 진돗개      --> 사용 안함 (메서드인지 헷갈릴 수 있으므로)
# # print(dog2.kind)                        # --> 진돗개      --> 사용 안함 (메서드인지 헷갈릴 수 있으므로)
# print(Dog.kind)                           # --> 진돗개

# 2)
# class Example:
#     shared = "공유 변수"    # 클래스 변수

#     def __init__(self, name):
#         self.name = name    # 인스턴스 변수

# e1 = Example("A")
# e2 = Example("B")
# # 클래스 변수값 변경
# Example.shared = "변경된 공유 변수"
# print(e1.shared)                           # --> 변경된 공유 변수
# print(e2.shared)                           # --> 변경된 공유 변수
# # 인스턴스 변수값 변경
# e1.name = "C"
# print(e1.name)                              # --> C
# print(e2.name)                              # --> B


# 사번 자동부여 클래스
# class Employee:
#     serial_num = 1000       # 클래스 변수
#     # 1)
#     def __init__(self, name):
#         Employee.serial_num += 1            # 메서드내 클래스변수 표현
#         self.id = Employee.serial_num       # 사번 부여
#         self.name = name                    # 메서드내 인스턴스변수 표현
#     # 2)
#     # def __init__(self, name):
#     #     self.serial_num = 1000                # 시리얼 번호는 인스턴스로 하면 사번이 모두 1001로 됨
#     #     self.serial_num +=1
#     #     self.id = self.serial_num
#     #     self.name = name
#     # 사번 : 1001, 이름 : 홍길동
#     # 사번 : 1001, 이름 : 임꺽정
#     # 사번 : 1001, 이름 : 이몽룡
#     # 사번 : 1001, 이름 : 심청이
#     # 사번 : 1001, 이름 : 변사또
#     # 사번 : 1001, 이름 : 전우치

#     def __str__(self):
#         return f"사번 : {self.id}, 이름 : {self.name}"
    
# e1 = Employee("홍길동")
# print(e1)                               # --> 사번 : 1001, 이름 : 홍길동
# e2 = Employee("임꺽정")
# print(e2)                               # --> 사번 : 1002, 이름 : 임꺽정
# employees = [Employee("이몽룡"), Employee("심청이"), Employee("변사또"), Employee("전우치")]
# for emp in employees:
#     print(emp)
# # 사번 : 1003, 이름 : 이몽룡
# # 사번 : 1004, 이름 : 심청이
# # 사번 : 1005, 이름 : 변사또
# # 사번 : 1006, 이름 : 전우치


# # 실슴2. Supermarket 클래스
# class Supermarket:
#     def __init__(self, location, name, product, customer):
#         self.location = location
#         self.name = name
#         self.product = product
#         self.customer = customer

#     def print_location(self):
#         return f"위치 : {self.location}"
    
#     def change_category(self, new_product):
#         self.product = new_product
#         return                                    # 여기선 리턴 굳이 안해도 됨

#     def show_list(self):
#         return f"상품 : {self.product}"
    
#     def enter_customer(self):
#         self.customer += 1
#         return                                    # 여기선 리턴 굳이 안해도 됨
    
#     def show_info(self):
#         return f"위치 : {self.location}, 이름 : {self.name}, 상품 : {self.product}, 고객수 : {self.customer}"


# store1 = Supermarket("마포구 염리동", "마켓온", "음료", 12)
# print(store1.show_info())
# print(store1.print_location())
# print(store1.show_list())
# store1.change_category("아이스크림")
# print(store1.show_list())
# store1.enter_customer()
# store1.enter_customer()
# print(store1.show_info())


# 실슴2. Supermarket 클래스 ㅡ 리더님 코드 _ 방법1
# class Supermarket:
#     total_customer = 0
#     def __init__(self, location, name, product, customer):
#         self.location = location
#         self.name = name
#         self.product = product
#         self.customer = customer
#         Supermarket.total_customer += customer
    
#     def print_location(self):
#         print(f"위치 : {self.location}")

#     def change_category(self, new_product):
#         self.product = new_product

#     def show_list(self):
#         print(f"상품 : {self.product}")

#     def enter_customer(self):
#         self.customer += 1
#         Supermarket.total_customer += 1

#     def show_info(self):
#         print(f"위치 : {self.location}, 이름 : {self.name}, 상품 : {self.product}, 고객수 : {Supermarket.total_customer}")

# # 인스턴스 변수만 있는 경우
# s1 = Supermarket("마포구 염리동", "마켓온", "음료", 12)
# s1.print_location()             # --> 위치 : 마포구 염리동
# s1.show_list()                  # --> 상품 : 음료
# s1.show_info()                  # --> 위치 : 마포구 염리동, 이름 : 마켓온, 상품 : 음료, 고객수 : 12
# s2 = Supermarket("은평구 응암동", "응암마켓", "과자", 9)
# s2.show_info()                  # --> 위치 : 은평구 응암동, 이름 : 응암마켓, 상품 : 과자, 고객수 : 9
# # 클래스변수 추가 후
# s2.show_info()                  #  --> 위치 : 은평구 응암동, 이름 : 응암마켓, 상품 : 과자, 고객수 : 21
# s2.enter_customer()
# s2.show_info()                  # 위치 : 은평구 응암동, 이름 : 응암마켓, 상품 : 과자, 고객수 : 22



#======= 클래스(Class) / 정보은닉 =======
# class Person:
#     def __init__(self):
#         self._name = ""
#         self._age = 0
#     # 1) 이름
#     # 이름 설정
#     def setname(self, name):
#         self._name = name
#     # 이름 출력
#     def getname(self):
#         return self._name

#     # 2) 나이
#     # 나이 설정
#     def setage(self, age):
#         self._age = age   
#     # 나이 출력
#     def getage(self, age):
#         return self._age

# p1 = Person()
# p1.setname("홍길동")
# print(p1.getname())                 # --> 홍길동


# 실습3. 건강상태 클래스 만들기
class HealthStatus:
    hp = 100

    def __init__(self, name):
        self._name = name
        self._hp = hp
    # 이름
    def set_name(self, name):
        self._name = name
    def get_name(self):
        return self._name
    # HP
    def set_hp(self, hp):
        self._hp = hp
    def get_hp(self):
        return self._hp

    # 운동
    def workout(self, hour):
        self.hour = hour
        self.total_hour += hour
        print(f"{self.hour}시간 운동하다")
        if self._hp==100:
            return self._hp
        self._hp += 1

    # 술
    def drink(self, glass):
        self.glass = glass
        self.total_glass += glass
        print(f"술을 {self.glass}잔 마시다")
        if self._hp==0:
            return self.hp
        self._hp -= 1

    # 건강상태 출력
    def show_status(self):
        print(f"총 {self.total_hour}시간 운동하다")
        print(f"술을 총 {self.total_glass}잔 마시다")
        print(f"{self._name}의 현재 hp : {self._hp}")
        print("===============================")
    

p1 = HealthStatus()
p2 = HealthStatus()
p1.setname("나몸짱")
p1.workout(2)
p1.workout(3)
p1.drink(2)
p1.show_status()
p2.setname("나약해")
