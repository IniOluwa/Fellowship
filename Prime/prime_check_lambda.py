# Initialize Empty List
the_list = []

# Create Loop To Populate List
i = 0
while i < 100:
	i = i + 1
	the_list.append(i)

# Prime Check Method
def prime(x):
    j = 0;
    for j in the_list:
        if x % i == 0 or x == i:
            return x
        else:
        	return False

check = range(2, 49)

print prime(8)

the_list = range(2, 10000000000)

# Lambda Prime Check
for i in range(2, 50):
    the_list = filter(lambda x: x == i or x % i, the_list)


n = input("Gimme the number: ")

print n
