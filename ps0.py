
#------Function 0----------
def is_even(number):
	'''This will tell if a number is even or odd.'''
	if number%2 == 0:
		return True
	else:
		return False

#-----Function 1------------
def number_of_digits(number):
	'''This will count how many digits are in a number.'''
	number = str(number)
	numberOfDigits = 0
	for character in number:
		numberOfDigits += 1
	return numberOfDigits
	
#-----Function 2--------------
def sum_digits(number):
	number = str(number)
	digits = [] 
	for character in number:
		character = int(character) 
		digits.append(character) 
	sumOfDigits = 0
	for x in digits:
		sumOfDigits += x
	return sumOfDigits
	
#--------Function 3---------------
def sum_less_int(number):
	sumLessInts = range(number)
	sum = 0
	for x in sumLessInts:
		sum += x
	return sum

#---------Function 4------------------	
def factorial(number):
	'''a number is given and the function takes all of the integers up to
	and including the given integer and multiplies them together'''
	total = 1
	while number > 1:
		total *= (number-1)
		number -= 1
	if number == 0:
		return 1
	else:
		return number

#--------------Function 5---------------------
def factor_of(firstNum, SecondNum):
	remainder = firstNum % SecondNum
	if remainder == 0:
		return True
	else:
		return False

#----------Function 6-----------------
def prime(number):
	divider = 2
	while divider < number:
		divided = number % divider
		if divided == 0:
			return True
		else:
			return False
		
#----------Function 7----------------
def is_perfect(number):
	factors = 0 # finds all factors and adds them together
	x = 1 #goes through all the numbes and tells what it is divisible by
	while x < number: # if the increasing number is higher than the given number then we already have all of the factors
 		if number % x == 0: #every time this equals 0 it finds a factor
 			factors += x 
 			x += 1
	if factors == number:
		return True
	else:
		return False

	
#------------Function 8----------------
def divisible_sum(number):
	if number % sum_of_digits(number) == 0:
		return True
	else:
		return False 














