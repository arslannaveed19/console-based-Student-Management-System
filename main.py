import os
import csv
def file():  # This Function Creat The CSV File If The File Not Exit
    file_nam="StdData.csv"
    if not os.path.exists(file_nam):
        with open(file_nam,"a") as file:
            writer=csv.writer(file)
            writer.writerow([
                "Name",
                "Roll NO",
                "Marks",
                "Grade"
            ])

#------------------------
def add_student():
        std_nam=input("Enter Student Name =")
        std_rollNo=int(input("Enter Student Roll No ="))
        std_marks=float(input("Enter Student Marks(out of 800) ="))
        std_grade=input("Enter Student Grade =")
        with open("StdData.csv","a",newline="") as f:
             writer=csv.writer(f)
             writer.writerow([std_nam,std_rollNo,std_marks,std_grade])

#------------------------
def view_student():
    with open ("StdData.csv","r") as f:
         reader=csv.DictReader(f)
         for std in reader:
              print("Name =",std["Name"])
              print("RollNo =",std["Roll No"])
              print("Marks =",std["Marks"])
              print("Grade =",std["Grade"])
              print("----------------")

#------------------------
def ser_student():
     vie_std=input("Enter Student Roll NO =")
     with open ("StdData.csv","r") as f:
         reader=csv.DictReader(f)
         for std in reader:
              if std["Roll No"]==vie_std:
                   print("Name =",std["Name"])
                   print("RollNo =",std["Roll No"])
                   print("Marks =",std["Marks"])
                   print("Grade =",std["Grade"])
                   return
         print(" Student Not Found ")

#------------------------
def update_student():
     st_dt=input("Enter Student Roll No =")
     with open("StdData.csv","r") as f:
          reader=csv.DictReader(f)#ya har row ko distnory bana deta ha 
          students=list(reader)# jo input lia us ko list ma store kar ta
          for std in students:
               if std["Roll No"]==st_dt:
                    found=True
                    print("1.Update Marks")
                    print("2.Update Grade")
                    user_upch=input("Enter Your Choice =")
                    if user_upch=="1": 
                         up_mak=input("Enter Update Marks(out of 800) =")
                         std["Marks"]=up_mak #old marks ke gha new marks store kar raha
                    elif user_upch=="2":
                         up_grade=input("Enter Update Marks =")
                         std["Grade"]=up_grade  #old marks ke gha new marks store kar raha
                    else:
                         print("Invalid Choice!")
               
          if found:
               with open ("StdData.csv","w",newline="") as f:
                    filed_names=["Name","Roll No","Marks","Grade"]
                    writer=csv.DictWriter(f,fieldnames=filed_names)
                    writer.writeheader()# ya file ka header read/write kar ta phale
                    writer.writerows(students)
                    print("Record Updated Successfully")                          
          else:
               print("~Student Not Found~")

#------------------------
def delete_student():
     roll_std=(input("Enter Roll No To Delete Student ="))
     with open("StdData.csv","r") as f:
          reader=csv.DictReader(f)
          students=list(reader)
          found=False
          for std in students:
               if std["Roll No"]==roll_std:
                    students.remove(std)
                    found=True
          if found:
               with open("StdData.csv","w") as f:
                    columns_name=["Name","Roll No","Marks","Grade"]
                    writer=csv.DictWriter(f,fieldnames=columns_name)
                    writer.writeheader()
                    writer.writerows(students)
               print("Record Deleted Successfully")

          else:
               print("Student Not Found")

#------------------------
def avrage_marks():
     st_roll=input("Enter Student Roll No =")
     with open ("StdData.csv","r") as f:
          reader=csv.DictReader(f)
          for roll_no in reader:
               if roll_no["Roll No"] ==st_roll:
                    marks=float(roll_no["Marks"])
                    avrage=marks*100/800
                    print(avrage)
                    break
          else:
               print("Student Not Found")

#------------------------ 
def interface():
    while True:
        print("1.Add Student")
        print("2.View Student")
        print("3.Search Student")
        print("4.Update Student")
        print("5.Delete Student")
        print("6.Calculate Average Marks")
        print("7.Exit")
        user_choice=int(input("Enter Your Choice ="))       
        if user_choice ==1:
             add_student()
        elif user_choice ==2:
             view_student()
        elif user_choice ==3:
             ser_student()
        elif user_choice ==4:
             update_student()
        elif user_choice ==5:
             delete_student()
        elif user_choice ==6:
             avrage_marks()
        elif user_choice==7:
             print("Thank you for using Student Management System!")
             return
        else:
             print("Wrong Choice<try again>")
interface()