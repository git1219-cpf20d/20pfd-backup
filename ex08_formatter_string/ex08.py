# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/python3/ex8.html
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc' -> print('abc')
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))
# print 'abc', -> print('abc', end=" ")

formatter = "{} {} {} {}"
formatter2 = "%r %r %r %r"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
  "Try your",
  "Own text here",
  "Maybe a poem",
  "Or a song about fear"
))

print(formatter2 % (5, 6, 7, 8))