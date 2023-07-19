import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

#
total_votes = 0 

with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

    for row in csv_reader:

        total_votes += 1 





print("Total number of votes: ", total_votes)


