import os
import platform
import mysql.connector as m
from tabulate import tabulate
bcd=m.connect(host="localhost",user="root",password="abcd1234",database="newstudent",charset="utf8")

if bcd.is_connected():
    print("SUCCESFULLY CONNECTED")
    print(">------------------------------------------------------------------------<")
    print('\n')
else:
    print("NOT CONNECTED")
    print(">------------------------------------------------------------------------<")
    print('\n')
mycursor=bcd.cursor(buffered=True)

#MENU FOR STUDENT MARKS MANAGEMENT SYSTEM SOFTWARE
print("*************************************************")
print("WELCOME TO STUDENT MARKS MANAGEMENT SYSTEM")
print("*************************************************")
print('\n')



#MODULE FOR NEW ADMISSION

def  newStudent():
    print('New student - Screen')   
    print('-'*120)
    print('\n')
    try:
        print(" CREATING STUDENT TABLE")
        newtable="CREATE TABLE IF NOT EXISTS STUDENT(ROLL_NO VARCHAR(5),SNAME CHAR(30),FNAME CHAR(30),MNAME CHAR(30) ,PHONE_NO VARCHAR(12), ADDRESS VARCHAR(100),SCLASS VARCHAR(5),SECTION VARCHAR(5),ADMISSION_NO  INT(10)  FOREIGN KEY)"
    except:
        print("sorry some error occured")
        
   
    mycursor.execute("SELECT * FROM STUDENT")    
    ROLL_NO=input("\n ENTER ROLL_NO : ")
    SNAME=input("\n ENTER STUDENT'S NAME : ")
    FNAME=input("\n ENTER FATHER'S NAME : ")
    MNAME=input("\n ENTER MOTHER'S NAME : ")
    PHONE=input("\n ENTER CONTACT NO. : ")
    ADDRESS=input("\n ENTER ADDRESS : ")
    SCLASS =input("\n ENTER CLASS : ")
    SECTION=input("\n ENTER SECTION : ")
    ADMISSION_NO=input("\n ENTER ADMISSION_NO : ")
    data=(ROLL_NO,SNAME,FNAME,MNAME,PHONE,ADDRESS ,SCLASS,SECTION,ADMISSION_NO)  
    new="INSERT INTO STUDENT VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    
    mycursor.execute(new,data)
    bcd.commit()
    print("DATA ENTERED SUCCESSFULLY")
    print(">------------------------------------------------------------------------<")
    print('\n')
    main()
      
#MODULE TO DISPLAY STUDENT'S DATA
def displayStudent():
    print('Show all students - Screen')
    print('-'*120)
    print('\n')
    SHOW='SELECT * FROM STUDENT ORDER BY CLASS DESC'
    mycursor.execute(SHOW)
    data=mycursor.fetchall()
    print(tabulate(data,headers=('ROLL_NO','SNAME','FNAME','MNAME','PHONE','ADDRESS' ,'SCLASS','SECTION','ADMISSION_NO'),tablefmt='psql',showindex='always'))
    print(">------------------------------------------------------------------------<")

    main()
    



#MODULE TO DELETE STUDENT'S DATA
def delete () :
    print('delete student data - Screen')
    print('-'*120)
    print('\n')
    DEL = input('Enter admission No :')
    delete='DELETE STUDENT,MARKS FROM STUDENT INNER JOIN MARKS ON MARKS.ADMISSION_NO = STUDENT.ADMISSION_NO WHERE STUDENT.ADMISSION_NO ='+DEL+';'
    mycursor=bcd.cursor(buffered=True)
    mycursor.execute(delete)
    
    bcd.commit()
    print("DATA DELETED SUCCESSFULLY")
    print(">------------------------------------------------------------------------<")
    print('\n')
    main()




#MODULE TO ENTER MARKS OF THE STUDENT
def marksStudent () :
    print('Marks creation - Screen')
    print('-'*120)
    print('\n')
    createTable ="""CREATE TABLE IF NOT EXISTS MARKS(ADMISSION_NO VARCHAR(10) PRIMARY KEY,S1 INT,S2 INT ,S3 INT ,S4 INT,S5 INT,S6 INT,TOTAL INT ,AVERAGE DECIMAL)"""
    mycursor.execute(createTable)
    admission_no=input("\n ENTER ADMISSION NO OF THE STUDENT :")
    
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
    
    
    print("\n Marks of the Student Entered Successfully !")
    print(">------------------------------------------------------------------------<")
    print('\n')

    main()


    
#MODULE TO GENERATE REPORT CARD FOR ALL STUDENTS
def reportCardAllStudent () :
    print('Report card of all students - Screen')
    print('-'*120)
    mycursor.execute("SELECT * FROM MARKS ORDER BY ADMISSION_NO ASC ")
    data=mycursor.fetchall()
    print(tabulate(data,headers=('admission_no','S1','S2','S3','S4','S5','S6','total','average'),tablefmt='psql',showindex='always'))
    print(">------------------------------------------------------------------------<")
    main()

#MODULE TO GENERATE REPORT CARD OF ONE STUDENTS
def reportCardOneStudent():
    print('Report card of one student - Screen')
    print('-'*120)
    admission_no=input("ENTER ADMISSION NO OF THE STUDENT :")
  
    newmarks="SELECT * FROM MARKS WHERE ADMISSION_NO= %s"
    mycursor.execute(newmarks,(admission_no,))
    data=mycursor.fetchall()
    if data:
        print(tabulate(data,headers=('admission_no','S1','S2','S3','S4','S5','S6','total','average'),tablefmt='psql',showindex='always'))
    
        print(">------------------------------------------------------------------------<")
        print('\n')
        main()
        

    else:
        print("Record Not Found , Please Try Again !")
        print(">------------------------------------------------------------------------<")
        print('\n')

        main()

#MODULE TO UPDATE STUDENT'S RECORD
def updateStudent():
      print('Modify Student Information - Screen')
      admission_no=input("ENTER ADMISSION NO : ")
      new="SELECT * FROM STUDENT WHERE ADMISSION_NO= %s"
      mycursor.execute(new,(admission_no,))
      data=mycursor.fetchall()
      if data:    
          print('\n. ENTER 1 FOR SNAME  ')
          print('\n. ENTER 2 FOR ROLL_NO  ')
          print('\n. ENTER 3 FOR SCLASS  ')
          print('\n. ENTER 4 FOR SECTION  ')
          print('\n')
          choice = int(input('Enter your choice :'))
          field=''
          if choice ==1:
              field ='SNAME' 
          elif choice == 2:
              field = 'ROLL_NO'
          elif choice == 3:
              field = 'CLASS'
          elif choice == 4:
              field = 'SECTION'
          else:
             print("Record Not Found Try Again !")
             print(">------------------------------------------------------------------------<")
             main()
          
          SELECT =input('ENTER THE CHANGE :')   
          up ='update STUDENT set '+field+' ="'+SELECT +'" where ADMISSION_NO='+admission_no+';'
          mycursor.execute(up)
          print('\n\n\n Student Record Updated.....')
          print(">------------------------------------------------------------------------<")
          main()
         
      else: 
         print("\nSomthing Went Wrong ,Please Try Again !")
         print(">------------------------------------------------------------------------<")
         main()
      
      
      


      

#MODULE FOR SEARCHING STUDENT DETAILS
def searchstudentdetails():
            print(' S E A R C H    M E N U')
            print('-'*120)
            print("\n1:TO SERACH BY STUDENT ROLL NUMBER")
            print("\n2:TO SEARCH BY STUDENT NAME")
            print('\n')
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
                else:
                    print(tabulate(data,headers=('ROLL_NO','SNAME','FNAME','MNAME','PHONE','ADDRESS' ,'SCLASS','SECTION','ADMISSION_NO'),tablefmt='psql',showindex='always'))
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
               else:
                    print(tabulate(data,headers=('ROLL_NO','SNAME','FNAME','MNAME','PHONE','ADDRESS' ,'SCLASS','SECTION','ADMISSION_NO'),tablefmt='psql',showindex='always'))
                    print(">------------------------------------------------------------------------<")
                    main()
            else:
               print("SORRY NO STUDENT FOUND")
               print(">------------------------------------------------------------------------<")
               main()

                     
#MODULE TO MODIFY MARKS
def modify_marks():
    print('Modify Marks - Screen')
    print('-'*120)
    admno = input('Enter admission No :')
    
    print('\n1.   S1  ')
    print('\n2.   S2  ')
    print('\n3.   S3  ')
    print('\n4.   S4  ')
    print('\n5.   S5  ')
    print('\n6.   S6  ')
    print('\n\n')
    choice = int(input('Enter Subject No. :'))
    field = ''
    if choice == 1:
       field = 'S1'
    if choice == 2:
       field = 'S2'
    if choice == 3:
       field = 'S3'
    if choice == 4:
       field = 'S4'
    if choice == 5:
       field = 'S5'
    if choice == 5:
       field = 'S6'

    value = input('Enter New Marks :')
    mar = 'update MARKS set '+field+' ='+value + ' where ADMISSION_NO ='+admno+';'
    mycursor.execute(mar)
    
    print('\n\n\n Marks Updated.....')
    main()

 
#MODULE FOR HELP
    
def helpMe():
    print("Please, Visit The Offcial Website Of D.A.V To Download The Mannual !!!")
    print(">------------------------------------------------------------------------<")
    main()


def main():
# global variable for report
 print("\n school_name =DAV Public School")
 print("\n school_address =ANPARA COLONY SONEBHADRA U.P")
 print("\n school_email = davanp@gmail.com")
 print("\n school_phone =1234560789")
 print('MAIN MENU - Screen')
 print('-'*120)
 print("-----------------------*******************----------------------")
 while(1):
    print("|\n	Enter 1 -  Add Student		                       |")
    print("|\n	Enter 2 -  Display Student's Data.		       |")
    print("|\n	Enter 3 -  Update Students's Data .		       |")
    print("|\n	Enter 4 -  To Delete Student's Data.		       |")
    print("|\n	Enter 5 -  Add Student's Marks Detail.		       |")
    print("|\n	Enter 6 -  TO MODIFY MARKS OF STUDENT.		       |")
    print("|\n	Enter 7 -  TO SEARCH A STUDENT RECORD.                 |")
    print("|\n	Enter 8 -  Generate All Student's Report Card.         |")
    print("|\n	Enter 9 -  Generate Student Wise Report Card.          |")
    print("|\n        Enter 10 -  Exit.	                               |")
    print("|\n        Enter 0 -  Help.	                               |")
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
        modify_marks()
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
        print('-'*120)
        main()

def pswd():
    p=input("PLEASE INPUT THE PASSWORD TO PROCEED :")
    if p=="GROUP":
        print("YOUR PASSWORD IS CORRECT... YOU CAN PROCEED")
        print(">------------------------------------------------------------------------<")
        print('\n')
        main()
    else:
        print("Wrong Password Please Try Again")
        print(">------------------------------------------------------------------------<")
        print('\n')
        pswd()
pswd()
