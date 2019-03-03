import os
import csv
import operator

#set path for budget file
electionDataCSV = os.path.join("Resources", "election_data1.csv")
electionOutput = os.path.join("Resources", "election_output.txt")

# read CSV file
with open(electionDataCSV,'r', newline='') as electionFile:

    electionReader = csv.reader(electionFile, delimiter=',')
    
    #skip header
    electionHeader = next(electionReader,None)
    
    #initalize variables
    totalVotes = 0
    totalCanditates = 0
    candidateDict = {}
        #loop through rows and calculate values
    for row in electionReader:
        totalVotes += 1
        candidateName = row[2]
        if candidateName in candidateDict:
            candidateDict[candidateName] += 1
        else:
            candidateDict[candidateName] = 1

    
    winner = max(candidateDict.items(), key=operator.itemgetter(1))[0]

    # print output
    print("Election Results")
    print("--------------------------")
    print(f"Total votes: {totalVotes}")
    print("--------------------------")
    output_var= "Election Results \n" + "-------------------------- \n" + "Total votes: " + str(totalVotes) + "\n"
    for row in candidateDict:
        candidatePercent = str("{0:.3f}".format(round((candidateDict[row] / totalVotes) * 100, 3))) + "%"
        CandidateCount = "(" + str(candidateDict[row]) + ")"
        print(row, ": " ,  candidatePercent, CandidateCount)
        output_var = output_var + row + ": " + candidatePercent +  CandidateCount + "\n"

    print("--------------------------")
    print("winner: ", winner)
    print("--------------------------")
    output_var = output_var + "--------------------------\n" + "winner: " +  str(winner) + "\n" +  "--------------------------"

with open(electionOutput,'w', newline='') as electionOut:
    electionOut.write(output_var)

