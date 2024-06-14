import mysql.connector as sql
import sys
abcd=sql.connect(host="localhost",user="root",password="abcd1234",database="mysql")
mycursor=abcd.cursor()
if abcd.is_connected():
    print("succesfully connected")
else:
    print("Not connected")


def  newStudent():
    try:
        print(" CREATING STUDENT TABLE")
        newtable="CREATE TABLE IF NOT EXISTS STUDENT(ROLL_NO INT(5),SNAME VARCHAR(30),FNAME VARCHAR(30),MNAME VARCHAR(30) ,PHONE_NO INT(12), ADDRESS VARCHAR(100),CLASS VARCHAR(5),SECTION VARCHAR(5), ADMISSION_NO  INT(10) PRIMARY KEY)"
    except:
         print("sorry some error occured")

    mycursor.execute(newtable)
    roll_no=input(" ENTER ROLL_NO : ")
    sname=input(" ENTER STUDENT'S NAME : ")
    fname=input(" ENTER FATHER'S NAME : ")
    mname=input(" ENTER MOTHER'S NAME : ")
    phone=input(" ENTER CONTACT NO. : ")
    address=input(" ENTER ADDRESS : ")
    sclass =input(" ENTER CLASS : ")
    section=input(" ENTER SECTION : ")
    admission_no=input(" ENTER ADMISSION_NO : ")
    newstudent="insert into student (roll_no,student name,mother name,father name,phone,address,class,section,admission_no) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values=(roll_no,sname,fname,mname,phone,address ,sclass,section,admission_no)
    mycursor.execute(newstudent,values)
    mycursor.execute("COMMIT")
    mycon.commit()
    cursor.close()

print("-----------------------*******************----------------------")
while(1):
    print("|	Enter 1 -  Add Student		                       |")
    print("|	Enter 2 -  Display Student's Data.		       |")
    print("|	Enter 3 -  Update Students's Data .		       |")
    print("|	Enter 4 -  Add Student's Marks Detail.		       |")
    print("|	Enter 5 - TO SEARCH A STUDENT RECORD.                  |")
    print("|	Enter 6 - Generate All Student's Report Card.          |")
    print("|	Enter 7 - Generate Student Wise Report Card.           |")
    print("|	Enter 8-  Exit.	                                       |")
    print("|	Enter 0(ZERO) - Help.	                               |")
    print("-----------------------*******************----------------------")
    choice=int(input("PLEASE  ENTER  YOUR  CHOICE:"))
      
    if choice==1:
        newStudent()
    elif choice==2:
        displayStudent()
    elif choice==3:
        updateStudent()
    elif choice==4:
        marksStudent()
    elif choice==5:
        marksStudent()    
    elif choice==6:
        reportCardAllStudent()
    elif choice==7:
        reportCardOneStudent()
    elif choice==8:
        quit()
    elif choice==0:
        helpMe()
    else:
        print("Sorry ,May Be You Are Giving Me Wrong Input,Please Try Again!")


