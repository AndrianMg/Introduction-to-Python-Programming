import subprocess
import sys
from io import StringIO
import os

def run_test_scenario(test_name, inputs):
    """Run the grade system with specific inputs and capture output"""
    print(f"\n{'='*50}")
    print(f"TEST SCENARIO: {test_name}")
    print(f"{'='*50}")
    
    # Create input string
    input_data = '\n'.join(inputs) + '\n'
    
    # Run the script with input
    try:
        result = subprocess.run(
            [sys.executable, 'grade_system.py'],
            input=input_data,
            text=True,
            capture_output=True,
            timeout=10
        )
        
        print("OUTPUT:")
        print(result.stdout)
        
        if result.stderr:
            print("ERRORS:")
            print(result.stderr)
            
    except subprocess.TimeoutExpired:
        print("Test timed out - likely due to system maintenance")
    except Exception as e:
        print(f"Error running test: {e}")

def main():
    print("Testing Grade System with Multiple Scenarios")
    print("Note: The system randomly chooses availability status, so we'll run multiple tests")
    
    # Test 1: Valid teacher login and grade update
    run_test_scenario(
        "Valid Teacher Login - Update Grade",
        ["teacher", "pass123", "yes", "Ali", "A"]
    )
    
    # Test 2: Valid student login
    run_test_scenario(
        "Valid Student Login",
        ["student", "stud456"]
    )
    
    # Test 3: Invalid username
    run_test_scenario(
        "Invalid Username",
        ["invalid_user", "password123"]
    )
    
    # Test 4: Invalid password
    run_test_scenario(
        "Invalid Password for Teacher",
        ["teacher", "wrong_password"]
    )
    
    # Test 5: Teacher login with invalid grade update
    run_test_scenario(
        "Teacher Login - Invalid Grade",
        ["teacher", "pass123", "yes", "Ali", "Z"]
    )
    
    # Test 6: Teacher login with invalid student name
    run_test_scenario(
        "Teacher Login - Invalid Student Name",
        ["teacher", "pass123", "yes", "NonExistentStudent", "A"]
    )
    
    # Test 7: Teacher login but decline to update
    run_test_scenario(
        "Teacher Login - Decline Update",
        ["teacher", "pass123", "no"]
    )
    
    # Test multiple runs to see system availability randomness
    print(f"\n{'='*50}")
    print("TESTING SYSTEM AVAILABILITY (Multiple Runs)")
    print(f"{'='*50}")
    
    available_count = 0
    maintenance_count = 0
    
    for i in range(5):
        print(f"\nRun {i+1}:")
        try:
            result = subprocess.run(
                [sys.executable, 'grade_system.py'],
                input="teacher\npass123\nno\n",
                text=True,
                capture_output=True,
                timeout=5
            )
            
            if "System Status: Available" in result.stdout:
                available_count += 1
                print("✓ System is Available")
            elif "Under Maintenance" in result.stdout:
                maintenance_count += 1
                print("✗ System Under Maintenance")
            else:
                print("? Unknown status")
                
        except Exception as e:
            print(f"Error in run {i+1}: {e}")
    
    print(f"\nSUMMARY:")
    print(f"Available: {available_count}/5 runs")
    print(f"Maintenance: {maintenance_count}/5 runs")

if __name__ == "__main__":
    main()