#!/usr/bin/env python3
"""
SCENARIO 4: RESILIENCE TEST - LOGIN FAILURE
===========================================
This demonstrates how the system behaves after failed login attempts.
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
        print("⚠️  ACCESS DENIED - Program terminating cleanly")
        return
    
    show_grades()
    print("\n Program ended safely and reliably.")

if __name__ == "__main__":
    print("🛡️  TESTING: RESILIENCE - LOGIN FAILURE HANDLING")
    print("=" * 60)
    
    print("\nTEST 1: Invalid username")
    print("-" * 30)
    print("Attempting login with: hacker / wrongpass")
    with patch('builtins.input', side_effect=["hacker", "wrongpass"]):
        main()
    
    print("\n" + "=" * 60)
    
    print("\nTEST 2: Valid user, wrong password")
    print("-" * 35)
    print("Attempting login with: teacher / wrongpass")
    with patch('builtins.input', side_effect=["teacher", "wrongpass"]):
        main()
    
    print("\n" + "=" * 60)
    print("RESULT: System handles failures gracefully, no crashes")
    print("Note: Users must restart program to retry login")
    print("=" * 60)