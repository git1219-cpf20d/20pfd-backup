# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/python3/ex13.html
#          https://youtu.be/FVum3IqlR4w
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc' -> print('abc')
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))
# print 'abc', -> print('abc', end=" ")
# 이 예제는 command-line 에서 실행시킬 것 / Please run this from the command-line
import sys

print("sys.argv =", sys.argv)
스크립트, 첫_번째, 두_번째, 세_번째 = sys.argv

print(
  (
    "스크립트 이름: %s\n"
    "첫_번째 변수: %s\n"
    "두_번째 변수: %s\n"
    "세_번째 변수: %s"
  ) % (
    스크립트, 첫_번째, 두_번째, 세_번째
  )
)
