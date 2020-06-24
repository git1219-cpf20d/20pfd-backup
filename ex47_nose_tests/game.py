# coding: utf8
# 참고문헌: http://learnpythonthehardway.org/python3/ex47.html
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc' -> print('abc')
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))
# print 'abc', -> print('abc', end=" ")
# raw_input('abc') -> input('abc')
# 오류노트 에 각자 오류노트 작성 / Please use your error-note

class room(object):

    def __init__(self, 이름, 설명):
        self.이름 = 이름
        self.설명 = 설명
        self.길_모음 = {}

    def 이동(self, 방향):
        return self.길_모음.get(방향, None)

    def 길_추가(self, 길_모음):
        self.길_모음.update(길_모음)
