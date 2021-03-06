# coding: utf-8
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 재귀호출로 factorial 을 계산하는 프로그램을 작성하시오
# Please write a program that calculates the factorial using the recursion
# 오류노트 에 각자 오류노트 작성 / Please use your error-note

count = 0
memo = {}

def factorial(n):

  global count, memo
  count += 1
  print(f"factorial({n})", count)
  if n in memo:
    result = memo[n]
  elif 1 >= n:
    result = 1
  else:
    result = n * factorial(n - 1)

  if n not in memo:
    memo[n] = result

  return result


for i in range(10):
  print(f"{i:2}! = {factorial(i)}")