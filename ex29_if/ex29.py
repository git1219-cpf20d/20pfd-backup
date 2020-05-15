# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/python3/ex29.html
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc' -> print('abc')
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))
# print 'abc', -> print('abc', end=" ")
# raw_input('abc') -> input('abc')
# 오류노트 에 각자 오류노트 작성 / Please use your error-note


사람 = 20
고양이 = 30
강아지 =15

if 사람 < 고양이:
  print("고양이가 너무 많아요! 세상은 멸망합니다!")

if 사람 > 고양이:
  print("고양이가 많지 않아요! 세상은 지속됩니다!")
  
if 사람 < 강아지:
  print("세상은 침에 젖습니다!")
  
if 사람 > 강아지:
  print("세상은 말랐습니다!")

강아지 += 5

if 사람 >= 강아지:
  print("사람은 강아지 보다 많거나 같습니다.")

if 사람 <= 강아지:
  print("사람은 강아지 보다 적거나 같습니다.")

if 사람 == 강아지:
  print("사람은 강아지와 수가 같습니다.")

print("고양이는 어떨까요?")

고양이 -= 10

if 사람 >= 고양이:
  print("사람은 고양이 보다 많거나 같습니다.")

if 사람 <= 고양이:
  print("사람은 고양이 보다 적거나 같습니다.")

if 사람 == 고양이:
  print("사람은 고양이와 수가 같습니다.")