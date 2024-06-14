import random 
lower_case="abcdefghijklmnopqrstuvwxyz"
upper_case=lower_case.upper()
number="0123456789"
symbols="!@#$%^&*/\|~.,=+_-"
Use_for=lower_case+upper_case+number+symbols
length_for_pass=8
amount=20
for x in range(amount):

     password="".join(random.sample(Use_for,length_for_pass))
     print("Your generated passwords are:",password)
