
# Reference -- https://en.wikipedia.org/wiki/Bisection_method
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number <= 0:
        return 0
    
    if number <= 2:
        return 1

    lower_bound = 0
    upper_bound = number # As square root of a number is always less than the number

    tolerance = 0.01 # trying to find the square root of a given number to an accurancy of 2 decimals

    while (True):
        guess = (lower_bound + upper_bound)/2
        difference = guess**2 - number
        # print('lower_bound = ' + str(lower_bound) + ' upper_bound = ' + str(upper_bound) + ' difference = ' + str(difference))
        if abs(difference) <= tolerance:
            break
        
        if difference < 0:
            lower_bound = guess
        else:
            upper_bound = guess

    #print(int(guess))
    return int(guess)

   
# testing edge cases
print ("Pass" if  (0 == sqrt(0)) else "Fail") 
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (0 == sqrt(-5)) else "Fail")

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")


