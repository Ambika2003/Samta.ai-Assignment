#  Task 1: Calculate Area with Conditions
# Write a Python function calculate_area that takes two parameters: length and width. It
# should calculate and return the area of a rectangle. However, add a condition: if the length
# is equal to the width, return "This is a square!" instead of the area. Then, write a program to
# input values for length and width from the user and call the calculate_area function to
# display either the area or the message.

def calculate_area(length,width):
    if length==width:
        return "This is a square!"
    else:
        rectangle_area=length*width
        return ("The area of rectangle is: ",rectangle_area)
print("Enter the length and width of rectangle")
rec_len=int(input("enter length: "))
rec_wid=int(input("enter width: "))
result=calculate_area(rec_len,rec_wid)
print(result)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

# Task 3: MySQL Database Operations with Python ( Compulsory )
# Problem Statement:
# Your task is to write a Python program that accomplishes the following:
# First create a database , table and add these column ‘student_id’, ‘first_name’, ‘last_name’,
# ‘age’, ‘grade’.
# Connects to your MySQL database with python.
# Inserts a new student record into the "students" table with the following details:
# First Name: "Alice"
# Last Name: "Smith"
# Age: 18
# Grade: 95.5
# Updates the grade of the student with the first name "Alice" to 97.0.
# Deletes the student with the last name "Smith."
# Fetches and displays all student records from the "students" table.

import mysql.connector
connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor=connection.cursor()
cursor.execute("create database school")
cursor.execute("use school")
cursor.execute("""
          create table students(
               student_id int auto_increment primary key,
               first_name varchar(50),
               last_name varchar(50),
               age int,
               grade float )
""")
cursor.execute("""
       insert into students(first_name, last_name, age, grade)
               values('Ambika','Maurya','24',98)
""")
connection.commit()
cursor.execute("""
            update students
               set grade=99.0
               where first_name='Ambika'
""")
connection.commit()
cursor.execute("""
           delete from students
               where last_name='Devi'   
""")
connection.commit()

cursor.execute("""
      select * from students
""")
results=cursor.fetchall()
for i in results:
    print(i)
cursor.close()
connection.close()

# Task 2: Generate Fibonacci Series
# Problem Statement:
# Write a Python program that generates the Fibonacci sequence up to a specified number of
# terms, n. The Fibonacci sequence starts with 0 and 1, and each subsequent number in the
# sequence is the sum of the two preceding numbers (e.g., 0, 1, 1, 2, 3, 5, 8, ...). Prompt the
# user to enter the number of terms (n) they want in the sequence and then display the
# Fibonacci sequence up to that number of terms.

def Fibonacci_sequence(n):
    first=0
    second=1
    for i in range(0,n):
        print(first)
        n=first+second
        first=second
        second=n
Fibonacci_sequence(int(input("enter number to get Fibonacci sequence: ")))
