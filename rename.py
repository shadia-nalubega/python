# capturing the user information
# at this point we are prompting the user to input their information
name = input("please enter your name")
age = input("please enter your age")
school = input("please enter your school")
program =input("please enter your program")
# each input field will print it's value
print(name)
print(age)
print(school)
print(program)
# grading the scores
score = int(input("please enter your score")) # the user inputs their marks
print(score)
if score > 85:
    print("Exceptional")
elif score >= 75:
    print("Excellent")
elif score >= 60:
    print("good")
else:
    print("pass")
print("Happy Easter") #the overall comment foe all
