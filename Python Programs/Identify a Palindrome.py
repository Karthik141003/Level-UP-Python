def palindrome(a):
    a=a.lower()
    if a==a[::-1]:
        print("True")
    else:
        print("False")
string=input()
palindrome(string)
