#First import the os ans csv module
import os
import csv

#Reading CSV files
election_data_csv = os.path.join("Resources", "election_data.csv")

#Set variable
total_ballots = 0
candidates = []
num_ballots = []
percent_ballots =[]


#Open csv file
with open(election_data_csv) as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile)

    #Skip header row 
    header = next(csv_reader)

    #Loop and extract total ballot amount, number of ballots and candidates
    for row in csv_reader:

        total_ballots += 1 

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_ballots.append(1)
        else:
            index = candidates.index(row[2])
            num_ballots[index] += 1
    
    #Loop percentage
    for votes in num_ballots:
        percentage = (votes/total_ballots) * 100
        percentage = "%.3f%%" % percentage
        percent_ballots.append(percentage)

    #Get the winner
    winner = max(num_ballots)
    index = num_ballots.index(winner)
    winner_candidate = candidates[index]
    
    #Print all info needed
    print("Election Results")
    print("-----------------------------------------")
    print(f"Total: ${total_ballots}")
    print("-----------------------------------------")
    for x in range(len(candidates)):
        print(f"{candidates[x]}: {(percent_ballots[x])} ({(num_ballots[x])})")
    print("-----------------------------------------")
    print(f"Winner: {winner_candidate}")
    print("-----------------------------------------")


    #Export all info needed to text file
    text_path = os.path.join('analysis', 'Export_Election_Results.txt')
    with open(text_path,"w") as text_file:
        text_file.write("Financial Analysis" + "\n")
        text_file.write("-----------------------------------------" + "\n")
        text_file.write(f"Total: ${total_ballots}"+ "\n")
        text_file.write("-----------------------------------------" + "\n")
        for x in range(len(candidates)):
            text_file.write(f"{candidates[x]}: {(percent_ballots[x])} ({(num_ballots[x])})"+ "\n")
        text_file.write("-----------------------------------------" + "\n")
        text_file.write(f"Winner: {winner_candidate}"+ "\n")
        text_file.write("-----------------------------------------" + "\n")


    text_file.close()