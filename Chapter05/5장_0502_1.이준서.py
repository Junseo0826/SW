'''
작성일 : 2023년 5월 2일
학과 : 컴퓨터 공학부
학번 : 202395025
이름 : 이준서
설명 : 문제1
       1부터 입력받은 수까지의 합을 구하는 프로그램을 작성하시오.
'''
# 1. 숫자를 입력받아 정수로 변환하여 input_num에 저장한다.
input_num = int(input('숫자 입력 :'))
# 2. 합계는 0
sum = 0
# 3. 수는 1부터 시작한다. (초기값, 시작값)
num = 1
# 4. 수는 입력받은 수까지 반복하면서 (조건식, 종료값)
while num <= input_num:
#   1) 합계를 계산한다.
    sum = sum + num
#   2) 수는 1씩 증가한다. (증감식) {증감식이 없으면 무한반복한다.}
    num = num + 1
# 5. "1부터 input_num까지의 합은 sum입니다."를 출력한다.
print('1부터 {}까지의 합은 {}입니다.' .format(input_num, sum))