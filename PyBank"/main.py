#import libraries
import os
import csv


# Path to collect data from the Resources folder
budget_data = os.path.join('Resources', 'budget_data.csv')

# Initialize variables to store calculated values
net_total=0
total_rows=0
data=[]

# Open the CSV file and create a CSV reader object
with open(budget_data, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)

# Read each row of the CSV and store it in the 'data' list
    for row in csvreader:
        data.append(row)
        total_rows += 1

# Calculate the net total from the stored data
    for row in data:
        net_total += int(row[1]) 
        net_total_formatted = f"${net_total:.0f}"

# Calculate the average change in "Profit/Losses" over the entire period, and then the average of those changes
differences = []
for i in range(1, len(data)):
    difference = int(data[i][1]) - int(data[i - 1][1])
    differences.append(difference)
average_change = sum(differences) / (total_rows - 1)
net_total_formatted = f"${net_total:.0f}"
average_change_formatted = f"${average_change:.2f}"


# Find the greatest increase and decrease in profits 
greatestIncrease = max(differences)
greatestDecrease = min(differences)
greatestIncrease_formatted= f"(${greatestIncrease:.0f})"
greatestDecrease_formatted= f"(${greatestDecrease:.0f})"

# Find the corresponding dates for greatest increase and decrease in profits
for i in range(len(differences)):
    if differences[i] == greatestIncrease:
        dateInc=(data[i+1][0])

for i in range(len(differences)):
    if differences[i] == greatestDecrease:
        dateDecr=(data[i+1][0])


# Print the financial analysis results
print("                 ")
print("Financial Analysis")
print("------------------------")
print("Total Months:", total_rows)
print("Total:", net_total_formatted)
print("Average Change:", average_change_formatted)
print("Greatest Increase in Profits:", dateInc, greatestIncrease_formatted)
print("Greatest Decrease in Profits", dateDecr,  greatestDecrease_formatted)
print("                 ")

# Create a txt file and output the results 
file_path = 'analysis/outputBank.txt'
# Open a file in write mode 
with open('output.txt', 'w') as file:
    # Write the output to the file
    file.write("                 \n")
    file.write("Financial Analysis\n")
    file.write("------------------------\n")
    file.write(f"Total Months: {total_rows}\n")
    file.write(f"Total: {net_total_formatted}\n")
    file.write(f"Average Change: {average_change_formatted}\n")
    file.write(f"Greatest Increase in Profits: {dateInc} {greatestIncrease_formatted}\n")
    file.write(f"Greatest Decrease in Profits {dateDecr} {greatestDecrease_formatted}\n")
