# # Define List Range
# the_list = range(1, 100)
#
# # Lambda Prime Check
# for i in range(2, 50):
#     the_list = filter(lambda x: x == i or x % i, the_list)

def prime_lambda(number):
	return number

print "Check If Number Is Prime."
print prime_lambda(input("Input Your Number: "))
