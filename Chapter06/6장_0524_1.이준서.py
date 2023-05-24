'''
작성일 : 05월 24일
학과 : 컴퓨터공학부
학번 : 202395025
이름 : 이준서
설명 : 
       6장 시퀀스 자료형
       05. 튜플
'''
# 튜플 생성
tuple1 = ()     # 빈 튜플 생성
tuple2 = ('a',)     # 원소가 하나여도 쉼표는 필수!!!!!!
tuple3 = ('a','b','c')

color = ('blue','black','green','black','white','white','white')
print('color 내용 : ', color)
print('color의 길이 : ', len(color))
print('white의 개수 : ', color.count('white'))
print('green의 위치 : ', color.index('green'))

# 실습 예제 6-7
# 2개의 튜플을 하나의 리스트로 만들기
fruit = ('사과', '배', '망고', '수박', '딸기')
price = (2000, 4000, 7000, 13000, 10000)

# 결과 : (사과, 2000, 배, 4000 ....)
fp_list = []    # 두개의 튜플이 저장될 리스트 생성
fp_tuple = ()   # 두개의 튜플이 저장될 튜플 생성
for i in range(len(fruit)):
    fp_list.append(fruit[i])
    fp_list.append(price[i])
#    fp_tuple.append(fruit[i])          # 튜플은 변경 불가 (append 사용 X)
#    fp_tuple.append(price[i])
print('과일 목록', fruit)
print('가격 목록', price)
print('과일의 가격 리스트 : ', fp_list)