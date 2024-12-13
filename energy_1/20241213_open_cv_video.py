import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
# 0 : 웹캠
# 영상파일 경로를 넣어도 됨

# codec = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('./results/output.avi', codec, 20.0, (640, 480))
plt.ion()       # 인터렉티드 모드 : 창이 열린 상태로 코드가 계속 실행됨됨
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("프레임을 읽지 못했습니다.")
        break

    # 원본
    original = frame.copy()

    # 가우시안 블러
    gaussian = cv2.GaussianBlur(frame, (7, 7), 0)

    # 출력
    plt.subplot(1,2,1)
    plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    plt.title("Original")
    plt.axis('off')

    plt.subplot(1,2,2)
    plt.imshow(cv2.cvtColor(gaussian, cv2.COLOR_BGR2RGB))
    plt.title("Gaussian")
    plt.axis('off')
    
    plt.pause(0.001)    # 창을 잠시 멈춤  (0.001:1밀리초초)
    plt.clf()           # 창에 있는 것 초기화

    # 종료조건 (이 방식으로는 안꺼짐)
    # if cv2.waitKey(1) & 0xFF==ord('q'):
    #     break

    # 종료조건
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


cap.release()               # 비디오캡쳐 해제
# out.release()               # 비디오캡쳐 해제
cv2.destroyAllWindows()     # 윈도우창 닫기
plt.close()

# 윈도우플레이어 레거시는 코덱으로 제대로 플레이가 안되는 듯
# 다른 영상플레이어 프로그램에서는 녹화영상 제대로 플레이 됨
