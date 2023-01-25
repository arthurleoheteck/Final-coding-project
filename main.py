import coh, overheads, profit_loss

#import the collaborate code and modulizrized python files
# each api.py, coh.py, overheads.py, profit_loss.py can be run separately for each member to contribute to the project
"""
This code imports the modules coh, overheads, and profit_loss and runs their respective functions, coh_function, overhead_function,
 and profitloss_function, with the variable forex passed as an argument. The variable forex is set to 1 and represents the exchange 
 rate for USD. Each module, coh.py, overheads.py, and profit_loss.py can be run separately by members contributing to the project. 
 The main() function is executed to run the overall program.
"""
def main():

    # updated exercise set forex  = 1, USD 
    forex = 1  

    overheads.overhead_function(forex)
    coh.coh_function(forex)
    profit_loss.profitloss_function(forex)

    return

#execute the main functions
main()
