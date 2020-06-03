# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/python3/ex17.html
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc' -> print('abc')
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))
# print 'abc', -> print('abc', end=" ")
# 이 예제는 command-line 에서 실행시킬 것 / Please run this from the command-line

# -*- coding: utf-8 -*-

import sys
import os

script, src, dest = sys.argv

print(f"{src}에서 {dest}로 복사합니다.")

with open(src, encoding='utf-8') as input_file:
  input_data = input_file.read()
 # input_file 이 닫힘

print(f"입력 파일은 {len(input_data)} 바이트 입니다.")

print(f"출력 파일이 있나요? {os.path.exists(dest)}")
print(f"이제 준비가 되었습니다. 계속하려면 Enter를, 취소하려면 Ctrl+C를 누르세요.")
input("> ")

with open(dest, 'wt', encoding='utf-8') as output_file:
  output_file.write(input_data)
# output_file 이 닫힘

print("좋습니다. 이제 완료되었습니다.")
