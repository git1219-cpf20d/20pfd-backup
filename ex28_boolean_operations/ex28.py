# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/python3/ex28.html
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# 각 논리식과 결과를 출력하는 프로그램 작성
# Please write a program evaluating and printing each logical operations
# ex: print("01. True and True =", (True and True))
# 오류노트 에 각자 오류노트 작성 / Please use your error-note

#python 2, 3 possible

print(" 1. True and True = %s" % str(True and True))
print(" 2. False and True = %s" % str(False and True))
print(" 3. 1==1 and 2==1 = %s" % ((1 == 1) and (2 == 1)))
print(" 4. 'test' == 'test' = %s" % str('test' == 'test'))
print(" 5. 1==1 or 2!=1 = %s" % ((1 == 1) or (2 != 1)))
print(" 6. True and 1==1 = %s" % str(True and (1 == 1)))
print(" 7. False and 0!=0 = %s" % str(False and (0 !=0)))
print(" 8. True or 1==1 = %s" % True or (1 == 1))
print(" 9. 'test' == 'testing' = %s" % str('test' == 'testing'))
print("10. 1!=0 and 2==1 = %s" % str((1 !=0) and (2 == 1)))
print("11. 'test'!='testing' = %s" % str('test' != 'testing'))
print("12. 'test'==1 = %s" % str('test' == 1))
print("13. not(True and False) = %s" % (not (True and False)))
print("14. not(1==1 and 0!=1) = %s" % (not ((1 == 1) and (0 != 1))))
print("15. not(10==1 or 1000==1000) = %s" % (not ((10 == 1) or (1000 == 1000))))
print("16. not(1!=10 or 3==4) = %s" % (not ((1 != 10) or (3==4))))
print("17. not('testing'=='testing' and 'Zed'=='Cool Guy') = %s" % (not (('testing' == 'testing') and ('Zed' == 'Cool Guy'))))
print("18. 1==1 and not('testing'==1 or 1==0) = %s" % ((1 == 1) and not (('testing' == 1) or (1 == 0))))
print("19. 'chunky'=='bacon' and not (3==4 or 3==3) = %s" % (('chunky' == 'bacon') and not ((3 == 4) or (3 == 3))))
print("20. 3==3 and not('testing'=='testing' or 'Python'=='Fun') = %s" % ((3 == 3) and not (('testing' == 'testing') or ('Python' == 'Fun'))))
print("extra 1. 'test and 'test' = = %s" % str('test' and 'test'))
print("extra 2. 1 and 1 = = %s" % str(1 and 1))
print("extra 3. False and 1 = = %s" % str(False and 1))
print("extra 4. true and 1 = = %s" % str(True and 1))

print('='*20)

#python 3 .ver
print(" 1. True and True :", True and True)
print(" 2. False and True :", False and True)
print(" 3. 1 == 1 and 2 == 1 :", 1 == 1 and 2 == 1)
print(" 4. 'test' == 'test' :", 'test' == 'test')
print(" 5. 1 == 1 or 2 != 1 :", 1 == 1 or 2 != 1)
print(" 6. True and 1 == 1 :", True and 1 == 1)
print(" 7. False and 0 != 0 :", False and 0 != 0)
print(" 8. True or 1 == 1 :", True or 1 == 1)
print(' 9. "test" == "testing" :', "test" == 'testing')
print('10. 1 != 0 and 2 == 1 :', 1 != 0 and 2 == 1)
print('11. "test" != "testing" :', 'test' != 'testing')
print('12. "test" == 1 :', 'test' == 1)
print('13. not (True and False) :', not (True and False))
print('14. not (1 == 1 and 0 != 1) :', not (1 == 1 and 0 != 1))
print('15. not (10 == 1 or 1000 == 1000) :', not (10 == 1 or 1000 == 1000))
print('16. not (1 != 10 or 3 == 4) :', not (1 != 10 or 3 == 4))
print('17. not ("testing" == "testing" and "prof. Lee" == "Cool Teacher") :', not ('testing' == 'testing' and 'prof. Lee' == 'Cool Teacher'))
print('18. 1 == 1 and (not ("testing" == 1 or 1 == 0)) :', 1 == 1 and (not ("testing" == 1 or 1 == 0)))
print('19. "chunky" == "bacon" and (not (3 == 4 or 3 == 3)) :', "chunky" == 'bacon' and (not (3 == 4 or 3 == 3)))
print('20. 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")) :', 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")))