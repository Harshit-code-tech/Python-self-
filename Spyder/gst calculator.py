OP=float(input("Enter Original Price:"))
NP = float(input("Enter Net Price:"))
GST_amount = NP - OP
GST_percent = ((GST_amount * 100) / OP)
print("GST = ",end='')  
print(GST_percent,end='')  
print("%")