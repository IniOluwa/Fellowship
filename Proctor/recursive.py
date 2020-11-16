# You need to design an iterative and a recursive function called replicate_iter and replicate_recur respectively
# which will receive two arguments:
# times which is the number of times to repeat and data which is the
# number or string to be repeated.

# The function should return an array containing repetitions of the data argument.
# For instance, replicate_recur(3, 5) or replicate_iter(3,5) should return [5,5,5].
# If the times argument is negative or zero, return an empty array. If the
# argument is invalid, raise a ValueError


def replicate_iter(times, data):
    if times <= 0:
        return []
    replication = [data] * times
    return replication

    # if times <= 0:
    #     return []
    # replica = []
    # for i in range(1, times + 1):
    #     replica.insert(i, data)
    # return replica


def replicate_recur(times, data):
    replicated = []
    if times is 0:
        return replicated
    replicated.insert(len(replicated) + 1, data)
    times -= 1
    return replicated + (replicate_recur(times, data))
