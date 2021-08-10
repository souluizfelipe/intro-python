#if age is 5, go to kindergarten
#if age 6 - 17 goes to grade 1 through 12
#if age > 17 goes to college
#Try to complete with 10 lines or less

age = eval(input("what is you're age: "))
if age < 5:
  print('stay home, have fun')
elif (age == 5):
  print('You can go to kindergarten')
elif (age >= 6) and (age <= 17):
  grade = age - 5
  print('You can go to grade {}'.format(grade))
else:
  print('You can go to College')

