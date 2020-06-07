# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/python3/ex40.html
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc' -> print('abc')
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))
# print 'abc', -> print('abc', end=" ")
# raw_input('abc') -> input('abc')
# 오류노트 에 각자 오류노트 작성 / Please use your error-note

mystuff = {'apple': "I AM APPLES!"}
print{mystuff['apple']}

import mystuff

mystuff.apple()
print(mystuff.tangerine)



class MyStuff(object):
  def __init__(self):
    self.tangerine = "And now a thousand years between"

  def apple(self):
    print("I AM CLASSY APPLES!")


# end class MyStuff

thing = MyStuff()
thing.apple()
print(thing.tangerine)


class MyStuff(object):
  def __init__(self, lyrics):
    self.lyrics = lyrics

  def sing_me_a_song(self):
    for line in self.lyrics:
      print(line)


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()