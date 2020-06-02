# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/python3/ex39.html
# 입력 후 add, commit / Enter source code, add, and commit
# 각 행 주석 입력 후 commit / Enter comment for each line and commit
# 각자 Study drills 시도 후 필요시 commit / Try Study Drills and commit if necessary
# print 'abc' -> print('abc')
# print 'abc', 123 -> print('abc %s' % (123))
# print 'abc', abc, 'def' -> print('abc %s def' % (abc))
# print 'abc', -> print('abc', end=" ")
# raw_input('abc') -> input('abc')
# 오류노트 에 각자 오류노트 작성 / Please use your error-note

states = {
  'Oregon': 'OR',
  'Florida': 'FL',
  'California': 'CA',
  'New York': 'NY',
  'Hawaii': 'HI',
}

# create a basic set of states and some cities in them
cities = {
  'CA': 'Los Angeles',
  'HI': 'Honolulu',
  'FL': 'Orlando',
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print('NY State has: %s' % cities['NY'])
print('OR State has: %s' % cities['OR'])

# print some states
print('-' * 10)
print("Hawaii's abbreviation is: %s" % states['Hawaii'])
print("Florida's abbreviation is: %s" % states['Florida'])

# print some states
print('-' * 10)
print("states = %s" % states)
print("states.item() = %s" % states.item())
print('-' * 10)
for state, abbrev in states.items():
  print("%s is abbreviated %s" % (state, abbrev))

# print every city in state
print('-' * 10)
for abbrev, city in cities.items():
  print("%s has the city %s" % (abbrev, city))

# now do both at the same time
print('-' * 10)
for state, abbrev in states.items():
  print("%s state is abbreviated %s and has city %s" % (
    state, abbrev, cities[abbrev]
  ))

print('-' * 10)
# safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
  print("Sorry no Texas yet")

# get a city with a default value
city = cities.get('TX', 'Not Entered Yet')
print("The city for the state 'TX' is: %s " % city)
