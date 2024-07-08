t = int(input('Enter number of rows: '))
def Leaf(n):
    for i in range(n):
        for j in range(n-i):
            print(' ', end=' ')
        for k in range(2*i+1):
            print('*',end=' ')
        print()
def Log(n):
    for i in range(n):
        for j in range(n-1):
            print(' ', end=' ')
        print('* * *')
Leaf(t)
Leaf(t)
Log(t)