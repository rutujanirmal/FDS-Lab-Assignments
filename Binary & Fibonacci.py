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


def FibonacciGenerator(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return FibonacciGenerator(n - 1) + FibonacciGenerator(n - 2)


def FibonacciSearch(arr, x):
    try:
        m = 0
        while FibonacciGenerator(m) < len(arr):  #
            m = m + 1
        offset = -1
        while (FibonacciGenerator(m) > 1):
            i = min(offset + FibonacciGenerator(m - 2), len(arr) - 1)
            if (x > arr[i]):
                m = m - 1
                offset = i
            elif (x < arr[i]):
                m = m - 2
            else:
                return i
        if (FibonacciGenerator(m - 1) and arr[offset + 1] == x):
            return offset + 1
        return -1
    except:
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
        f = FibonacciSearch(arr, x)
        if (f == -1):
            print("Roll.No:: ", x, " was absent for training\n")
        else:
            print("Roll.No:: ", x, " was present for training\n")
    elif (a == 3):
        print("thank you")
        loop = 0
    else:
        print("You entered something wrong")
