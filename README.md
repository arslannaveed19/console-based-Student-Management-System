# Student Management System 

A beginner-friendly **Python Student Management System** that stores student records in a CSV file and provides basic CRUD operations.

## Features

* Add Student
* View All Students
* Search Student by Roll No
* Update Student Marks or Grade
* Delete Student
* Calculate Student Percentage
* Store data permanently in a CSV file
* Automatic CSV file creation if the file does not exist

## Technologies Used

* Python
* CSV Module
* OS Module
* Functions
* Loops
* Dictionaries
* Lists
* File Handling
* Conditional Statements

## Project Structure

```text
Student-Management-System/
│
├── main.py
├── StdData.csv
└── README.md
```

## Menu

```text
1. Add Student
2. View Student
3. Search Student
4. Update Student
5. Delete Student
6. Calculate Average Marks
7. Exit
```

## How It Works

### 1. Add Student

The program takes:

* Student Name
* Roll Number
* Marks out of 800
* Grade

and stores the record in `StdData.csv`.

### 2. View Student

Displays all students stored in the CSV file.

### 3. Search Student

Searches for a student using their Roll Number.

### 4. Update Student

Allows the user to update:

* Student Marks
* Student Grade

### 5. Delete Student

Deletes a student's complete record using their Roll Number.

### 6. Calculate Percentage

The program calculates the student's percentage using:

```python
percentage = marks * 100 / 800
```

## Example CSV Data

```text
Name,Roll No,Marks,Grade
Arslan,101,650,A
Ali,102,580,B
Ahmed,103,490,C
```

## How to Run

Make sure Python is installed, then run:

```bash
python main.py
```

The program will automatically create `StdData.csv` if it does not already exist.

## Learning Purpose

This project was created to practice Python fundamentals, especially:

* File Handling
* CSV Files
* Functions
* CRUD Operations
* Lists and Dictionaries
* Loops
* Conditional Statements

## Future Improvements

* Add input validation
* Automatically calculate grades
* Add student attendance
* Add login system
* Use SQLite/MySQL database
* Build a web version using FastAPI
