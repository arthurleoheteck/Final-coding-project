"""
This is a Python script that computes the difference in cash on hand between days if the current day's value is lower than the previous day's, 
based on data from a "Cash on Hand" .csv file. The result is appended to a "summary_report.txt" file and printed to the console. 
The coh_function calculates the cash deficit using a single argument forex and formats the result as a string.
"""



#Cash-On-Hand csv: The program will compute the difference in Cash-on-Hand if the current day is lower than the previous day.
from pathlib import Path
import csv
# csv file and path
fp = Path.cwd()/"csv_reports/Cash on Hand.csv"
fp_report = Path.cwd()/"summary_report.txt"

def coh_function(forex):

    # programme will read the csv file to append profit and quantity from the csv.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        # skip header of the table first row
        next(reader) 

        # creates 3 empty lists to store profit and quantity by each cluster
        # empty list 'day' to store all the days
        # empty list 'cash on hand' to store all the profit
        # empty list day_deficit stored
        # empty list coh_deficit stored
        # programme will count to the total record 
        # txt_return to return the outcome of the string
        day = [] 
        coh = []
        day_deficit = [] 
        coh_deficit = []
        count       = 0
        txt_return  = ""
        
        # append profit and quantity as a list back to each empty list
        for row in reader:
            
            #row[0] for column 0 day, row[1] for column 1 profit
            day.append(row[0])
            coh.append(float(row[1]))
            
            if count > 0:     
                # Previous day profit is greater than current. Programme will then calculate the profit deficit and store the day of the deficit in text file
                if coh[count-1] > coh[count] :
                       day_deficit.append(row[0])
                       coh_deficit.append( coh[count-1]  - float(row[1]))                        
            count = count + 1          

        file.close()

    deficit_count = len(day_deficit)
    if deficit_count == 0 :
        txt_return = "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUSE DAY\n"
        
    else:
        i = 0
        while i < deficit_count: 
            txt_return = txt_return + "[CASH DEFICIT] DAY {:.1f}, AMOUNT: USD{:.0f}\n".format( int(day_deficit[i]), coh_deficit[i] * forex)
            i = i + 1
     
    print(txt_return)
    #programme will then append the final results to the summary_report.txt
    with open(fp_report,'a') as fileReport:
        fileReport.write(txt_return )
        fileReport.close()     
   
#modular for  individual coding and testing
#coh_function(1)

