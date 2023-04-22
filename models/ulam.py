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
    nums = [1, 2]
    for i in range(3, n):
        count = 0
        for j in range(len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[j] + nums[k] == i:
                    count += 1
        if count == 1:
            nums.append(i)
    print(nums)
    return nums
    pre = [];
    sum = 0
    for i in range(n):
        if i in nums:
            sum += 1
        pre.append(sum)

    return pre


def main():
    real = ulam(6000);
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
    plt.title('Distribution of the Ulam numbers')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
