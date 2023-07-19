import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

# Lists to store data
greatest_inc_profit = []
greatest_dec_profit = []
total_months = 0
profit = 0
month_of_change = []
net_change_list = []

with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)
   

    for row in csv_reader:
        # Loop through rows and add up the total amount of months and total amount of profit
        total_months += 1
        profit += int(row[1])

        #Calculate the net profit over the entire period and the average of those changes
        prev_net_profit = int(row[1])
        net_change = int(row[1]) - prev_net_profit
        net_change_list += [net_change]
        month_of_change += [row[0]]

   # Calculate the greatest increase:
      

      # Calculate the greatest decrease:
       #YOUR CODE HERE

        
# Calculate the Average Net Change
net_monthly_avg = sum(net_change_list) / len(net_change_list)





print("Total Months : " , total_months)
print("Total Profit : ",profit)

    


