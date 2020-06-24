# -*- coding: utf8 -*-
# 현금카드 클래스를 구현하시오
# Please implement CashCardClass
# 현금카드 클래스의 인스턴스를 만들어 사용하는 프로그램을 작성하시오
# Please write a program that creates instances of the CashCardClass
# 여러 장의 현금카드를 만들 수 있는지 확인하시오
# See if an instance of the CashCardClass is independent from other instances


class SimpleCashCard:
  def __init__(self):
    print(f"{__class__} __init__()")

    self.balance_won = 0

  def deposit(self, amount_won):
    print(f"{__class__} deposit({amount_won})")

    self.balance_won += amount_won

  def withdraw(self, amount_won):
    print(f"{__class__} withdraw({amount_won})")

    self.balance_won += (-amount_won)

  def check_balance(self):
    print(f"{__class__} check_balance()")

    return self.balance_won

def main():
  from CashCard_user import chk_bal

  myCard = SimpleCashCard()

  print("myCard 에 10000원 입금")
  myCard.deposit(10000)
  chk_bal("입금 후 잔고 확인", myCard)

  print("myCard 에 1000원 출금")
  myCard.withdraw(1000)
  chk_bal("출금 후 잔고 확인", myCard)

  mySistersCard = SimpleCashCard()
  chk_bal("잔액 확인 myCard", myCard)
  chk_bal("잔액 확인 mySistersCard", mySistersCard)

  print(f"myCard : {myCard}")
  print(f"mySistersCard : {mySistersCard}")


print(f"{__file__} : __name__ = {__name__}")

if "__main__" == __name__:
  main()