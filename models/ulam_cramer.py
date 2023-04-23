from matplotlib import pyplot as plt
import numpy as np
import random

# Precalculates sieve for all numbers <= n
def ulam_model(n):
    nums = []
    for i in range(1, n):
        if random.random() <= 0.074:
            nums.append(i)
    print(nums)
    return nums

# def ulam(n):
#     nums = [1, 2]
#     i = 3
#     while len(nums) < n:
#         count = 0
#         for j in range(len(nums) - 1):
#             for k in range(j + 1, len(nums)):
#                 if nums[j] + nums[k] == i:
#                     count += 1
#         if count == 1:
#             nums.append(i)
#         i += 1
#     return nums


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
    fake = ulam_model(10000)
    real = []
    for i in range(1, len(fake)):
        real.append(ulam(i))
    line = []
    sum = 0
    for i in range(len(real)):
        sum += 13.51
        line.append(sum)
    #fake = cramer_model(1000000);
    plt.plot(np.array(fake), label = "Fake Ulam numbers")
    plt.plot(np.array(real), label = "Actual Ulam numbers")
    plt.plot(line, label = "y = 13.51x")
    # plt.plot(np.array(fake), label = "P'")
    plt.xlabel('x')
    plt.ylabel('U_x')
    plt.legend()
    plt.savefig("../images/Ulam_cramer.pdf", format="pdf", bbox_inches="tight")
    plt.show()

if __name__ == "__main__":
    main()
