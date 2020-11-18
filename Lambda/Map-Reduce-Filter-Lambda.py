an_array = [1, 2, 3, 4, 5, 6, 7 , 8, 9, 0]

# This adds all the values in the list
print reduce(lambda x, y: x + y, an_array)

# This runs whatever command you structure out for it
print map(lambda x: x * 1 + 10, an_array)

# This gives you the value that can fully divide the number you ask it to.
print filter(lambda x: x % 2 == 0, an_array)