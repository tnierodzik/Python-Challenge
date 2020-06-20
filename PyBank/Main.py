import csv
import os

print("Financial Analysis")
print("----------------------")

csvpath = os.path.join('..','PyBank','budgetdata.csv')

profit_loss = []
date= []

total = 0
total_months = 0

with open(csvpath, "r") as csvfile:

	csvreader = csv.reader(csvfile,delimiter=',')
	csv_header = next(csvreader)

	for row in csvreader:

		total_months = total_months + 1
		total = total + int(row[1])
		profit_loss.append(int(row[1]))

		average = (sum(profit_loss)/len(profit_loss))
		maximum = max(profit_loss)
		minimum = min(profit_loss)

		date.append(row[0])
		max_date = date[profit_loss.index(maximum)]
		min_date = date[profit_loss.index(minimum)]

print(f"Total Months: {str(total_months)}")
print(f"Total: {str(total)}")
print(f"Average Change: {int(average)}")
print(f"Greatest Increase in Profits: {str(max_date)} {int(maximum)}")
print(f"Lowest Increase in Profits: {str(min_date)} {int(minimum)}")

output_file = os.path.join("Financial Analysis.csv")

with open(output_file,"w") as text:

		text.write("Financial Analysis" + "\n")
		text.write("----------------------------------------------------------------" + "\n")
		text.write("Total Months: "+ str(total_months) + "\n")
		text.write("Total: " + str(total) + "\n")
		text.write("Average Change: " + str(average) + "\n")
		text.write("Greatest Increase in Profits: " + str(max_date) + "     $" + str(maximum) + "\n")
		text.write("Greatest Decrease in Profits: " + str(min_date) + "     $" + str(minimum))