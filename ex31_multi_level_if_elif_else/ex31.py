# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/python3/ex31.html
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc' -> print('abc')
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))
# print 'abc', -> print('abc', end=" ")
# raw_input('abc') -> input('abc')
# 오류노트 에 각자 오류노트 작성 / Please use your error-note


print("문이 두 개 있는 어두운 방에 들어왔습니다. \n1번과 2번 중 어느 방으로 들어갈까요?")

문 = input("> ")

if "1" == 문:
  print("거대한 곰이 치즈 케이크를 먹고 있습니다. 어떻게 할까요?")
  print("1. 케이크를 빼앗는다.")
  print("2. 곰에게 소리를 지른다.")

  곰 = input("> ")

  if "1" == 곰:
    print("곰이 당신의 얼굴을 먹어치웁니다. 잘했어요!")
  elif "2" == 곰:
    print("곰이 당신의 다리를 먹어치웁니다. 잘했어요!")
  else:
    print("음, %s 행동을 하는 것이 더 나았을 것 같네요. 곰이 도망갑니다." % 곰)

elif "2" == 문:
  print("당신은 크롤루 눈동자의 끝없는 눈동자를 처다봅니다.")
  print("1. 블루베리.")
  print("2. 노란 재킷 빨래집게.")
  print("3. 리볼버가 울부짖는 소리 이해하기.")

  광기 = input("> ")

  if ("1" == 광기) or ("2" == 광기):
    print("당신의 몸은 젤리의 마음의 힘으로 살아남았습니다. 잘했어요!")
  else:
    print("광기가 당신의 눈을 썩은 시궁창으로 만듭니다. 잘했어요!")

else:
  print("비틀거리며 걷다 발을 헛디뎌 칼 위로 떨어져 죽습니다. 잘했어요!")