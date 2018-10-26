import math
import itertools as it
import time
import numpy as np
import operator

#Decorator that displays amount of time program took to run
def timedec(PEN):
    def wrapper(*args, **kwargs):
        start = time.time()
        print PEN(*args, **kwargs)
        elapsed = (time.time() - start)
        print "%s seconds" % elapsed

    return wrapper()

#Sieve of Erathosthenes 
def actualsieve(n):
    nums = np.arange((n))
    nums = np.ma.array(nums, mask = False)

    nums.mask[::2] = True; nums.mask[2] = False #eliminate evens

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

    return nums

def testprime(x):
    return all((x %n != 0 for n in range(2, int(math.floor(math.sqrt(x))))))

def testpalin(n):
    o = str(n)
    return all((o[-x] == o[x - 1] for x in xrange(len(o)/2 + 1)))     

def product(iterable):
    return reduce(operator.mul, iterable, 1)

def factorial(n):
    return product((x for x in xrange(1, n+1)))

def divisors(n):
    list1 = [] ; list2 = []
    for x in xrange(2, int(math.floor(math.sqrt(n))) + 1):
        if n % x == 0:
            list1.append(x); list2.insert(0, n / x)
    return iter(set([1] + list1 + list2))
