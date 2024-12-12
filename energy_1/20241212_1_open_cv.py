import cv2
# 1) 이미지 컬러로 불러오기
# image_color=cv2.imread("./dog_cat.jpg", cv2.IMREAD_COLOR)
# image_gray=cv2.imread("./dog_cat.jpg", cv2.IMREAD_GRAYSCALE)

# 이미지 크기 확인
# print(image_color.shape)
# print(image_gray.shape)


# cv2.imshow("Color Image", image_color)
# cv2.imshow("Gray Image", image_gray)


# # 화면창 종료문 (데이터 누수방지 목적)
# key = cv2.waitKey(0)      # waitKey(0)은 무한대 대기 상태가 됨
# if key == ord ('q') :   # 키보드에서 q를 입력한 경우에만 
#     print(chr(key))     # 키보드 입력된 q를 출력

# # # 창 닫기 
# # cv2.destroyAllWinows()      # 모든 창 닫기
# # cv2.destroyWinow(winname)  # 지정한 창 닫기
# cv2.waitKey(2000)
# cv2.destroyAllWinows()

# 이미지 저장
# cv2.imwrite("./raw data/output-gray_image.jpg", image_gray)



image_BGR=cv2.imread(r"C:\Users\praye\Documents\Bootcamp\energy_1\dog_cat.jpg", cv2.IMREAD_COLOR)
image_color=cv2.imread(r"C:\Users\praye\Documents\Bootcamp\energy_1\dog_cat.jpg", cv2.IMREAD_COLOR)
# print(image_color.shape)        # 원본 : (427, 640, 3)

# 색상공간 변환
# HSV : Hue(색상), Saturation(채도), Value(명도)  -> 디테일한 색상 추출할때 HSV중 H를 자주 사용함
# gray = cv2.cvtColor(image_BGR, cv2.COLOR_RGB2GRAY)
# hsv = cv2.cvtColor(image_BGR, cv2.COLOR_RGB2HSV)


# 이미지 자르기 = 배열 슬라이싱  [y축배열, x축배열]
# roi = image_color[50:300, 100:300]          # 원본 파일자체를 변경함
# roi = image_color[50:300, 100:300].copy()        # 사본 파일자체를 변경함

# cv2.imshow("roi Image", image_color)
# cv2.waitKey(0)
# cv2.destroyAllWinows()

# cv2.imshow("roi Image", roi)
# cv2.waitKey(0)
# cv2.destroyAllWinows()


# # 이미지 크기 조정
# resized_image = cv2.resize(image_BGR, (300, 200))       # 사이즈 직접 지정
# scale = 0.5
# resized_image = cv2.resize(image_BGR, None, fx=scale, fy=scale) # 지정한 비율에 맞춰서 각 축별로 사이즈 변경




# # 이미지상 객체의 위치값 반환 받는 함수---------------------------
# image_color=cv2.imread(r"C:\Users\praye\Documents\Bootcamp\energy_1\dog_cat.jpg", cv2.IMREAD_COLOR)
# def mouse_click(e, x, y, flag, param):
#     if e==cv2.EVENT_LBUTTONDOWN:        # 마우스 좌클릭 누르면
#         print(f"마우스 위치 : x={x}, y={y}")

# cv2.imshow("Image", image_color)

# # 마우스 콜백함수
# cv2.setMouseCallback('Image', mouse_click)
# # 마우스 위치 : x=285, y=120
# # 마우스 위치 : x=436, y=120
# # 마우스 위치 : x=287, y=400
# # 마우스 위치 : x=424, y=401

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# # roi만 표시되도록 하는 방법---------------------------
# start, end = None, None

# def mouse_select(e, x, y, flag, param):
#     global start, end
#     if e == cv2.EVENT_LBUTTONDOWN :     # 마우스 좌클릭 누르면
#         start = (x, y)
#     elif e == cv2.EVENT_LBUTTONUP:      # 드래그 후 버튼을 놓으면
#         end = (x, y)
#         # 영역 표시
#         roi = image_color[start[1]:end[1], start[0]:end[0]].copy()
#         cv2.imshow("select", roi)

# image_color=cv2.imread(r"C:\Users\praye\Documents\Bootcamp\energy_1\dog_cat.jpg", cv2.IMREAD_COLOR)
# cv2.imshow("Image", image_color)

# # 마우스 콜백함수
# cv2.setMouseCallback('Image', mouse_select)
# # 위치로 지정한 이미지만 별도 출력

# cv2.waitKey(0)
# cv2.destroyAllWindows()



# # 이미지 회전 ---------------------------
# image_color=cv2.imread(r"C:\Users\praye\Documents\Bootcamp\energy_1\dog_cat.jpg", cv2.IMREAD_COLOR)

# (h, w) = image_color.shape[:2]        # 중심좌표 : 이미지에서 가로, 세로 정보만 가져옴
# center = (w//2, h//2)           # 이미지의 중심위치 계산

# matrix = cv2.getRotationMatrix2D(center, 180, 1.0)   # 이미지의 매트릭스 행렬 생성  (중심좌표, 회전각도, ?)
# rotated = cv2.warpAffine(image_color, matrix, (w,h))    # 행렬이용한 회전된 이미지 생성

# cv2.imshow("Image", rotated)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # 이미지 이동 ---------------------------
# import numpy as np
# image_color=cv2.imread(r"C:\Users\praye\Documents\Bootcamp\energy_1\dog_cat.jpg", cv2.IMREAD_COLOR)

# (h, w) = image_color.shape[:2]        # 이미지에서 가로, 세로 정보만 가져옴
# center = (w//2, h//2)                 # 이미지의 중심위치 계산

# matrix = np.float32([[1, 0, 100], [0, 1, 50]])      # [1, 0, x축이동], [0, 1, y축이동]
# move = cv2.warpAffine(image_color, matrix, (w, h))

# cv2.imshow("Image", move)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 실습1. 이미지 처리
# 1) 이미지 읽어서 크기 출력
import cv2
image=cv2.imread(r"C:\Users\praye\Documents\Bootcamp\energy_1\dog_cat.jpg", 
                 cv2.IMREAD_COLOR)
print(image.shape)
# cv2.imshow("Image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 2) 이미지를 흑백으로 변환하고 화면에 표시
image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
# cv2.imshow("Gray Image", image_gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 3) 이미지를 50%크기로 축소하고 새로운 창에 표시
resize_scale = 0.5
image_50 = cv2.resize(image, None, fx=resize_scale, fy=resize_scale)
# cv2.imshow("50% Image", image_50)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 4) 이미지 90도 회전하여 저장
(h, w) = image.shape[:2]
center = (w//2, h//2)

matrix = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated_image = cv2.warpAffine(image_color, matrix, (w,h))

cv2.imwrite(r"C:\Users\praye\Documents\Bootcamp\energy_1\results\output_rotated_image.jpg", 
            rotated_image)
# cv2.imshow("Rotated Image", rotated_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
