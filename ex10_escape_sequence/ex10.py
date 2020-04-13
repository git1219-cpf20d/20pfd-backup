# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/python3/ex10.html
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc' -> print('abc')
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))
# print 'abc', -> print('abc', end=" ")

# -*- coding: utf-8 -*-

tabby_cat = "\t난 탭이 됨."
persian_cat = "나는\n분리됨."
backlash_cat = "나는 \\ 고 \\ 양이."

fat_cat = """
할 일 목록:
\t* 고양이 밥
\t* 물고기
\t* 개박하\n\t* 오리새
"""

print(tabby_cat)
print(persian_cat)
print(backlash_cat)
print(fat_cat)

while True:
  for i in ["/","-","|","\\","|"]:
    print("%s\r" % i,)