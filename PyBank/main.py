import os
import csv

budgetcsv=os.path.join('budget_data.csv')

months=0
profit_loss=0
greatest_profit=0
profitmonth=None
greatest_loss=0
lossmonth=None

with open(budgetcsv) as csvfile:
    budgetreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(budgetreader)

    
    for row in budgetreader:
        months = months+1
        profit_loss = profit_loss+int(row[1])

        if profitmonth is None:
            greatest_profit = int(row[1])
            profitmonth = row[0]
            greatest_loss = int(row[1])
            lossmonth = row[0]
            firstprofitvalue = greatest_profit
            firstlossvalue = greatest_loss

        else: 
            if int(row[1]) > greatest_profit:
                greatest_profit = int(row[1])
                profitmonth = row[0]

            if int(row[1]) < greatest_loss:
                greatest_loss = int(row[1])
                lossmonth = row[0]

    averagechange = (int(row[1]) - firstprofitvalue) / months




    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: ",months)
    print("Total: $",profit_loss)
    print("Average Change: ",averagechange)
    print("Greatest Increase in Profits: ",profitmonth, "($",greatest_profit,")")
    print("Greatest Decrease in Profits: ",lossmonth, "($",greatest_loss,")")

file = open('budget_data_export.txt', 'w')
file.write("Financial Analysis\n")
file.write("----------------------------\n")
file.write("Total Months: {0}\n".format(months))
file.write("Total: ${0}\n".format(profit_loss))
file.write("Average Change: {0}\n".format(averagechange))
file.write("Greatest Increase in Profits: {0} (${1})\n".format(profitmonth, greatest_profit))
file.write("Greatest Decrease in Profits: {0} (${1})\n".format(lossmonth, greatest_loss))
file.close()