'''
작성일 : 05월 17일
학과 : 컴퓨터공학부
학번 : 202395025
이름 : 이준서
설명 : 
        로또 번호
'''
# 1. 로또 번호 저장 할 세트 만들기
# 2. 6번 반복하기
#       1) 1~45 사이의 값을 세트 변수에 추가
# 3. 로또 번호 출력
import random

lotto = set()
for i in range(6):
    lotto.add(random.randint(1, 45))
print('이번주 로또 번호 : ',lotto)

lotto2 = set()
while len(lotto2) != 6:
    lotto2.add(random.randint(1, 45))
print('이번주 로또 번호 : ',lotto2)

lotto3 = set()
while True :
    lotto3.add(random.randint(1, 45))
    if len(lotto3) == 6:
        break
print('이번주 로또 번호 : ',lotto3)