# Write two functions, isOdd() and isEven(), with a single numeric parameter named number. 
# The isOdd() function returns True if number is odd and False if number is even. 
# The isEven() function returns the True if number is even and False if number is odd. 
# Both functions return False for numbers with fractional parts, such as 3.14 or -4.5. 
# Zero is considered an even number.

def is_even(num):
    return (num % 2) == 0.0

        
def is_odd(num):
    return (num % 2) == 1

    
assert is_odd(42) == False
assert is_odd(9999) == True
assert is_odd(-10) == False
assert is_odd(-11) == True
assert is_odd(3.1415) == False
assert is_even(42) == True
assert is_even(9999) == False
assert is_even(-10) == True
assert is_even(-11) == False
assert is_even(3.1415) == False