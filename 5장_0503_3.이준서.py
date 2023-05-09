'''
작성일 : 2023년 5월 3일
학과 : 컴퓨터 공학부
학번 : 202395025
이름 : 이준서
설명 : 문제3
       1부터 10까지의 정수 중 사용자가 입력한 숫자의 배수만을 더하여 출력하는 프로그램을
       작성하시오.
'''
# 1. 정수를 입력 받는다. (배수 = input_num)
# 2. 숫자가 1부터 (num)
# 3. 합계는 0
# 4. 숫자가 10까지 반복하면서 (num)
#   a 수를 1씩 증가시킨다.
#   1) 만약에 수가 입력 받은수의 배수이면 
#       1-1) 합계를 계산한다.
#       b-1 수를 1씩 증가시킨다.
#   c 수를 1씩 증가시킨다.
#   2) 아니면 (배수가 아니면)
#       b-2 수를 1씩 증가시킨다.
#       2-1) 다시 처음으로 돌아간다. (continue)
#   d 수를 1씩 증가시킨다.
# 5. 합계를 출력한다.

input_num = int(input('정수를 입력하시오 :'))
num = 0
total = 0
while num <= 10:
       num = num + 1
       if num % input_num == 0:
              total = total + num
       else:
              continue
print('{}의 배수의 합 :{}' .format(input_num, total))

print('================================================')

input_num = int(input('정수를 입력하시오 :'))
num = 1
total = 0
while num <= 10:
       if num % input_num == 0:
              total = total + num
              num = num + 1
       else:
              num = num + 1
              continue
              num = num + 1      # continue 다음에 어떤 코드를 사용하더라도 절대로 사용되지 않는다.
print('{}의 배수의 합 :{}' .format(input_num, total))

print('================================================')

# num이 (증감식을 만나지 못하여) 계속 1이된다.
#input_num = int(input('정수를 입력하시오 :'))
#num = 0
#total = 0
#while num <= 10:
#       if num % input_num == 0:
#              total = total + num
#       else:
#              continue
#       num = num + 1
#print('{}의 배수의 합 :{}' .format(input_num, total))

print('=================== for 반복문 ===========================')

input_num = int(input('정수를 입력하시오 :'))
total = 0
for num in range(1, 11):
       if num % input_num == 0:
              total = total + num
       else:
              continue
print('{}의 배수의 합 :{}' .format(input_num, total))

print('=================== for 반복문 ===========================')

input_num = int(input('정수를 입력하시오 :'))
total = 0
for num in range(1, 11):
       if num % input_num != 0:
              continue
       else:
              total = total + num
print('{}의 배수의 합 :{}' .format(input_num, total))