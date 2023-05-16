'''
작성일 : 2023년 5월 16일
학과 : 컴퓨터 공학부
학번 : 202395025
이름 : 이준서
설명 : 문제1
       10개의 정수를 입력 받아 합을 구하는 프로그램을 작성하시오.
       단, 짝수 번째에 입력되는 숫자는 양수를 음수로, 음수는 양수로 바꾸어 합을 구하시오.
'''
# 1. sum = 0
sum = 0
# 2. count = 1
count = 1
# 3. count는 1부터 10까지 반복
for count in range(1,11):
#   1) 정수 입력받아 num에 저장한다.
    num = int(input(str(count) + '{}번째 정수를 입력하세요 :'))
#   2) 만약 count % 2 == 0이면
    if count % 2 == 0:
#       2-1) sum = sum - num
        sum = sum - num
#   3) 아니면
    else :
#       3-1) sum = sum + num
        sum = sum + num
# 4. 합계 출력
print('합계는 {}입니다.' .format(sum))

print('==========================================')

count = 1
sum = 0
while count <= 10:
    num = int(input(str(count) + '{}번째 정수를 입력하세요 :'))
    if num % 1 == 0:
        num = num * -1
    sum = num + sum
    count = count + 1
print('합계는 {}입니다.' .format(sum))

print('==========================================')

count = 1
sum = 0
# while True = 무한반복 => break 사용
while True :
    num = int(input('{}번째 정수 입력 :' .format(count)))
    if count % 2 == 0:
        num = -num
# += 결합 연산자 sum = sum + num (왼쪽 부호가 먼저 계산)
    sum += num
    count += 1
    
    if count > 10:
        break
print('10개 정수의 합 : {}' .format(sum))