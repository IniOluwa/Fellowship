# Implementing fizzbuzz using lambda functions
the_list = []

i = 0
while i < 30:
	i = i + 1
	the_list.append(i)

print filter(lambda x: x % 3 == 0, the_list) 
print "fizz"

print filter(lambda x: x % 5 == 0, the_list)
print "buzz"
 
print filter(lambda x: x % 3 == 0 and x % 5 == 0, the_list) 
print "fizzbuzz"