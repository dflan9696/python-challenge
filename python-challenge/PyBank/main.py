# import os

import os
import csv

# import csv

budget_path = os.path.join("Resources", "budget_data.csv")

# output to text

text_path = "output.txt"

# print headers

print("Financial Analysis")
print("--------------------")

# Open the CSV

with open(budget_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # find total months

    header = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(row)
        total_months = len(rows)
    print("Total Months: " + str(total_months))

with open(budget_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")  

    # find total profits  

    header = next(csvreader)
    total = 0
    for row in csvreader:
        total += int(row[1])
    print("Total: $" + str(total))

with open(budget_path, "r") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")

    # declare variables

    previous_profit = 0
    profit_change_list = []
    month_change = 0
    profit_average = 0
    greatest_decrease = ["", 9999999]
    greatest_increase = ["", 0]

    # find average change of profit
    
    for row in csvreader:
        profit_change = float(row["Profit/Losses"]) - previous_profit
        previous_profit = float(row["Profit/Losses"])
        profit_change_list = profit_change_list + [profit_change]
        month_change = [month_change] + [row["Date"]]

        # greatest increase in revenue (date and amount)
        
        if profit_change>greatest_increase[1]:
            greatest_increase[1] = profit_change
            greatest_increase[0] = row['Date']

        # greatest decrease in revenue (date and amount) 
        
        if profit_change<greatest_decrease[1]:
            greatest_decrease[1] = profit_change
            greatest_decrease[0] = row['Date']
    
     
    profit_average = sum(profit_change_list)/len(profit_change_list)

    # print outputs

    print("Average Change: $" + str(profit_average))
    print("Greatest Increase in Profits: " + greatest_increase[0] + " $(" + str(greatest_increase[1]) + ")")
    print("Greatest Decrease in Profits: " + greatest_decrease[0] + " $(" + str(greatest_decrease[1]) + ")")

    # print outputs to text file

with open(text_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % total_months)
    file.write("Total Revenue: $%d\n" % total)
    file.write("Average Revenue Change $%d\n" % profit_average)
    file.write("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
    file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))

