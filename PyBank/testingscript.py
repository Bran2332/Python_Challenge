import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

# Lists to store data
greatest_inc_profit = ["", 0]
greatest_dec_profit = ["", 9999999999999999999]
total_months = 0
month_of_change = []
net_change_list = []
profit = 0

with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)
   

    for row in csv_reader:
        # Loop through rows and add up the total amount of months
        # Track the total
        total_months += 1
        profit += int(row[1])

        first_row = csv_header
  
        prev_net = int(row[1])
        
        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]


      # Calculate the greatest increase:
      #YOUR CODE HERE

      # Calculate the greatest decrease:
       #YOUR CODE HERE
    


        
# Calculate the Average Net Change
net_monthly_avg = sum(net_change_list) / len(net_change_list)

print(net_change)






