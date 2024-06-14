import os
import platform
import mysql.connector as m
bcd=m.connect(host="localhost",user="root",password="abcd1234",database="newstudent",charset="utf8")

if bcd.is_connected():
    print("SUCCESFULLY CONNECTED")
    print(">------------------------------------------------------------------------<")
else:
    print("NOT CONNECTED")
    print(">------------------------------------------------------------------------<")
mycursor=bcd.cursor(buffered=True)

#MENU FOR STUDENT MARKS MANAGEMENT SYSTEM SOFTWARE
print("*************************************************")
print("WELCOME TO STUDENT MARKS MANAGEMENT SYSTEM")
print("*************************************************")
#MODULE FOR NEW ADMISSION

def  newStudent():
    try:
        print(" CREATING STUDENT TABLE")
        newtable="CREATE TABLE IF NOT EXISTS STUDENT(ROLL_NO VARCHAR(5),SNAME CHAR(30),FNAME CHAR(30),MNAME CHAR(30) ,PHONE_NO VARCHAR(12), ADDRESS VARCHAR(100),SCLASS VARCHAR(5),SECTION VARCHAR(5), ADMISSION_NO  INT(10) PRIMARY KEY)"
    except:
        print("sorry some error occured")
        
   
    mycursor.execute("SELECT * FROM STUDENT")    
    ROLL_NO=input(" ENTER ROLL_NO : ")
    SNAME=input(" ENTER STUDENT'S NAME : ")
    FNAME=input(" ENTER FATHER'S NAME : ")
    MNAME=input(" ENTER MOTHER'S NAME : ")
    PHONE=input(" ENTER CONTACT NO. : ")
    ADDRESS=input(" ENTER ADDRESS : ")
    SCLASS =input(" ENTER CLASS : ")
    SECTION=input(" ENTER SECTION : ")
    ADMISSION_NO=input(" ENTER ADMISSION_NO : ")
    data=(ROLL_NO,SNAME,FNAME,MNAME,PHONE,ADDRESS ,SCLASS,SECTION,ADMISSION_NO)  
    new="INSERT INTO STUDENT VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    
    mycursor.execute(new,data)
    bcd.commit()
    mycursor.close()

#MODULE TO UPDATE STUDENT'S RECORD
def updateStudent():
    admission_no=int(input("ENTER ADMISSION NO :"))
    new="SELECT * FROM STUDENT WHERE ADMISSION_NO= %d"
    mycursor.execute(new,admission_no)
    data=mycursor.fetchall()
    if data:
        print("PRESS 1 FOR NAME")
        print("PRESS 2 FOR CLASS")
        print("PRESS 3 FOR ROLL NO")
        choice=int(input("Enter Your Choice"))
        if choice==1:
            name=input("ENTER NAME OF THE STUDENT  :")
            newstudent="UPDATE STUDENT SET name= %s WHERE ADMISSION_NO =%d"
            mycursor.execute(new,name,admission_no)
            mycursor.execute("COMMIT")
            print("NAME UPDATED")
            print(">------------------------------------------------------------------------<")
            main()

        elif choice == 2:
            std=input("ENTER CLASS OF THE STUDENT   :")
            newstudent="UPDATE STUDENT SET class= %s WHERE ADMISSION_NO=%d"
            mycursor.execute(newstudent,(std,admission_no))
            mycursor.execute("COMMIT")
            print("CLASS UPDATED")
            print(">------------------------------------------------------------------------<")
            main()


        elif choice==3:
            roll_no=int(input("ENTER ROLL NO OF THE STUDENT  :"))
            newstudent="UPDATE	STUDENT SET ROLL_NO=%s	WHERE ADMISSION_NO = %d"
            mycursor.execute(newstudent,(ROLL_NO,admission_no))
            mycursor.execute("COMMIT")
            print("ROLL NO UPDATED")
            print(">------------------------------------------------------------------------<")
            main()

        else:
            print("Record Not Found Try Again !")
            print(">------------------------------------------------------------------------<")
            main()
    else:
        print("\nSomthing Went Wrong ,Please Try Again !")
        print(">------------------------------------------------------------------------<")
        main()


#MODULE TO DISPLAY STUDENT'S DATA
def displayStudent():
    mycursor.execute("SELECT * FROM STUDENT")
    data=mycursor.fetchall()
    print(data)
    mycursor.close()

    
def main():
 # global variable for report
 print("school_name =DAV Public School")
 print("school_address =ANPARA COLONY SONEBHADRA U.P")
 print("school_email = davanp@gmail.com")
 print("school_phone =1234560789")
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
    choice=int(input('PLEASE  ENTER  YOUR  CHOICE:'))
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
        main()

def pswd():
    p=input("Password:")
    if p=="GROUP":
        main()
    else:
        print("Wrong Password")
        pswd()
pswd()


# global variable for report
print("school_name =DAV Public School")
print("school_address =ANPARA COLONY SONEBHADRA U.P")
print("school_email = davanp@gmail.com")
print("school_phone =1234560789")
