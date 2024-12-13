# 실습. 손 윤곽선을 감지하고 필터를 추가하기

import cv2
import numpy as np
import matplotlib.pyplot as plt
""" 내 코드드
cap = cv2.VideoCapture(0)

plt.ion()       # 인터렉티드 모드 : 창이 열린 상태로 코드가 계속 실행됨됨
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 7)) # 서브플롯 미리 생성 
fig.show()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("프레임을 읽지 못했습니다.")
        break

    # 원본
    original = frame.copy()

    # 샤프닝 커널
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    # 윤곽선(컨투어)감지
    frame_gray = cv2.cvtColor(original, cv2.COLOR_RGB2GRAY)
    _, binary = cv2.threshold(frame_gray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    results_con = frame.copy()
    for contour in contours:
        M = cv2.moments(contour)
        if M['m00'] != 0:
            cx = int(M['m10']/ M['m00'])     # x기준 중심심
            cy = int(M['m01']/ M['m00'])     # y기준 중심심
            cv2.circle(results_con, (cx, cy), 5, (0, 0, 0), -1)   # 중심에 검은점 생성
        else : 
            print("컨투어 면적 : 0")

        # 컨투어 그리기
        cv2.drawContours(results_con, [contour], -1, (0, 255, 0), 2)   # 테두리에 녹색선 생성 (R, G, B)
        filtered_cont = cv2.filter2D(results_con, -1, kernel)

    # 출력
    ax1.clear()
    ax2.clear()
    ax3.clear()

    # plt.subplot(1, 3, 1)
    ax1.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    ax1.set_title("Original")
    ax1.axis('off')

    # plt.subplot(1, 3, 2)
    ax2.imshow(cv2.cvtColor(results_con, cv2.COLOR_BGR2RGB))
    ax2.set_title("Contours")
    ax2.axis('off')
    
    # plt.subplot(1, 3, 3)
    ax3.imshow(cv2.cvtColor(filtered_cont, cv2.COLOR_BGR2RGB))
    ax3.set_title("Filtered")
    ax3.axis('off')

    fig.canvas.draw()           # 창에 위의 plot들을 출력
    fig.canvas.flush_events()   # 
    # plt.pause(0.001)    # 창을 잠시 멈춤  (0.001:1밀리초)
    # plt.clf()           # 창에 있는 것 초기화

    # 종료조건
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()               # 비디오캡쳐 해제
cv2.destroyAllWindows()     # 윈도우창 닫기
plt.ioff()                  # 인터랙티브 모드 비활성화
plt.close('all')            # 모든 matplotlib 창 닫기

# 카메라와 루프내 else문에 있는 출력은 처리 속도가 느려서
# q를 눌러 윈도우 창이 꺼지고 한참 후에 종료 됨
# 그래서 영상에 대한 처리는 주피터노트북에서 실행하는 것은 비추

"""
"""
# 리더님 코드 ㅡ 1

# 샤프닝 필터 커널
kernal = np.array([[0, -1 ,0],
                   [-1, 7, -1],
                   [0, -1 ,0]])

# 웹캠 열기
cap = cv2.VideoCapture(0)

# 예외처리
if not cap.isOpened():
    print("영상이 열리지 않습니다.")
    exit()

plt.ion()   # 인터랙티브 모드 활성화

while True:
    ret, frame = cap.read()
    if not ret:
        print("프레임을 열 수 없습니다.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                      # 그레이스케일로 변환
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)        # 이진화 처리리
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # 컨투어 감지
    contour_frame = frame.copy()
    cv2.drawContours(contour_frame, contours, -1, (0, 255, 0),2)                # 컨투어 그리기
    sharp = cv2.filter2D(contour_frame, -1, kernal)


    # 원본 출력
    plt.subplot(2,2,1)
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.title("Original")
    plt.axis('off')

    # 컨투어 출력
    plt.subplot(2,2,2)
    plt.imshow(cv2.cvtColor(contour_frame, cv2.COLOR_BGR2RGB))
    plt.title("Contour")
    plt.axis('off')

    # 샤프닝 필터터 출력
    plt.subplot(2,2,3)
    plt.imshow(cv2.cvtColor(sharp, cv2.COLOR_BGR2RGB))
    plt.title("Filtered")
    plt.axis('off')

    plt.pause(0.001)
    plt.clf()

    key=cv2.waitKey(1)
    if key == ord('q'):
        break

# 리소스 해제
cap.release()
cv2.destroyAllWindows()
plt.ioff()      # 인터랙티브 모드 비활성화

"""

# 리더님 코드 ㅡ 2

# 샤프닝 필터 커널
kernal = np.array([[0, -1 ,0],
                   [-1, 7, -1],
                   [0, -1 ,0]])

# 웹캠 열기
cap = cv2.VideoCapture(0)

# 예외처리
if not cap.isOpened():
    print("영상이 열리지 않습니다.")
    exit()

plt.ion()   # 인터랙티브 모드 활성화
fig, axes = plt.subplots(2, 2, figsize=(10, 10))             # <-- subplot 미리 설정하는 방법 
                                                            # (fig=전체, axes에는 각 plot이 배열형태로 각각 저장)

while True:
    ret, frame = cap.read()
    if not ret:
        print("프레임을 열 수 없습니다.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                      # 그레이스케일로 변환
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)        # 이진화 처리리
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # 컨투어 감지
    contour_frame = frame.copy()
    cv2.drawContours(contour_frame, contours, -1, (0, 255, 0),2)                # 컨투어 그리기
    sharp = cv2.filter2D(contour_frame, -1, kernal)


    # 원본 출력
    axes[0,0].subplot(2,2,1)
    axes[0,0].imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    axes[0,0].set_title("Original")
    axes[0,0].axis('off')

    # 컨투어 출력
    axes[0,1].imshow(cv2.cvtColor(contour_frame, cv2.COLOR_BGR2RGB))
    axes[0,1].set_title("Contour")
    axes[0,1].axis('off')

    # 샤프닝 필터터 출력
    axes[1,0].imshow(cv2.cvtColor(sharp, cv2.COLOR_BGR2RGB))
    axes[1,0].set_title("Filtered")
    axes[1,0].axis('off')

    plt.pause(0.001)
    # plt.clf()

    key=cv2.waitKey(1)
    if key == ord('q'):
        break

# 리소스 해제
cap.release()
cv2.destroyAllWindows()
plt.ioff()      # 인터랙티브 모드 비활성화

