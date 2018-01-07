#!/usr/bin/python

#The while loop.
count = 0
while count < 5:
	print count, " is  less than 5"
	count = count + 1
else:
	print count, " is not less than 5"
	
	
# The for loop
for letter in 'Python':     # First Example
	print 'Current Letter :', letter

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # Second Example
	print 'Current fruit :', fruit

print "Good bye!"


fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
	print 'Current fruit :', fruits[index]

print "Good bye!"


for num in range(10,20):     #to iterate between 10 to 20
	for i in range(2,num):    #to iterate on the factors of the number
		if num%i == 0:         #to determine the first factor
			j=num/i             #to calculate the second factor
			print '%d equals %d * %d' % (num,i,j)
			break #to move to the next number, the #first FOR
		else:                  # else part of the loop
			print num, 'is a prime number'
			
			
			
# Break and continue statements
for letter in 'Python':     # First Example
	if letter == 'h':
		break
	print 'Current Letter :', letter
  
var = 10                    # Second Example
while var > 0:              
	print 'Current variable value :', var
	var = var -1
	if var == 5:
		break

print "Good bye!"





for letter in 'Python':     # First Example
	if letter == 'h':
		continue
	print 'Current Letter :', letter

var = 10                    # Second Example
while var > 0:              
	var = var -1
	if var == 5:
		continue
	print 'Current variable value :', var
print "Good bye!"




# If..then....else
var = 100
if var < 200:
	print "Expression value is less than 200"
	if var == 150:
		print "Which is 150"
	elif var == 100:
		print "Which is 100"
	elif var == 50:
		print "Which is 50"
	elif var < 50:
		print "Expression value is less than 50"
else:
	print "Could not find true expression"

print "Good bye!"

