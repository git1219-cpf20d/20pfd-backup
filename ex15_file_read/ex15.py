# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/python3/ex15.html
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

with open(filename, encoding='utf-8') as txt:
  print("여기 너의 파일 %r:" % filename)
  print(txt.read())

print("파일 이름을 다시 써줘:")
file_again = input("> ")

with open(file_again, encoding='utf-8') as txt_again:
  print(txt_again.read())
  