# Set operations

# remove duplicate elements
def Remove(list1):
    final_list = []
    for num in list1:
        if num not in final_list:
            final_list.append(num)
    return final_list


# union operation
def Union(list1, list2):
    final_list = list1.copy()
    for num in list2:
        if num not in list1:
            final_list.append(num)
    return final_list


# intersection operation
def Intersection(list1, list2):
    final_list = []
    for num in list1:
        if num in list2:
            final_list.append(num)
        else:
            None
    return final_list


# difference operation
def Difference(list1, list2):
    final_list = []
    for num in list1:
        if num not in list2:
            final_list.append(num)
    return final_list


# symmetric difference
def SymDifference(list1, list2):
    intersection = Intersection(list1, list2)
    union = Union(list1, list2)
    return Difference(union, intersection)


# main
# input
u = []
n = int(input("Enter total no of students in the class :"));
print("Enter roll no of students :")
for i in range(0, n):
    element = int(input())
    u.append(element)

c = []
n1 = int(input("Enter total no of students who play cricket :"));
print("Enter roll no of students who play cricket :")
for i in range(0, n1):
    element = int(input())
    c.append(element)
b = []
n2 = int(input("Enter total no of students who badminton :"));
print("Enter roll no of students who play badminton :")
for i in range(0, n2):
    element = int(input())
    b.append(element)

f = []
n3 = int(input("Enter total no of students who play football :"));
print("Enter roll no of students who play football :")
for i in range(0, n3):
    element = int(input())
    f.append(element)

# removing duplicates
u = Remove(u)
c = Remove(c)
b = Remove(b)
f = Remove(f)

# printing all lists
print("Group A : CRICKET :: ", c)
print("Group B : BADMINTON :: ", b)
print("Group C : FOOTBALL :: ", f)

# menu
loop = 1
while loop:  # expected output
    print("\n1.List of students who play both cricket and badminton")  # [5]
    print("2.List of students who play either cricket or badminton but not both")  # [1, 2, 7, 10]
    print("3.Number of students who play neither cricket nor badminton")  # [3,4,6,8,9]
    print("4.Number of students who play cricket and football but not badminton")  # [10]
    print("5.Quit")
    choice = int(input("Enter Choice :: "))
    if choice == 1:
        print("\nStudents who play both cricket and badminton\n", Intersection(c, b))
    elif choice == 2:
        print("\nStudents who play either cricket or badminton but not both\n", SymDifference(c, b))
    elif choice == 3:
        print("\nNumber of students who play neither cricket nor badminton ::", len(Difference(u, Union(c, b))),
              "\nRoll.NO :: ", Difference(u, Union(c, b)))
    elif choice == 4:
        print("\nNumber of students who play cricket and football but not badminton",
              len(Difference(Intersection(c, f), b)),
              "\nRoll.NO :: ", Difference(Intersection(c, f), b))
    elif choice == 5:
        print("\nThank you")
        loop = 0
    else:
        print("\nYou entered something wrong")

# expected input
# u = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # class
# c = [2, 5, 10]  # cricket
# b = [1, 5, 7]  # badminton
# f = [5, 7, 10]  # football
