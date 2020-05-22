# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/python3/ex35.html
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc' -> print('abc')
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))
# print 'abc', -> print('abc', end=" ")
# raw_input('abc') -> input('abc')
# 오류노트 에 각자 오류노트 작성 / Please use your error-note

from sys import exit


def gold_room(n):
   n += 1
   print(f"This room is full of gold. How much do you take?({n})")
   choice = input("> ")

   if "0" in choice or "1" in choice:
       how_much = int(choice)
   else:
        dead("Man, learn to type a number.",)
        how_much = 0

   if how_much < 50:
       print("Nice, you're not greedy, you win!")
       exit(0)
   else:
        dead("You greedy bastard!")


def bear_room(n):
    n += 1
    print(f"There is a bear here.({n})")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if "take honey" == choice:
            dead("The bear looks at you than slaps your face off.")
        elif "taunt bear" == choice and not bear_moved:
           print("The bear has moved from the door. you can go through it now.")
           bear_moved = True
        elif "taunt bear" == choice and bear_moved:
           print("The bear gets pissed off and chews your leg off.")
        elif "open door" == choice and bear_moved:
            gold_room(n)
        else:
            print("I got no idea what that means.")

def cthulhu_room(n):
    n += 1
    print(f"Here you see the great evil Cthulhu.({n})")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start(n)
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room(n)


def dead(why):
    print(why, "Good job!")
    exit(0)


def start(n):
   n += 1
   print(f"You are in a dark room.({n})")
   print("There is a door to your right and left.")
   print("Which one do you take?")

   choice = input("> ")

   if "left" == choice:
       bear_room(n)
   elif "right" == choice:
       cthulhu_room(n)
   else:
       dead("You stumble around the room until you starve. ")


start(0)
       