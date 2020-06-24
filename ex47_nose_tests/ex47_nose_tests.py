# coding: utf8
# 참고문헌: http://learnpythonthehardway.org/python3/ex47.html
# http://nose.readthedocs.io/en/latest/usage.html
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc' -> print('abc')
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))
# print 'abc', -> print('abc', end=" ")
# raw_input('abc') -> input('abc')
# 오류노트 에 각자 오류노트 작성 / Please use your error-note
pwd

rm ex47_nose_tests.py
rm game.py
git add
git commit -m "ex47 : removed prior files"

cp -r ../ex46_proj/skeleton/ ./ex47/

git add ./ex47/
git commit -m "copied from ex46"
pushd ex47

git mv NAME/ ex47/
git commit -m "renamed folder NAME/ to ex47/"

git mv tests/NAME_test.py tests/ex47_test.py
git commit -m "renamed test file"
