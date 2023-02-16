
array1 = [10, 22, 9, 33, 21, 50, 41, 60, 80]


def men(array, n):
    global maximum
    if n == 1:
        return 1
    maxend = 1

    for i in range(1, n):
        con = men(array, i)
        if array[i - 1] < array[n - 1] and con+ 1 > maxend:
            maxend = con + 1

    maximum = max(maximum, maxend)
    return maxend


def lis(array1):
    global maximum
    m = len(array1)
    maximum = 1
    men(array1, m)
    return maximum


n = len(array1)

print("Length of LIS for ", array1, " is ", lis(array1))
