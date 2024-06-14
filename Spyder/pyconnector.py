import os
import platform
import mysql.connector as m
bcd=m.connect(host="localhost",user="root",password="abcd1234",database="newstudent",charset="utf8")

if bcd.is_connected():
    print("succesfully connected")
else:
    print("Not connected")
mycursor=bcd.cursor()

#MODULE FOR NEW ADMISSION

def  newStudent():
    try:
        print(" Creating STUDENT table")
        newtable="CREATE TABLE IF NOT EXISTS STUDENT(ROLL_NO int(5),SNAME VARCHAR(30),FNAME VARCHAR(30),MNAME VARCHAR(30) ,PHONE_NO VARCHAR(12), ADDRESS VARCHAR(100),CLASS VARCHAR(5),SECTION VARCHAR(5), ADMISSION_NO  VARCHAR(10) PRIMARY KEY)"
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
      
#MODULE TO DISPLAY STUDENT'S DATA
def displayStudent():
    mycursor.execute("SELECT * FROM STUDENT")
    data=mycursor.fetchall()
    print(data)
    mycursor.close()


#MODULE TO UPDATE STUDENT'S RECORD
def updateStudent():
    admission_no=input("ENTER ADMISSION NO :")
    newstudent="SELECT * FROM STUDENT WHERE admission_no= %s"
    mycursor.execute(newstudent,(admission_no,))
    data=mycursor.fetchall()
    if data:
        print("PRESS 1 FOR NAME")
        print("PRESS 2 FOR CLASS")
        print("PRESS 3 FOR ROLL NO")
        choice=int(input("Enter Your Choice"))
        if choice==1:
            name=input("ENTER NAME OF THE STUDENT  :")
            newstudent="UPDATE STUDENT SET name= %s WHERE admission_no =%s"
            mycursor.execute(newstudent,(name,admission_no))
            mycursor.execute("COMMIT")
            print("NAME UPDATED")
        elif choice == 2:
            std=input("ENTER CLASS OF THE STUDENT   :")
            newstudent="UPDATE STUDENT SET class= %s WHERE admission_no=%s"
            mycursor.execute(newstudent,(std,admission_no))
            mycursor.execute("COMMIT")
            print("CLASS UPDATED")
        elif choice==3:
            roll_no=int(input("ENTER ROLL NO OF THE STUDENT  :"))
            newstudent="UPDATE	STUDENT SET roll_no=%s	WHERE admission_no = %s"
            mycursor.execute(newstudent,(roll_no,admission_no))
            mycursor.execute("COMMIT")
            print("ROLL NO UPDATED")
        else:
            print("Record Not Found Try Again !")
            mycursor.close()
    else:
        print("\nSomthing Went Wrong ,Please Try Again !")


#MODULE TO ENTER MARKS OF THE STUDENT
def marksStudent () :
    createTable ="""CREATE TABLE IF NOT EXISTS MARKS(ADMISSION_NO VARCHAR(10) PRIMARY KEY,S1 INT,S2 INT ,S3 INT ,S4 INT,S5 INT,S6 INT,TOTAL INT ,AVERAGE DECIMAL)"""
    mycursor.execute(createTable)
    admission_no=input("ENTER ADMISSION NO OF THE STUDENT :")
    S1=int(input("\n ENTER MARKS OF SUBJECT 1 : "))
    S2=int(input("\n ENTER MARKS OF SUBJECT 2 : "))
    S3=int(input("\n ENTER MARKS OF SUBJECT 3 : "))
    S4=int(input("\n ENTER MARKS OF SUBJECT 4 : "))
    S5=int(input("\n ENTER MARKS OF SUBJECT 5 : "))
    S6=int(input("\n ENTER MARKS OF SUBJECT 6 : "))
    total = S1 + S2 + S3 + S4 + S5 + S6
    average = total/6
    newstudent="INSERT INTO MARKS(ADMISSION_NO,S1,S2,S3,S4,S5,S6, TOTAL,AVERAGE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values=(admission_no,s1,s2,s3,s4,s5,s6, total , average)
    mycursor.execute(newstudent,values)
    mycursor.execute("COMMIT")
    mycursor.close()
    print("\nMarks of the Student Entered Successfully !")

def reportCardAllStudent () :
    mycursor.execute("SELECT * FROM MARKS")
    data=mycursor.fetchall()
    print(data)
    mycursor.close()

#MODULE TO GENERATE REPORT CARD OF ONE STUDENTS
def reportCardOneStudent():
    admission_no=input("ENTER ADMISSION NO OF THE STUDENT :")
  
    newstudent="SELECT * FROM MARKS WHERE ADMISSION_NO= %s"
    mycursor.execute(newstudent,(admission_no,))
    data=mycursor.fetchall()
    if data:
        print(data)
    else:
        print("Record Not Found , Please Try Again !")
        mycursor.close()

#MODULE FOR SEARCHING STUDENT DETAILS
def searchstudentdetails():
            print("1:TO SERACH BY STUDENT ROLL NUMBER")
            print("2:TO SEARCH BY STUDENT NAME")
            c=int(input("ENTER YOUR CHOICE"))
        #searching by student roll number
            if c==1:
             try:
                roll=int(input("ENTER STUDENT ROLL NUMBER TO SEARCH"))
                qry="SELECT * FROM STUDENT where roll=%d"%roll
                cursor.execute(qry)
                data=cursor.fetchall()
                if len(data)==0:
                    print("STUDENT NOT FOUND")
                print("ROLL NO","STUDENT NAME","CLASS","SECTION","SUBJECT1","SUBJECT2","SUBJECT3","SUBJECT4","SUBJECT5","SUBJECT6","TOTALMARKS","PERCENTAGE")
                for i in data:
                    j=str(i).split()
                    for k in j:
                        print(k,end="    ")
                    print()
             except:
                print("SORRY SOME ERROR OCCURED")

        #searching by student name
            if c==2:
             try:
                 name=input("ENTER STUDENT NAME TO SEARCH")
                 qry="SELECT * FROM STUDENT where name='%s'"%name
                 cursor.execute(qry)
                 data=cursor.fetchall()
                 if len(data)==0:
                    print("STUDENT NOT FOUND")
                    print("ROLL NO","STUDENT NAME","CLASS","SECTION","SUBJECT1","SUBJECT2","SUBJECT3","SUBJECT4","SUBJECT5","SUBJECT6","TOTALMARKS","PERCENTAGE")
                 for i in data:
                    j=str(i).split()
                    for k in j:
                        print(k,end="    ")
                    print()
             except:
                    print("SORRY SOME ERROR OCCURED")
                     
  
#MODULE FOR HELP
    
def helpMe():
    print("Please, Visit The Offcial Website Of D.A.V To Download The Mannual !!!")

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

