from matplotlib import pyplot as plt
import numpy as np
import random

# Precalculates sieve for all numbers <= n
def sieve(n):
    prime = [True for i in range(n + 1)]
    i = 2
    while i * i <= n:
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
        i += 1
    last_prime = -1
    gaps = []
    for i in range(n + 1):
        if prime[i]:
            if last_prime != -1:
                if len(gaps) == 0:
                    gaps.append(i - last_prime)
                else:
                    gaps.append(max(gaps[-1], i - last_prime))
            last_prime = i
    return gaps

def original_model(n):
    # Assume 2 is in the model because 1 / ln(2) > 1
    gaps = []
    last_prime = 2
    for i in range(3, n + 1):
        if random.random() <= 1 / np.log(i):
            if len(gaps) == 0:
                gaps.append(i - last_prime)
            else:
                gaps.append(max(gaps[-1], i - last_prime))
            last_prime = i
    return gaps

def improved_model(n):
    gaps = []
    last_prime = 2
    for i in range(3, n + 1, 2):
        if random.random() <= 2 / np.log(i):
            if len(gaps) == 0:
                gaps.append(i - last_prime)
            else:
                gaps.append(max(gaps[-1], i - last_prime))
            last_prime = i
    return gaps

def main():
    upper_bound = 10000000
    real = sieve(upper_bound)
    original = original_model(upper_bound)
    improved = improved_model(upper_bound)
    plt.plot(np.array(real), label = "P")
    plt.plot(np.array(original), label = "Original")
    plt.plot(np.array(improved), label = "Improved")

    plt.xlabel('x')
    plt.ylabel('Maximal gap up until g_x')
    plt.title('Maximal gaps of actual primes vs Cramer\'s model')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
