#we'll provide different output based on age
#1 - 18 ->  important
#21, 50, > 65 -> important
#All others -> not important

#recive age and store in age
#if age is both grather then, or equal to 1 and less then or equal to 18 Important
#if age is either 21 or 50, also important
#we check if age is less then 65, we convert tru to false and vice versa

age = eval(input("enter your age: "))

if (age >= 1) and (age <= 18):
  print('Important birthday')
elif (age == 21) or (age == 50):
  print('Important birthday')
elif not(age < 65):
  print('Important birthday')
else:
  print('Sorry, Not Important birthday')

