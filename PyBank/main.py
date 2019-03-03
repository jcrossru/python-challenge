import os
import csv

#set path for budget file
budgetDataCSV = os.path.join("Resources", "budget_data.csv")
budgetOutput = os.path.join("Resources", "budget_output.txt")

# read CSV file
with open(budgetDataCSV,'r', newline='') as budgetfile:

    budgetreader = csv.reader(budgetfile, delimiter=',')
    
    #skip header
    budgetHeader = next(budgetreader,None)
    
    #initalize variables
    rowCounter = 0
    netProfitLoss = 0
    averageChange = 0
    prevAmount=0
    averageProfitLoss = 0
    firstRowFlag = "Y"
    greatestIncreaseProfit = 0
    greatestIncreaseMonth = "None"
    greatestDecreaseLoss = 0
    greatestDecreaseMonth = "None"
    profitLoss = 0

    #loop through rows and calculate values
    for row in budgetreader:
        rowCounter += 1
        netProfitLoss += int(row[1])
        profitLoss =  int(row[1]) - prevAmount
        if firstRowFlag == "Y":
            firstRowFlag = "N"
        else:
            averageProfitLoss += profitLoss

        if greatestIncreaseProfit < profitLoss:
            greatestIncreaseProfit = profitLoss
            greatestIncreaseMonth = row[0]   

        if greatestDecreaseLoss > profitLoss:
            greatestDecreaseLoss = profitLoss
            greatestDecreaseMonth = row[0]   

        prevAmount = int(row[1])

    averageChange = round(averageProfitLoss / (rowCounter - 1), 2)

    # print output
    print("Financial Analysis")
    print("--------------------------")
    print(f"Total months: {rowCounter}")
    print(f"Total: ${netProfitLoss}")
    print(f"Average  Change: ${averageChange}")
    print(f"Greatest Increase in Profits: {greatestIncreaseMonth} $({greatestIncreaseProfit})")
    print(f"Greatest Decrease in Profits: {greatestDecreaseMonth} $({greatestDecreaseLoss})")

    output_var= "Financial Analysis \n" + "-------------------------- \n" + "Total months: " + str(rowCounter)  + "\nTotal: $" +  str(netProfitLoss) + "\nAverage  Change: $" + str(averageChange) + "\nGreatest Increase in Profits: " + greatestIncreaseMonth + " $" + str(greatestIncreaseProfit) + "\nGreatest Decrease in Profits: " + greatestDecreaseMonth + " $" + str(greatestDecreaseLoss)

with open(budgetOutput,'w', newline='') as budgetOut:
    budgetOut.write(output_var)

