def sort_string(a):
    b=a.split(' ')
    b.sort()
    d=''
    for i in b:
        d=d + i + " "
    print('Sorted String:',d)
string=input()
sort_string(string)
