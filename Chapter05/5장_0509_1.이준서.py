'''
작성일 : 2023년 5월 9일
학과 : 컴퓨터 공학부
학번 : 202395025
이름 : 이준서
설명 : 문제1
       정수를 입력 받아 입력 받은 수가 소수인지 아닌지 판단하는 프로그램을 작성하시오.
'''
# 1. 정수를 입력받는다.
input_num = int(input('정수를 입력하시오 :'))
# 2. num을 2부터 입력받은 정수까지 반복한다.
for num in range(2, input_num+1):
#   1) 만약 input_num % num == 0이면
    if input_num % num == 0:
#   2)    멈춘다.
        break
# 3. 만약 input_num == num이면
if input_num == num:
#   1) "input_num은 소수입니다."를 출력한다.
    print('{}은 소수입니다.' .format(input_num))
# 4. 아니면
else :
#   1) "input_num은 소수가 아닙니다."를 출력한다.
    print('{}은 소수가 아닙니다.' .format(input_num))
if input_num // num == 1:
    print('{}은 소수입니다.' .format(input_num))
else :
    print('{}은 소수가 아닙니다.' .format(input_num))

print('=======================================')

input_num = int(input('정수를 입력하시오 :'))
count = 0
for num in range(2, input_num+1):
    if input_num % num == 0:
        count = count + 1
if count == 1:
    print('{}은 소수입니다.' .format(input_num))
else :
    print('{}은 소수가 아닙니다.' .format(input_num))