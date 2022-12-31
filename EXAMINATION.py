import csv_query
import COURSE
import matplotlib.pyplot as plt
import numpy as np


def enterExamMarks(Course_ID_s,Marks_Obtained_s):
	for i in range(len(Course_ID_s)):
		Marks_Obtained_List = []
		for Student_ID in Marks_Obtained_s[i]:
			Marks_Obtained_List.append(":".join([Student_ID ,str(Marks_Obtained_s[i][Student_ID]) ]))
		csv_query.updateTable('course',[Course_ID_s[i],'','-'.join(Marks_Obtained_List)])

def viewPerformance():
	students = csv_query.selectRecordsByField('student','Student ID')
	courses  = csv_query.selectRecordsByField('course','Course ID')
	course_performances = []
	for course in courses:
		course_performances.append([course]+COURSE.viewPerformance(course))
	#print(course_performances)
	#print()
	student_performances = []
	for student in students:
		student_performance = [student]
		for course_performance in course_performances:
			#print(course_performance)
			#print()
			for record in course_performance[1:]:
				#print(record)
				if record[0] == student:
					student_performance.append(course_performance[0]+':'+record[3])
					break
		student_performances.append(student_performance)
	#print(student_performances)
	return student_performances
 #Show Scatter Plot

def showExamStats():
	courses_table = csv_query.selectAllRecords('course')
	courses_dict = dict()
	for course in courses_table:
		marks = list()
		batch = list()
		for marks_i in course[2].split('-'):
			marks.append(marks_i.split(':')[1])
			batch.append(csv_query.selectRecordByID('student',marks_i.split(':')[0])[3])
		courses_dict[course[0]] = [ marks, batch ]
	#print(courses_dict)
	np.random.seed(19680801)
	for course in courses_dict:
		plt.scatter( courses_dict[course][1], np.array(courses_dict[course][0]) , label = course , alpha = 0.5)
	plt.legend()
	plt.show()
