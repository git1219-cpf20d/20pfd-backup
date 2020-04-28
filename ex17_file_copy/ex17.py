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

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("%s에서 %s로 복사합니다" % (from_file, to_file))

# 이 두 줄은 한줄로도 쓸 수 있습니다. 어떻게 할까요?
in_file = open(from_file, encoding="utf-8")
indata = in_file.read()

print("입력 파일은 %d 바이트 입니다" % len(indata))

print("출력 파일이 존재하나요? %r" % exists(to_file))
print("준비되었습니다. 계속하려면 리턴 키를, 취소하려면 CTRL-C를 누르세요.")
input()

out_file = open(to_file, 'w', encoding='utf-8')
out_file.write(indata)

print("좋습니다. 모두 완료되었습니다.")

out_file.close()
in_file.close()
