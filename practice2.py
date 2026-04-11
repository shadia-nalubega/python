def tests(test1, test2):
	# since it is a dynamic function, we are saying if the argument of test1 is equal to the argument of test2,return the argument of test 1
	if test1 == test2:
		#
		return test1
	else:
		# otherwise, we are saying that the computer should return the argument of test2
		return test2
# at this point we are prompting the user to input their marks for the different tests
test1 = int(input('Please enter Marks for test one: '))
test2 = int(input('Please enter Marks for test two: '))
# tests(67,90)
print(tests(test1,test2))

def courseWrk(cswork):
	# the testsmark are equal to the marks in the tests function above with their corresponding arguments
	testsMark = tests(test1,test2)
	# we are getting the average tests coursework by adding the marks of the coursework and the testmark then dividing by two
	avgtestsCswork = (cswork + testsMark)/2
	# here the fnltestcourse work is given by avgtest course work we have got above times 40/100
	fnltestsCswork = avgtestsCswork * (40/100)
	# at first we are going to print the average tests course work
	print(avgtestsCswork)
	# then we will print the final tests course work
	print('your final coursework marks is: ', fnltestsCswork)
	print(fnltestsCswork)
# here we are prompting the user to input their course work marks
cswork = int(input('Please enter your course work Marks: '))
# at this point we are invoking the function to be executed. After running the terminal, we will see the final course work marks
courseWrk(cswork)
