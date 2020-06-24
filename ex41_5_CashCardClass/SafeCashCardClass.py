# -*- coding: utf8 -*-
# 현금카드 클래스를 상속받아 잔고가 0보다 작아지지 않는 안전현금카드 클래스를 구현하시오
# By inheriting the CashCardClass, implement SafeCashCardClass whose balance has minimum value of zero.
# 안전현금카드가 의도한 대로 작동하는지 확인하는 프로그램을 작성하시오
# Please write a program that verifies the SafeCashCardClass.

from CashCardClass import SimpleCashCard as CashCard


class safeCashCard(CashCard):
  def withdraw(self, amount_won):

    print(f"{__class__} withdraw({amount_won})")

    if self.check_balance() > amount_won:
      super().withdraw(amount_won)

    else:
      print("** 오류 발생 **")
      print("잔고가 부족합니다")
      print("인출되지 않았습니다")

def main():
  from CashCard_user import chk_bal

  myCard = CashCard()

  mySafeCard = SafeCashCard()

  mySistersSafeCard = SafeCashCard()

  myCard.deposit(10000)
  mySafeCard.deposit(10000)
  mySistersSafeCard.deposit(200000)

  chk_bal("myCard 입금 후 잔고 확인", myCard)
  chk_bal("mySafeCard 입금 후 잔고 확인", mySafeCard)
  chk_bal("mySistersSafeCard 입금 후 잔고 확인", mySistersSafeCard)

  myCard.withdraw(100000)
  mySafeCard.withdraw(100000)
  mySistersSafeCard.withdraw(100000)

  chk_bal("myCard 입금 후 잔고 확인", myCard)
  chk_bal("mySafeCard 입금 후 잔고 확인", mySafeCard)
  chk_bal("mySistersSafeCard 입금 후 잔고 확인", mySistersSafeCard)

if "__main__" == __name__:
  main()