gradePercent = float(input("Please Enter your Grade Percentage: "))

if gradePercent == 90 or gradePercent <= 100:
    print(f"Grade:{gradePercent} \nYou have an A (Excellent!)")
elif gradePercent == 80 or gradePercent <= 89:
    print(f"Grade:{gradePercent} \nYou have a B (Good!)")
elif gradePercent == 70 or gradePercent <= 79:
    print(f"Grade:{gradePercent} \nYou have a C (Average!)")
elif gradePercent == 60 or gradePercent <= 69:
    print(f"Grade:{gradePercent} \nYou have a D (Needs Improvement!)")
elif gradePercent == 0 or gradePercent <= 59:
    print(f"Grade:{gradePercent} \nYou have a F (Fail!)")
else:
    print("Invalid Input!")