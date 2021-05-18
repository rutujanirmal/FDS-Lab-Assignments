# write a python code to compute following operations on string
# 1.To display word with longest length
# 2.To determine the frequency of occurance of a particular character
# 3.To check whether given string is palindrome or not
# 4.To display index of first apperance if s subtring
# 5.To count the occurance of each word in the string

def long_word(l):
    long = 0
    num = -1
    for i in l:
        num += 1
        if len(str(i)) > long:
            long = len(str(i))
            ind = num
    print(l[ind])


def frequency(string, c):
    print(c, "occurs", string.count(c), "times in", string)


def palindrome(l):
    li = "".join(l)
    rev = li[::-1]
    if li == rev:
        print("\nString is palindrome")
    else:
        print("\nString is NOT a palindrome")


def first_ind(string, subs):
    if  subs in string:
        print(subs, "occurs at", string.index(subs), "index")
    else:
        print(subs, "not present")


def occ_words(l):
    ind = -1
    for i in l:
        ind += 1
        if str(i) not in l[ind + 1:]:
            print(i, "occurs", l.count(i))


# main
string = input("Enter the string :: ")
while True:
    print(" \n 1.To display word with longest length")
    print(" 2.To determine the frequency of occurance of a particular character")
    print(" 3.To check whether given string is palindrome or not")
    print(" 4.To display index of first apperance of subtring")
    print(" 5.To count the occurance of each word in the string")
    print(" 6.Quit")
    ch = int(input("\nEnter choice :: "))
    l = string.split(" ")
    if ch == 1:
        long_word(l)
    elif ch == 2:
        c = input("\nEnter the character :: ")
        frequency(string, c)
    elif ch == 3:
        palindrome(l)
    elif ch == 4:
        subs = input("Enter substring :: ")
        first_ind(string, subs)
    elif ch == 5:
        occ_words(l)
    elif ch == 6:
        print("Thank you")
        break
    else:
        print("You entered something Wrong")



