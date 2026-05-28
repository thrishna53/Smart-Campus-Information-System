# ==========================================================
# SMART CAMPUS INFORMATION SYSTEM
# Mini Project Integration (Lab 1 to Lab 8)
# ==========================================================

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================================
# MODULE 1: Student Registration and Grade Evaluation
# ==========================================================

def student_registration():
    print("\n===== STUDENT REGISTRATION =====")

    name = input("Enter student name: ")
    score = float(input("Enter exam score (0-100): "))

    if 90 <= score <= 100:
        grade = "A"
        remark = "Excellent"

    elif score >= 75:
        grade = "B"
        remark = "Very Good"

    elif score >= 60:
        grade = "C"
        remark = "Good"

    elif score >= 40:
        grade = "D"
        remark = "Average"

    else:
        grade = "F"
        remark = "Needs Improvement"

    print("\n--- Student Report ---")
    print("Name:", name)
    print("Score:", score)
    print("Grade:", grade)
    print("Remark:", remark)


# ==========================================================
# MODULE 2: Course Enrollment Management
# ==========================================================

def course_enrollment():
    print("\n===== COURSE ENROLLMENT =====")

    courses = []
    max_courses = 5

    while True:

        if len(courses) >= max_courses:
            print("Maximum course limit reached!")
            break

        course = input("Enter course name (or 'done' to finish): ")

        if course.lower() == "done":
            break

        credits = input("Enter credit value: ")

        if not credits.isdigit():
            print("Invalid credit value!")
            continue

        credits = int(credits)

        if credits <= 0:
            print("Credits must be positive!")
            continue

        courses.append((course, credits))

        print("Course added successfully.\n")

    print("\n--- Enrollment Report ---")

    for c, cr in courses:
        print("Course:", c, "| Credits:", cr)

    print("Total Courses:", len(courses))


# ==========================================================
# MODULE 3: Student Record Management
# ==========================================================

students = []

def student_record_management():

    print("\n===== STUDENT RECORD MANAGEMENT =====")

    n = int(input("Enter number of students: "))

    for i in range(n):

        name = input("Enter student name: ")
        age = int(input("Enter age: "))

        grades = []

        for j in range(3):
            mark = int(input(f"Enter mark {j+1}: "))
            grades.append(mark)

        student = {
            "name": name,
            "age": age,
            "grades": grades
        }

        students.append(student)

    print("\n--- Student Records ---")

    for s in students:
        print("Name:", s["name"])
        print("Age:", s["age"])
        print("Grades:", s["grades"])
        print("---------------------")

    # Set operations

    event_A = {"Arjun", "Rahul", "Anita"}
    event_B = {"Rahul", "Anita", "Kiran"}

    print("\n--- Event Analysis ---")

    print("Common Participants:", event_A & event_B)
    print("All Participants:", event_A | event_B)
    print("Only Event A:", event_A - event_B)


# ==========================================================
# MODULE 4: Sorting and Searching Student IDs
# ==========================================================

def sorting_searching():

    print("\n===== SORTING AND SEARCHING =====")

    student_ids = [105, 102, 110, 108, 101, 115]

    print("Original IDs:", student_ids)

    # Bubble Sort

    n = len(student_ids)

    for i in range(n):
        for j in range(0, n-i-1):

            if student_ids[j] > student_ids[j+1]:

                temp = student_ids[j]
                student_ids[j] = student_ids[j+1]
                student_ids[j+1] = temp

    print("Sorted IDs:", student_ids)

    # Linear Search

    target = int(input("Enter ID to search: "))

    found = -1

    for i in range(len(student_ids)):

        if student_ids[i] == target:
            found = i
            break

    if found != -1:
        print("Linear Search: ID found at index", found)

    else:
        print("ID not found")

    # Binary Search

    low = 0
    high = len(student_ids) - 1

    found = -1

    while low <= high:

        mid = (low + high) // 2

        if student_ids[mid] == target:
            found = mid
            break

        elif student_ids[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    if found != -1:
        print("Binary Search: ID found at index", found)

    else:
        print("ID not found")


# ==========================================================
# MODULE 5: Fee Calculation using Functions
# ==========================================================

def calculate_fee(tuition_fee, hostel_fee=0, transport_fee=0):

    total = tuition_fee + hostel_fee + transport_fee

    return total


def fee_module():

    print("\n===== FEE CALCULATION =====")

    tuition = float(input("Enter tuition fee: "))
    hostel = float(input("Enter hostel fee: "))
    transport = float(input("Enter transport fee: "))

    total = calculate_fee(tuition, hostel, transport)

    print("Total Fee =", total)


# ==========================================================
# MODULE 6: File Handling for Student Academic Records
# ==========================================================

def file_management():

    print("\n===== FILE MANAGEMENT =====")

    with open("student_records.txt", "w") as file:

        file.write("ID,Name,Marks\n")
        file.write("101,Arjun,85\n")
        file.write("102,Meera,92\n")
        file.write("103,Ravi,76\n")
        file.write("104,Anita,89\n")

    print("Records written successfully.")

    print("\nReading Records:")

    with open("student_records.txt", "r") as file:

        records = file.readlines()

        for record in records:
            print(record.strip())

    total_students = 0
    total_marks = 0

    highest = -1
    topper = ""

    for record in records[1:]:

        parts = record.strip().split(",")

        marks = int(parts[2])

        total_students += 1
        total_marks += marks

        if marks > highest:
            highest = marks
            topper = parts[1]

    average = total_marks / total_students

    print("\n--- Report ---")

    print("Total Students:", total_students)
    print("Average Marks:", average)
    print("Topper:", topper)
    print("Highest Marks:", highest)


# ==========================================================
# MODULE 7: Directory Scanning with Exception Handling
# ==========================================================

class MissingFileOrFolderError(Exception):
    pass


def scan_directory(path):

    try:

        if not os.path.exists(path):
            raise FileNotFoundError("Invalid directory path")

        print("\nScanning Directory:\n")

        for root, dirs, files in os.walk(path):

            level = root.replace(path, "").count(os.sep)

            indent = " " * 4 * level

            print(f"{indent}{os.path.basename(root)}/")

            sub_indent = " " * 4 * (level + 1)

            for f in files:
                print(f"{sub_indent}{f}")

            if not files and not dirs:
                raise MissingFileOrFolderError(
                    f"Empty folder detected: {root}"
                )

    except FileNotFoundError as e:
        print("Error:", e)

    except MissingFileOrFolderError as e:
        print("Custom Error:", e)

    except Exception as e:
        print("Unexpected Error:", e)


def directory_module():

    print("\n===== DIRECTORY SCANNER =====")

    path = input("Enter directory path: ")

    scan_directory(path)


# ==========================================================
# MODULE 8: Student Performance Analytics
# ==========================================================

def performance_analytics():

    print("\n===== PERFORMANCE ANALYTICS =====")

    data = {
        "Name": ["Arjun", "Meera", "Ravi", "Anita"],
        "Math": [85, 92, 76, 89],
        "Science": [88, 95, 70, 91],
        "English": [90, 87, 72, 94]
    }

    df = pd.DataFrame(data)

    print("\n--- Raw Data ---")
    print(df)

    print("\n--- Statistical Summary ---")
    print(df.describe())

    scores = df[["Math", "Science", "English"]].to_numpy()

    mean_scores = np.mean(scores, axis=0)
    median_scores = np.median(scores, axis=0)
    std_scores = np.std(scores, axis=0)

    print("\n--- NumPy Analysis ---")

    print("Mean Scores:", mean_scores)
    print("Median Scores:", median_scores)
    print("Standard Deviation:", std_scores)

    print("\n--- Top Performers ---")

    top_math = df.loc[df["Math"].idxmax(), "Name"]
    top_science = df.loc[df["Science"].idxmax(), "Name"]
    top_english = df.loc[df["English"].idxmax(), "Name"]

    print("Math Topper:", top_math)
    print("Science Topper:", top_science)
    print("English Topper:", top_english)

    # Visualization

    subjects = ["Math", "Science", "English"]

    plt.bar(subjects, mean_scores)

    plt.title("Average Scores per Subject")

    plt.xlabel("Subjects")
    plt.ylabel("Average Score")

    plt.show()

    df.plot(x="Name",
            y=["Math", "Science", "English"],
            kind="bar")

    plt.title("Student Performance Comparison")

    plt.ylabel("Scores")

    plt.show()


# ==========================================================
# MAIN MENU SYSTEM
# ==========================================================

def main():

    while True:

        print("\n====================================")
        print(" SMART CAMPUS INFORMATION SYSTEM ")
        print("====================================")

        print("1. Student Registration")
        print("2. Course Enrollment")
        print("3. Student Record Management")
        print("4. Sorting and Searching")
        print("5. Fee Calculation")
        print("6. File Management")
        print("7. Directory Scanner")
        print("8. Performance Analytics")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_registration()

        elif choice == "2":
            course_enrollment()

        elif choice == "3":
            student_record_management()

        elif choice == "4":
            sorting_searching()

        elif choice == "5":
            fee_module()

        elif choice == "6":
            file_management()

        elif choice == "7":
            directory_module()

        elif choice == "8":
            performance_analytics()

        elif choice == "9":
            print("Exiting System...")
            break

        else:
            print("Invalid choice! Try again.")


# ==========================================================
# PROGRAM EXECUTION
# ==========================================================

if __name__ == "__main__":
    main()
