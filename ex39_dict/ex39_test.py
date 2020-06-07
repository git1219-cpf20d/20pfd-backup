# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/python3/ex39.html
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc' -> print('abc')
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))
# print 'abc', -> print('abc', end=" ")
# raw_input('abc') -> input('abc')
# 오류노트 에 각자 오류노트 작성 / Please use your error-note

things = ['a', 'b', 'c', 'd']
# 또는 Or
# things = list('abcd')
print('print(things[1]): ')
print(things[1])
things[1] = 'z'
print('print(things[1]): ')
print(things[1])
print('print(things): ')
print(things)

stuff = {'name': 'Zed', 'age': 36, 'height': 6 * 12 + 2}
print("print(stuff['name']): ")
print(stuff['name'])
print("print(stuff['age']): ")
print(stuff['age'])
print("print(stuff['height']): ")
print(stuff['height'])
stuff['city'] = 'San Francisco'
print("print(stuff['city']): ")
print(stuff['city'])

stuff[1] = 'Wow'
stuff[2] = 'Neato'
print('print(stuff[1]): ')
print(stuff[1])
print('print(stuff[2]): ')
print(stuff[2])
print('print(stuff): ')
print(stuff)

del stuff['city']
del stuff[1]
del stuff[2]
print('print(stuff): ')
print(stuff)