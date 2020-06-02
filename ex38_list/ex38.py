# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/python3/ex38.html
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc' -> print('abc')
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))
# print 'abc', -> print('abc', end=" ")
# raw_input('abc') -> input('abc')
# 오류노트 에 각자 오류노트 작성 / Please use your error-note

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("What there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while 10 != (len(stuff)):
  next_one = more_stuff.pop()
  print("Adding: %s" % next_one)
  stuff.append(next_one)
  print("There are %d items now." % len(stuff))

print("There we go :%s" % str(stuff))
print("Let's do some things with stuff")

print("stuff[1] = %s" % stuff[1])
print("stuff[-1] = %s" % stuff[-1])
print("stuff.pop() = %s" % stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
