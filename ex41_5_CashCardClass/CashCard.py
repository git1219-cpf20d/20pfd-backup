# -*- coding: utf8 -*-
# 입금, 출금, 잔고확인 기능을 갖는 현금카드 모듈을 구현하시오
# Please implement CashCard module capable of deposit, withdraw, and check-balance
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 오류노트 에 각자 오류노트 작성 / Please use your error-note


balance_won = 0

def deposit(amount_won):
  global balance_won

  balance_won += amount_won

def withdraw(amount_won):
  global balance_won

  balance_won += (-amount_won)

def check_balance():
  return balance_won

print(f"{__file__} : __name__ = {__name__}")