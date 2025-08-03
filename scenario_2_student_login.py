#!/usr/bin/env python3
"""
SCENARIO 2: VALID STUDENT LOGIN
===============================
This demonstrates student access - they can view grades but cannot modify them.
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

def main():
    print("Dependable Grade System\n")
    print(" System Status: Available\n")
    
    user = login()
    if not user:
        return
    
    show_grades()
    
    if user == "teacher":
        if input("\nUpdate a grade? (yes/no): ").lower() == "yes":
            print("Teacher functionality would be available here")
    
    print("\n Program ended safely and reliably.")

if __name__ == "__main__":
    print("👤 TESTING: STUDENT ACCESS CONTROL")
    print("=" * 50)
    print("Login credentials: student / stud456")
    print("-" * 50)
    
    # Simulate student login
    with patch('builtins.input', side_effect=["student", "stud456"]):
        main()
    
    print("\n" + "=" * 50)
    print("RESULT: Student can view grades but has NO update options")
    print("=" * 50)