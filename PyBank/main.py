#First import the os ans csv module
import os
import csv

#Reading CSV files
budget_data_csv = os.path.join("Resources", "budget_data.csv")


#Open csv file
with open(budget_data_csv) as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile)

    #Skip header row 
    header = next(csv_reader)

    #Store as list
    data_list = list(csv_reader)

    #Extract months
    months = [row[0] for row in data_list]

    #Calculate the total number of months with lenght of the months
    total_months = len(set(months))

    #Extract amounts from profit and losses
    amount = [int(row[1]) for row in data_list]

    #Calculate the changes in amount of the profit and losses over the total period
    changes = [amount[x] - amount[x - 1] for x in range(1, len(amount))]

    #Calculate the average of the changes
    average_change = sum(changes) / len(changes)

    #Get greatest increase 
    greatest_increase_amount = max(changes)
    #Get date for greatest increase
    increase_date_index = changes.index(greatest_increase_amount)
    greatest_date = months[increase_date_index + 1]

    #Get greatest decrease 
    greatest_decrease_amount = min(changes)
    #Get date for greatest decrease
    decrease_date_index = changes.index(greatest_decrease_amount)
    lowest_date = months[decrease_date_index + 1]
    

    #Print all info needed
    print("Financial Analysis")
    print("-----------------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${sum(amount)}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_date} (${greatest_increase_amount})")
    print(f"Greatest Decrease in Profits: {lowest_date} (${greatest_decrease_amount})")

    #Export all info needed to text file
    file = open("export.txt","w")
    file.write("Financial Analysis" + "\n")
    file.write("-----------------------------------------" + "\n")
    file.write(f"Total Months: {total_months}" + "\n")
    file.write(f"Total: ${sum(amount)}" + "\n")
    file.write(f"Average Change: ${average_change:.2f}" + "\n")
    file.write(f"Greatest Increase in Profits: {greatest_date} (${greatest_increase_amount})" + "\n")
    file.write(f"Greatest Decrease in Profits: {lowest_date} (${greatest_decrease_amount})" + "\n")
    file.close()


