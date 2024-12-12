# 웹 크롤링 실습 ㅡ 리더님 코드
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
import requests


#옵션객체
options = Options()
#옵션추가
options.add_argument("--start-maximized")
options.add_argument("--incognito")

service = Service()
driver = webdriver.Chrome(service=service, options=options)


# #실습1 =============================
# driver.get("https://github.com/login")

# driver.find_element(By.ID, "login_field").send_keys("ysdls")
# driver.find_element(By.ID, "password").send_keys("")
# driver.find_element(By.NAME, "commit").click()


# name = driver.find_element(By.XPATH, '//*[@id="switch_dashboard_context_left_column-button"]/span[1]/span/span[2]')
# print(f"사용자 이름은: {name.text}")
# # =====================================

# #실습2. 쇼핑몰 ==============================================================
# driver.get("https://www.11st.co.kr/")

# find = driver.find_element(By.XPATH, '//*[@id="tSearch"]/form/fieldset/input')
# find.send_keys("노트북")
# find.send_keys(Keys.ENTER)

# time.sleep(5)

# items = driver.find_elements(By.CSS_SELECTOR, ".c-search-list__item")

# for item in items:
#     name = item.find_element(By.CSS_SELECTOR, ".c-search-list__item > div .c-card-item__name > dd").text
#     price = item.find_element(By.CSS_SELECTOR, ".c-search-list__item > div .c-card-item__price > span").text
#     price = int(price.replace(",", ""))
#     if price >= 500000:
#         print(f"상품명: {name}, 가격: {price}")

# # ==============================================================================================

# EC 메서드
# EC.title_is("문자열") # 현재 페이지 제목이 지정된 문자열과 일치할때
# EC.title_contains("문자열") # 현재 페이지 제목에 문자열이 포함될때
# EC.presence_of_element_located((By.ID, "아이디값")) # DOM이 존재할때(화면표시안되도됨)
# EC.visibility_of_element_located((By.CSS_SELECTOR, "선택자")) # DOM이 존재할때(화면에표시)
# EC.presence_of_all_elements_located((By.CSS_SELECTOR, "선택자")) # DOM에 모든요소가 존재할때
# EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "선택자")) # DOM에 모든요소가 존재할떄
# EC.element_to_be_clickable((By.CSS_SELECTOR, "선택자")) # 요소가 화면에 표시되고 클릭이 가능할때
# EC.element_to_be_selected((By.CSS_SELECTOR, "선택자")) # 요소가 선택된 상태가될때




# 실습3 ============================================
driver.get("https://www.agoda.com/ko-kr")
time.sleep(3)

search = driver.find_element(By.ID, 'textInput')
search.click()
search.send_keys("도쿄")

time.sleep(3)
search.send_keys(Keys.ESCAPE)

checkin = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "check-in-box"))
)
checkin.click()
#driver.find_element(By.ID, "check-in-box").click()
#time.sleep(3)


#driver.find_element(By.XPATH, '//*[@id="DatePicker__Accessible"]/div/div[2]/div[2]/div[3]/div[1]/div[3]').click()
check_in_day = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="DatePicker__Accessible"]/div/div[2]/div[2]/div[3]/div[1]/div[3]'))
)
check_in_day.click()

driver.find_element(By.XPATH, '//*[@id="DatePicker__Accessible"]/div/div[2]/div[1]/div[3]/div[1]/div[7]').click()
driver.find_element(By.ID, 'occupancy-box').click()

tab = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="Tabs-Container"]/button'))
)
tab.click()
#driver.find_element(By.XPATH, '//*[@id="Tabs-Container"]/button').click()
#time.sleep(5)

# 마지막으로 열린 탭으로 전환
driver.switch_to.window(driver.window_handles[-1])

hotel = WebDriverWait(driver,10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".hotel-list-container h3"))
)
price = WebDriverWait(driver,10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.hotel-list-container .PropertyCardPrice__Value'))
)
hotels = driver.find_elements(By.CSS_SELECTOR, ".hotel-list-container h3")
prices = driver.find_elements(By.CSS_SELECTOR, '.hotel-list-container .PropertyCardPrice__Value')

print(f"호텔명: {hotels[0].text}, 가격: {prices[0].text}")
# ============================================

# 실습4 ======================================
# driver.get("https://www.google.com/imghp")
# time.sleep(2)

# search = driver.find_element(By.ID, "APjFqb")
# search.send_keys("코끼리")
# search.send_keys(Keys.ENTER)
# time.sleep(2)

# for i in range(5):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)

# images = driver.find_elements(By.CSS_SELECTOR, "img.YQ4gaf")
# os.makedirs("./1205/images", exist_ok=True) # 폴더생성. 존재하면 무시

# code = 1
# for image in images:
#     src = image.get_attribute("src")
#     if "https" in src:
#         #print(src)
#         res = requests.get(src)
#         #print(res.content) 
#         # res.content 이미지, 동영상 값
#         # res.status_code : 응답코드
#         # res.headers : http 헤더의 정보 반환
#         # res.url : 최종 url 반환
#         with open(f"./1205/images/img_{code}.png", "wb") as file:
#             file.write(res.content)
#         code += 1
            




input("대기")  