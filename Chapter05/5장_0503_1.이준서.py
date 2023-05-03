'''
작성일 : 2023년 5월 2일
학과 : 컴퓨터 공학부
학번 : 202395025
이름 : 이준서
설명 : 문제1
       사용자로부터 입력 받은 숫자에 해당하는 구구단을 출력하는 프로그램을 작성하시오.
'''
# 알고리즘 for
# 1. 숫자를 입력받아 정수로 변환한 후 input_num에 저장한다.
input_num = int(input('숫자 입력 :'))
print('{} 단' .format(input_num))
# 2. 곱하는 수를 1~9까지 반복하면서:
for num in range(1,10):
#   1) 구구단을 출력한다.
    print('{} * {} = {}' .format(input_num, num, input_num*num))



# 알고리즘 while
# 1. 숫자를 입력받아 정수로 변환한 후 input_num01에 저장한다.
input_num01 = int(input('숫자 입력 :'))
print('{} 단' .format(input_num01))
# 2. 수는 1부터 시작한다.
num01 = 1
# 3. 수는 1부터 9까지 반복하면서
while num01 <= 9:
#   1) 구구단을 출력한다.
    print('{} * {} = {}' .format(input_num01, num01, input_num01*num01))
#   2) 수는 1씩 증가한다.
    num01 = num01 + 1