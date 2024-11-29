# 파일 입출력

# 1) 파일 쓰기
# with open("file_in_out_test.txt", "w", encoding="utf-8") as file:   # 파일없으면 신규 생성
#     file.write("안녕하세요\n")                     # with문에서 \n 없으면 한 출로 계속 작성됨
#     file.write("파이썬 쓰기연습\n")

# --> 같은 폴더 위치에 "안녕하세요 파이썬 쓰기 연습" 내용이 포함된 신규파일 생성
# ** "w" : 기존 파일에 덮어쓰기가 됨

# 파일 추가
# with open("file_in_out_test.txt", "a", encoding="utf-8") as file:
#     file.write("내용추가 using 'a' \n")
#     file.write("11111111 \n")

# ** 기존 내용을 지우지 않고 그 아래에 해당 내용이 추가됨
# ** 숫자도 문자(열)로 입력해야 내용이 추가 됨

# 리스트 내용을 파일에 추가
# lines = ['첫번째\n', '두번째\n', '세번째\n']
# with open("file_in_out_test_2.txt", "w", encoding="utf-8") as file:
#     file.writelines(lines)


# with open("user.txt", "w", encoding="utf-8") as file:
#     while True:
#         line = input("파일에 넣을 문자열 입력(종료하려면 '종료' 입력): ")
#         if line == "종료":
#             print("입력을 종료합니다.\n")
#             break
#         file.write(line + "\n")
# git bash에서 입력내용 및 출력
# 파일에 넣을 문자열 입력(종료하려면 '종료' 입력): 동해물과
# 파일에 넣을 문자열 입력(종료하려면 '종료' 입력): 백두산이
# 파일에 넣을 문자열 입력(종료하려면 '종료' 입력): 마르고
# 파일에 넣을 문자열 입력(종료하려면 '종료' 입력): 닳도록
# 파일에 넣을 문자열 입력(종료하려면 '종료' 입력): 하느님이
# 파일에 넣을 문자열 입력(종료하려면 '종료' 입력): 보우하사
# 파일에 넣을 문자열 입력(종료하려면 '종료' 입력): 우리나라
# 파일에 넣을 문자열 입력(종료하려면 '종료' 입력): 만세
# 파일에 넣을 문자열 입력(종료하려면 '종료' 입력): 종료
# 입력을 종료합니다.



# 2) 파일 읽기
# (기존 파일이 인코딩 되었으면 읽을때도 같은 인코딩 필요)
# with open("user.txt", "r", encoding="utf-8") as file:
#     print(file.read())
# # git bash 출력결과
# # 해물과
# # 백두산이
# # 마르고
# # 닳도록
# # 하느님이
# # 보우하사
# # 우리나라
# # 만세


# with open("user.txt", "r", encoding="utf-8") as file:
#     print(file.readline())
#     print(file.readline())

# # # git bash 출력결과  (한줄씩 공백이 생김)
# # 동해물과
# # 
# # 백두산이
# # 

# with open("user.txt", "r", encoding="utf-8") as file:
#     print(file.readlines())
# # # ['동해물과\n', '백두산이\n', '마르고\n', '닳도록\n', '하느님이\n', '보우하사\n', '우리나라\n', '만세\n']

# with open("user.txt", "r", encoding="utf-8") as file:
#     line = file.readline()
#     while line:
#         print(line.strip())
#         line = file.readline()
# # 동해물과
# # 백두산이
# # 마르고
# # 닳도록
# # 하느님이
# # 보우하사
# # 우리나라
# # 만세


# with open("user.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()
#     for idx, value in enumerate(lines):
#         print(f"{idx} 인덱스의 값은 {value.strip()}입니다.")
# # 0 인덱스의 값은 동해물과입니다.
# # 1 인덱스의 값은 백두산이입니다.
# # 2 인덱스의 값은 마르고입니다.
# # 3 인덱스의 값은 닳도록입니다.
# # 4 인덱스의 값은 하느님이입니다.
# # 5 인덱스의 값은 보우하사입니다.
# # 6 인덱스의 값은 우리나라입니다.
# # 7 인덱스의 값은 만세입니다.

 
# 3) 바이너리 파일 ㅡ 영상, 이미지, 음성 등


