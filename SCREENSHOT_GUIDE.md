# Grade System Demo - Screenshot Guide

## 📸 Screenshot-Ready Files

I have created individual demonstration files that produce clean, formatted output perfect for screenshots. Each file tests a specific aspect of the system:

### 1. **scenario_1_maintenance.py** - System Availability
**What it demonstrates:** How the system behaves when under maintenance
**Key points for screenshot:**
- Shows "System Status: Under Maintenance" message
- Demonstrates complete access blocking
- Clean program termination

**Run with:** `python3 scenario_1_maintenance.py`

---

### 2. **scenario_2_student_login.py** - Student Access Control  
**What it demonstrates:** Student can view grades but cannot modify them
**Key points for screenshot:**
- Shows successful student login (student/stud456)
- Displays grades to student
- **Important:** Notice NO "Update a grade?" prompt for students
- This proves students CANNOT change grades

**Run with:** `python3 scenario_2_student_login.py`

---

### 3. **scenario_3_invalid_grade.py** - Reliability Testing
**What it demonstrates:** System properly handles invalid grade input
**Key points for screenshot:**
- Shows teacher login and successful authentication
- Shows "BEFORE UPDATE" grades
- Shows "Invalid grade." error message when entering "X"
- Shows "AFTER UPDATE ATTEMPT" with unchanged grades
- Proves data integrity is maintained

**Run with:** `python3 scenario_3_invalid_grade.py`

---

### 4. **scenario_4_login_failure.py** - Resilience Testing
**What it demonstrates:** How system handles failed login attempts
**Key points for screenshot:**
- Shows two types of login failures:
  1. Invalid username ("hacker")
  2. Valid user with wrong password ("teacher")
- Shows "Login Failed." messages
- Shows clean program termination without crashes
- Demonstrates no retry mechanism (must restart)

**Run with:** `python3 scenario_4_login_failure.py`

---

### 5. **scenario_5_successful_update.py** - Successful Operation
**What it demonstrates:** Teacher successfully updating a grade
**Key points for screenshot:**
- Shows teacher login and authentication
- Shows initial grades clearly labeled
- Shows successful grade update (Ali: B → A)
- Shows updated grades with changes highlighted
- Demonstrates normal system operation

**Run with:** `python3 scenario_5_successful_update.py`

---

## 📊 Additional Files for Reference

### **visual_demo.py** - Complete Test Suite
- Runs all scenarios in sequence
- Good for comprehensive overview
- Run with: `python3 visual_demo.py`

### **grade_system_demo.py** - Original Code
- The original demonstration code
- Can be run interactively
- Run with: `python3 grade_system_demo.py`

### **test_results_report.md** - Detailed Analysis
- Comprehensive analysis of all test results
- Security, reliability, and integrity findings
- Recommendations for production use

---

## 🎯 Key Screenshot Recommendations

For the most impactful screenshots, capture these specific scenarios:

1. **Integrity Evidence:** `scenario_2_student_login.py`
   - Clearly shows students have NO grade modification options

2. **Reliability Evidence:** `scenario_3_invalid_grade.py`  
   - Shows system properly rejecting invalid input

3. **Availability Evidence:** `scenario_1_maintenance.py`
   - Shows how downtime affects user access

4. **Resilience Evidence:** `scenario_4_login_failure.py`
   - Shows graceful handling of authentication failures

5. **Success Case:** `scenario_5_successful_update.py`
   - Shows normal operation when everything works correctly

Each file produces clean, well-formatted output with clear headers and explanations that will look professional in screenshots or documentation.