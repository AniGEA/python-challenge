#import libraries
import os
import csv

##Path to the election data CSV file
election_data = os.path.join('Resources', 'election_data.csv')

# Initializing variables
data = []
total_candidates = 0
counter_dict = {}

# Open the CSV file and read its contents
with open(election_data, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)

    # Iterate over each row in the CSV file
    for row in csvreader:
        data.append(row)
        total_candidates += 1
        candidate_name = row[2]

         # Update the counter dictionary with the candidate's vote count
        if candidate_name in counter_dict:
            counter_dict[candidate_name] += 1
        else:
            counter_dict[candidate_name] = 1

# Determine the winner based on the candidate with the maximum votes
winner = max(counter_dict, key=counter_dict.get)

# Print the election results to the terminal
print("                               ")
print("Election Results")
print("-----------------------------")
print("Total Votes:", total_candidates)
print("-----------------------------")

# Iterate over the counter dictionary and print the percentage of votes for each candidate
for candidate, votes in counter_dict.items():
    percentage = (votes / total_candidates) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

# Print the winner of the election
print("-----------------------------")
print(f"Winner: {winner}")
print("-----------------------------")


# Create a txt file and output the results 
file_path = 'analysis/outputPoll.txt'
# Open a file in write mode
with open(file_path, 'w') as file:
    # Write the output to the file
    file.write("                 \n")
    file.write("Election Results\n")
    file.write("------------------------\n")
    file.write(f"Total Votes: {total_candidates}\n")
    file.write("-----------------------------\n")
    
    for candidate, votes in counter_dict.items():
        percentage = (votes / total_candidates) * 100
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    
    file.write("------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("------------------------\n")