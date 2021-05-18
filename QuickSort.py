def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]             #swapping
    arr[i + 1], arr[high] = arr[high], arr[i + 1]       #swapping
    return (i + 1)


def quicksort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


# input array
arr = []
n = int(input("Enter the number of students :: "))
print("Enter percentage of all students :: ")
for i in range(0, n):
    arr.append(float(input()))

# qucik sort
quicksort(arr, 0, n - 1)
while(True):
    print("MENU::\n1.Display in ascending order.\n2.Display Top 5 scores\n3.Quit")
    n=int(input("Enter :: "))
    if(n==1):
        # displaying acending order list
        print("Percentage in ascending order is:")
        print(arr)
    elif(n==2):
        # dispalying top 5 scores(top scores if less than 5 students)
        print("Top Score")
        try:
            for i in range(-1, -6, -1):
                print(-i,"rank :: ",arr[i])
        except:
            None
    elif(n==3):
        print("Thank u")
        break
    else:
        print("You entered something wrong")
