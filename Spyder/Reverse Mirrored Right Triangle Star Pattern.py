rows = int(input("Please Enter the Total Number of Rows  : "))

print("Reverse Mirrored Right Triangle Star Pattern") 
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if(j < i):
            print(' ', end = '  ')
        else:
            print('*', end = '  ')
    print()