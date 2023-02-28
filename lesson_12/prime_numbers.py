def is_prime(n):
    if n > 1:  
        for x in range(2, n):  
            if n % x == 0:  
                return False
        return True
    else:
        return False