# selenium

from selenium import webdriver                              # 웹 프로그램 실행
from selenium.webdriver.chrome.service import Service       # 웹 프로그램 설치
from webdriver_manager.chrome import ChromeDriverManager    # 크롬 드라이버관련
from selenium.webdriver.common.by import By                 # find의 By 사용시
from selenium.webdriver.common.keys import Keys             # send_keys에서 Keys 사용시
import time                                                 # 화면 대기(sleep) 사용
from selenium.webdriver.chrome.options import Options       # 웹 프로그램 실행시 옵션 적용

# driver = webdriver.Chrome()
# driver.get("https://www.naver.com/")
# print(driver.title)
# driver.quit()             # quit()를 해줘 데이터 누수가 없음

# driver_E = webdriver.Edge()
# driver_E.get("https://www.naver.com/")
# print(driver_E.title)

# GUI없이 백그라운드에서 웹 화면 열기 ㅡ Oprtions 이용
options = Options()
options.add_argument("--start-maximized")
#options.add_argument("--headless")
options.add_argument("--disable-notifications")
options.add_argument("--incognito")
service = Service(ChromeDriverManager().install())        # 크롬 브라우저 설치
driver = webdriver.Chrome(service=service, options=options)


# # GUI를 이용한 웹 화면 열기
# service = Service(ChromeDriverManager().install())        # 크롬 브라우저 설치
# driver = webdriver.Chrome(service=service)
# driver.maximize_window()                                # 웹 창 크기 최대화

driver.get("https://www.google.com/")
print(driver.title)
print(driver.current_url)
# 무한스크롤페이지의 스크롤내리기
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")      
# 현재 윈도우창(window.)의 스크롤하기(scrollTo) 문서의 body 길이만큼(document.body.scrollHeight)

# 대기
driver.implicitly_wait(5) # 최대 5초동안 대기 / 찾는 요소가 나타나면 5초 대기 무시하고 바로 다음 명령문 실행



# 검색창
# search_input = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
# print(search_input)

# # 검색어
# search_input.send_keys("파이썬 코딩연습")
# search_input.send_keys(Keys.ENTER)


# # 화면 스크린샷
# driver.save_screenshot("screenshotByphthon.png")
# driver.save_screenshot("./1204/screenshotByphthon.png")
# 경로 지정할때 : .(현재위치)/하위폴더명/.../파일명.png


# # 검색어 삭제
# time.sleep(2)
# search_input.clear()

# Gmail (링크주소(href) 추출)
email_text=driver.find_element(By.XPATH, '//*[@id="gb"]/div/div[1]/div/div[1]/a')
href = email_text.get_attribute("href")
print(href)                  # --> https://mail.google.com/mail/&ogbl
print

input("대기")

driver.quit()               # quit()을 해줘야 데이터 누수가 없음
