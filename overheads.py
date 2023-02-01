
"""This program will find the highest overhead category in a CSV file named "Overhead.csv" located in the "csv_reports" directory.
The program reads the CSV file, compares the overhead values in each row, and stores the category with the highest overhead.
Output: The highest overhead category and its value are printed and saved in a text file.
"""

# Overheads csv: The program will find the highest overhead category.

from pathlib import Path
import csv
# This is the CSVv file and path.
fp = Path.cwd()/"csv_reports/Overhead.csv"
fp_report = Path.cwd()/"summary_report.txt"

def overhead_function(forex):

    # It will read the csv file to append the profit and quantity from the csv.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        max_category = ""
        max_overheads = 0.00

        # Reads each record and stores only the highest overheads and category.
        count = 0
        for row in reader: 
        
            # Checks whether the row is empty, if not, that row can be a new line.
            if not row:
                continue

            # Stores the first record as max catergory and max overheads.
            # Row[0] for colume 0 category, row[1] for column 1 overheads.
            if count == 0:
                max_category    = row[0]
                max_overheads   = float(row[1])
                count = count + 1
            
            # Compares and keeps the maximum category and overheads.
            if  float(row[1]) > max_overheads:
                max_category    = row[0]
                max_overheads   = float(row[1])

        file.close()
        
    txt_return = "[HIGHEST OVERHEADS] {}: {:.2f}%\n".format(max_category.upper(), max_overheads)
    print(txt_return)
    
    
    # Append the result to the summary_report.txt
    with fp_report.open(mode="w", encoding="UTF-8", newline="") as fileReport:
            fileReport.write(txt_return)
            fileReport.close()   

    
# For individual coding and testing.     
# overhead_function(1)
