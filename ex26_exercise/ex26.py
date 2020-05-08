# 아래 링크의 파일을 받아 틀린 곳을 수정하시오 
# Download a file from the following link and correct
# https://learnpythonthehardway.org/python3/exercise26.txt

#교재 링크 https://learnpythonthehardway.org/book/exercise26.txt에서 다운 받은 파일

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words): #: 추가(*함수 명령어 끝엔 항상 : 있는지 확인 해보기)
    """Prints the first word after popping it off."""
    word = words.pop(0) # poop -> pop
    print (word) #괄호 추가

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) # ) 괄호 추가
    print (word) # 괄호 추가

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print ("Let's practice everything.") #위에 print (word)도 마찬가지지만 print 뒤 ()있는지 확인
print ('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.') #마찬가지, ( )추가

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print ("--------------") # ()추가
print (poem)             # ()추가 
print ("--------------") # ()추가

five = 10 - 2 + 3 - 6 # 결과값이 5가 나오도록 5를 6으로 변경
print ("This should be five: %s" % five) # () 추가

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000 #\가 아니라 /로 변경(연산을 하고 싶은 것이므로)
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) # 식 중간 == -> = 수정, start-point  -> start_point

print ("With a starting point of: %d" % start_point)#()추가
print ("We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates))#()추가

start_point = start_point / 10

print ("We can also do that this way:") #() 추가
print ("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))# crabapples-> crates start_pont-> start_point, start_point괄호 닫고 () 추가

sentence = "All good things come to those who wait."
# god -> good, weight-> wait 오타수정 \t 삭제
words = break_words(sentence) # ex25 import 할 필요 없으므로 ex25. 삭제
sorted_words = sort_words(words) # ex25 import 할 필요 없으므로 ex25. 삭제

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words) #. 제거
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence) # ex25 import 할 필요 없으므로 ex25. 삭제
print(sorted_words) # print<- 오타수정(t추가) 후 ()추가

print_first_and_last(sentence)# first(f추가) 오타수정
print_first_and_last_sorted(sentence) # 함수인자인 print_first_and_last_sorted(sentence) 로 수정 a->and, senence-> sentence. 그후 print_first_and_last(sentence)에 귀속되어 있지 않도록 밖으로 빼준뒤 문장 뒤 v 삭제
