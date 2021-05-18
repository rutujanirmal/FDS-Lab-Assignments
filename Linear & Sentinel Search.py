def sentinel_search(arr, n, x):
    last = arr[n - 1]
    arr[n - 1] = x
    i = 0

    while (arr[i] != x):
        i += 1
    arr[n - 1] = last

    if ((i < n - 1) or (x == arr[n - 1])):
        print("Roll.No::", x, "was present for training")
    else:
        print("Roll.No::", x, "was absent for training")


def linear_search(arr, n, x):
    i = 0
    for i in range(0, n):
        if (arr[i] == x) & (i < n):
            print("Roll.No::", x, "was present for training")
            break;
    else:
        print("Roll.No::", x, "was absent for training")


arr = []
n = int(input("Enter the number of students :: "))
print("Enter Roll no. of students :: ")
for i in range(0, n):
    arr.append(int(input()))
loop = 1
while (loop):
    print(arr)
    print("1.sentinel search")
    print("2.linear search")
    print("3.Quit")
    a = int(input("Enter your choice"))
    if (a == 1 or a == 2):
        x = int(input("Enter Roll.No to be searched"))

    if a == 1:
        sentinel_search(arr, n, x)
    elif a == 2:
        linear_search(arr, n, x)
    elif a == 3:
        print("Thank you")
        loop = 0
    else:
        print("You entered something wrong")
    print("----------------")
