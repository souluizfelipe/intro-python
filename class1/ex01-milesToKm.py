#problem: allow user to enter miles and convert to km
# km = 1.60934 miles
# output = x miles is y km

#input miles 
#convert miles to km
#print result

miles = input("type the value in Miles to convert to KM: ")
miles = float(miles)

kmInMiles = 1.60934

km = miles * kmInMiles

print("{} miles is {} km".format(miles, km))