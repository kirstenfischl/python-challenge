import csv

if __name__ == '__main__':
    with open('election_data.csv') as csvfile:
        py_poll_reader = csv.reader(csvfile, delimiter=',')
        votes = 0
        candidates = dict()

        for row in py_poll_reader:
            if row[0] != "Voter ID":
                votes += 1
                if row[2] in candidates:
                    candidates[row[2]] += 1
                else:
                    candidates[row[2]] = 1

    with open('PyPoll.txt', "w") as txtfile:
        winner = None
        print("Election Results")
        txtfile.write("Election Results\n")
        print("-------------------------")
        txtfile.write("-------------------------\n")
        print("Total Votes: {0}".format(votes))
        txtfile.write("Total Votes: {0}\n".format(votes))
        print("-------------------------")
        txtfile.write("-------------------------\n")
        for name in candidates:
            if winner is None:
                winner = name
            else:
                if candidates[name] > candidates[winner]:
                    winner = name
            percent = candidates[name]/votes*100
            print("{}: {:.3f}% ({})".format(name, percent, candidates[name]))
            txtfile.write("{}: {:.3f}% ({})\n".format(name, percent, candidates[name]))
        print("-------------------------")
        txtfile.write("-------------------------\n")
        print("Winner: {0}".format(winner))
        txtfile.write("Winner: {0}\n".format(winner))
        print("-------------------------")
        txtfile.write("-------------------------\n")
