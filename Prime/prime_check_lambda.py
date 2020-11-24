# Define List Range
the_list = range(1, 100)

# Lambda Prime Check
for i in range(2, 50):
    the_list = filter(lambda x: x == i or x % i, the_list)

n = input("Gimme the number: ")

print n
