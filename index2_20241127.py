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


# 실습1. 사칙연산 클래스 만들기
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    # 덧셈 메서드
    def add(self):
        return self.num1 + self.num2
    
    # 뺄셈 메서드
    def sub(self):
        return self.num1 - self.num2

    # 곱셈 메서드
    def mul(self):
        return self.num1 * self.num2

    # 나눗셈 메서드
    def div(self):
        if self.num2 == 0 :
            print("분모값이 0이므로 나눗셈을 할 수 없습니다.")
            return None
        else : 
            return self.num1 / self.num2

print(Calculator(5, 3).add())
print(Calculator(5, 3).sub())
print(Calculator(5, 3).mul())
print(f"{Calculator(5, 3).div():.2f}")

