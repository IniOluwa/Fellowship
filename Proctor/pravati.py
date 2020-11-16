# Returns the sum of every two-digit/tens number in a list
def pravati(the_list):
    two_digit_sum = 0
    for number in the_list:
        # Handles Positive Digits
        if number > 9 and number < 100:
            two_digit_sum += number
        # Handles Negative Digits
        elif number > -100 and number < -9:
            two_digit_sum += number
    return two_digit_sum
