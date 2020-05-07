import math

def nxtPrime(prime):
    checkPrimes = [2, 3]
    for num in range(int(math.sqrt(prime))):
        for i in range(int(math.sqrt(num))):
            if(not(num % i)):
                checkPrimes.append(num)
    #while(true):
    #    prime += 2
    return checkPrimes

##def getPrimesInRange(low, high):
##    primes = []
##    checkPrimes = []
##    prime = true
##    
##    for num in range(low, high):
##        primes.append(num)
##
##    for num in range(len(primes)-1, -1, -1):
##        while(prime & notToMax):
            

#getPrimesTo(100, 1)

#primesInRange(10**10*5, 10**10*5 + 1000)

print(nxtPrime(17))




































