#import dependencies
import os
import csv

#path
budget_data = os.path.join("PyBank/Resources/budget_data.csv")
output = os.path.join("PyBank/Analysis/Pybank_Analysis.txt")

#Define variables
months = []
profit_loss_changes = []

count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0

#open and read csv
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:

        #count of months
        count_months += 1

        #total Profit/Losses
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        if (count_months == 1):

            # Make the value of previous month to be equal to current month
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:

            # find change in profit loss 
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            # Add to the months[]
            months.append(row[0])

            # Add to profit_loss_changes[]
            profit_loss_changes.append(profit_loss_change)

            # Prepare next loop by assigning current month to last month i
            previous_month_profit_loss = current_month_profit_loss

    #sum and average of Profit/Losses
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)

    #highest and lowest change
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    # match highest and lowest values with corresponding month
    highest_month = profit_loss_changes.index(highest_change)
    lowest_month = profit_loss_changes.index(lowest_change)

    #assign variables for best and worst month
    best_month = months[highest_month]
    worst_month = months[lowest_month]

#Print analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {count_months}")
print(f"Total: ${net_profit_loss}")
print(f"Average Change: ${average_profit_loss}")
print(f"Greatest Increase in Profits: {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses: {worst_month} (${lowest_change})")    
    
with open(output, "w") as text:
    text.write("Financial Analysis\n")
    text.write("----------------------------\n")
    text.write(f"Total Months: {count_months}\n")
    text.write(f"Total: ${net_profit_loss}\n")
    text.write(f"Average Change: ${average_profit_loss}\n")
    text.write(f"Greatest Increase in Profits: {best_month} (${highest_change})\n")
    text.write(f"Greatest Decrease in Losses: {worst_month} (${lowest_change})\n")


