# matrix manipulations
def Display(A,c):
    print("Matrix",c)
    for i in A:
        print(*i)


def Addition(A, B):
    print("Addition :: ")
    Add = []
    for i in range(r1):
        a = []
        for j in range(c1):
            a.append(A[i][j] + B[i][j])
        Add.append(a)
    for r in Add: print(*r)


def Subtraction(A, B):
    print("Subtraction :: ")
    Sub = []
    for i in range(r1):
        s = []
        for j in range(c1):
            s.append(A[i][j] - B[i][j])
        Sub.append(s)
    for r in Sub: print(*r)


def Multipication(A, B):
    print("Multiplication :: ")
    Multi = []
    for i in range(r1):
        r = []
        for j in range(c2):
            sum = 0
            for k in range(r2):
                sum = sum + (A[i][k] * B[k][j])
            r.append(sum)
        Multi.append(r)
    for l in Multi: print(*l)


def Transpose(A, r1, c1):
    print("Original Matrix ::")
    for l in A: print(*l)
    print("Transpose of matrix: ")
    tra_a = []
    for k in range(c1):
        r = []
        for j in range(r1):
            r.append(A[j][k])
        tra_a.append(r)
    for l in tra_a: print(*l)


# matrix rows cols input
print("Note:\n1.For addtition and subtraction enter r1=r2 and c1=c2\n2.For multiplication c1=r2")
print("MATRIX A :: ")
r1 = int(input("Enter no. of rows r1 :: "))
c1 = int(input("Enter no. of cols c1 :: "))
print("MATRIX B :: ")
r2 = int(input("Enter no. of rows r2 :: "))
c2 = int(input("Enter no. of cols c2 :: "))

# matrix input
print("enter ", r1 * c1, " elements in RM implementation")
A = []
for i in range(r1):
    r = []
    for j in range(c1):
        r.append(int(input()))
    A.append(r)

print("enter ", r2 * c2, " elements in RM implementation")
B = []
for i in range(r2):
    r = []
    for j in range(c2):
        r.append(int(input()))
    B.append(r)

# menu
loop = 1
while loop:
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Transpose\n5.Quit")
    ch = int(input("Enter :: "))
    if ch == 1:
        if r1 == r2 and c1 == c2:
            Display(A,"A")
            Display(B, "B")
            Addition(A, B)
        else:
            print("Dimension Error r1!=r2 or c1!=c2")
    elif ch == 2:
        if r1 == r2 and c1 == c2:
            Display(A, "A")
            Display(B, "B")
            Subtraction(A, B)
        else:
            print("Dimension Error r1!=r2 or c1!=c2")
    elif ch == 3:
        if c1 == r2:  # and r1 == c2:
            Display(A, "A")
            Display(B, "B")
            Multipication(A, B)
        else:
            print("Dimension Error c1!=r2")
    elif ch == 4:
        print("\nWhich matrix\n1.Matrix A\n2.Matrix B")
        c = int(input("Enter :: "))
        if c == 1:
            Transpose(A, r1, c1)
        elif c == 2:
            Transpose(B, r2, c2)
        else:
            print("Entered something wrong!")
    elif ch == 5:
        print("Thank You!")
        loop = 0
    else:
        print("You entered something wrong")

