import csv_query
import COURSE
import matplotlib.pyplot as plt

def createBatch(Batch_ID , Batch_Name ,Department_ID ,List_of_Courses, List_of_Students):
    record = csv_query.selectRecordByID('department',Department_ID) 
    if(len(record)==0):
        print("Department Not Found!")
        return
    batch_exists = csv_query.insertIntoTable('batch',[Batch_ID , Batch_Name, record[0] , ':'.join(List_of_Courses), ':'.join(List_of_Students) ]) 
    if(batch_exists):
        print("Batch record already exists!")
    else:
        if(len(record[2])==0):
            csv_query.updateTableA('department',[record[0],'',Batch_ID])
        else :
            csv_query.updateTableA('department',[record[0],'',':'+Batch_ID])
        

def viewAllStudents(Batch_ID):
    record = csv_query.selectRecordByID('batch',Batch_ID)
    students = record[4].split(':')
    return students
    #print("Students Of "+record[1]+" Batch record[2]    return students

def viewAllCourses(Batch_ID):
    record = csv_query.selectRecordByID('batch',Batch_ID)
    courses = record[3].split(':')
    #print("Courses taught in "+record[1]+" Batch :")
    return courses

def viewPerformance(Batch_ID):
    students = viewAllStudents(Batch_ID)
    courses  = viewAllCourses(Batch_ID)
    student_marks = [0]*len(students)
    for course in courses:
        course_marks = COURSE.viewPerformance(course)
        for marks in course_marks:
            try:
                student_marks[students.index(marks[0])] += int(marks[3])
            except:
                continue
    percentages = []
    for marks in student_marks:
        percentages.append(marks/len(courses))
    
    report = []
    for i in range(len(students)):
        student = students[i]
        student_record = csv_query.selectRecordByID('student',student)
        report.append([ student_record[0], student_record[2], student_record[1], percentages[i]  ])
        """
            Student_ID | Class_Roll_Number | Student_Name | Percentage
        """
    return report

def viewPerformanceChart(Batch_ID):
    report = viewPerformance(Batch_ID)
    students = []
    percentages = []
    for record in report:
        students.append(record[0]+"\n"+record[2])
        percentages.append(record[3])
    plt.pie(percentages,labels=students)
    plt.show()