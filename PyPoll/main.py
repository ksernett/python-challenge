import os
import csv

#link to [election_data.csv]
election_csv = os.path.join("Resources", "election_data.csv")
#read csv file
with open(election_csv, 'r') as data_file:
    csvreader = csv.reader(data_file, delimiter=',')
    next(csvreader)
#create variables
    total_votes= 0
    charles_votes = 0
    charles_percent = 0.0
    diana_votes = 0
    diana_percent = 0.0
    raymon_votes = 0
    raymon_percent = 0.0
    election_runoff = []
    for row in csvreader:
    #* The total number of votes cast
        total_votes = total_votes +1
        #total votes and percentage for Charles
        if row[2] == "Charles Casper Stockham":
            charles_votes = charles_votes +1
        charles_percent = (charles_votes/total_votes)*100
        #total votes and percentage for Diana
        if row[2] == "Diana DeGette":
            diana_votes = diana_votes +1
        diana_percent = (diana_votes/total_votes)*100
        #total votes and percentage for Raymon
        if row[2] == "Raymon Anthony Doane":
            raymon_votes = raymon_votes +1
        raymon_percent = (raymon_votes/total_votes)*100

#* The winner of the election based on popular vote.
election_runoff.append(int(charles_votes))
election_runoff.append(int(diana_votes))
election_runoff.append(int(raymon_votes))
winner_votes = max(election_runoff)
if winner_votes == int(charles_votes):
        winner = "Charles Casper Stockham"
elif winner_votes == int(diana_votes):
        winner = "Diana DeGette"
else:
        winner = "Anthony Doane"



#print analysis to the terminal

print('Election Results \n ---------------------------- \n Total Votes: {} \n ------------------------- \n Charles Casper Stockham: {}% ({}) \n Diana DeGette: {}% ({}) \n Raymond Anthony Doane: {}% ({}) \n ------------------------- \n Winner: {} \n -------------------------'.format(total_votes, charles_percent, charles_votes, diana_percent, diana_votes, raymon_percent, raymon_votes, winner))


#export a text file with the results
f = open('analysis/pypoll_results.txt', 'a')
f.write('Election Results \n ---------------------------- \n Total Votes: {} \n ------------------------- \n Charles Casper Stockham: {}% ({}) \n Diana DeGette: {}% ({}) \n Raymond Anthony Doane: {}% ({}) \n ------------------------- \n Winner: {} \n -------------------------'.format(total_votes, charles_percent, charles_votes, diana_percent, diana_votes, raymon_percent, raymon_votes, winner))
f.close()