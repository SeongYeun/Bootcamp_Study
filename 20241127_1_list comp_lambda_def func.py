# 실습6. 함수 종합 프로그래밍 ㅡ 리더님 코드
# 초기 날씨 데이터 ㅡ [날짜 / 도시 / 일평균 기온 / 일 강수량]
weather_data = [
    ["2024-11-20", "서울", 15.2, 0.0],
    ["2024-11-20", "부산", 18.4, 0.0],
    ["2024-11-21", "서울", 10.5, 2.3],
    ["2024-11-21", "부산", 14.6, 1.2],
    ["2024-11-22", "서울",  8.3, 0.0],
    ["2024-11-22", "부산", 12.0, 0.0]
]
print(list(filter(lambda x : x[1], weather_data)))

# 1:도시의 평균 기온 계산 함수 ㅡ lambda 미사용
def avg_temperatures(weather_data):
    city = input("도시 이름을 입력하세요.: ")
    total = 0
    count = 0
    for data in weather_data:
        if data[1] == city:
            total += data[2]
            count += 1
    # print(total, count)
    return city, total/count

# 1:도시의 평균 기온 계산 함수 ㅡ lambda 사용
# def avg_temperatures(weather_data):
#     city = input("도시 이름을 입력하세요.: ")
#     temp = filter(lambda x: x[1] == city, weather_data)     # 도시 추출
#     temperatures = list(map(lambda x: x[2], temp))          # 기온 추출
#     if not temperatures:
#         return city, None
#     else:
#         return city, sum(temperatures)/len(temperatures)

# 2:최고/최저 기온 찾기 함수 ㅡ 리스트 내포 사용
def maxmin_temperatures(weather_data):
    city = input("도시 이름을 입력하세요.: ")
    temperatures = [ data[2] for data in weather_data if data[1] == city]
    if not temperatures:
        return city, None, None
    else:
        return city, max(temperatures), min(temperatures)

# # 2:최고/최저 기온 찾기 함수 ㅡ lambda 사용
# def maxmin_temperatures(weather_data):
#     city = input("도시 이름을 입력하세요.: ")
#     temp = filter(lambda x: x[1] == city, weather_data)     # 도시 추출
#     temperatures = list(map(lambda x: x[2], temp))          # 기온 추출
#     if not temperatures:
#         return city, None, None
#     else:
#         return city, max(temperatures), min(temperatures)
    
#  3:강수량 분석 함수
def total_rain_day(weather_data): 
    total_rain_day()  #  <- 강수량 분석 함수
    city = input("도시 이름을 입력하세요.: ")
    temp = filter(lambda x: x[1] == city, weather_data)     # 도시 추출
    rain = list(map(lambda x: x[3], temp))                  # 강수량 추출
    total_rain = sum(rain)                                  # 총 강수량
    rain_day = len(list(filter(lambda x : x>0, rain)))      # 비가 온 일수
    return city, total_rain, rain_day
    
# 데이터 추가 함수
def add_weather(weather_data):
    date = input("날짜를 입력하세요. (YYYY-MM-DD): ")
    city = input("도시 이름을 입력하세요.: ")
    temperatures = float(input("평균 기온을 입력하세요. (℃): "))
    rain = float(input("강수량을 입력하세요. (mm): "))
    weather_data.append([date, city, temperatures, rain])
    return city

# 전체 데이터 출력
def all_data(weather_data):
    print("\n현재 저장된 날씨 데이터:")
    for data in weather_data:
        print(f"날짜: {data[0]}, 도시: {data[1]}, 평균 기온: {data[2]}℃, 강수량: {data[3]}mm")

# 메인 프로그램 함수
def main_program():
    while True:
        print("\n[날씨 데이터 분석 프로그램]")
        print("1. 평균 기온 계산")
        print("2. 최고/최저 기온 찾기")
        print("3. 강수량 분석")
        print("4. 날씨 데이터 추가")
        print("5. 전체 데이터 출력")
        print("6. 종료")
        choice = input("원하는 기능의 번호를 입력하세요: ")
        # 1: 평균기온 계산
        if choice == "1":
            city, avg_result = avg_temperatures(weather_data) # <- 도시의 평균 기온 계산 함수
            if avg_result is None :
                print(f"{city}의 정보가 존재하지 않습니다.")
            else:
                print(f"{city}의 평균 기온: {avg_result:.2f}℃")
        # 2: 최고/최저 기온 찾기
        elif choice == "2":
            city, max_t, min_t = maxmin_temperatures(weather_data) # <- 최고/최저 기온 찾기 함수
            if max_t is None:
                print(f"{city}의 정보가 존재하지 않습니다.")
            else:
                print(f"{city}의 최고 기온: {max_t}℃, 최저 기온: {min_t}℃")
        # 3: 강수량 분석
        elif choice == "3":
            city, total_rain, rain_day = total_rain_day(weather_data) # <- 강수량 분석 함수
            print(f"{city}의 총 강수량 : {total_rain:.1f}mm")
            print(f"{city}의 비가 온 날 : {rain_day}일")
        # 4: 날씨 데이터 추가
        elif choice == "4":
            city = add_weather(weather_data) # 데이터 추가 함수
            print(f"{city}의 날씨 데이터가 추가되었습니다.")
        # 5: 날씨 데이터 출력
        elif choice == "5":
            all_data(weather_data)
        # 6: 프로그램 종료
        elif choice == "6":
            print("프로그램을 종료합니다.") 
            break
        else:
            print("1~6까지의 번호를 입력하세요.")


# 프로그램 실행 함수
main_program()





# 배운 코드 표현
# if not 변수명: 
#     return city, None
# weather_data가 전역변수이기 때문에 매개변수와 인수를 생략해도 실행에 문제는 없지만
# 전역변수라도 매개변수와 인수를 정의해주는 것이 좀더 깔끔한 코드임

# weather_data는 가변객체인 리스트로 재할당만 하지 않는다면 함수 해당 리스트내 요소를 전부 삭제해도 문제되지 않고
# global을 사용하지 않아도 함수 밖의 weather_data에 새로운 내용이 반영됨



