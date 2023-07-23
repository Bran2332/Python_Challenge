import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")


candidates = []
candidate_votes = {}
total_votes = 0 

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

    for row in csv_reader:
        #count total amount of votes
        total_votes += 1 
        current_candidate = row[2] 
         

        #looks through row 2 and adds names to empty list, avoiding duplicates
        if current_candidate not in candidates:
            candidates.append(current_candidate)
            candidate_votes[current_candidate] = 0 

        candidate_votes[current_candidate] += 1 
        
  

percentage_of_votes_Charles = candidate_votes["Charles Casper Stockham"] / total_votes * 100
percentage_of_votes_Diana = candidate_votes["Diana DeGette"] / total_votes * 100
percentage_of_votes_Raymon = candidate_votes["Raymon Anthony Doane"] / total_votes * 100

#The winner of the election based on popular vote

print("Election Results")
print("---------------------------------------")
# Total number of votes
print("Total number of votes: ", total_votes)
print("---------------------------------------")
# The total number of votes each candidate won
print(candidate_votes)
print("Charles", percentage_of_votes_Charles, "%")
print("Diane",percentage_of_votes_Diana, "%")
print("Raymon",percentage_of_votes_Raymon, "%")
print("Winner is Diana Degette with", candidate_votes["Diana DeGette"], "votes")
#save the output file path
output_file = os.path.join("analysis", "PyPoll_Analysis_results.csv")

# open the output file, create the rows with the results and then export a csv file.
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Election Results"])
    writer.writerow(["---------------------------------------"])
# Total number of votes
    writer.writerow(["Total number of votes: ", total_votes])
    writer.writerow(["---------------------------------------"])
# The total number of votes per candidate and the percentage
    writer.writerow(["Votes per candidate: ", candidate_votes])
    writer.writerow(["Charles", (str(percentage_of_votes_Charles)) + "%" + " of votes"])
    writer.writerow(["Diane", (str(percentage_of_votes_Diana)) + "%" + " of votes"])
    writer.writerow(["Raymon", (str(percentage_of_votes_Raymon)) + "%" + " of votes"])
    writer.writerow(["The winner is ", candidates[1]])