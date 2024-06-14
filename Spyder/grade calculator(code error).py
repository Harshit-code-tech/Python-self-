eng=int(input("Enter marks of English: "))
phy=int(input("Enter marks of Physics: "))
che=int(input("Enter marks of Chemistry: "))
math=int(input("Enter marks of Math: "))
ip=int(input("Enter marks of Information Practice: "))
avg=(eng+phy+che+math+ip)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80 & avg<90):
    print("Grade: B")
elif(avg>=70 & avg<80):
    print("Grade: C")
elif(avg>=60 & avg<70):
    print("Grade: D")
else:
    print("Grade: F")