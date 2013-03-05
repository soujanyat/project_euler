#!/usr/bin/env python
# Largest prime factor
"""
#prime number : A prime number is any natural number that can only be divided
#by 1 or itself. E.G. 7 is a prime number because it can only be divided by
#1 or 7 while 10 is not a prime number because its divisors are 1,2,5,10.

#Method to find prime factor-->: The method of finding prime factors is called
#Prime Factorisation.  It involves taking a number and dividing it by the
#smallest prime possible, then taking what is remaining and dividing that by
#the smallest prime possible; keep doing this until the remainder is a prime.

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#Answer = 6857
"""

import time

n = 600851475143
i = 2
while i * i < n:
    while n % i == 0:
        n = n / i
    i = i + 1
start = time.time()
end_time = (time.time() - start)

print "result %s returned after %s seconds." % (n, end_time)


#import time
 
#def largest_prime_factor(n):
 
    #largest_factor = 1
 
    ## remove any factors of 2 first
    #while n % 2 == 0:
        #largest_factor = 2
        #n = n/2
 
    ## now look at odd factors
    #p = 3
    #while n != 1:
        #while n % p == 0:
            #largest_factor = p
            #n = n/p
        #p += 2
 
    #return largest_factor
 
#start = time.time()
#for i in range(100000): a = largest_prime_factor(600851475143)
#elapsed = (time.time() - start)
 
#print "result %s returned after %s seconds (100,000 iterations)." % (a, elapsed)
