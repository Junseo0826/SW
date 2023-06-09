'''
작성일 : 2023년 4월 19일
학과 : 컴퓨터 공학부
학번 : 202395025
이름 : 이준서
설명 : [숫자 -> 연산자 -> 숫자] 순으로 입력 받아 사칙연산의 결과를 출력하는 계산기 프로그램
       을 작성하시오.
       단, [+,-,*,/] 이외의 연산자를 입력하면 "해당 연산자가 없습니다."를 출력합니다.
'''
# 1. 첫번째 숫자를 정수로 변환하여 첫번째 숫자 정수 num1에 저장한다.
num1 = int(input('첫번째 숫자 입력 :'))
# 2. 두번째 숫자를 정수로 변환하여 두번째 숫자 정수 num2에 저장한다.
num2 = int(input('두번째 숫자 입력 :'))
# 3. 연산자를 연산자 변수 cal에 저장한다.
cal = input('연산자 입력 :')
# 4. 만약 cal == + 이면
#   1) num1 + num2 = 00을 출력한다.
if cal == '+':
    print('{} + {} = {}' .format(num1, num2, num1+num2))
# 5. 아니고 만약 cal == - 이면
#   1) num1 - num2 = 00을 출력한다.
elif cal == '-':
    print('{} - {} = {}' .format(num1, num2, num1-num2))
# 6. 아니고 만약 cal == * 이면
#   1) num1 * num2 = 00을 출력한다.
elif cal == '*':
    print('{} * {} = {}' .format(num1, num2, num1*num2))
# 7. 아니고 만약 cal == / 이면
#   1) num1 / num2 = 00을 출력한다.
elif cal == '/':
    print('{} / {} = {}' .format(num1, num2, num1/num2))
# 8. 아니면
#   1) "해당 연산자는 없습니다."를 출력한다.
else :
    print('해당 연산자는 없습니다.')