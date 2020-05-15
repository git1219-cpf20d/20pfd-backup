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


print("Let's practice everything.") #위에 print (word)도 마찬가지지만 print 뒤 ()있는지 확인
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.') #마찬가지, ( )추가

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""

print("--------------") # ()추가
print(poem) # ()추가
print("--------------") # ()추가

five = 10 - 2 + 3 - 6 # 결과값이 5가 나오도록 5를 6으로 변경
print("This should be five: %s" % five) # () 추가

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000 #\가 아니라 /로 변경(연산을 하고 싶은 것이므로)
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) # 식 중간 == -> = 수정, start-point  -> start_point

print("With a starting point of: %d" % start_point)#()추가
print("We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates))#()추가

start_point = start_point / 10

print("We can also do that this way:") #() 추가
print("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))# crabapples-> crates start_pont-> start_point, start_point괄호 닫고 () 추가

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

print('-'*20)
#https://learnpythonthehardway.org/python3/exercise26.txt 여기서 다운 받은 파일

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input() #<-input 행 추가
print("How much do you weight?", end=' ') #weight 오타 수정과 )추가
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

print('-'*20)

from sys import argv # import 행 추가

script, filename = argv

#txt = open(filename)#nme->name
with open(filename, encoding='utf-8') as txt:
  print("Here's your file %r:" % filename)# %r 사용
  print(txt.read())#tx->txt with as 문장으로 교체

#print("Here's your file {filename}:")
#print(txt.read())#tx->txt

print("Type the filename again:")
file_again = input("> ")

#txt_again = open(file_again)

with open(file_again, encoding='utf-8') as txt_again:
  print(txt_again.read())#_read -> .read 변경
# 위와 동일하게 with as 방식으로 변경

print('-'*20)

print("Let's practice everything.")#작은에서 큰따옴표로 변경
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')# with가 명령인자로 작동되지 않도록 쓸데없는 줄바꿈 삭제

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------") #따옴표 추가
print(poem)                                 
print("--------------") #따옴표 추가


five = 10 - 2 + 3 - 6 #결과 값이 5가 나오도록 수정
print(f"This should be five: {five}") #괄호 주의

def secret_formula(started): #:추가
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100 # / 추가
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)
#crates 추가

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way.")#:지우고, .추가
formula = secret_formula(start_point)#_추가
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

print('-'*20)

people = 20
cats = 30 #cates -> cats 오타 수정
dogs = 15


if people < cats:
    print ("Too many cats! The world is doomed!") #()추가

if people > cats: # <를  >로
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs: # :추가
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs: #:추가
    print("People are less than or equal to dogs.")#큰따옴표 추가


if people == dogs: #=->==
    print("People are dogs.")