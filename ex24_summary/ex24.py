# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/python3/ex24.html
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc' -> print('abc')
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))
# print 'abc', -> print('abc', end=" ")
# raw_input('abc') -> input('abc')
# 오류노트 에 각자 오류노트 작성 / Please use your error-note

print("모든 것을 연습해봅시다.")
print('\\을 이용해 \n 새 행이나 \t 탭을 입력하는 탈출문자열에 대해 \'알아야만\'한다고 합니다.')

시 = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print('-'*20)
print(시)
print('-'*20)

다섯 = 10 - 2 +  3 - 6
print(f"이 값은 다섯입니다: {다섯}")
def 비밀_공식(시작):
  젤리알 = 시작 * 500
  그릇 = 젤리알 / 1000
  상자 = 그릇 / 100
  return 젤리알, 그릇, 상자
시작점 = 10000
젤리, 그릇, 상자 = 비밀_공식(시작점)

# 문자열 형식을 지정하는 다른 방법이 있습니다.
print("시작점: {}".format(시작점))

# f 문자열을 쓰는 것과 같습니다.
print(f"젤리 {젤리}알, {그릇}그릇, {상자}상자가 있습니다.")

시작점 *= 0.1

print("이렇게 할 수도 있습니다.")
공식 = 비밀_공식(시작점)

# 리스트를 포멧 문자열에 적용하는 방법입니다.
print("젤리 {}알, {}그릇, {}상자가 있습니다.".format(*공식))