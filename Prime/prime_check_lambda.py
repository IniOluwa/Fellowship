# Numbers Range For Prime Check
numbers = range(1, 101)

# Numbers List To Be Checked For Finding Prime
numbers_check = range(2, 10)

# Prime Lambda Function
def prime_lambda(number):
	# Lambda Prime Check
	for num in numbers_check:
	    prime_list = filter(lambda x: x is not num and x % num is 0, numbers)
	return prime_list

# Number Input
print "Check If Number Is Prime In The Range Of 100."
print prime_lambda(input("Input Your Number: "))
