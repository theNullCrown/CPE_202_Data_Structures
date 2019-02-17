def bears(n): 
    if n < 42: 
        return False 
    if n == 42: 
        return True 
    else: 
        if n % 5 == 0: 
            test_3 = bears(n - 42)
        if n % 2 == 0:  
            test_1 = bears(n // 2)
        if n % 3 == 0 or n % 4 == 0: 
            if n > 9: 
                second_last = (n % 100) // (10) 
                first_last = (n % 10) 
                if second_last != 0 and first_last != 0: 
                    multiply = (second_last * first_last)  
                    test_2 = bears(n - multiply) 
        return False
        
bears(250)