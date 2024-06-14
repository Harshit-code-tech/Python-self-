rows = int(input("Enter Hollow Right Inverted Triangle Rows = "))

print("Hollow Inverted Right Triangle Star Pattern") 

for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        if i == 1 or i == rows or j == 1 or j == i:
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print()

