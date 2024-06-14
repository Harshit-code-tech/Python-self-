ac = float(input("Enter the Cost Price: "))
sc = float(input("Enter the Sales Price: "))
 
if(ac > sc):
    amount = ac - sc
    print("Total Loss Amount = {0}".format(amount))
elif(sc > ac):
    amount = sc - ac
    print("Total Profit = {0}".format(amount))
else:
    print("No Profit No Loss!!!")