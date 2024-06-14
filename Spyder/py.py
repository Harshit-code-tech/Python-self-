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



#MODULE TO DISPLAY STUDENT'S DATA
def displayStudent():
    mycursor.execute("SELECT * FROM STUDENT")
    data=mycursor.fetchall()
    print(data)
    mycursor.close()





#MODULE FOR SEARCHING STUDENT DETAILS
def searchstudentdetails():
            print("1:TO SERACH BY STUDENT ROLL NUMBER")
            print("2:TO SEARCH BY STUDENT NAME")
            c=int(input("ENTER YOUR CHOICE :"))
        #searching by student roll number
            if c==1:
             
                ROLL_NO=int(input("ENTER STUDENT ROLL NUMBER TO SEARCH :"))
                qry="SELECT * FROM STUDENT WHERE ROLL_NO= %s"
                mycursor.execute(qry,(ROLL_NO,))
                data=mycursor.fetchall()
                if len(data)==0:
                    print("STUDENT NOT FOUND")
                    print("ROLL NO","STUDENT NAME","CLASS","SECTION","SUBJECT1","SUBJECT2","SUBJECT3","SUBJECT4","SUBJECT5","SUBJECT6","TOTALMARKS","PERCENTAGE")
                for i in data:
                    j=str(i).split()
                    for k in j:
                        print(k,end="    ")
                    print()
            else:
                print("SORRY SOME ERROR OCCURED")

        #searching by student name
            if c==2:
             
                 name=input("ENTER STUDENT NAME TO SEARCH :")
                 qry="SELECT * FROM STUDENT WHERE SNAME=%s"
                 mycursor.execute(qry,(name,))
                 data=mycursor.fetchall()
                 if len(data)==0:
                    print("STUDENT NOT FOUND")
                    print("ROLL NO","STUDENT NAME","CLASS","SECTION","SUBJECT1","SUBJECT2","SUBJECT3","SUBJECT4","SUBJECT5","SUBJECT6","TOTALMARKS","PERCENTAGE")
                 for i in data:
                    j=str(i).split()
                    for k in j:
                        print(k,end="    ")
                    print()
            else:
                    print("SORRY SOME ERROR OCCURED")
                     
  
def main():
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
        searchstudentdetails()    
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
PRINT("school_name =DAV Public School")
school_address ='ANPARA COLONY SONEBHADRA U.P'
school_email = 'davanp@gmail.com'
school_phone ='1234560789'
