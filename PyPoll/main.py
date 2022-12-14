# import dependencies
import os
import csv

#path
poll_path = os.path.join('PyPoll/Resources/election_data.csv')
output = os.path.join("PyPoll/Analysis/PyPoll_Analysis.txt")

#variables
votes = []
candidates = []
Charles_Stockham = []
Diana_DeGette = []
Raymon_Doane = []
Stockham_votes = 0
DeGette_votes = 0
Doane_votes = 0

#open and read csv
with open(poll_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #loop to store data in votes and candidates
    for row in csvreader:
        votes.append(int(row[0]))
        candidates.append(row[2])

    #total vote count    
    total_votes = (len(votes))

    #votes per candidate
    for candidate in candidates:
        if candidate == "Charles Casper Stockham":
            Charles_Stockham.append(candidates)
            Stockham_votes = len(Charles_Stockham)

        elif candidate == "Diana DeGette":
            Diana_DeGette.append(candidates)
            DeGette_votes = len(Diana_DeGette)

        else:
            Raymon_Doane.append(candidates)
            Doane_votes = len(Raymon_Doane)

        #% of votes per candidate
        Stockham_percent = round(((Stockham_votes / total_votes) * 100), 3)
        DeGette_percent = round(((DeGette_votes / total_votes) * 100), 3)
        Doane_percent =  round(((Doane_votes / total_votes) * 100), 3)

        #Winner
        if Stockham_percent > max(DeGette_percent, Doane_percent):
            winner = "Charles Casper Stockham"
        elif DeGette_percent > max(Stockham_percent, Doane_percent):
            winner = "Diana DeGette"
        else:
            winner = "Raymon Anthony Doane"

    #Print Results
    print("Election Results")
    print("\n-----------------------\n")
    print(f"Total Votes: {total_votes}")
    print("\n-----------------------\n")
    print(f"Charles Casper Stockham: {Stockham_percent}% ({Stockham_votes})")
    print(f"Diana DeGette Stockham: {DeGette_percent}% ({DeGette_votes})")
    print(f"Raymon Anthony Doane: {Doane_percent}% ({Doane_votes})")
    print("\n-----------------------\n")
    print(f"Winner: {winner}")
    print("\n-----------------------\n")

  


    
    
        
