# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/python3/ex25.html
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc' -> print('abc')
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))
# print 'abc', -> print('abc', end=" ")
# raw_input('abc') -> input('abc')
# 오류노트 에 각자 오류노트 작성 / Please use your error-note
import ex25

sentence = "All good things come to those who wait."
words = ex25.break_words(sentence)
print("words = %s" % words)
sorted_words = ex25.sort_words(words)
print("sorted_words = %s" % sorted_words)
ex25.print_first_word(words)
ex25.print_last_word(words)
print("words = %s" % words)
ex25.print_first_word(sorted_words)
ex25.print_last_word(sorted_words)
print("sorted_words = %s" % sorted_words)
sorted_words = ex25.sort_sentence(sentence)
print("sorted_words = %s" % sorted_words)
ex25.print_first_and_last(sentence)
ex25.print_first_and_last_sorted(sentence)