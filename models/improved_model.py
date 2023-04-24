from matplotlib import pyplot as plt
import numpy as np
import random
import sympy
from sympy.ntheory.factor_ import totient
import math
import operator
import functools

def original_model(n, l):
    # Assume 2 is in the model because 1 / ln(2) > 1
    primes = [2]
    i = 3
    while (len(primes) < l):
        if random.random() <= 1 / np.log(i):
            primes.append(i)
        i += 1
    return primes

def improved_model(p, l, phi):
    # Assume 2 is in the model because 1 / ln(2) > 1
    primes = [2]
    i = 3
    while (len(primes) < l):
        if math.gcd(i, p) == 1 and random.random() <= p / (phi * np.log(i)):
            primes.append(i)
        i += 1
    return primes

def main():
    upper_bound = 10000
    real = list(sympy.primerange(upper_bound))
    original = original_model(upper_bound, len(real))
    k = math.floor(np.log(len(real)))
    p = functools.reduce(operator.mul, real[0:k], 1)
    phi = sympy.totient(p)
    improved = improved_model(p, len(real), phi)
    plt.plot(np.array(real), label = "P")
    plt.plot(np.array(original), label = "Original")
    plt.plot(np.array(improved), label = "Improved")

    plt.xlabel('x')
    plt.legend()
    plt.savefig("../images/Improvement.pdf", format="pdf", bbox_inches="tight")
    plt.show()

if __name__ == "__main__":
    main()
