'''
작성일 : 2023년 5월 2일
학과 : 컴퓨터 공학부
학번 : 202395025
이름 : 이준서
설명 : 문제2
       두 수를 입력 받아 두 수 사이의 모든 정수 값을 더하여 출력하는 프로그램을 작성하시
       오.
'''
# 1. 첫번째 숫자를 입력받아 정수로 변환하여 input_num_1에 저장한다.
input_num_1 = int(input('첫번째 숫자 입력 :'))
# 1. 두번째 숫자를 입력받아 정수로 변환하여 input_num_2에 저장한다.
input_num_2 = int(input('두번째 숫자 입력 :'))

# 판단 => 변수 값 교환
if input_num_1 > input_num_2:
    temp = input_num_1
    input_num_1 = input_num_2
    input_num_2 = temp

# 2. 합계는 0
sum = 0
# 3. 수는 input_num_1부터 시작한다. (초기값, 시작값)
num = input_num_1
# 4. 수는 input_num_1에서 input_num_2까지 반복하면서 (조건식, 종료값)
while num <= input_num_2:
#   1) 합계를 계산한다.
    sum = sum + num
#   2) 수는 1씩 증가한다. (증감식) {증감식이 없으면 무한반복한다.}
    num = num + 1
# 5. "input_num1부터 input_num2까지의 합은 sum입니다."를 출력한다.
print('{}부터 {}까지의 합은 {}입니다.' .format(input_num_1, input_num_2, sum))