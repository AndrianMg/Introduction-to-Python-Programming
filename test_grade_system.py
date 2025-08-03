import random
from unittest.mock import patch
import io
import sys

# Original code with slight modifications for testing
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

# Test scenarios
def test_scenario(scenario_name, inputs, force_available=None):
    print(f"\n{'='*60}")
    print(f"TEST SCENARIO: {scenario_name}")
    print('='*60)
    
    # Reset grades for each test
    global GRADES
    GRADES = {"Ali": "B", "Sara": "A", "Omar": "C"}
    
    # Capture output
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()
    
    try:
        with patch('builtins.input', side_effect=inputs):
            if force_available is not None:
                with patch('random.choice', return_value="available" if force_available else "maintenance"):
                    main()
            else:
                main()
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        sys.stdout = old_stdout
        output = captured_output.getvalue()
        print(output)
        return output

if __name__ == "__main__":
    print("TESTING GRADE SYSTEM DEMO")
    print("=" * 60)
    
    # Test 1: System under maintenance
    test_scenario("1. System Under Maintenance", [], force_available=False)
    
    # Test 2: Valid student login
    test_scenario("2. Valid Student Login", ["student", "stud456"], force_available=True)
    
    # Test 3: Valid teacher login - view only
    test_scenario("3. Valid Teacher Login (View Only)", ["teacher", "pass123", "no"], force_available=True)
    
    # Test 4: Valid teacher login - update valid grade
    test_scenario("4. Teacher Updates Valid Grade", ["teacher", "pass123", "yes", "Ali", "A"], force_available=True)
    
    # Test 5: Teacher tries invalid grade
    test_scenario("5. Teacher Tries Invalid Grade", ["teacher", "pass123", "yes", "Sara", "X"], force_available=True)
    
    # Test 6: Teacher tries invalid student
    test_scenario("6. Teacher Tries Invalid Student", ["teacher", "pass123", "yes", "John", "A"], force_available=True)
    
    # Test 7: Invalid login credentials
    test_scenario("7. Invalid Login Credentials", ["hacker", "wrongpass"], force_available=True)
    
    # Test 8: Wrong password for valid user
    test_scenario("8. Wrong Password for Valid User", ["teacher", "wrongpass"], force_available=True)
    
    print("\n" + "="*60)
    print("ANALYSIS AND FINDINGS")
    print("="*60)
    
    print("\n🔍 RELIABILITY TESTING:")
    print("- Invalid grade handling: System properly rejects invalid grades (like 'X')")
    print("- Invalid student names: System handles non-existent students gracefully")
    print("- System availability: Random maintenance mode simulates real-world reliability issues")
    print("- Input validation: All user inputs are validated before processing")
    
    print("\n🔒 INTEGRITY TESTING:")
    print("- Student access control: Students CANNOT modify grades")
    print("- Role-based permissions: Only teachers can access grade update functionality")
    print("- Authentication required: System requires valid login before any operations")
    print("- Data protection: Grade modification requires proper authorization")
    
    print("\n📊 SECURITY OBSERVATIONS:")
    print("- Password protection: Each user role has password protection")
    print("- Session management: Failed login prevents access to system")
    print("- Input sanitization: User inputs are stripped and validated")
    print("- Privilege separation: Clear distinction between student and teacher capabilities")
    
    print("\n❌ POTENTIAL VULNERABILITIES:")
    print("- Hardcoded credentials: Passwords are stored in plain text")
    print("- No password complexity requirements")
    print("- No session timeout or logout functionality")
    print("- No audit trail for grade changes")
    print("- Random system availability could be problematic in production")