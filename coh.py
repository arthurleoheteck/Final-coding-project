#Cash-On-Hand csv: The program will compute the difference in Cash-on-Hand if the current day is lower than the previous day.
from pathlib import Path
import csv
# csv file and path
fp = Path.cwd()/"csv_reports/Cash on Hand.csv"
fp_report = Path.cwd()/"summary_report.txt"

def coh_function(forex):

    # read the csv file to append profit and quantity from the csv.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        # skip header of the table first row
        next(reader) 

        # create 3 empty lists to store profit and quantity by each cluster
        # day to store all the days
        # coh to store all the profit
        # day_deficit stored
        # coh_deficit stored
        # count to the total record 
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
                # Previouse day profit is greater than current. Then calculate the profit deficit and store the day of the deficit
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
    #append the result to the summary_report.txt
    with open(fp_report,'a') as fileReport:
        fileReport.write(txt_return )
        fileReport.close()     
   
#modular for  individual coding and testing
#coh_function(1)

