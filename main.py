import STUDENT
import COURSE
import BATCH
import DEPARTMENT
import EXAMINATION
import csv_query

def loadDefaults():
	DEPARTMENT.createDepartment('CSE' , 'Computer Science and Engineering' , list())
	DEPARTMENT.createDepartment('ECE' , 'Electronics and Communication Engineering' , list())
	COURSE.createCourse('C001', 'Python Programming', dict())
	COURSE.createCourse('C002', 'Physics', dict())
	BATCH.createBatch('CSE22', 'CSE 2022-26', 'CSE', ['C001','C002'], list())
	BATCH.createBatch('CSE21', 'CSE 2021-25', 'CSE', ['C001','C002'], list())
	BATCH.createBatch('ECE22', 'ECE 2022-26', 'ECE', ['C002'], list())
	STUDENT.createStudent('CSE2201', 'Bhaskar Saha', '01', 'CSE22')
	STUDENT.createStudent('CSE2101', 'Nirban Roy', '01', 'CSE21')
	STUDENT.createStudent('ECE2201', 'Sumit Tiwari', '01', 'ECE22')
	STUDENT.createStudent('ECE2202', 'Amavasya Kapoor', '02', 'ECE22')
	EXAMINATION.enterExamMarks(['C001','C002'], [{'CSE2201':95,'CSE2101':73},{'CSE2201':65,'CSE2101':78,'ECE2201':34,'ECE2202':95}])
def mainMenu():
	print("MODULES")
	print("1. Student")
	print("2. Course")
	print("3. Batch")
	print("4. Department")
	print("5. Examination")
def studentMenu():
	print("OPERATIONS")
	print("1. Create Student")
	print("2. Update Student")
	print("3. Remove Student")
	print("4. Generate Report")
def courseMenu():
	print("OPERATIONS")
	print("1. Create Course")
	print("2. View Performance")
	print("3. Course Statistics")
def batchMenu():
	print("OPERATIONS")
	print("1. Create Batch")
	print("2. Show All Students")
	print("3. Show All Courses")
	print("4. View Performance")
	print("5. View Performance Chart")
def departmentMenu():
	print("OPERATIONS")
	print("1. Create Department")
	print("2. Show All Batches")
	print("3. View Average Performance")
	print("4. Department Statistics")
def examinationMenu():
	print("OPERATIONS")
	print("1. Enter Marks")
	print("2. View Performance")
	print("3. Examination Statistics")
def studentOperations():
	while(True):
		studentMenu()
		choice = int(input("Choose an option : "))
		if(choice==1):
			student_id = input("Student ID : ")
			name = input("Name : ")
			roll = input("Class Roll Number : ")
			batch = input("Batch : ")
			STUDENT.createStudent(student_id, name, roll, batch)
		elif(choice==2):
			student_id = input("Student ID : ")
			name = input("Name : ")
			roll = input("Class Roll Number : ")
			batch = input("Batch : ")
			STUDENT.updateStudent(student_id, name, roll, batch)
		elif(choice==3):
			student_id = input("Student ID : ")
			STUDENT.removeStudent(student_id)
		elif(choice==4):
			student_id = input("Student ID : ")
			STUDENT.generateReport(student_id)
		else:
			print("Invalid Choice!")
		if(input("Do you wish to continue(y/n)? ")!='y'):
			break
def courseOperations():
	while(True):
		courseMenu()
		choice = int(input("Choose an option : "))
		if(choice==1):
			course = input("Course ID : ");
			course_name = input("Course Name : ")
			marks_obtained = dict()
			COURSE.createCourse(course,course_name,marks_obtained)
		elif(choice==2):
			course = input("Couse ID : ")
			COURSE.viewPerformance(course)
		elif(choice==3):
			course = input("Couse ID : ")
			COURSE.showCourseStats(course)
		else :
			print("Invalid Choice!")
		if(input("Do you wish to continue(y/n)? ")!='y'):
			break
def batchOperations():
	while(True):
		batchMenu()
		choice = int(input("Choose an option : "))
		if(choice==1):
			batch_id = input("Batch ID : ")
			batch_name = input("Batch Name : ")
			department_id = input("Department ID : ")
			courses = input("List of Courses(seperated by comma) : ").split(',')
			students = list()
			BATCH.createBatch(batch_id,batch_name,department_id,courses,students)
		elif(choice==2):
			batch_id = input("Batch ID : ")
			print("Students : ",BATCH.viewAllStudents(batch_id))
		elif(choice==3):
			batch_id = input("Batch ID : ")
			print("Courses : ", BATCH.viewAllCourses(batch_id))
		elif(choice==4):
			batch_id = input("Batch ID : ")
			performance = BATCH.viewPerformance(batch_id)
			print("%15s | %20s | %15s | %15s"%("Student ID" , "Class Roll Number" , "Student Name" , "Percentage"))
			for record in performance:
				print("%15s | %20s | %15s | %15g"%tuple(record))
		elif(choice==5):
			batch_id = input("Batch ID : ")
			BATCH.viewPerformanceChart(batch_id)
		else:
			print("Invalid Choice!")
		if(input("Do you wish to continue(y/n)? ")!='y'):
			break
def departmentOperations():
	while(True):
		departmentMenu()
		choice = int(input("Choose an option : "))
		if(choice==1):
			department_id = input("Department ID : ")
			department_name = input("Department Name : ")
			batches = list()
			DEPARTMENT.createDepartment(department_id,department_name,batches)
		elif(choice==2):
			department_id = input("Department ID : ")
			print("Batches : ", DEPARTMENT.viewAllBatches(department_id))
		elif(choice==3):
			department_id = input("Department ID : ")
			print("Average Performance : ", DEPARTMENT.viewAvgPerformance(department_id))
		elif(choice==4):
			department_id = input("Department ID : ")
			DEPARTMENT.showDepartmentStats(department_id)
		else:
			print("Invalid Choice!")
		if(input("Do you wish to continue(y/n)? ")!='y'):
			break
def examinationOperations():
	while(True):
		examinationMenu()
		choice = int(input("Choose an option : "))
		if(choice==1):
			courses = csv_query.selectRecordsByField('course','Course ID')
			marks_obtained = list()
			for course in courses:
				marks = dict()
				while(True):
					print("["+str(course)+"]")
					student_id = input("Student ID : ")
					marks[student_id] = int(input("Marks Obtained : "))
					if(input("Do you wanna enter more marks for this course(y/n)? ")!='y'):
						break
				marks_obtained.append(marks)
			EXAMINATION.enterExamMarks(courses,marks_obtained)
		elif(choice==2):
			performance = EXAMINATION.viewPerformance()
			print("%15s | %s"%('Student ID', 'Marks Obtained'))
			for record in performance:
				print("%15s | %s"%(record[0],' , '.join(record[1:]) ))
		elif(choice==3):
			EXAMINATION.showExamStats()
		else:
			print("Invalid Choice!")
		if(input("Do you wish to continue(y/n)? ")!='y'):
			break
def main():
	choice = input("Do you wish to load default database?(y/n)  ")
	if(choice=='y'):
		csv_query.dropDatabase()
		csv_query.createDatabase()
		loadDefaults()
		print("Database loaded successfully!")
	while(True):
		mainMenu()
		choice = int(input("Choose a Module You Wish To Work With? "))
		if(choice==1):
			studentOperations()
		elif(choice==2):
			courseOperations()
		elif(choice==3):
			batchOperations()
		elif(choice==4):
			departmentOperations()
		elif(choice==5):
			examinationOperations()
		else:
			print("Invalid Choice!")
		if(input("Do you wish to continue(y/n)? ")!='y'):
			break

main()


