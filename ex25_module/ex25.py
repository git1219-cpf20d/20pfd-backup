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

def break_words(stuff):
  """이 함수는 문자열을 단어로 쪼개 줍니다."""
  words = stuff.split(' ')
  return words


def sort_words(words):
  """단어를 정렬합니다."""
  return sorted(words)


def print_first_word(words):
  """첫 단어를 꺼내서 출력합니다."""
  word = words.pop(0)
  print(word)


def print_last_word(words):
  """마지막 단어를 꺼내서 출력합니다."""
  word = words.pop(-1)
  print(word)


def sort_sentence(sentence):
  """한 문장을 통째로 받아 단어를 정렬해서 반환합니다."""
  words = break_words(sentence)
  return sort_words(words)


def print_first_and_last(sentence):
  """문장의 처음과 마지막 단어를 출력합니다."""
  words = break_words(sentence)
  print_first_word(words)
  print_last_word(words)


def print_first_and_last_sorted(sentence):
  """단어를 정렬하고 처음과 마지막 단어를 출력합니다."""
  words = sort_sentence(sentence)
  print_first_word(words)
  print_last_word(words)
