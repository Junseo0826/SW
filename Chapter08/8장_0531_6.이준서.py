'''
작성일 : 05월 31일
학과 : 컴퓨터공학부
학번 : 202395025
이름 : 이준서
설명 : 
        8장 파일 입출력
'''
# 5명 학생의 성적 저장 파일 만들기 실습 예제 8-2
# write() 메소드와 readline() 메소드를 이용하여
# 학생 이름과 3과목의 성적을 리스트로 생성하여 파일에 저장.
# 입력 예) 홍길동 100 95 77
with open('student.txt', 'w') as f:
    for i in range(5) :
        student = input(str(i+1) + '번 학생 이름과 3과목 성적 입력 : ')
        f.write(student + "\n")
        
print('== 학생 정보 읽어오기 ==')    
with open('student.txt', 'r') as f:
    while True :
        line = f.readline()
        
        if line == '' :
            break 
        
        print(line, end='')
        
   