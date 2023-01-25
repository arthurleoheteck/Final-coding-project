#Overheads csv: The program will find the highest overhead category.
from pathlib import Path
import csv
# csv file and path
fp = Path.cwd()/"csv_reports/Overhead.csv"
fp_report = Path.cwd()/"summary_report.txt"

def overhead_function(forex):

    # read the csv file to append profit and quantity from the csv.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        max_category = ""
        max_overheads = 0.00

        # read each record and store the only highest overheads and category
        for row in reader:            
        #compare and keep the maximum category and overheads
        #row[0] for column 0 category, row[1] for column 1 overheads
            if  float(row[1]) > max_overheads:
                max_category    = row[0]
                max_overheads   = float(row[1])
        
        file.close()
        
            
    txt_return = "[HIGHEST OVERHEADS] {}: {:.2f}%\n".format(max_category.upper(), max_overheads)
    print(txt_return)
    
    
    #append the result to the summary_report.txt
    with fp_report.open(mode="w", encoding="UTF-8", newline="") as fileReport:
            fileReport.write(txt_return)
            fileReport.close()   

    
# for individual coding and testing     
#overhead_function(1)
