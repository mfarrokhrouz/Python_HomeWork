# Clear the Screen
import os
os.system('clear')
# Module for reading CSV files
import csv

# Introducing the Lists and Integers
Total_Votes=[]
Total_County = []
Total_Candidate =[]
List_Candidates=[]
List_County = []
Sum1 = 0
Sum2 = 0
Sum3 = 0


#Reading the CSV File
csvpath = os.path.join("..", "Resources", "election_data.csv")

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    # Read each row of data after the header
    for row in csvreader:
        Total_Votes.append(row[0])
        Total_Candidate.append(row[2])

# Change the List of String to the List of Integers
Votes = ([int(x) for x in Total_Votes])

# List of the Candidates
for i in Total_Candidate:
    if i not in List_Candidates:
        List_Candidates.append(i)

# In This Part, the Percentage of Each Candidate is Calculated
for k in range(0,int(len(Total_Votes))):
    if Total_Candidate[k] == List_Candidates[0]:
        Sum1 = Sum1 + 1
    if Total_Candidate[k] == List_Candidates[1]:
        Sum2 = Sum2 +1 
    if Total_Candidate[k] == List_Candidates[2]:
        Sum3 = Sum3 + 1    
SumSum = Sum1 + Sum2 + Sum3

# This Section Determines the Winner of the Voting
for m in range(0,len(List_Candidates)):
    if Sum1 > Sum2 and Sum1 > Sum3:
        Winner = List_Candidates[0]
    if Sum2 > Sum1 and Sum2 > Sum3:
        Winner = List_Candidates[1]
    if Sum3 > Sum1 and Sum3 > Sum2:
        Winner = List_Candidates[2]
    

# This Section Presents the Print of the File Output
print("Election Results")
print("------------------------------------------------------")
print(f"Total Votes: ", len(Total_Votes))
print("------------------------------------------------------")
print(f"List of the Candidates is: " + str(List_Candidates))
print("------------------------------------------------------")
print(List_Candidates[0] + " : " + str(round(Sum1 * 100 / SumSum, 3)) + "%   ("+ str(Sum1) + ")")
print(List_Candidates[1] + " : " + str(round(Sum2 * 100 / SumSum, 3)) + "%   ("+ str(Sum2) + ")")
print(List_Candidates[2] + " : " + str(round(Sum3 * 100 / SumSum, 3)) + "%   ("+ str(Sum3) + ")")
print("------------------------------------------------------")
print("Winner: " + Winner)

# Preparation of the Text File as Requested
with open("PyPoll.txt", "a") as f:
    print("Election Results", file=f)
    print("------------------------------------------------------", file=f)
    print(f"Total Votes: ", len(Total_Votes), file=f)
    print("------------------------------------------------------", file=f)
    print(f"List of the Candidates is: " + str(List_Candidates), file=f)
    print("------------------------------------------------------", file=f)
    print(List_Candidates[0] + " : " + str(round(Sum1 * 100 / SumSum, 3)) + "%   ("+ str(Sum1) + ")", file=f)
    print(List_Candidates[1] + " : " + str(round(Sum2 * 100 / SumSum, 3)) + "%   ("+ str(Sum2) + ")", file=f)
    print(List_Candidates[2] + " : " + str(round(Sum3 * 100 / SumSum, 3)) + "%   ("+ str(Sum3) + ")", file=f)
    print("------------------------------------------------------", file=f)
    print("Winner: " + Winner, file=f)      