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
        newtable="CREATE TABLE IF NOT EXISTS STUDENT(ROLL_NO VARCHAR(5),SNAME CHAR(30),FNAME CHAR(30),MNAME CHAR(30) ,PHONE_NO VARCHAR(12), ADDRESS VARCHAR(100),SCLASS VARCHAR(5),SECTION VARCHAR(5), ADMISSION_NO  INT(10)  AUTO_INCREMENT)"
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
    print("DATA ENTERED SUCCESSFULLY")
    print(">------------------------------------------------------------------------<")
    
    main()
      
#MODULE TO DISPLAY STUDENT'S DATA
def displayStudent():
    df=pd.read_sql("SELECT * FROM STUDENT","bcd")
    
    data=mycursor.fetchall()
    print(data)
    print(">------------------------------------------------------------------------<")

    main()
    

#MODULE TO UPDATE STUDENT'S RECORD
def updateStudent():
    admission_no=input("ENTER ADMISSION NO : ")
    new="SELECT * FROM STUDENT WHERE ADMISSION_NO= %s"
    mycursor.execute(new,(admission_no,))
    data=mycursor.fetchall()
    if data:
        print("PRESS 1 FOR NAME")
        print("PRESS 2 FOR CLASS")
        print("PRESS 3 FOR ROLL NO")
        choice=int(input("Enter Your Choice"))
        if choice==1:
            name=input("ENTER NAME OF THE STUDENT  :")
            newstudent="UPDATE STUDENT SET SNAME={} WHERE ADMISSION_NO={}".format(name)
            mycursor.execute(new,(newstudent,name,))
            bcd.commit()
            print("NAME UPDATED")
            print(">------------------------------------------------------------------------<")
            main()

        elif choice == 2:
            std=input("ENTER CLASS OF THE STUDENT   :")
            newstudent="UPDATE * FROM STUDENT SET SCLASS= %s WHERE ADMISSION_NO=%s"
            mycursor.execute(newstudent,std)
            mycursor.execute("COMMIT")
            print("CLASS UPDATED")
            print(">------------------------------------------------------------------------<")
            main()


        elif choice==3:
            roll_no=int(input("ENTER ROLL NO OF THE STUDENT  :"))
            newstudent="UPDATE * FROM STUDENT SET ROLL_NO=%s	WHERE ADMISSION_NO = %s"
            mycursor.execute(newstudent,roll_no)
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



#MODULE TO DELETE STUDENT'S DATA
def delete () :
    SNAME=input("STUDENT NAME:")
    ROLL_NO=input("STUDENT ROLL NO.:")
    ADMISSION_NO=input("STUDENT ADMISSION NO.:")
    data=(SNAME,ROLL_NO,ADMISSION_NO)
    
    rst="DELETE FROM STUDENT WHERE SNAME=%s AND ROLL_NO=%s"
    gst=["DELETE FROM MARKS WHERE ADMISSION_NO=%s"]
    mycursor=bcd.cursor(buffered=True)
    mycursor.execute(rst,gst,(data,))
    
    bcd.commit()
    print("DATA ENTERED SUCCESSFULLY")
    print(">------------------------------------------------------------------------<")
    main()



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
    values=(admission_no,S1,S2,S3,S4,S5,S6, total , average)
    mycursor.execute(newstudent,values)
    mycursor.execute("COMMIT")
    
    print("\nMarks of the Student Entered Successfully !")
    print(">------------------------------------------------------------------------<")

    main()
#MODULE TO GENERATE REPORT CARD FOR ALL STUDENTS
def reportCardAllStudent () :
    mycursor.execute("SELECT * FROM MARKS")
    data=mycursor.fetchall()
    print(data)
    print(">------------------------------------------------------------------------<")
    main()

#MODULE TO GENERATE REPORT CARD OF ONE STUDENTS
def reportCardOneStudent():
    admission_no=input("ENTER ADMISSION NO OF THE STUDENT :")
  
    newstudent="SELECT * FROM MARKS WHERE ADMISSION_NO= %s"
    mycursor.execute(newstudent,(admission_no,))
    data=mycursor.fetchall()
    if data:
        print(data)
        print(">------------------------------------------------------------------------<")
        main()

    else:
        print("Record Not Found , Please Try Again !")
        print(">------------------------------------------------------------------------<")

        main()

#MODULE FOR SEARCHING STUDENT DETAILS
def searchstudentdetails():
            print("1:TO SERACH BY STUDENT ROLL NUMBER")
            print("2:TO SEARCH BY STUDENT NAME")
            c=int(input("ENTER YOUR CHOICE :"))
        #searching by student roll number
            if c==1:
             
                roll=int(input("ENTER STUDENT ROLL NUMBER TO SEARCH :"))
                qry="SELECT * FROM STUDENT WHERE ROLL_NO=%s"
                mycursor.execute(qry,(roll,))
                data=mycursor.fetchall()
                if len(data)==0: 
                    print("SORRY NO STUDENT FOUND")
                    print(">------------------------------------------------------------------------<")
                for i in data:
                    j=str(i).split()
                    for k in j:
                        print(k,end="    ")
                    print()
                    print(">------------------------------------------------------------------------<")
                    main()
               

#searching by student name
            elif c==2:
             
               name=input("ENTER STUDENT NAME TO SEARCH :")
               qry="SELECT * FROM STUDENT WHERE SNAME=%s"
               mycursor.execute(qry,(name,))
               data=mycursor.fetchall()
               if len(data)==0: 
                   print("SORRY NO STUDENT FOUND")
                   print(">------------------------------------------------------------------------<")
               for i in data:
                   j=str(i).split()
                   for k in j:
                       print(k,end="    ")
                   print()
                   print(">------------------------------------------------------------------------<")
                   main()
            else:
               print("SORRY NO STUDENT FOUND")
               print(">------------------------------------------------------------------------<")
               main()

                     
  
#MODULE FOR HELP
    
def helpMe():
    print("Please, Visit The Offcial Website Of D.A.V To Download The Mannual !!!")
    print(">------------------------------------------------------------------------<")
    main()


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
    print("|	Enter 4 -  To Delete Student's Data.		       |")
    print("|	Enter 5 -  Add Student's Marks Detail.		       |")
    print("|	Enter 6 -  TO CHANGE MARKS OF STUDENT.		       |")
    print("|	Enter 7 -  TO SEARCH A STUDENT RECORD.                 |")
    print("|	Enter 8 -  Generate All Student's Report Card.         |")
    print("|	Enter 9 -  Generate Student Wise Report Card.          |")
    print("|	Enter 10 -  Exit.	                               |")
    print("|	Enter 0 -  Help.	                               |")
    print("-----------------------*******************----------------------")
    choice=int(input('PLEASE  ENTER  YOUR  CHOICE:'))
    if choice==1:
        newStudent()
    elif choice==2:
        displayStudent()
    elif choice==3:
        updateStudent()
    elif choice==4:
        delete()
    elif choice==5:
        marksStudent()
    elif choice==6:
        markschange()
    elif choice==7:
        searchstudentdetails()
    elif choice==8:
        reportCardAllStudent()
    elif choice==9:
        reportCardOneStudent()
    elif choice==10:
        print("Thank you for visiting... come again")
        quit()
    elif choice==0:
        helpMe()
    else:
        print("Sorry ,May Be You Are Giving Me Wrong Input,Please Try Again!")
        main()

def pswd():
    p=input("PLEASE INPUT THE PASSWORD TO PROCEED :")
    if p=="GROUP":
        print("YOUR PASSWORD IS CORRECT... YOU CAN PROCEED")
        print(">------------------------------------------------------------------------<")
        main()
    else:
        print("Wrong Password Please Try Again")
        print(">------------------------------------------------------------------------<")
        pswd()
pswd()
