import math
import itertools as it
import time
import numpy as np
import operator

#Decorator that displays amount of time it took function to run
def timedec(PEN):
    def wrapper(*args, **kwargs):
        start = time.time()
        print PEN(*args, **kwargs)
        elapsed = (time.time() - start)
        print "%s seconds" % elapsed

    return wrapper()

def PE1():
    return sum((x for x in range(1000) if x% 3 == 0 or x% 5 == 0))

#Find sum of even fibonacci numbers less that 4-million
def PE2():

    def fib(n):
        fibtup = (0, 1)
        fiblist = []
        while fibtup[1] < n:
            fiblist.append(fibtup[1])
            fibtup = (fibtup[1], sum(fibtup))        
           
        return fiblist
        
    return sum((x for x in fib(4000000) if x%2 == 0))


    '''
Returns array of all prime numbers < n using the Sieve of
Eratosthenes 
    '''
    '''
Makes n-size numpy array of True/False values and then masks values
that are multiples of prime numbers
    '''
def actualsieve(n):
    nums = np.arange((n))
    nums = np.ma.array(np.arange(n), mask = False)

    nums.mask[::2] = True; nums.mask[2] = False
    def maskarray(a, val):
        a.mask[val] = True

    def morefilter(multit, pr, counter): 
        #slower than below (calling is expensive)
        if counter > pr:
            multit = it.ifilter(lambda x: x%pr, multit)

    for x in xrange(3, int(math.floor(math.sqrt(n))) + 1, 2): #odds
        multgen = (a*x for a in xrange(x, int(math.floor(n/x))+1) if a % 2)

        if x > 3:
            multgen = it.ifilter(lambda x: x % 3, multgen)

        [maskarray(nums, mult) for mult in multgen]

    return nums.compressed()


def testprime(x):
    return all((x %n != 0 for n in range(2, int(math.floor(math.sqrt(x))))))

#Find largest prime factor of a big number
def PE3():

    bignum = 600851475143 
    primes = actualsieve(int(math.floor(math.sqrt(bignum))))
    print "primes generated"

    primes = (int(x) for x in primes if x > 1)
    return max((x for x in primes if bignum % x == 0))

def testpalin(n):
    o = str(n)
    return all((o[-x] == o[x - 1] for x in xrange(len(o)/2 + 1)))     

#Find largest palindrome product 
def PE4(): 

    tresdig = (x*y for x in xrange(110, 1000, 11) for y in xrange(100, 1000))
    return max((n for n in tresdig if testpalin(n)))

#Find smallest number divisible by the numbers 1-20
def PE5(maxfac):
    # could make faclist, i.e only have x%16, no need for x%8, x%4 etc.
    def facgen():
        x = maxfac
        while all((x % n == 0 for n in range(2, maxfac + 1))) == False:
            x += 10
            yield x
        
    return max(facgen())

#Difference between sum of squares and square of sums of 1-100
def PE6():
    return (sum(x for x in xrange(1, 101)))**2 - sum(x**2 for x in xrange(1, 101)) 

#Find 10001st prime
@timedec
def PE7():
    primegen = actualsieve(int(4e6))
    return list(it.islice(primegen, 10001, 10002))

def product(iterable):
    return reduce(operator.mul, iterable, 1)

#Find largest product of 13 adjacent numbers in this big number
def PE8():
    bignum = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
    return max(product(int(num) for num in it.islice(bignum, n, n+13))
            for n in xrange(len(bignum) - 13))
    
#Find a*b*c of pythagorean triplet where a+b+c = 1000
def PE9():
    #Returns generator of pythagorean triplets less than some number
    def gettrips(maxnum):
        n = [num**2 for num in xrange(1, maxnum)]
        print 'list done'
        return ((a,b,c) for a in n for b in n for c in
                n if a < b and a + b == c)

    trip = it.ifilter(lambda tup: tup[0]**0.5 + tup[1]**0.5 +
        tup[2]**0.5 == 1000 , gettrips(1000))

    return [n[0]**0.5 * n[1]**0.5 * n[2]**0.5 for n in trip]

def PE10():
    '''
With actual sieve, took 1.68 sec as opposed to ~60 sec w/old sieve
function
    '''
    return np.sum(actualsieve(2000000)) - 1 #1 is not counted as prime this prob

'''
separate challenge: come up with recursive fib(a, b), that uses
constant space
'''
