
#------Function 0----------
def is_even(number):
	'''This will tell if a number is even or odd.'''
	if number%2 == 0:
		return True
	else:
		return False

#-----Function 1------------
def number_of_digits(number):
	'''This will count how many digits are in a number. Non-negative'''
	numberOfDigits = 0
	while number > 0:
		number /= 10
		numberOfDigits += 1
	
	return numberOfDigits

	
#-----Function 2-------------- 
def sum_digits(number):
	"""Takes a non negative integer as a parameter returns the sum of the digits"""
	sum = 0

	while digits > 0:
		finalNumber = digits % 10
		digits -= finalNumber 
		#this will get the last digit and then subtract it
		sum += finalNumber
		digits /= 10
	
	return sum
	
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
	if number == 0:
		return 1
	else:
		total = number
		while number != 1:
			number -= 1
			total *= number
		return total
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
	factors = 0 
	for x in range(1,number): 
		if number % x == 0: 
			factors += x
	if number == factors:
		return True
	else:
		return False
	
	
#------------Function 8----------------
def divisible_sum(number):
	if number % sum_digits(number) == 0:
		return True
	else:
		return False 














