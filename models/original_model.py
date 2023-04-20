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

def cramer_model(n):
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

def main():
    real = sieve(1000000);
    fake = cramer_model(1000000);
    plt.plot(np.array(real), label = "P")
    plt.plot(np.array(fake), label = "P'")
    plt.xlabel('x')
    plt.ylabel('Maximal gap up until g_x')
    plt.title('Maximal gaps of actual primes vs Cramer\'s model')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
