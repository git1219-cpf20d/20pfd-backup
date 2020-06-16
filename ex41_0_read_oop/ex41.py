# coding: utf8
# 참고문헌: http://learnpythonthehardway.org/python3/ex41.html
#   https://wikidocs.net/28
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))
# 오류노트 에 각자 오류노트 작성 / Please use your error-note
# 메시지는 적당히 한글로 변경 / If necessary, localize messages
# urlopen 은 urllib.request 에서 / urlopen is available in urllib.request

import random
import sys
from urllib.request import urlopen

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
  "class %%%(%%%):":
   "클래스 %%% 를 만든다. 부모클래스 %%% 로부터 상속받는다.",
  '''class %%%(object):
/tdef __init__(self,***)''':
"클래스 %%% 에는 __init__ 함수가 있고 그 매개변수는 self 와 *** 이다.",
"*** = %%%()":
 "*** 을(를) 클래스 %%% 의 인스턴스로 만든다.",
 # "클래스 %%% 의 인스턴스로 *** 을(를) 만든다."
"***.***(@@@)":
 "객체 ***로 부터 함수 *** 를 찾아 호출한다. 매개변수는 self 와 @@@이다.",
"***.*** = '***'":
 "객체 ***로 부터 속성 *** 을 찾아 그 값을 '***' 으로 바꾼다",
}

PHRASE_FIRST = False
if (len(sys.argv) == 2) and (sys.argv[1] == "한글"):
  PHRASE_FIRST = True

for word in urlopen(WORD_URL).readlines():
  WORDS.append((word.decode("utf-8").strip()))

def convert(snippet, phrase):
  class_name = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
  other_names = random.sample(WORDS, snippet.count("***"))

  results = []
  param_names = []

for i in range(0, snippet.count("@@@")):
  param_count = random.radint(1, 3)
  param_names.append(', '.join(random.sample(WORDS, param_count)))

for sentence in snippet, phrase:
  result = sentence[:]

  for word in class_names:
    result = result.replace("%%%", str(word), 1)

  for word in other_names:
    result = result.replace("***", str(word), 1)
  
  for word in other_names:
    result = result.replace("@@@", str(word), 1)

  results.append(result)

return results

try:
  while True:
    snippets = list(PHRASES.keys())
    random.shuffle(snippets)

    for snippet in snippet:
      phrase = PHRASES[snippet]
      question, answer = convert(snippet, phrase)
      if PHRASE_FIRST:
        question, answer = answer, question

      print(question)
      input("> ")
      print("답: %s\n\n" % answer)
except E0FError:
  print("\n안녕")