import coh, overheads, profit_loss

#import the collaborate code and modulizrized python files
# each api.py, coh.py, overheads.py, profit_loss.py can be run separately for each member to contribute to the project

def main():

    # updated exercise set forex  = 1, USD 
    forex = 1  

    overheads.overhead_function(forex)
    coh.coh_function(forex)
    profit_loss.profitloss_function(forex)

    return

#execute the main functions
main()