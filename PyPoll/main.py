import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

#Lists

candidates = []

vote_counter = {}

total_votes = 0 

with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

    for row in csv_reader:
        #count total amount of votes
        total_votes += 1 
        candidate_names = row[2]  

        #looks through row 2 and adds names to empty list, avoiding duplicates
        if candidate_names not in candidates:
            candidates.append(candidate_names)

            vote_counter[candidate_names] = 0 

        vote_counter[candidate_names] += 1  


print(vote_counter)
                      



        

        
        
        

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote

                        



print("Election Results")
print("---------------------")

print("Total number of votes: ", total_votes)


