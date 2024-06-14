num = int(input('Enter number of rows: '))
def triangle(n):
    for i in range(n):
        for k in range(i+1):
            print(1+i,end=' ')
        print()
def pole(n):
    for i in range(n):
        print(1+i)

triangle(num)
triangle(num)
pole(num)