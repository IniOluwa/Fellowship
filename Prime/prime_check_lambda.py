# # Numbers Range For Prime Check
# numbers = range(1, 101)
#
# # Numbers List To Be Checked For Finding Prime
# numbers_check = range(2, 10)
#
# # Prime Lambda Function
# def prime_lambda(number):
#
# 	# Check If Number Exists In Range
# 	if number not in numbers:
#
# 		# Return Number Not In Range Error
# 		return "The Query Number Is Not In The Currently Allowed Range."
#
# 	# Define Empty Prime List
# 	prime_list = []
#
# 	# # Lambda Prime Check
# 	# for num in numbers_check:
# 	#     prime_list = reduce(lambda x: x is not num and x % num is 0, numbers)
# 	# return prime_list
#
# 	# Lambda Prime Check
# 	for num in numbers_check:
# 		print num
# 		# Update Prime List With Lambda Results
# 	    prime_list += reduce(lambda x: x is not num and x % num is 0, numbers)
# 		print prime_list
#
# 	# Return Prime List Results
# 	# return prime_list
#
# 	# # Lambda Prime Check
# 	# prime_list = filter(lambda x: x is not number and x % number is 0, numbers)
# 	# return prime_list
#
# 	# # Lambda Prime Check
# 	# prime_list = filter(lambda x: x % y is 0 and x is not y, numbers)
# 	# return prime_list
#
# # Number Input
# print "Check If Number Is Prime In The Range Of 100."
# print prime_lambda(input("Input Your Number: "))

# Numbers Range For Prime Check
numbers = range(1, 101)

# Numbers List To Be Checked For Finding Prime
numbers_check = range(2, 10)

# Prime Lambda Function
def prime_lambda(number):

	# Check If Number Exists In Range
	if number not in numbers:

		# Return Number Not In Range Error
		return "The Query Number Is Not In The Currently Allowed Range."

	# Define Empty Prime List
	prime_list = []

	# Lambda Prime Check
	for num in numbers_check:
		# Update Prime List With Lambda Results
	    prime_list += filter(lambda x: x % num is 0 and x is not num, numbers)
	# Return Prime List Results
	return set(prime_list)

# Number Input
print "Check If Number Is Prime In The Range Of 100."
print prime_lambda(input("Input Your Number: "))
