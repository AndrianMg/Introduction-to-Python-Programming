import random
from unittest.mock import patch
import time

# Original code with modifications for visual demo
USERS = {"teacher": "pass123", "student": "stud456"}
GRADES = {"Ali": "B", "Sara": "A", "Omar": "C"}

def check_availability():
    status = random.choice(["available", "maintenance"])
    if status == "available":
        print(" System Status: Available\n")
        return True
    else:
        print(" System Status: Under Maintenance. Try again later.")
        return False

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
    if not check_availability():
        return
    user = login()
    if not user:
        return
    show_grades()
    if user == "teacher":
        if input("\nUpdate a grade? (yes/no): ").lower() == "yes":
            update_grade()
            show_grades()
    print("\n Program ended safely and reliably.")

def visual_demo(scenario_name, inputs, force_available=None):
    print("=" * 80)
    print(f"DEMO SCENARIO: {scenario_name}")
    print("=" * 80)
    
    # Reset grades for each test
    global GRADES
    GRADES = {"Ali": "B", "Sara": "A", "Omar": "C"}
    
    # Show the inputs that will be used
    if inputs:
        print("Simulated User Inputs:")
        for i, inp in enumerate(inputs, 1):
            print(f"  Input {i}: {inp}")
        print("-" * 40)
    
    try:
        with patch('builtins.input', side_effect=inputs):
            if force_available is not None:
                with patch('random.choice', return_value="available" if force_available else "maintenance"):
                    main()
            else:
                main()
    except Exception as e:
        print(f"Error occurred: {e}")
    
    print("\n" + "=" * 80)
    print("END OF SCENARIO")
    print("=" * 80)
    print("\n" * 2)

if __name__ == "__main__":
    print("GRADE SYSTEM VISUAL DEMONSTRATION")
    print("=" * 80)
    print("This demo shows various test scenarios with clear visual output")
    print("=" * 80)
    print("\n")
    
    # Demo 1: System Under Maintenance
    visual_demo("1. SYSTEM UNDER MAINTENANCE", [], force_available=False)
    
    # Demo 2: Valid Student Login
    visual_demo("2. VALID STUDENT LOGIN", ["student", "stud456"], force_available=True)
    
    # Demo 3: Valid Teacher Login - View Only
    visual_demo("3. VALID TEACHER LOGIN (VIEW ONLY)", ["teacher", "pass123", "no"], force_available=True)
    
    # Demo 4: Teacher Updates Valid Grade
    visual_demo("4. TEACHER UPDATES VALID GRADE", ["teacher", "pass123", "yes", "Ali", "A"], force_available=True)
    
    # Demo 5: Teacher Tries Invalid Grade
    visual_demo("5. TEACHER TRIES INVALID GRADE", ["teacher", "pass123", "yes", "Sara", "X"], force_available=True)
    
    # Demo 6: Teacher Tries Invalid Student
    visual_demo("6. TEACHER TRIES INVALID STUDENT", ["teacher", "pass123", "yes", "John", "A"], force_available=True)
    
    # Demo 7: Invalid Login Credentials
    visual_demo("7. INVALID LOGIN CREDENTIALS", ["hacker", "wrongpass"], force_available=True)
    
    # Demo 8: Wrong Password for Valid User
    visual_demo("8. WRONG PASSWORD FOR VALID USER", ["teacher", "wrongpass"], force_available=True)
    
    print("DEMONSTRATION COMPLETE")
    print("=" * 80)