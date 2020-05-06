# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/python3/ex21.html
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc' -> print('abc')
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))
# print 'abc', -> print('abc', end=" ")
# raw_input('abc') -> input('abc')
# 오류노트 에 각자 오류노트 작성 / Please use your error-note

def 더하기(a, b):
  print(f"덧셈 {a} + {b}")
  return a + b


def 빼기(a, b):
  print(f"뺄셈 {a} - {b}")
  return a - b


def 곱하기(a, b):
  print(f"곱셈 {a} * {b}")
  return a * b


def 나누기(a, b):
  print(f"나눗셈 {a} / {b}")
  return a / b


print("함수만으로 계산해봅시다")

나이_yr = 더하기(15, 10)
키_cm = 빼기(200, 18)
몸무게_kg = 곱하기(29, 3)
아이큐 = 나누기(450, 3)

print("나이: %d, 키: %d, 몸무게: %d, 아이큐: %d" % (나이_yr, 키_cm, 몸무게_kg, 아이큐))

# 추가 점수 문제, 아무렇게나 쓰세요.
print('\n')
print("문제를 하나 드리겠습니다.")

값 = 더하기(나이_yr, 빼기(키_cm, 곱하기(몸무게_kg, 나누기(아이큐, 2))))

print("결과:", 값, "손으로 계산할 수 있나요?")
