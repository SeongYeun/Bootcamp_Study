# # 실습1. github 크롤링
# from selenium import webdriver                              
# from selenium.webdriver.chrome.service import Service       
# from webdriver_manager.chrome import ChromeDriverManager    
# from selenium.webdriver.common.by import By                 
# from selenium.webdriver.common.keys import Keys             
# import time                                                 
# from selenium.webdriver.chrome.options import Options       

# # 웹 여는 옵션 설정
# options = Options()
# options.add_argument("--start-maximized")
# options.add_argument("--disable-notifications")
# options.add_argument("--incognito")
# service = Service(ChromeDriverManager().install())        
# driver = webdriver.Chrome(service=service, options=options)

# # 웹 열기
# driver.get("https://github.com/login")
# print("\n\n")
# print(driver.title)
# print(driver.current_url,"\n")

# # 로그인
# id_github = 'sandra.s.kang@gmail.com'
# pw_github = "aaa"
# id_input = driver.find_element(By.XPATH, '//*[@id="login_field"]')
# pw_input = driver.find_element(By.XPATH, '//*[@id="password"]')
# id_input.send_keys(id_github)
# pw_input.send_keys(pw_github)
# pw_input.send_keys(Keys.ENTER)

# # 사용자 대시보드 > 프로필로 이동
# icon_1 = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[2]/div[3]/deferred-side-panel/include-fragment/react-partial-anchor/button/span/span/img")
# icon_1.click()
# profile = driver.find_element(By.XPATH, '//*[@id=":rf:"]')
# profile.click()

# time.sleep(3)
# # 사용자 이름/프로필 관련 정보 크롤링
# user_name = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/main/div/div/div[1]/div/div/div[1]/div[2]/h1/span[2]')
# print(f"사용자 이름 : {user_name.text}\n\n")

# driver.quit()

##### 출력물 #####
# Sign in to GitHub · GitHub
# https://github.com/login 

# 사용자 이름 : SeongYeun


# user_status = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/main/div/div/div[1]/div/div/div[2]/div/form')
# print(f"사용자 상태 : {user_status.text.strip()}")




# # 실습2. 쇼핑몰 크롤링하기
# from selenium import webdriver                              
# from selenium.webdriver.chrome.service import Service       
# from webdriver_manager.chrome import ChromeDriverManager    
# from selenium.webdriver.common.by import By                 
# from selenium.webdriver.common.keys import Keys             
# import time                                                 
# from selenium.webdriver.chrome.options import Options       

# # 웹 여는 옵션 설정
# options = Options()
# options.add_argument("--start-maximized")
# options.add_argument("--disable-notifications")
# options.add_argument("--incognito")
# service = Service(ChromeDriverManager().install())        
# driver = webdriver.Chrome(service=service, options=options)

# # 웹 열기
# driver.get("https://shopping.naver.com/ns/home")
# print("\n\n")
# print(driver.title)
# print(driver.current_url,"\n")

# # 특정 검색어로 검색
# search_input = driver.find_element(By.XPATH, '//*[@id="gnb-gnb"]/div[2]/div/div[2]/div[1]/form/div/div/div/div/input')
# search_product = "로봇청소기"
# search_input.send_keys(search_product)
# search_input.send_keys(Keys.ENTER)
# print(search_product,"\n")

# # 검색 결과에서 가격이 50만원 이상인 상품 이름과 가격 추출
# price_input = driver.find_element(By.XPATH, '//*[@id="filter_min_price"]')
# minimum_price = "500000"
# price_input.send_keys(minimum_price)
# price_input.send_keys(Keys.ENTER)
# print(minimum_price)

# # 상품명과 상품가격 추출
# products_name = driver.find_elements(By.CLASS_NAME, "basicProductCardInformation_title__Bc_Ng")
# products_price = driver.find_elements(By.CLASS_NAME, "priceTag_inner_price__TctbK")
# products_price = [i.text for i in products_price]
# products_price = [products_price[i].replace("\n", "") for i in range(len(products_price))]
# n = 5
# products = list(zip(products_name[:n], products_price[:n]))
# for name, price in products:
#     print(f"제품명 : {name.text}")
#     print(f"\tㄴ> 제품가격 : {price}")
# time.sleep(3)
# driver.quit()


# # 실습3. 여행사이트 크롤링하기
from selenium import webdriver                              
from selenium.webdriver.chrome.service import Service       
from webdriver_manager.chrome import ChromeDriverManager    
from selenium.webdriver.common.by import By                 
from selenium.webdriver.common.keys import Keys             
import time                                                 
from selenium.webdriver.chrome.options import Options      
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait

# 웹 여는 옵션 설정
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--incognito")
service = Service(ChromeDriverManager().install())        
driver = webdriver.Chrome(service=service, options=options)

# 웹 열기
driver.get("https://www.agoda.com/ko-kr/?ds=GYW6AMvPqobehvmv")
print("\n\n")
print(driver.title)
print(driver.current_url,"\n")


# ================  EC 메서드  ================ #
# EC.title_is('title') # 현재 웹페이지의 탭 이름(title)이 지정된 문자열과 일치할때
# EC.title_contains('title') # 현재 웹페이지의 탭 이름(title)에 지정된 문자열이 포함될때
# EC.presence_of_element_located((By.ID, "아이디값")) # DOM이 존재할때 (화면에 안보이는 것도)
# EC.presence_of_all_elements_located((By.CSS_SELECTOR, "선택자")) # DOM에 모든요소가 존재할때 ㅡ 많이 사용됨
# EC.visibility_of_element_located((By.CSS_SELECTOR, "선택자")) # DOM이 존재할때 (화며에 보이는 것만)
# EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "선택자"))  # DOM에 모든요소가 존재할때 (화면에 보이는 것만) ㅡ 많이 사용됨
# EC.element_to_be_clickable((By.CSS_SELECTOR, "선택자")) # 화면에 표시되는 요소가 클릭이 가능할 때
# EC.element_to_be_selected((By.CSS_SELECTOR, "선택자"))  # 요소가 선택된 상태가 될때



# 도시 검색
search_click = driver.find_element(By.XPATH, '//*[@id="autocomplete-box"]').click()
search = "바르셀로나"
search_input = driver.find_element(By.XPATH, '//*[@id="textInput"]')
search_input.send_keys(search)

search_resutl_1 = driver.find_element(By.CSS_SELECTOR, 'ul.AutocompleteList > li')
search_resutl_1.click()
# print(search_resutl_1.text,"\n")
time.sleep(5)
# 일정 선택
start_date = "2024-12-16"
end_date = "2024-12-19"
checkin = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(By.CSS_SELECTOR, f'[data-selenium-date="{start_date}"]')
)
# start = driver.find_element(By.CSS_SELECTOR, f'[data-selenium-date="{start_date}"]').click()
checkin.click()
print(start_date)
end = driver.find_element(By.CSS_SELECTOR, f'[data-selenium-date="{end_date}"]').click()
print(end_date)
find = driver.find_element(By.XPATH, '//*[@id="Tabs-Container"]/button').click()
time.sleep(15)
# 검색 결과중 첫번째 숙소 정보
driver.switch_to.window(driver.window_handles[-1]) # 마지막 열린 탭으로 이동
print("윈도우창 전환")
# dynamic-style-typographystyle-452 ae7b2-ae7b2-box ae7b2-inline ae7b2-m-none           <<< class가 여러개인 상황 (스페이스바로 구분된 상황)
# hotel_name = driver.find_elements(By.CSS_SELECTOR, "h3.dynamic-style-typographystyle-452.ae7b2-ae7b2-box.ae7b2-inline.ae7b2-m-none")
hotel_name = driver.find_elements(By.CSS_SELECTOR, ".hotel-list-container h3")
hotel_name = [i.text for i in hotel_name]
print(hotel_name[1])
# dynamic-style-typographystyle-489 ae7b2-ae7b2-box ae7b2-m-none
classname = "dynamic-style-typographystyle-643 ae7b2-ae7b2-box ae7b2-m-none"
classname = classname.replace(" ",".")
print(classname)
hotel_price = driver.find_elements(By.CLASS_NAME, classname)
hotel_price = [i.text for i in hotel_price]
print(hotel_price[1])

time.sleep(30)

# # driver.quit()


# # 실습4. 이미지 크롤링하기
# from selenium import webdriver                              
# from selenium.webdriver.chrome.service import Service       
# from webdriver_manager.chrome import ChromeDriverManager    
# from selenium.webdriver.common.by import By                 
# from selenium.webdriver.common.keys import Keys             
# from selenium.webdriver.chrome.options import Options       
# import os, requests, time

# # 웹 여는 옵션 설정
# options = Options()
# options.add_argument("--start-maximized")
# options.add_argument("--disable-notifications")
# options.add_argument("--incognito")
# service = Service(ChromeDriverManager().install())        
# driver = webdriver.Chrome(service=service, options=options)

# # 웹 열기
# driver_path = 'path/to/chromedriver'
# driver = webdriver.Chrome()  #executable_path=driver_path
# driver.get("https://images.google.com/?hl=ko")
# print("\n\n")
# print(driver.title)
# print(driver.current_url,"\n")

# # 동물 검색
# search_input = driver.find_element(By.ID, 'APjFqb')
# search = "강아지"
# search_input.send_keys(search)
# search_input.send_keys(Keys.ENTER)
# time.sleep(3)

# # 무한스크롤 적용
# scroll_times=3
# # <div jscontroller="XW992c" jsmodel="sFFyCd" class="wIjY0d jFk0f" jsdata="JDto1e;_;Ck7eZ8" jsaction="rcuQ6b:npT2md" data-hveid="CBIQAA">
# for _ in range(scroll_times):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)
# print("스크롤 완료")


# # 이미지 순차 저장
# imgs = driver.find_elements(By.CSS_SELECTOR, ".mNsIhb img")
# os.makedirs("./imgs", exist_ok=True)    # 저장할 폴더 생성
# # folder_add = os.path.join(os.path.expanduser("~"), 'dog_imgs')       # 저장위치 절대경로 생성
# # img = driver.find_elements(By.CLASS_NAME, "czzyk.XOEbc")
# # for i, img in enumerate(imgs):
# #     img_src = img.get_attribute('src')
# #     file_path = os.path.join(folder_add, f"dog_img_{i}.png")
# #     print(img_src)
# #     # with open(file_path, 'wb') as f:
# #     #     f.write(img_src)

# for i, img in enumerate(imgs): 
#     img_url = img.get_attribute('src') 
#     if img_url: 
#         img_data = requests.get(img_url).content 
#         file_path = os.path.join("./imgs", f"dog_img_{i}.png") 
#         with open(f"./dog_imgs/dog_{i}.png", 'wb') as file: 
#             file.write(img_data)
# # links = driver.find_elements(By.TAG_NAME, 'a')
# # for link in links: 
# #     href = link.get_attribute('href') 
# #     print(href)
#     # with open(f"dog_{i}.png", 'wb') as img_file:
#     #     img_file.write(link)
