import math
import petools as pe
import itertools as it
import numpy as np


#Takes 20 x 20 grid of numbers, finds greatest product of four adjacent numbers (horizantally, vertically or diagonally
def PE11():
    longstring = open('p11.txt', 'r')
    rows = [line.rstrip('\n').split(' ') for line in longstring.readlines()]
    arr = np.array(rows, dtype = 'int')
    dim = arr.shape[1]
    maxrow = max(np.product(arr[n:n+4,m]) for n in xrange(dim - 3) for m in
            xrange(dim))
    maxcol = max(np.product(arr[n,m:m+4]) for n in xrange(dim) for m in
            xrange(dim - 3))

    def getdiag1(x, y):
        return pe.product(arr[x+i, y+i] for i in [0,1,2,3])

    def getdiag2(x,y):
        return pe.product(arr[x-i, y+i] for i in [0,1,2,3])

    maxdiag1 = max(getdiag1(n,m) for n in xrange(dim-3) for m
            in xrange(dim-3))
    maxdiag2 = max(getdiag2(n,m) for n in xrange(3, dim) for m
            in xrange(dim-3))

    return max(maxdiag2, maxdiag1, maxcol, maxrow)


[Ma-[Ma--
#gets nth triangle number
def tri(n):
    return sum(i for i in xrange(n+1))

#returns generator of factors of n, probably not best way
def getfacs(n):
    it1 = [n/i for i in xrange(1, int(math.floor(n**0.5)) + 1) if n%i
            == 0]
    it2 = [n/i for i in it1]
    return list(set(it1 + it2)) #to remove duplicates

#Find first triangular number with over five hundred divisors    
def PE12():
    notfound = True
    n = 1
    while notfound:
        if len(getfacs(tri(n))) < 501:
            n += 1; continue
        else:
            return tri(n)

#finds longest collatz sequence with starting number < 1,000,000
#collatz is iterative sequence where n -> n/2 if n even, n -> 3n + 1 if n odd
#a collatz sequence will end at 1 (but this is not yet proven!)
def PE14():
    def collatz(n, count):
        count += 1
        if n == 1:
            return count

        elif n%2:
            n = 3*n + 1
            return collatz(n, count)

        elif n%2 == 0:
            n = n / 2
            return collatz(n, count)
    
    def genmaxind(gen):
        #or could yield some inds somehow
        genmax = 0; maxind=0; ind = 0

        for i in gen:
            ind +=1
            if i > genmax:
                genmax = i
                maxind = ind
            else:
                continue

        return maxind

    collgen = (collatz(num, 0) for num in xrange(1, 1000000))
    return genmaxind(collgen)

#combinatorics question
def PE15():
    return pe.factorial(40) / (pe.factorial(20) * pe.factorial(20))


def PE16():
    return sum(int(char) for char in str(2**1000))

#@pe.timedec
def PE18():
    trilines = open("P18_tri.txt", 'r').readlines()
    trilines = [line.rstrip('\n') for line in trilines]
    bestsums = []
    print trilines

#find sum of digits in n!
def PE20(n):
    factval = str(reduce(lambda x, y: x * y, xrange(1, n)))
    return reduce(lambda x, y : int(x) + int(y), factval)

print PE20(100)
        

