# -*- coding: utf8 -*-
# 안전현금카드 클래스를 상속받아 거래내역을 기록하는 내역현금카드 클래스를 구현하시오
# By inheriting the SafeCashCardClass, implement TrackingCashCardClass that keeps track of transactions
# 내역현금카드 클래스가 의도한 대로 작동하는지 확인하는 프로그램을 작성하시오
# Please write a program that verifies the TrackingCashCardClass.

import time

from SafeCashCardClass import SafeCashCard

class HistoryCashCard(SafeCashCard):

  def __init__(self):
    print(f"{__class__} __init__()")

    super().__init__()

    self.history = []

  def deposit(self, amount_won):
    print(f"{__class__} deposit({amount_won})")

    super().deposit(amount_won)

    self.record_history('deposit', amount_won)

  def withdraw(self, amount_won):
    print(f"{__class__} withdraw({amount_won})")

    super().withdraw(amount_won)

    self.record_history('withdraw', amount_won)

  def record_history(self, activity, amount_won):
    self.history.append(
      {
        'time' : time.localtime(),
        'balance' : self.check_balance(),
        'activity' : activity,
        'amount' : amount_won,
      }
    )

  def show_history(self):
    print(f"{__class__} show_history()")

    print(f"{'time and date':25s} {'activity':10s} {'amount':10s} {'balance':10s}")

    for record in self.history:
      print(
        f"{time.asctime(record['time']):25} "
        f"{record(record['activity']):10} "
        f"{record(record['amount']):10} "
        f"{record(record['balance']):10} "
      )

def main():
  print("main 객체 생성 ".ljust(60, '*'))
  myHistCard = HistoryCashCard()
  print("main 10000원 입금 ".ljust(60, '*'))
  myHistCard.deposit(10000)
  print("main 9000원 출금 ".ljust(60, '*'))
  myHistCard.withdraw(9000)
  print("main 9000원 출금 ".ljust(60, '*'))
  myHistCard.withdraw(9000)
  print("main 내역 확인 ".ljust(60, '*'))
  myHistCard.show_history()
  print("main 끝")

if "__main__" == __name__:
  main()
  