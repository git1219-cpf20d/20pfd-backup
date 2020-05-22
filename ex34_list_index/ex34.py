# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/python3/ex33.html
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc' -> print('abc')
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))
# print 'abc', -> print('abc', end=" ")
# raw_input('abc') -> input('abc')
# 오류노트 에 각자 오류노트 작성 / Please use your error-note

import random

animals = ['곰', '비단뱀', '공작', '캥거루', '고래', '오리너구리']
ordinals = ['첫',        '두',     '세',     '네', '다섯', '여섯']

print(f' 1) {1} 번에 있는 동물은 {animals[1]} 이다.')
print(f' 2) {ordinals[2]} 번째 동물은 {animals[2]} 이다.')
print(f' 3) {ordinals[0]} 번째 동물은 {animals[0]} 이다.')
print(f' 4) {3} 번에 있는 동물은 {animals[3]} 이다.')
print(f' 5) {ordinals[4]} 번째 동물은 {animals[4]} 이다.')
print(f' 6) {2} 번에 있는 동물은 {animals[2]} 이다.')
print(f' 7) {ordinals[5]} 번째 동물은 {animals[5]} 이다.')
print(f' 8) {4} 번에 있는 동물은 {animals[4]} 이다.')

for i in range(9, 9+6):
  k = random.randint(0, 5)
  print(f'{i:2d}) {ordinals[k]} 번째 동물은 {animals[k]} 이다.')