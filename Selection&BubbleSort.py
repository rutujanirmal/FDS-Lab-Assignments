def selection_sort(arr, n):
    for i in range(0, n):
        min = i
        for j in range(i + 1, n):
            if [arr[min] > arr[j]]:
                min = j
            arr[i], arr[min] = arr[min], arr[i]


def bubble_sort(arr, n):
    for i in range(0, n):
        swapped = 0
        for j in range(0, n - i - 1):
            if (arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = 1
        if (swapped == 0):
            break


arr = []
n = int(input("Enter the number of students :: "))
print("Enter percentage of all students :: ")
for i in range(0, n):
    arr.append(float(input()))

# menu
print("\n", arr, "\n")
print("ENTER THE METHOD YOU WANT TO USE :: ")
print("1.Selection sort")
print("2.Bubble sort")
choice = int(input("Enter choice here :: "))
if (choice == 1):
    selection_sort(arr, n)
elif (choice == 2):
    bubble_sort(arr, n)
else:
    print("You entered something wrong")
    exit()

# displaying acending order list
print("\nPercentage in ascending order is:")
print(arr)

# dispalying top 5 scores(top scores if less than 5 students)
print("\nTop Score")
try:
    for i in range(-1, -6, -1):
        print(-i, "rank :: ", arr[i])
except:
    None

