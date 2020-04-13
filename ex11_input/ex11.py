# coding: utf-8
# 참고문헌: https://learnpythonthehardway.org/python3/ex11.html
#          https://www.youtube.com/playlist?list=PLA6B0Lmr9oJMSQ8K3UndQ0FY0XfKByN7L
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc' -> print('abc')
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))
# print 'abc', -> print('abc', end=" ")
# raw_input('abc') -> input('abc')
# 프로그램 실행 후 대기상태이면 키보드로 입력하고 Enter /
# After starting the program, when it waits, enter a string and press Enter
# https://youtu.be/BKbmzJ5rSE4

# -*- coding: utf-8 -*-
print("몇 살이죠?", end=' ')
나이 = input()
print("키는 얼마죠?", end=' ')
키 = input()
print("몸무게는 얼마죠?", end=' ')
몸무게 = input()

print(f"네, 나이는 {나이}살, 키는 {키}cm, 몸무게는 {몸무게}kg 이네요.\a")
