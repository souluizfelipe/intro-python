#input 2 numbers,
num1, num2 = input("type 2 numbers ").split()

num1 = int(num1)
num2 = int(num2)
#sum the numbers,
sum = num1 + num2
#substract
diff = num1 - num2
#multiply
multi = num1 * num2
#divide
div = num1 / num2
#module
mod = num1 % num2
#print the results

print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, diff))
print("{} * {} = {}".format(num1, num2, multi))
print("{} / {} = {}".format(num1, num2, div))
print("{} % {} = {}".format(num1, num2, mod))