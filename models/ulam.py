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



def ulam(n):
    if n <= 2:
        return n
    mx = 1352000
    lst = [1, 2] + [0] * mx
    sums = [0] * (mx * 2 + 1)
    sums[3] = 1
    size = 2
    while size < n:
        query = lst[size-1] + 1
        while True:
            if sums[query] == 1:
                for i in range(size):
                    sum = query + lst[i]
                    t = sums[sum] + 1
                    if t <= 2:
                        sums[sum] = t
                lst[size], size = query, size + 1
                break
            query += 1
    return query

def main():
    real = []
    for i in range(600):
        real.append(ulam(i))
    line = []
    sum = 0
    for i in range(len(real)):
        sum += 13.51
        line.append(sum)
    #fake = cramer_model(1000000);
    plt.plot(np.array(real), label = "Ulam numbers")
    plt.plot(line, label = "y = 13.51x")
    # plt.plot(np.array(fake), label = "P'")
    plt.xlabel('x')
    plt.ylabel('U_x')
    plt.legend()
    plt.savefig("../images/Ulam_distribution.pdf", format="pdf", bbox_inches="tight")
    plt.show()

if __name__ == "__main__":
    main()
