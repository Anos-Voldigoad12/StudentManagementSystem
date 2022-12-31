import csv_query
import BATCH
import matplotlib.pyplot as plt

def createDepartment(Department_ID , Department_Name , List_of_Batches):
    department_exists = csv_query.insertIntoTable('department',[Department_ID , Department_Name , ':'.join(List_of_Batches)]) 
    if(department_exists):
        print("Department record already exists!")

def viewAllBatches(Department_ID):
    record = csv_query.selectRecordByID('department',Department_ID)
    batches = record[2].split(':')
    #print("Batches Of "+record[1]+" Department :")
    return batches

def viewAvgPerformance(Department_ID):
    batches = viewAllBatches(Department_ID)
    batch_average = 0
    for batch in batches:
        report = BATCH.viewPerformance(batch)
        batch_performance = 0
        num_of_students = 0
        for record in report:
            batch_performance += record[3]
            num_of_students += 1
        batch_average += (batch_performance/num_of_students)
    return batch_average/len(batches)

def showDepartmentStats(Department_ID):
    batches = viewAllBatches(Department_ID)
    batch_averages= []
    for batch in batches:
        report = BATCH.viewPerformance(batch)
        batch_performance = 0
        num_of_students = 0
        for record in report:
            batch_performance += record[3]
            num_of_students += 1
        batch_averages.append(batch_performance/num_of_students)
    plt.plot(batches,batch_averages)
    plt.show()


