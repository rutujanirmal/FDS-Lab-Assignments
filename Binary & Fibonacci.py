def binary_search(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            print("Roll.No:: ", x, " was present for training\n")
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, r, x)
    else:
        print("Roll.No:: ", x, " was absent for training\n")


def fibonacci(item, x, n):
    fib2 = 0 
    fib1 = 1
    fibn = fib2 + fib1 
    while (fibn < n):
        fib2 = fib1
        fib1 = fibn
        fibn = fib2 + fib1
    offset = -1
    while (fibn > 1):
        i = min(offset + fib2, n - 1)

        if (item[i] < x):
            fibn = fib1
            fib1 = fib2
            fib2 = fibn - fib1
            offset = i
        elif (item[i] > x):
            fibn = fib2
            fib1 = fib1 - fib2
            fib2 = fibn - fib1
        else:
            return i

    if (fib1 and item[n - 1] == x):
        return n - 1;

    return -1


arr = []
n = int(input("Enter the number of students :: "))
print("Enter Roll no. of students :: ")
for i in range(0, n):
    arr.append(int(input()))
arr.sort()
loop = 1
while (loop):
    print(arr)
    print("1.Binary search")
    print("2.Fibonacci search")
    print("3.Quit")
    a = int(input("Enter your choice"))
    if (a == 1 or a == 2):
        x = int(input("Enter Roll.No to be searched"))

    if (a == 1):
        binary_search(arr, 0, n - 1, x)
    elif (a == 2):
        f = fibonacci(arr, x, len(arr))
        if (f == -1):
            print("Roll.No:: ", x, " was absent for training\n")
        else:
            print("Roll.No:: ", x, " was present for training\n")
    elif (a == 3):
        print("thank you")
        loop = 0
    else:
        print("You entered something wrong")

