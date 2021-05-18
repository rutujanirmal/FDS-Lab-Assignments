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


# input
u = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]  # class
c = [2, 5, 9, 12, 13, 2, 15, 16, 17, 18, 19]  # cricket
b = [1, 2, 5, 9, 10, 11, 9, 12, 13, 15]  # badminton
f = [2, 4, 5, 6, 7, 9, 13, 16]  # football

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
while loop:                                                         #expected output
    print("\n1.List of students who play both cricket and badminton")  # [2,5,9,12,13,15]
    print("2.List of students who play either cricket or badminton but not both")  # [1,10,11,16,17,18,19]
    print("3.Number of students who play neither cricket nor badminton")  # [3,4,6,7,8,14]
    print("4.Number of students who play cricket and football but not badminton")  # [16]
    print("5.Quit")
    choice = int(input("Enter Choice :: "))
    if choice == 1:
        print("\nStudents who play both cricket and badminton\n", Intersection(c, b))
    elif choice == 2:
        print("\nStudents who play either cricket or badminton but not both\n", SymDifference(c, b))
    elif choice == 3:
        print("\nNumber of students who play neither cricket nor badminton ::",len(Difference(u, Union(c, b))),
              "\nRoll.NO :: ",Difference(u, Union(c, b)))
    elif choice == 4:
        print("\nNumber of students who play cricket and football but not badminton",len(Difference(Intersection(c, f), b)),
              "\nRoll.NO :: ",Difference(Intersection(c, f), b))
    elif choice == 5:
        print("\nThank you")
        loop = 0
    else:
        print("\nYou entered something wrong")
