# Ella Sepetjian
# SVAD 220
# M02 Lab Case Study by Ella Sepetjian
# 6/20/2022
# This Python application will accept student names and GPAs and test if the student
# qualifies for either the Dean's List or the Honor Roll

L_Name = input("Hello and welcome!\nPlease enter the student's last name or enter 'ZZZ' to quit: ")

while L_Name != "ZZZ":
    F_Name = input("Thank you! Now please enter the student's first name: ")
    GPA = float(input("Thank you! Next enter the student's GPA as a floating point number: "))
        
    if GPA >= 3.5:
        print(F_Name, L_Name," has made the Dean's List!")
        break
    elif GPA >= 3.25:
        print(F_Name, L_Name," has made the Honor Roll!")
        break
    else:
        print("Sorry",F_Name, L_Name,"has not reached a GPA greater than 3.25.")
        break
    
