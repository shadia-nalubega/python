#Step 1: Define the function student_data
def student_data():
    #Step 2: capture student's personal information
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))   # convert age from string to integer.
    school = input("Name of school: ")
    subject = input("Class subject: ")

    # Step 3: Capture student's score and convert it to integer
    grade = int(input("Please enter your score: "))
    
    # Step 4: Check if score is valid
    # score should not be above 100
    if grade > 100:
        result = "Please enter correct score"
    # Determine grade based on score
    elif grade > 85:
        result = "Exceptional"  # above 85
    elif 75 <= grade <= 85:
        result = "Excellent"  # 75-85
    elif 60 <= grade <= 75:
        result = "Good"  # 60-75
    else:
        result = "Pass"  # 0-60

    # Display student's results
    print("\n---Student Report---")
    print("Name:", name)
    print("Age:", age)
    print("School:", school)
    print("Subject", subject)
    print("Grade:", result)

# Call the function student_data to be excecuted
student_data()