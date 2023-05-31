'''
작성일 : 05월 31일
학과 : 컴퓨터공학부
학번 : 202395025
이름 : 이준서
설명 : 
        8장 파일 입출력      
'''
# writelines() 메소드
list1 = ['월요일\n','화요일\n','수요일\n','목요일\n','금요일\n','토요일\n','일요일\n']

# readlines() 메소드 사용하여 파일의 모든 내용을 리스트로 변환
print('== 리스트로 반환 ==')
with open('linetest.txt', 'r') as f :
    textlist = f.readlines()        # f.readlines => 파일의 내용을 리스트로 반환해준다.
    print(textlist)
    print('textlist 자료형 : ', type(textlist))