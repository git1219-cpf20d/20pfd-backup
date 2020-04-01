# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/python3/ex5.html
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc' -> print('abc')
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))
# 변수명에는 되도록 단위를 포함 / Add units to the variable names

my_name = "Gong In Taek"
my_age  = 25
my_height_cm = 182
my_weight_kg = 87
my_eyes_color = 'Brown'
my_teeth_color = 'White'
my_hair_color = 'Black'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height_cm} centimeters tall.")
print(f"He's {my_weight_kg} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes_color} eyes and {my_hair_color} hair.")
print(f"His teeth are usually {my_teeth_color} depending on the coffee.")

#this line is trickky, try to get it exactly right
total = my_age + my_height_cm + my_weight_kg
print(f"If I add {my_age}, {my_height_cm}, and {my_weight_kg}) I get {total}.")