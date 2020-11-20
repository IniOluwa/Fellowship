# Check Prime Function
def prime(x):
    for i in range(1, 100):
        if x % i != 0 or x == i:
            # Return Not Prime Message
            return str(x) + " Is Not Prime."

    # Return Prime Message
    return str(x) + " Is A Prime Number."

# Get User Input
print "Check If A Number Between 1 and 100 is Prime."
print prime(input("Enter The Number: "))
