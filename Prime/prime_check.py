numbers = range(1, 101)
numbers_check = range(2, 10)

# Check Prime Function
def prime(number):

    # Check If Number Does Not Exist In Numbers List
    if number not in numbers:

        # Return Number Not In Range Error
        return "Your Number Is Not In The Range of Allowed Numbers At This Time."

    # Loop Through Numbers Check List
    for i in numbers_check:
        # Check Prime Number Conditions
        if number % i is 0 and number is not i:
            # Return Not Prime Message
            return str(number) + " Is Not Prime."

    # Return Prime Message
    return str(number) + " Is A Prime Number."

# Get User Input
print "Check If A Number Between 1 and 100 is Prime."
print prime(input("Enter The Number: "))
