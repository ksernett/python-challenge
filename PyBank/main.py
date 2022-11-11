import os
import csv
#establish variables
months = 0
total_amt = 0
profit = []
profit_change = []
date = []
avg_change = 0.0
max_change_date = ()
min_change_date = ()
max_change = 0.0
min_change = 0.0

#link to [budget_data.csv](PyBank/Resources/budget_data.csv). 
budget_csv = os.path.join("Resources", "budget_data.csv")
#read csv file
with open(budget_csv, 'r') as budget_file:
    csvreader = csv.reader(budget_file, delimiter=',')
    next(csvreader)

#calculate the total number of months included in the dataset
    for row in csvreader:
        months = months + 1
#calculate the net total amount of "Profit/Losses" over the entire period
        total_amt += int(row[1])
#calculate changes in "Profit/Losses" over the entire period, 
        profit.append(float(row[1]))
        date.append(row[0])


#calculate changes in "Profit/Losses" and find the average
    for i in range(1,len(profit)):
        profit_change.append(profit[i] - profit[i-1])   
        avg_change = sum(profit_change)/len(profit_change)
#find the max and min increase as well as the date
        max_change = max(profit_change)
        min_change = min(profit_change)

        max_change_date = str(date[profit_change.index(max(profit_change))])
        min_change_date = str(date[profit_change.index(min(profit_change))])


#print the analysis to the terminal
print('Financial Analysis \n ---------------------------- \n Total Months: {} \n Total: ${} \n Average Change: $ {} \n Greatest Increase in Profits: {} (${}) \n Greatest Decrease in Profits: {} (${})'.format(months, total_amt, avg_change, max_change_date, max_change, min_change_date, min_change))


#print analysis to a txt file 
f = open('analysis/pybank_results.txt', 'a')
f.write('Financial Analysis \n ---------------------------- \n Total Months: {} \n Total: ${} \n Average Change: $ {} \n Greatest Increase in Profits: {} (${}) \n Greatest Decrease in Profits: {} (${})'.format(months, total_amt, avg_change, max_change_date, max_change, min_change_date, min_change))
f.close()