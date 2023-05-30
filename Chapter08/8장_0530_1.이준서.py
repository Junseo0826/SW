'''
작성일 : 05월 30일
학과 : 컴퓨터공학부
학번 : 202395025
이름 : 이준서
설명 : 
        8장 파일 입출력
'''
# open() 함수로 파일 쓰기 - write() 메소드
f = open('C:/Users/Public/Documents/test.txt', 'w')   # 파일 오픈(쓰기)

# 파일에 쓸 내용
for i in range(1, 11):
    f.write('{}번째 메세지입니다. \n' .format(i))

f.close()   # 파일 종료