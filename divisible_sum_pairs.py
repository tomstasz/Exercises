def divisible_sum_pairs(n, k, arr):
    counter = 0
    for i in range(n):
        for number in arr[i+1:]:
            if (ar[i] + number) % k == 0:
                counter += 1
    return counter


n = 6
k = 3
ar = [1, 3, 2, 6, 1, 2]

print(divisible_sum_pairs(n, k, ar))