def isprime(n):
    if n<=1:
        return False
    elif n==2:
        return True
    else:
        sqrt = int(n**0.5)
        for i in range(2,sqrt+1):
            if n % i == 0:
                return False 
        return True