import random 

 

# Simulated users with roles 

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

 

if __name__ == "__main__": 

    main()