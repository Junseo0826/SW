'''
작성일 : 2023년 3월 29일
학과 : 컴퓨터 공학부
학번 : 202395025
이름 : 이준서
설명 : 수령액을 계산한다.
'''
# 1. 본봉 300만원을 본봉 변수 mon에 저장.
mon = 300

# 2. 수당 30만원을 수당 변수 ins에 저장.
ins = 30

# 3. 총액 : 본종 + 수당 총액변수 : sum
sum = mon + ins

# 4. 총액에 0.2를 곱하여 세금 계산한다. 세금 변수 : tax
tax = sum * 0.2

# 5. 수령액 = 총액 - 세금
#    수령액 변수 : total
total = sum - tax

print("수령액은 {}만원 입니다." .format(total))