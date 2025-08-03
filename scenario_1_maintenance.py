#!/usr/bin/env python3
"""
SCENARIO 1: SYSTEM UNDER MAINTENANCE
====================================
This demonstrates what users see when the system is down for maintenance.
"""

import random
from unittest.mock import patch

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

def main():
    print("Dependable Grade System\n")
    if not check_availability():
        return
    print("This line should not appear if system is under maintenance")

if __name__ == "__main__":
    print("🔧 TESTING: SYSTEM AVAILABILITY")
    print("=" * 50)
    print("Simulating system downtime...")
    print("-" * 50)
    
    # Force maintenance mode for demonstration
    with patch('random.choice', return_value="maintenance"):
        main()
    
    print("\n" + "=" * 50)
    print("RESULT: System correctly blocked access during maintenance")
    print("=" * 50)