import os
import csv

def createDatabase():
    if( not(os.path.exists('./databases/student.csv')) ):
        file = open('./databases/student.csv','w+',newline='')
        csvwriter = csv.writer(file)
        csvwriter.writerow(['Student ID','Name','Class Roll Number','Batch ID'])
        file.close()
    if( not(os.path.exists('./databases/course.csv')) ):
        file = open('./databases/course.csv','w+',newline='')
        csvwriter = csv.writer(file)
        csvwriter.writerow(['Course ID','Course Name','Marks Obtained'])
        file.close()
    if( not(os.path.exists('./databases/batch.csv')) ):
        file = open('./databases/batch.csv','w+',newline='')
        csvwriter = csv.writer(file)
        csvwriter.writerow(['Batch ID','Batch Name','Department ID','List of Courses', 'List of Students'])
        file.close()
    if( not(os.path.exists('./databases/department.csv')) ):
        file = open('./databases/department.csv','w+',newline='')
        csvwriter = csv.writer(file)
        csvwriter.writerow(['Department ID','Department Name','List of Batches'])
        file.close()

def getHeader(table_name):
    file = open('./databases/'+table_name+'.csv','r',newline='')
    csvreader = csv.reader(file)
    header = next(csvreader)
    file.close()
    return header

def selectAllRecords(table_name):
    file = open('./databases/'+table_name+'.csv','r',newline='')
    csvreader = csv.reader(file)
    header = next(csvreader)
    records = []
    for record in csvreader:
        if len(record)==0:
            continue
        records.append(record)
    file.close()
    return records

def selectRecordByID(table_name,primary_id):
    file = open('./databases/'+table_name+'.csv','r',newline='')
    csvreader = csv.reader(file)
    header = next(csvreader)
    records = []
    for record in csvreader:
        if len(record)==0:
            continue
        if (record[0] == primary_id):
            records = record
    file.close()
    return records

def selectRecordsByFieldVal(table_name,field_name,field_val):
    field_num = getHeader(table_name).index(field_name)
    file = open('./databases/'+table_name+'.csv','r',newline='')
    csvreader = csv.reader(file)
    header = next(csvreader)
    records = []
    for record in csvreader:
        if len(record)==0:
            continue
        if(record[field_num]==field_val):
            records.append(record)
    file.close()
    return records

def selectRecordsByField(table_name,field_name):
    field_num = getHeader(table_name).index(field_name)
    file = open('./databases/'+table_name+'.csv','r',newline='')
    csvreader = csv.reader(file)
    header = next(csvreader)
    records = []
    for record in csvreader:
        if len(record)==0:
            continue
        records.append(record[field_num])
    file.close()
    return records

def insertIntoTable(table_name,record):
    if(len(selectRecordByID(table_name,record[0]))==0):
        file = open('./databases/'+table_name+'.csv','a',newline='')
        csvwriter = csv.writer(file)
        csvwriter.writerow(record)
        file.close()
        return False
    else:
        return True

def updateTable(table_name,updated_record):
    if(len(updated_record[0])==0):
        print("ERROR : Primary Key can not be empty.")
        return
    prev_record = selectRecordByID(table_name,updated_record[0])
    if(len(prev_record)==0):
        print("ERROR : Record Not Found.")
        return
    for i in range(len(prev_record)):
        if(len(updated_record[i])==0):
            updated_record[i] = prev_record[i]
    file = open('./databases/'+table_name+'.csv','r',newline='')
    lines = []
    for row in file:
        if(row=="\r\n"):
            continue
        if(row.split(',')[0]==updated_record[0]):            
            row = ','.join(updated_record)+'\n'
        lines.append(row)
    file.close()
    file = open('./databases/'+table_name+'.csv','w',newline='')
    file.writelines(lines)
    file.close()

def updateTableA(table_name,updated_record):
    if(len(updated_record[0])==0):
        print("ERROR : Primary Key can not be empty.")
        return
    prev_record = selectRecordByID(table_name,updated_record[0])
    if(len(prev_record)==0):
        print("ERROR : Record Not Found.")
        return
    for i in range(1,len(prev_record)):
        if(len(updated_record[i])==0):
            updated_record[i] = prev_record[i]
        else :
            updated_record[i] = prev_record[i] + updated_record[i]
    file = open('./databases/'+table_name+'.csv','r',newline='')
    lines = []
    for row in file:
        if(row=="\r\n"):
            continue
        if(row.split(',')[0]==updated_record[0]):            
            row = ','.join(updated_record)+'\n'
        lines.append(row)
    file.close()
    file = open('./databases/'+table_name+'.csv','w',newline='')
    file.writelines(lines)
    file.close()

def deleteFromTable(table_name,primary_id):
    if(len(selectRecordByID(table_name,primary_id))==0):
        print("ERROR : Primary Key can not be empty.")
        return
    prev_record = selectRecordByID(table_name,primary_id)
    if(len(prev_record)==0):
        print("ERROR : Record Not Found.")
        return
    file = open('./databases/'+table_name+'.csv','r',newline='')
    lines = []
    for row in file:
        if(row=="\r\n"):
            continue
        if(row.split(',')[0]==primary_id):            
            continue
        lines.append(row)
    file.close()
    file = open('./databases/'+table_name+'.csv','w',newline='')
    file.writelines(lines)
    file.close()

def dropTable(table_name):
    file = './databases/'+table_name+'.csv'
    if(os.path.exists(file)):
        os.remove(file)
    else:
        print("Error : File Not Found!")

def dropDatabase():
    dropTable('student')
    dropTable('course')
    dropTable('batch')
    dropTable('department')

createDatabase()