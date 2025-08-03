#!/usr/bin/env python3
"""
SCENARIO 5: SUCCESSFUL GRADE UPDATE
===================================
This demonstrates a teacher successfully updating a student's grade.
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
    
    old_grade = GRADES[name]
    GRADES[name] = new
    print(f" Grade updated successfully.")
    print(f" ✓ {name}: {old_grade} → {new}")

def main():
    print("Dependable Grade System\n")
    print(" System Status: Available\n")
    
    user = login()
    if not user:
        return
    
    print("📊 INITIAL GRADES:")
    show_grades()
    
    if user == "teacher":
        if input("\nUpdate a grade? (yes/no): ").lower() == "yes":
            print("\n🔄 UPDATING GRADE...")
            update_grade()
            print("\n📊 UPDATED GRADES:")
            show_grades()
    
    print("\n Program ended safely and reliably.")

if __name__ == "__main__":
    print("✅ TESTING: SUCCESSFUL GRADE UPDATE")
    print("=" * 50)
    print("Teacher successfully updates Ali's grade B → A")
    print("Login: teacher / pass123 → Update: Ali → Grade: A")
    print("-" * 50)
    
    # Simulate successful grade update
    with patch('builtins.input', side_effect=["teacher", "pass123", "yes", "Ali", "A"]):
        main()
    
    print("\n" + "=" * 50)
    print("RESULT: Grade successfully updated and displayed")
    print("=" * 50)