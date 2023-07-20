import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

# Lists to store data
greatest_inc_profit = ["", 0]
greatest_dec_profit = ["", 90000000000]
total_months = 0
profit = 0
month_of_change = []
net_change_list = []

with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    #skip the header row and first row of data
    csv_header = next(csv_reader)
    first_row = next(csv_reader)
    # Add 1 to months to make up for the lost value from the above statemnet and add the first value of profit as well
    total_months += 1
    profit += int(first_row[1])
    #prev_net is now the value of the first row of data that was skipped
    prev_net = int(first_row[1])
    

    for row in csv_reader:
        # Loop through rows and add up the total amount of months and total amount of profit
        
        profit += int(row[1])
        total_months += 1

        #Calculate the net profit over the entire period
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]
        # Calculate the Average Net Change
        net_monthly_avg = sum(net_change_list) / len(net_change_list)
         # Calculate the greatest increase:
        if net_change > greatest_inc_profit[1]:
            greatest_inc_profit[0] = row[0]
            greatest_inc_profit[1] = net_change

        # Calculate the greatest decrease:
        if net_change < greatest_dec_profit[1]:
            greatest_dec_profit[0] = row[0]
            greatest_dec_profit[1] = net_change


print("Total Months : " , total_months)
print("Total Profit : ", "$" + (str(profit)))
print("Average Change : ", "$",net_monthly_avg)
print("Greatest Increase in Profits: ", greatest_inc_profit[0], "$", greatest_inc_profit[1])
print("Greatest Decrease in Profits: ", greatest_dec_profit[0], "$", greatest_dec_profit[1])

#save the output file path
output_file = os.path.join("PyBank_Analysis.csv")

# open the output file, create the rows with the results and then export a csv file.
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Total Months:", total_months])
    writer.writerow(["Total Profit:", "$" + (str(profit))])
    writer.writerow(["Average Change:", "$" + (str(net_monthly_avg))])
    writer.writerow(["Greatest Increase in Profits:", greatest_inc_profit[0], "$" + (str(greatest_inc_profit[1]))])
    writer.writerow(["Greatest Decrease in Profits:", greatest_dec_profit[0], "$" + (str(greatest_dec_profit[1]))])

    

    


