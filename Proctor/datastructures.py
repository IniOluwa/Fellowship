# Write a function called manipulate_data which will act as follows:

# When given a list of integers, return a list, where the first element is
# the count of positives numbers and the second element is the sum of
# negative numbers.

# NB: Treat 0 as positive.


def mainpulate_data(data):
    if type(data) != list:
        return 'Only lists allowed'
    positives = 0
    negatives = 0
    for iter in range(len(data)):
        if data[iter] >= 0:
            positives += 1
        elif data[iter] < 0:
            negatives += data[iter]

    return [positives, negatives]

print mainpulate_data([-1, 2, 6, 7, -9, -2])
