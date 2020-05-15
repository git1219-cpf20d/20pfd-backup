# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/python3/ex30.html
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc' -> print('abc')
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))
# print 'abc', -> print('abc', end=" ")
# raw_input('abc') -> input('abc')
# 오류노트 에 각자 오류노트 작성 / Please use your error-note


사람 = 30
자동차 = 40
버스 = 15

if 자동차 > 사람:
  print("차를 타야 해요.")
elif 자동차 < 사람:
  print("차를 안타야 해요.")
else:
  print("결정할 수 없어요.")

if 버스 > 자동차:
  print("버스가 너무 많아요.")
elif 버스< 자동차:
  print("버스를 탈 수도 있어요.")
else:
  print("아직도 결정할 수 없어요.")

if 사람 > 버스:
  print("좋아요 버스를 탑시다.")
else:
  print("좋아요 그럼 전 집에 있죠.")

print('-' * 20)

사람 += 20

if 자동차 > 사람:
  print("차를 타야 해요.")
elif 자동차 < 사람:
  print("차를 안타야 해요.")
else:
  print("결정할 수 없어요.")

if 사람 > 버스:
  print("좋아요 버스를 탑시다.")
else:
  print("좋아요 그럼 전 집에 있죠.")

print('-' * 20)

버스 += 50

if 버스 > 자동차:
  print("버스가 너무 많아요.")
elif 버스< 자동차:
  print("버스를 탈 수도 있어요.")
else:
  print("아직도 결정할 수 없어요.")

if 사람 > 버스:
  print("좋아요 버스를 탑시다.")
else:
  print("좋아요 그럼 전 집에 있죠.")

print('-' * 20)

if 자동차 > 사람:
  print("차를 타야 해요.")
elif 자동차 < 사람:
  print("차를 안타야 해요.")
else:
  print("결정할 수 없어요.")

if 버스 > 자동차:
  print("버스가 너무 많아요.")
elif 버스< 자동차:
  print("버스를 탈 수도 있어요.")
else:
  print("아직도 결정할 수 없어요.")