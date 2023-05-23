'''
작성일 : 05월 23일
학과 : 컴퓨터공학부
학번 : 202395025
이름 : 이준서
설명 : 
       6장 시퀀스 자료형
       04. 리스트
'''
# 리스트 생성
list1 = [1,2,3,4,5]
print("list1 내용 : ", list1)
print("list1 자료형 : ", type(list1))

list2 = [1, 'one', (1,2,3), "python"]
print("list2 내용 : ", list2)
print("list2 자료형 : ", type(list2))

language = 'python'
list3 = list(language)
print("list3 내용 : ", list3)
print("list3 자료형 : ", type(list3))

tuple1 = (1,2,3,4,5)
list4 = list(tuple1)
print("list4 내용 : ", list4)
print("list4 자료형 : ", type(list4))

# 사전은 키와 값으로 구성되어 있다.
# 리스트로 변환하면 키만 리스트로 생성된다.
dic1 = {1:'one', 2:'two', 3:'three'}
list5 = list(dic1)
print("list5 내용 : ", list5)
print("list5 자료형 : ", type(list5))

# 1~9까지 정수를 리스트로 생성하시오.
list6 = list(range(1,101))
print("list6 내용 : ", list6)
print("list6 자료형 : ", type(list6))

# 리스트 내용 삽입, 삭제
list1[2] = (1,2,3)  # 2번지에 튜플 삽입(덮어쓰기-교환)
print("list1 내용 : ", list1)

del list1[0]    # 0번지 삭제
print("list1의 첫번째 요소 삭제 후 내용 : ", list1)

# 합계 계산 sum() 함수 사용
# print("list1의 요소들의 합 : ", sum(list1)) # 오류 = 데이터 타입이 다름

list7 = [1,2,3,4,5]
print('list7의 요소들의 합 : ', sum(list7))
print('list7의 요소 중 최댓값 : ', max(list7))
print('list7의 요소 중 최솟값 : ', min(list7))

# 리스트 메소드 활용
# append(), count(), insert(), remove(), sort(), pop(), index()

# 좋아하는 과일 리스트를 생성하시오. 좋아하는 순서대로
fruits = ['사과', '포도', '산딸기', '수박']
print('내가 좋아하는 과일 리스트 : ', fruits)

# 3번째로 좋아하는 과일을 출력하시오.
print('세 번째로 좋아하는 과일 : ', fruits[2])

# 4번째로 좋아하는 과일을 '두리안'으로 바꾸시오.
fruits[3] = '두리안'
print('내가 좋아하는 과일 리스트(두리안 교체) : ', fruits)

# 마지막에 '바나나'를 추가하시오.
fruits.append('바나나')
print('내가 좋아하는 과일 리스트(바나나 추가) : ', fruits)

# 수박을 삭제하시오.
fruits.pop(3)   # index(주소)로 접근
print('내가 좋아하는 과일 리스트(수박 삭제) : ', fruits)

# 바나나를 삭제하시오.
fruits.remove('바나나') # 내용 입력으로 삭제
print('내가 좋아하는 과일 리스트(바나나 삭제) : ', fruits)

# 빈 리스트 animal 에 토끼, 강아지, 고양이를 차례대로 추가하시오.
animal = []
animal.append('토끼')
animal.append('강아지')
animal.append('고양이')
print('줄을 서시오 ~ ', animal)

# 강아지 앞에 여우가 새치기를 합니다.
animal.insert(1, '여우')
print('줄을 서시오 ~ (여우 삽입)', animal)

# 사전순으로 정리하시오.(오름차순)
animal.sort()
print('가나다순으로 줄을 서시오 ~ ', animal)

# 역순으로 정리하시오.(내림차순)
animal.reverse()
print('역순으로 줄을 서시오 ~ ', animal)

# 몇 마리의 동물들이 줄을 서 있는지 알려주시오.
print('몇 마리가 있나요? ', len(animal), '마리')