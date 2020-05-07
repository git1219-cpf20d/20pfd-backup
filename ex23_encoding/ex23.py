# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/python3/ex23.html
#         http://eclass.kpu.ac.kr/ilosfiles/editor-file/0A5852CD36/201902/795852C031795A5BCB33785053CF.png
#         https://learnpythonthehardway.org/python3/languages.txt
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))
# print 'abc', -> print('abc', end=" ")
# 이 예제는 command-line 에서 실행시킬 것 / Please run this from the command-line


import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
  line = language_file.readline()

  if line:
    print_line(line, encoding, errors)
    return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
  next_lang = line.strip()
  raw_bytes = next_lang.encode(encoding, errors=errors)
  cooked_string = raw_bytes.decode(encoding, errors=error)

  print(raw_bytes, "<===>", cooked_string)


with open("languages.txt") as languages:
  main(languages, input_encoding, error)
