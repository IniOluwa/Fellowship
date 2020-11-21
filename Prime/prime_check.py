numbers = range(1, 101)
numbers_check = range(2, 10)

# Check Prime Function
def prime(number):

    # Check If Number Exist In List
    if number in numbers:
        # Loop Through Numbers Check List
        for i in numbers_check:
            # Check Prime Number Conditions
            if number % i is 0 and number is not i:
                # Return Not Prime Message
                return str(number) + " Is Not Prime."
            else:
                # Return Prime Message
                return str(number) + " Is A Prime Number."
    else:
        return "Your Number Is Not In The Range of Allowed Numbers At This Time."

# Get User Input
print "Check If A Number Between 1 and 100 is Prime."
print prime(input("Enter The Number: "))
