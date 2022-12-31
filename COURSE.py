import csv_query
import matplotlib.pyplot as plt

def createCourse(Course_ID, Course_Name, Marks_Obtained):
	Marks_Obtained_List = []
	for Student_ID in Marks_Obtained:
		Marks_Obtained_List.append(":".join([Student_ID],Marks_Obtained[Student_ID]))
	course_exists = csv_query.insertIntoTable('course',[Course_ID, Course_Name, '-'.join(Marks_Obtained_List)])
	if (course_exists):
		print("Course record already exists!")

def viewPerformance(Course_ID):
	record = csv_query.selectRecordByID('course',Course_ID)
	temp_students = record[2].split('-')
	students = []
	for student in temp_students:
		temp_student = csv_query.selectRecordByID('student',student.split(":")[0])+[student.split(":")[1]]
		students.append( [temp_student[0],temp_student[2],temp_student[1],temp_student[4]] )
	
	return students
	"""
	print("Marks of Students in "+record[1])
	print("=================================================")
	print("Class Roll Number | Student Name | Marks Obtained")
	print("=================================================")
	for student in students:
		print("        %2s          |     %s         |       %2s        "%(student[2],student[1],student[4]))
	"""

def getGrade(marks):
	if(marks>=90):
		return 'A'
	elif(marks>=80):
		return 'B'
	elif(marks>=70):
		return 'C'
	elif(marks>=60):
		return 'D'
	elif(marks>=50):
		return 'E'
	else:
		return 'F'

def showCourseStats(Course_ID):
	grades = {'A':0 , 'B':0 , 'C':0 , 'D':0 , 'E':0 , 'F':0}
	record = csv_query.selectRecordByID('course',Course_ID)
	temp_students = record[2].split('-')
	students = []
	for student in temp_students:
		grades[getGrade(int(student.split(":")[1]))] += 1
	x = list(grades.keys())
	y = list(grades.values())
	#Plot a Histogram
	plt.bar(x,y,align='center')
	plt.xlabel('Grades')
	plt.ylabel('Number of Students')
	plt.yticks(y)
	plt.show()