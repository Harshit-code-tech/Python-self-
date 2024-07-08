

n = int(input("Enter a number of n:"))

for i in range(n):
    print("1"*(n-i-1),chr(65+i) ,end=" ")
    if i>=1:
        print(" "*(i-1),chr(65+i) ,end=" "*i)
    print()
for i in range(n):
    print("1"*i,chr(65+i),end=" ")
    if i!= n-1:
        print(" "*(n-i-1)+chr(65+i),end=" "*i)
    print()