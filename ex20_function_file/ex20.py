# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/python3/ex20.html
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

script, input_file = sys.argv


def print_all(f):
  print(f.read())


def rewind(f):
  f.seek(0)


def print_a_line(line_count, f):
  print(line_count, f.readline())


with open(input_file, encoding='utf-8') as current_file:
  
  print('\n')
  print("파일 전체를 출력해 봅시다.\n")

  print_all(current_file)

  print('\n')
  print("이미 txt 파일을 한 번 읽었으므로,\n이번에는 테이프처럼 되감아 위치정보를 초기화 시켜 봅시다.")

  rewind(current_file)

  print('\n')
  print("세 줄을 출력해 봅시다.")

  print('\n')
  current_line = 1
  print_a_line(current_line, current_file)

  current_line = current_line + 1
  print_a_line(current_line, current_file)
  
  current_line = current_line + 1
  print_a_line(current_line, current_file)

  rewind(current_file)

  print('\n')
  print("이번엔 네 줄을 출력해 봅시다.")

  print('\n')
  current_line = 1
  print_a_line(current_line, current_file)

  current_line = current_line + 1
  print_a_line(current_line, current_file)
  
  current_line = current_line + 1
  print_a_line(current_line, current_file)

  current_line = current_line + 1
  print_a_line(current_line, current_file)
  print('\n')
