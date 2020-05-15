# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/python3/ex32.html
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc' -> print('abc')
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))
# print 'abc', -> print('abc', end=" ")
# raw_input('abc') -> input('abc')
# 오류노트 에 각자 오류노트 작성 / Please use your error-note


숫자목록 = [1,2, 3, 4, 5]
과일목록 = ['사과', '귤', '배', '살구']
잔돈목록 = [1, '십원', 2, '백원', 3, '오백원']

# 첫 번째 for 순환문은 list를 따라 돕니다.
for 숫자 in 숫자목록:
  print(f"이 수는 {숫자}")

# 위와 같습니다.
for 과일 in 과일목록:
  print(f"과일 종류: {과일}")

# 숫자와 문자열이 섞여 있는 list도 돌 수 있습니다.
for 잔돈 in 잔돈목록:
  print(f"받은 잔돈 {잔돈}")

# list를 만들 수도 있는데, 먼저 빈 것으로 시작합니다.
원소목록 = []

# 그리고 0에서 5까지 세는 range 함수를 사용합니다.
for i in range(0, 5+1):
  print(f"list에 숫자 {i}를 더합니다.")
  # append는 list가 알아듣는 함수입니다.
  원소목록.append(i)

# 이것도 출력할 수 있습니다.
for i in 원소목록:
  print(f"원소는 {i}")