'''
작성일 : 2023년 4월 11일
학과 : 컴퓨터 공학부
학번 : 202395025
이름 : 이준서
설명 : 입력 받은 정수가 짝수인지 홀수인지 판단하는 프로그램을 작성하시오.
'''
# 1. 입력받은 숫자를 정수로 변환하여 숫자 변수 num에 저장한다.
num = int(input('숫자 입력 :'))
# 2. 만약 숫자가 짝수이면 :
#       1) "입력한 숫자 00는 짝수입니다."를 출력한다.
if num % 2 == 0 :
    print('입력한 숫자 {}는 짝수입니다.' .format(num))
# 3. 아니면 :
#       1) "입력한 숫자 00는 홀수입니다."를 출력한다.
else :
    print('입력한 숫자 {}는 홀수입니다.' .format(num))
# 4. 조건과 상관없이 "감사합니다."를 출력한다.
print('감사합니다.')