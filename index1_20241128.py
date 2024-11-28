#======= 클래스(Class) / 상속 =======
# 1) 부모클래스 w/o 생성자
# class Animal:                       # 부모 클래스
#     def speak(self):
#         print("동물이 소리를 냅니다.")
    
#     def move(self):
#         print("동물이 움직입니다.")

# class Cat(Animal):                  # 자식 클래스(상속받은 부모클래스)
#     def meow(slef):
#         print("야옹~!")

# cat = Cat()         # 자식 클래스의 객체 생성
# # 자식 클래스 객체에 부모 메서드 호출
# cat.speak()         # 동물이 소리를 냅니다.
# cat.move()          # 동물이 움직입니다.
# cat.meow()          # 야옹~!



# # 2) 부모클래스 w/ 생성자
# class Animal:                                       # 부모 클래스
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name}가 소리를 냅니다.")

#     def move(self):
#         print(f"{self.name}가 움직입니다.")
    
# class Cat(Animal):                                  # 자식 클래스(상속받은 부모클래스)
# # 부모 클래스에 생성자에 대해 자식 클래스에서도 생성자 설정해줘야 함
#     def __init__(self, name, sound="야옹"):         # 변수는 부모 클래스 먼저, 자식클래스 변수 나중에  (관례)
#         super().__init__(name)                      # <<<  부모클래스 생성자를 호출
#         self.sound = sound
    
#     def meow(self):
#         print(f"{self.name}가 {self.sound}소리 냅니다.")        # 부모클래스내 변수명(name) 그대로 사용 (관례)
    
# cat = Cat("장화")
# cat.speak()             # --> 장화가 소리를 냅니다.
# cat.move()              # --> 장화가 움직입니다.
# cat.meow()              # --> 장화가 야옹소리 냅니다.
# cat = Cat("장화", "캬아악")
# cat.meow()              # --> 장화가 캬아악소리 냅니다.

# # 3) 다중상속
# class Engine:                               # 부모클래스_1
#     def __init__(self, horsepower):
#         self.horsepower = horsepower
#         self.count = count

# class Wheels:                               # 부모클래스_2
#     def __init__(self, count):
#         self.count = count
    
# class Car(Engine, Wheels):                   # 자식클래스 (다중상속)
#     def __init__(self, horsepower, count, wheel_count):
#         Engine.__init__(self, horsepower, count)   # self 입력해야 함
#         Wheels.__init__(self, wheel_count)        # self 입력해야 함

#     def info(self):
#         print(f"이 자동차는 {self.horsepower} 마력과 {self.wheel_count}개의 바퀴를 가지고 있다.")
    
#     def test(self):
#         print(f"어디? {self.count}")
    

# car = Car(100, 50, 4)
# car.info()                  # --> 이 자동차는 100 마력과 4개의 바퀴를 가지고 있다.
# car.test()                  # --> 어디? 4



# 클래스명.mro()
# print(Car.mro())
# [<class '__main__.Car'>, <class '__main__.Engine'>, <class '__main__.Wheels'>, <class 'object'>]





# #======= 클래스(Class) / 다형성 =======
# # 오버라이딩 : 자식 클래스에서 부모 클래스내 메서드를 재정의
# class Parent:
#     def greet(self):
#         print("안녕하세요. 부모 클래스입니다.")

# class Child(Parent):
#     def greet(self):                                # 부모클래스내 메서드를 재정의
#         super().greet()
#         print("안녕하세요. 자식 클래스입니다.")

# p = Parent()
# c = Child()
# p.greet()                   # --> 안녕하세요. 부모 클래스입니다.
# c.greet()                   # --> 안녕하세요. 자식 클래스입니다.

# # 자식클래스 greet 매서드내에 super.greet()추가 후
# c.greet()                   # --> 안녕하세요. 자식 클래스입니다.
# # 안녕하세요. 부모 클래스입니다.
# # 안녕하세요. 자식 클래스입니다.



# 실습. 상속과 오버라이딩
class Product:                      # 부모 클래스
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # 재고 업데이트 메서드
    def update_quantity(self, amount):
        self.quantity += amount
        print(f"{self.name} 재고가 {amount}만큼 {'증가' if amount > 0 else '감소'}했습니다. 현재 재고: {self.quantity}")

    # 상품 정보 출력 메서드
    def display_info(self):
        print(f"상품명: {self.name}")
        print(f"가격: {self.price}원")
        print(f"재고: {self.quantity}개")

class Electronic(Product):
    def __init__(self, name, price, quantity, warranty_period=12):
        super().__init__(name, price, quantity)
        self.warranty_period = warranty_period

    # 보증기간 연장 메서드
    def extend_warranty(self, months):
        self.warranty_period += months
        print(f"보증 기간이 {months}개월 연장되었습니다. 현재 보증기간 : {self.warranty_period}개월")
        
    # 상품 정보 출력 메서드 (오버라이딩)
    def display_info(self):
        super().display_info()
        print(f"보증 기간 : {self.warranty_period}개월")

class Food(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date
    
    # 유통기한 유효 여부 확인 메서드
    def is_expired(self, current_date):
        self.current_date = current_date
        if self.current_date > self.expiration_date :
            print(f"{self.name} 는 유통기한이 지났습니다.")
        else :
            print(f"{self.name} 는 유통기한이 지나지 않았습니다.")
        
    # 상품 정보 출력 메서드 (오버라이딩)
    def display_info(self, current_date):
        super().display_info()
        self.is_expired(current_date)

tv = Electronic("스마트 TV", 1500000, 5, 24)
tv.display_info()
tv.extend_warranty(12)
tv.display_info()

apple = Food("사과", 3000, 50, "2024-11-10")
apple.is_expired("2024-11-05")
apple.is_expired("2024-11-11")
apple.display_info("2024-11-05")
apple.display_info("2024-11-11")
