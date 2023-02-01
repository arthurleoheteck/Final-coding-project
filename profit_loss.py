
""" The profitloss_function takes a forex parameter and computes the difference between the net profit of consecutive days.
If the net profit on a certain day is lower than the previous day, 
the day and the difference in profit are stored. The result is printed and appended to the summary_report.txt file."""

#Profit & Loss csv : The program will compute the difference in the net profit column if net profit on the current day is lower than the previous day.

#Cash-On-Hand csv: The program will compute the difference in Cash-on-Hand if the current day is lower than the previous day.
from pathlib import Path
import csv
# csv file and path
fp = Path.cwd()/"csv_reports/Profit & Loss.csv"
fp_report = Path.cwd()/"summary_report.txt"

def profitloss_function(forex):

    # read the csv file to append profit and quantity from the csv.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        # create 3 empty lists to store profit and quantity by each cluster
        # day to store all the days
        # coh to store all the profit
        # day_deficit stored
        # coh_deficit stored
        # count to the total record 
        # txt_return to return the outcome of the string
        day             = [] 
        profit          = []
        day_deficit     = [] 
        profit_deficit  = []
        count           = 0
        txt_return      = ""
        
        # append profit and quantity as a list back to each empty list
        for row in reader:
            
            #row[0] for column 0 day, row[4] for column 4 profit
            day.append(row[0])
            profit.append(int(row[4]))
            
            if count > 0:                 
                # if Previous day profit is greater than current. Then calculate the profit deficit and store the day of the deficit
                if profit[count-1] > profit[count] :
                       day_deficit.append(row[0])
                       profit_deficit.append(profit[count-1] - int(row[4])) 
                       
            count = count + 1          
        
        file.close()
                    
    deficit_count = len(day_deficit)
    #if count is not 0 the code uses a while loop to iterate "deficit_count" number of times and concatenates a string "txt_return" to each iteration
    if deficit_count == 0 :    
        txt_return = "[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"
    else:
        i = 0
        while i < deficit_count: 
            txt_return = txt_return + "[PROFIT DEFICIT] DAY {:.1f}, AMOUNT: USD{:.0f}\n".format(int(day_deficit[i]), profit_deficit[i] * forex)            
            i = i + 1
    
    print(txt_return)        
    
    #append the result to the summary_report.txt
    with open(fp_report,'a') as fileReport:
        fileReport.write(txt_return)
        fileReport.close()     

    return 

# modular for  individual coding and testing
# profitloss_function(1)
