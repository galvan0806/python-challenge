#First import the os ans csv module
import os
import csv

#Reading CSV files
election_data_csv = os.path.join("Resources", "election_data.csv")

#Open csv file
with open(election_data_csv) as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile)

    #Skip header row 
    header = next(csv_reader)

    #Store as list
    data_list = list(csv_reader)