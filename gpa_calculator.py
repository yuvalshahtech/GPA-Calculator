def display_data(name,subject,marks,gpa):
    print(f"Name: {name}")
    print(f"Subject: {subject}")
    print(f"Marks: {marks}")
    print(f"GPA: {gpa}")

def calculate_gpa(marks):
    gpa=marks/10
    return gpa

def validate_marks(marks):
    while marks<0 or marks>100:
        marks=int(input("Please enter valid marks!!: "))
    return marks

def main():
    name=input("Enter your name: ").title().strip()
    subject=input("Enter the name of subject: ").title().strip()
    marks=int(input(f"Enter the marks you got in {subject}: "))
    marks=validate_marks(marks)
    gpa=calculate_gpa(marks)
    print("\n----GPA Result----")
    display_data(name,subject,marks,gpa)

if __name__=="__main__":
    main()
