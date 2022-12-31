import csv_query
import os

def createStudent(Student_ID , Name , Class_Roll_Number , Batch_ID):
    if(len(Batch_ID)!=0):
        record = csv_query.selectRecordByID('batch',Batch_ID)
        if(len(record)!=0):
            student_exists = csv_query.insertIntoTable('student',[Student_ID , Name , Class_Roll_Number , record[0]]) 
            if(student_exists):
                print("Student record already exists!")
                return
            if(len(record[4])==0):
                csv_query.updateTable('batch',[record[0],'','','',Student_ID])
            else :
                csv_query.updateTable('batch',[record[0],'','','',record[4]+':'+Student_ID])
            
        else:
            print("Specified Batch does not exist!")    
    else:
        print("Batch ID can not be empty!")

def updateStudent(Student_ID , Name , Class_Roll_Number , Batch_ID):
    if(len(Batch_ID)!=0):
        record = csv_query.selectRecordByID('batch',Batch_ID)
        if(len(record)!=0):
            prev_batch = csv_query.selectRecordByID('batch',csv_query.selectRecordByID('student',Student_ID)[3])
            csv_query.updateTable('batch',[prev_batch[0],'','','',prev_batch[4].replace(Student_ID,'')])
            csv_query.updateTable('batch',[record[0],'','','',record[0]+':'+Student_ID])
        else:
            print("Specified Batch does not exist!")
            return    
    csv_query.updateTable('student',[Student_ID , Name , Class_Roll_Number , Batch_ID])

def removeStudent(Student_ID):
    if(len(csv_query.selectRecordByID('student',Student_ID))==0):
        print("Student does not exist!")
        return
    prev_batch = csv_query.selectRecordByID('batch',csv_query.selectRecordByID('student',Student_ID)[3])  
    csv_query.updateTable('batch',[prev_batch[0],'','','',prev_batch[4].replace(Student_ID,' ')])
    csv_query.deleteFromTable('student',Student_ID)
    if(os.path.exists('./reports/'+Student_ID+".txt")):
        os.remove('./reports/'+Student_ID+".txt")
    print("Student successfully removed.")

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


def generateReport(Student_ID):
    student_record = csv_query.selectRecordByID('student',Student_ID)
    batch_record   = csv_query.selectRecordByID('batch',student_record[3])
    courses = batch_record[3].split(":")
    course_marks  = []
    for course in courses:
        student_marks = csv_query.selectRecordByID('course',course)[2].split("-")
        for x in student_marks:
            if(x.split(':')[0]==Student_ID):
               course_marks.append(x.split(':')[1])
               break 
    if(len(course_marks)==0):
        print("All marks have not yet been uploaded")
        return
    file = open('./reports/'+Student_ID+".txt",'w+')
    file.write("==============================================================\n")
    file.write("                      STUDENT REPORT\n")
    file.write("==============================================================\n")
    file.write("Student ID : "+Student_ID+"\n")
    file.write("Student Name : "+student_record[1]+"\n")
    for i in range(len(courses)):
        file.write("["+courses[i]+"]"+" Percentage : "+course_marks[i]+" Grade : "+getGrade(int(course_marks[i]))+" ")
        file.write("Fail" if(getGrade(int(course_marks[i])))=='F' else "Pass")    
        file.write("\n")
    file.write("==============================================================\n")


