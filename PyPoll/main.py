import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

#Lists


candidates = []
clean_candidates_list = []

total_votes = 0 

with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

     for row in csv_reader:

        total_votes += 1 
        
        if row[2] not in clean_candidates_list:
            clean_candidates_list.append(row[2])
        


                          
print(clean_candidates_list)



print("Election Results")
print("---------------------")

print("Total number of votes: ", total_votes)


