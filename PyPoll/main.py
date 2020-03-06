import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
election_csv=os.path.join(dir_path,'..', 'PyPoll', 'election_data.csv')

votes=0
khan_votes=0
correy_votes=0
li_votes=0
otooley_votes=0

with open(election_csv) as csvfile:
    election_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(election_reader)

    
    for row in election_reader:
        votes = votes+1

        if row[2] == "Khan":
            khan_votes=khan_votes+1

        if row[2] == "Correy":
            correy_votes=correy_votes+1

        if row[2] == "Li":
            li_votes=li_votes+1
        
        if row[2] == "O'Tooley":
            otooley_votes=otooley_votes+1

    khan_percent="{0:.2%}".format(khan_votes/votes)
    correy_percent="{0:.2%}".format(correy_votes/votes)
    li_percent="{0:.2%}".format(li_votes/votes)
    otooley_percent="{0:.2%}".format(otooley_votes/votes)

    if khan_votes > correy_votes and khan_votes > li_votes and khan_votes > otooley_votes:
        winner="Khan"
    if correy_votes > khan_votes and correy_votes > li_votes and correy_votes > otooley_votes:
        winner="Correy"
    if li_votes > khan_votes and li_votes > correy_votes and li_votes > otooley_votes:
        winner="Li"
    if otooley_votes > khan_votes and otooley_votes > li_votes and otooley_votes > correy_votes:
        winner="Correy"

    print("ELection Results")
    print("----------------------------")
    print("Total Votes: ",votes)
    print("----------------------------")  
    print("Khan: ",khan_percent, "(",khan_votes,")")  
    print("Correy: ",correy_percent, "(",correy_votes,")")
    print("Li: ", li_percent, "(",li_votes,")")  
    print("O'Tooley: ", otooley_percent, "(",otooley_votes,")")  
    print("----------------------------")    
    print("Winner: ",winner)
    print("----------------------------")  

file = open('election_data_export.txt', 'w')
file.write("ELection Results\n")
file.write("----------------------------\n")
file.write("Total Votes: {0}\n".format(votes))
file.write("----------------------------\n")
file.write("Khan: {0} ({1})\n".format(khan_percent, khan_votes))
file.write("Correy: {0} ({1})\n".format(correy_percent, correy_votes))
file.write("Li: {0} ({1})\n".format(li_percent, li_votes))
file.write("O'Tooley: {0} ({1})\n".format(otooley_percent, otooley_votes))
file.write("----------------------------\n")
file.write("Winner: {0}\n".format(winner))
file.write("----------------------------\n")
file.close()