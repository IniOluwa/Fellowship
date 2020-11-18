# Impelmenting fizzbuzz with just one lambda function
the_list = []

i = 0
while i < 30:
    i = i + 1
    the_list.append(i)

fb = filter(lambda x: x % 3 == 0 or x % 5 == 0 or x %
            3 == 0 and x % 5 == 0, the_list)
print fb

j = 0
while j < len(fb):
    if fb[j] % 3 == 0 and fb[j] % 5 == 0:
        print "fizzbuzz"
    elif fb[j] % 3 == 0:
        print "fizz"
    elif fb[j] % 5 == 0:
        print "buzz"
    else:
        print "Null"
    j = j + 1
