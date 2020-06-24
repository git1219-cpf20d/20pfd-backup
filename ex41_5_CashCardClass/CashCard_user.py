# -*- coding: utf8 -*-
# 현금카드 모듈을 불러들여 사용하는 프로그램을 작성하시오
# Please write a program that imports the CashCard module and use it
# 여러 장의 현금 카드를 만들 수 있는지 확인해 보시오
# See if you can make multiple CashCard's independent from each other
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 오류노트 에 각자 오류노트 작성 / Please use your error-note

import CashCard as CashCard_module

def chk_bal(massage, account):

  print(f"{message} : {account.check_balance()}")

def main():
  chk_bal("CashCard_module 잔액 확인", CashCard_module)

  print("현금 카드에 10000원 입금")
  CashCard_module.deposit(10000)

  chk_bal("입금 후 잔고 확인", CashCard_module)

  print("1000원 출금")
  CashCard_module.withdraw(1000)

  chk_bal("출금 후 잔고 확인", CashCard_module)

  import CashCard as mySistersCard_module

  chk_bal("CashCard_module 잔액 확인", CashCard_module)
  chk_bal("mySistersCard_module 잔액 확인", mySistersCard_module)

print(f"{__file__} : __name__ = {__name__}")

if "__main__" == __name_:
  main()