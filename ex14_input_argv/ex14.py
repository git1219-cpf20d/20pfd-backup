# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/python3/ex14.html
#          https://youtu.be/tNObT7IeUfo
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc' -> print('abc')
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))
# print 'abc', -> print('abc', end=" ")
# raw_input('abc') -> input('abc')
# 이 예제는 command-line 에서 실행시킬 것 / Please run this from the command-line

import sys

스크립트, 사용자_이름 = sys.argv
프롬프트 = '> '
# python 3.6 이상에서만 가능
print(f"안녕하십니까? {사용자_이름}, 나는 {스크립트} 스크립트 입니다.")
# 다른 프로그래밍 언어에서도 비슷한 방식 사용
print("안녕하십니까? %s, 저는 %s 스크립트입니다." % (
  사용자_이름, 스크립트
  )
)
print("몇가지 질문을 하겠습니다.")
print(f"{사용자_이름}, 저를 좋아하십니까?")
좋아 = input(프롬프트)

print("f{사용자_이름}, 어디에 사십니까?")
사는_곳 = input(프롬프트)

print(f"이번주 주말에 무엇을 하십니까?")
할_일 = input(프롬프트)

print(f"""
좋아요. 저를 좋아하십니까? 질문에는 {좋아}.
주소는 {사는_곳} 입니다. 어딘지는 잘 모르겠습니다.
그리고 주말에는 {할_일}을 합니다. 멋져요.
""")
