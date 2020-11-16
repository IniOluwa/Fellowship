# Create a function called binary_converter. Inside the function,
# implement an algorithm to convert decimal numbers between 0 and 255 to
# their binary equivalents.

# For any invalid input, return string Invalid input

# Example: For number 5 return string 101


def binary_converter(number):
    if number < 0 or number > 255:
        return 'Invalid input'
    number_binary = bin(number)
    return number_binary[2:]

print binary_converter(0)
