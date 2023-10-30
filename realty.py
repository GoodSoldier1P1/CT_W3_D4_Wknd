class Investmentreturn():
    def __init__(self) -> None:
        self.income = 0
        self.expenses = 0
        self.coc = 0


    def anuals(self):
        income = input("What is your monthly Income on the property? ")
        expenses = input("What are your monthly expenses on the property? ")
        self.coc = int(income) - int(expenses)    # cash flow
        
        print(self.coc)
        a_cf = int(self.coc) * 12          # anual cash flow

        total_invest = input("What is your total investment? (Down Payment, Closing Cost, etc)")
        roi = a_cf / int(total_invest)
        percent = roi * float(100)

        print(f"Your ROI is {percent}%")
    
    def runner(self):
        while True:
            options = input("Would you like to know what your ROI is in just 3 easy steps? (yes or no) ")
            if (options == 'no'):
                break
            else:
                self.anuals()
                break



soldierRealty = Investmentreturn()
soldierRealty.runner()



### For this Example
# Monthly Income == 2,000
# Monthly Expenses == 1,610
# Total Investment == 50,000