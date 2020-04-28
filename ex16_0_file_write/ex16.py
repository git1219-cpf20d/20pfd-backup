# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/python3/ex16.html
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc' -> print('abc')
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))
# print 'abc', -> print('abc', end=" ")
# raw_input('abc') -> input('abc')
# 이 예제는 command-line 에서 실행시킬 것 / Please run this from the command-line

# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print("%r 파일을 지우려 합니다." % filename)
print("취소하려면 CTRL+C(^C)를 누르세요.")
print("진행하려면 리턴을 누르세요.")

input("?")

print("파일 여는 중...")
target = open(filename, 'w', encoding='utf-8')
print("파일 내용을 지웁니다. 안녕히!")

print("이제 세 줄에 들어갈 내용을 묻겠습니다.")

line1 = input("1행: ")
line2 = input("2행: ")
line3 = input("3행: ")

print("이 내용을 파일에 씁니다.")

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print('마지막으로 닫습니다.')
target.close()
