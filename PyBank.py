import os
os.system('clear')
# Module for reading CSV files
import csv

csvpath = os.path.join("..", "Resources", "budget_data.csv")
# Definition of the Lists
month = []
Prof_Loss = []
Prof_Tot = []
Sub = []
M =[]
#Reading the CSV File
Output_File = os.path.join("output.csv")
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    # Read each row of data after the header
    for row in csvreader:
        month.append(row[0])
        Prof_Loss.append(row[1])
        Prof_Tot.append(row[1])
    Prof_Tot =[0] + Prof_Tot
    
    # print(Prof_Loss)
    # print(Prof_Tot)
    # print(len(Prof_Loss))
    # print(len(Prof_Tot))
    

    # Changing the List of String to the List of Integers
    PL = ([int(x) for x in Prof_Loss])
    Sum = sum(PL)
    # print(PL)
     # Changing the List of String to the List of Integers
    PT = ([int(x) for x in Prof_Tot])
    # print(PT)

    # Definition of the List of Monthly Differences
    for i in range(0,len(month)):
        Sub.append(PL[i]-PT[i])     
    Sub.pop(0)
    Total = sum(Sub)
    Max_Index = Sub.index(max(Sub))+1
    Min_Index = Sub.index(min(Sub))+1
    Month1 = month[Max_Index]
    Month2 = month[Min_Index]
    

# This Section Presents the Print of the File Output
print("Financial Analysis")
print("------------------------------------------------------")
print(f"Total Months: ", int(len(month)))
print(f"Total: $" , int(Sum))
print(f"Average Change: $", round(Total/(len(Sub)), 2))
print(f"Greatest Increase in Profit: "+ Month1 + "   ($" + str(max(Sub))+")")
print(f"Greatest Decrease in Profit: "+ Month2 + "   ($" + str(min(Sub))+")")
print("------------------------------------------------------")

# Preparation of the Text File as Requested
with open("PyBank.txt", "a") as f:
    print("Financial Analysis", file=f)
    print("------------------------------------------------------", file=f)
    print(f"Total Months: ", int(len(month)), file=f)
    print(f"Total: $" , int(Sum), file=f)
    print(f"Average Change: $", round(Total/(len(Sub)), 2), file=f)
    print(f"Greatest Increase in Profit: "+ Month1 + "   ($" + str(max(Sub))+")", file=f)
    print(f"Greatest Decrease in Profit: "+ Month2 + "   ($" + str(min(Sub))+")", file=f)
    print("------------------------------------------------------", file=f)