# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/python3/ex19.html
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc' -> print('abc')
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))
# print 'abc', -> print('abc', end=" ")
# raw_input('abc') -> input('abc')

def cheese_and_crackers(cheese_count, boxes_of_crackers):
  print('치즈가 %d 개 있어요!' % cheese_count)
  print('크래커가 %d 상자 있어요!' % boxes_of_crackers)
  print('파티를 벌이기에 충분하네요!')
  print('담요 한 장 가져 오세요.\n')


print('함수에 그냥 숫자를 직접 줄 수 있습니다.')
cheese_and_crackers(20, 30)

print('스크립트의 변수를 쓸 수도 있고요.')
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print('안에서 계산을 해도 됩니다.')
cheese_and_crackers(10 + 20, 5 + 6)

print('합쳐서 변수도 쓰고 계산도 할 수 있습니다.')
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)
