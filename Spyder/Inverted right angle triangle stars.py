rows = int(input("Please Enter the total Number of Rows  : "))
 
print("Inverted Right Angle Triangle of Stars") 
i = rows
while(i > 0):
    j = i
    while(j > 0):      
        print('* ', end = '  ')
        j = j - 1
    i = i - 1
    print()