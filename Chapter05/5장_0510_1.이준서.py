'''
작성일 : 2023년 5월 10일
학과 : 컴퓨터 공학부
학번 : 202395025
이름 : 이준서
설명 : 문제1
       사용자로부터 하나의 정수를 입력 받아 다음과 같이 *을 출력하는 프로그램을 작성하
       시오.
       
       정수 입력 : 4
       *
       **
       ***
       ****
'''
# 1. 정수를 입력받는다.
input_line = int(input('정수 입력 :'))
# 2. 줄은 1부터 입력받은 수 까지
for line in range(1,input_line+1):
#   1) 별은 1부터 줄까지
    for star in range(1,line+1):
#       1-1) 별을 출력한다.
        print('*', end=' ')
#   2) 줄을 바꿔준다.
    print()         # 줄바꿈
    

input_line = int(input('정수 입력 :'))
for line in range(input_line):
    for star in range(line+1):
        print('*', end=' ')
    print()         # 줄바꿈