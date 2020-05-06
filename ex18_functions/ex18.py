# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/python3/ex18.html
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc' -> print('abc')
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))
# print 'abc', -> print('abc', end=" ")
# raw_input('abc') -> input('abc')

# argv를 쓴 스크립트와 비슷한 함수
def print_two(*args):
  print('args = %r' % str(args))
  arg1, arg2 = args
  print('실행인자1: %r, 실행인자2: %r' % (arg1, arg2))


# 좋아요. 사실 *args 는 필요가 없습니다. 그냥 이렇게 하죠.
def print_two_again(arg1, arg2):
  print('실행인자1: %r, 실행인자2: %r' % (arg1, arg2))


# 이 함수는 실행인자를 하나만 받습니다.
def print_one(arg1):
  print('실행인자1: %r' % arg1)


# 이 함수는 실행인자를 하나도 받지 않습니다.
def print_none():
  print('아무것도 받지 않음')


print_two('IT1', 'Gong2')
print_two_again('IT3', 'Gong4')
print_one('First!5')
print_none()
