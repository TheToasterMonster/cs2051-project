import time
import numpy as np
import matplotlib.pyplot as plt
import math
import sympy
from timer import timed
import random

def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
def corseltCriterion(n):
    for i in range(2, n - 1):
        if n % i == 0:
            if i - 1 % n - 1 != 0 and isPrime(i) and i^2 % n == 0:
                return False
    return True
@timed
def SieveOfEratosthenes(n):
    list = []
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n + 1):
        if prime[p]:
            list.append(p)
    return list
@timed
def findPrimeWithFerm(n):
    b = 3
    while b < n:
        if np.gcd(b, n) == 1:
            if pow(b, n - 1, n) != 1:
                return 0
        b = b + 1
    return 1
def generatePrimeWithFerm(num):
    list = []
    for i in range(3, num):
        if findPrimeWithFerm(i) == 1:
            list.append(i)
    return list
@timed
def findPrimeWithMillerRandUnop(num, k):
    num2 = num - 1
    pow2 = 0
    while num2 % 2 == 0:
        num2 = int(num2/2)
        pow2 = pow2 + 1
    for i in range(k):
        a = random.randint(2, num - 2)
        x = pow(a, num2, num)
        y = 0
        for i in range(pow2):
            y = pow(x, 2, num)
            if y == 1 and (x != 1) and x != (num - 1):
                return 0
            x = y
        if (y != 1):
            return 0
    return 1
def generatePrimeWithMillerRandUnop(n, k):
    list = []
    for i in range(4, n):
        if findPrimeWithMillerRandUnop(i, k) == 1:
            list.append(i)
    return list
def isCarm(n):
    b = 2
    while b < n:
        if np.gcd(b, n) == 1:
            if pow(b, n - 1, n) != 1:
                return 0
        b = b + 1
    if not isPrime(b):
        return 1
    else:
        return 2
def carmList(num):
    returnable = set()
    for i in range(num):
        if isCarm(i) == 1:
            returnable.add(i)
            print(i)
    return returnable
def getCoordinate(num):
    return num*np.cos(num), num*np.sin(num)
def create_plot(nums, times):
    plt.style.use("dark_background")
def getAccuracy(nums, k):
    primeList = set(sympy.primerange(5, k))
    return primeList.difference(set(nums))
def main():
    timeForMiller = []
    timeForFermat = []
    timeForSieve = []
    start = 10000000
    end = 10000000000
    for c in range(5):
        g = random.randint(start, end)
        start1 = time.time()
        SieveOfEratosthenes(g)
        end1 = time.time()
        timeForSieve.append(end1 - start1)
        start2 = time.time()
        findPrimeWithFerm(g)
        end2 = time.time()
        timeForFermat.append(end2 - start2)
        start3 = time.time()
        findPrimeWithMillerRandUnop(g, 5)
        end3 = time.time()
        timeForMiller.append(end3 - start3)
        start = start + end
        end = 2 * end
    plt.figure().canvas.manager.set_window_title("Prime Generating Algorithms - Time Complexity")
    plt.xlabel("No. of Numbers")
    plt.ylabel("Execution Time (ms)")
    plt.plot([i for i in range(len(timeForSieve))], [1000 * i for i in timeForSieve], label="Time For Sieve")
    plt.plot([i for i in range(len(timeForFermat))], [1000 * i for i in timeForFermat], label="Time For Fermat")
    plt.plot([i for i in range(len(timeForMiller))], [1000 * i for i in timeForMiller], label="Time For Miller-Rand")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()