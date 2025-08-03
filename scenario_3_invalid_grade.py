#!/usr/bin/env python3
"""
SCENARIO 3: RELIABILITY TEST - INVALID GRADE
=============================================
This demonstrates what happens when a teacher enters an invalid grade.
"""

import random
from unittest.mock import patch

USERS = {"teacher": "pass123", "student": "stud456"}
GRADES = {"Ali": "B", "Sara": "A", "Omar": "C"}

def check_availability():
    return True  # Force available for this demo

def login():
    print(" Login to Grade System")
    user = input("Username: ").strip()
    pwd = input("Password: ").strip()
    if USERS.get(user) == pwd:
        print(" Login Successful!\n")
        return user
    else:
        print(" Login Failed.\n")
        return None

def show_grades():
    print(" Current Grades:")
    for student, grade in GRADES.items():
        print(f" - {student}: {grade}")

def update_grade():
    name = input("Enter student name to update: ").strip()
    if name not in GRADES:
        print(" Student not found!")
        return
    new = input("Enter new grade (A-F): ").upper().strip()
    if new not in ["A","B","C","D","F"]:
        print(" Invalid grade.")
        return
    GRADES[name] = new
    print(" Grade updated successfully.")

def main():
    print("Dependable Grade System\n")
    print(" System Status: Available\n")
    
    user = login()
    if not user:
        return
    
    print("BEFORE UPDATE:")
    show_grades()
    
    if user == "teacher":
        if input("\nUpdate a grade? (yes/no): ").lower() == "yes":
            update_grade()
            print("\nAFTER UPDATE ATTEMPT:")
            show_grades()
    
    print("\n Program ended safely and reliably.")

if __name__ == "__main__":
    print("🔍 TESTING: RELIABILITY - INVALID GRADE INPUT")
    print("=" * 55)
    print("Teacher attempts to enter invalid grade 'X' for Sara")
    print("Login: teacher / pass123 → Update: Sara → Grade: X")
    print("-" * 55)
    
    # Simulate teacher trying invalid grade
    with patch('builtins.input', side_effect=["teacher", "pass123", "yes", "Sara", "X"]):
        main()
    
    print("\n" + "=" * 55)
    print("RESULT: System rejected invalid grade, data unchanged")
    print("=" * 55)