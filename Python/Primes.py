import math

def getPrimesTo(max, p = 0):
    primes = []
    count = 0
    length = max

    for i in range(2, max):
        primes.append(i)
    
    while(length > len(primes)):
        length = len(primes)
        num = primes[count]
        for i in range(len(primes)-1, count, -1):
            if(not(primes[i]%num)):
                del primes[i]
        count += 1
    
    if(p):
        print(primes)

    return primes

def primesInRange(min, max):
    print("Primes from " + str(min) + " to " + str(max) + ":")
    
    primes = []
    for i in range(min, max):
        primes.append(i)

    checkPrimes = getPrimesTo(int(math.sqrt(max)+1))
    #print(checkPrimes)
    
    for checkPrime in checkPrimes:
        for i in range(len(primes)-1, -1, -1):
            if(not(primes[i]%checkPrime)):
                del primes[i]

    print(primes)


#getPrimesTo(100, 1)

primesInRange(10**10*5, 10**10*5 + 1000)






































