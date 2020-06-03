# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/python3/ex12.html
#          https://youtu.be/rwEHu5lWPx4 (pydoc)
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc' -> print('abc')
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))
# print 'abc', -> print('abc', end=" ")
# raw_input('abc') -> input('abc')

나이 = input("몇 살이죠? ")
키 = input("키는 얼마죠? ")
몸무게 = input("몸무게는 얼마죠? ")

print(f"네, 나이는 {나이}살, 키는 {키}cm, 몸무게는 {몸무게}kg 이네요.")

학교 = input("학교는 어디죠? ")
학년 = input("몇 학년 인가요? ")

print(f"학교는 {학교}다니고 있고, 학년은 {학년}이군요. 반갑습니다.")