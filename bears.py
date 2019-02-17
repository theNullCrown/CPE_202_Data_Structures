## Name: Allie Blaising, project #1

def bears(n): 
    if n < 42: # if n is less than 42, then you violate rule to win the game 
        return False 
    if n == 42: 
        return True # base case 
    else: 
        if n % 5 == 0: # if n is divisible by 5, then we can give back 42 bears, i.e. n-42 
            test_3 = bears(n - 42) # call bears on updated n 
            if test_3: # if test_3 returns a true, i.e. n == 42 (above), then we return True 
                return True
        if n % 3 == 0 or n % 4 == 0: # if n is divisible by 3 or 4, then we can multiply the last two # and give back that # bears
            if n > 9: # only multiply the last two if it's a number in the tenths or above 
                second_last = (n % 100) // (10) # to find the second to last number 
                first_last = (n % 10) # to find the last number 
                if second_last != 0 and first_last != 0: # check to make sure both # aren't zero so we aren't multiplying by zero 
                    multiply = (second_last * first_last)  
                    test_2 = bears(n - multiply) # call bears on updated n 
                    if test_2: # if test_3 returns a true, i.e. n == 42 (above), then we return True 
                        return True
        if n % 2 == 0: # if n is divisible by 2, then we can divide n by 2 
            test_1 = bears(n // 2) # cal bears on updated n 
            if test_1: # if test_3 returns a true, i.e. n == 42 (above), then we return True 
                return True 
        return False 