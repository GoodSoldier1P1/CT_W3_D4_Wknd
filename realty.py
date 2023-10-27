class Investmentreturn():
    def __init__(self, income, expenses, coc) -> None:
        self.income = income
        self.expenses = expenses
        self.coc = coc


    def anuals(self):

        c_flow = self.income - self.expenses    # cash flow
        print(c_flow)
        print(self.income)
        print(self.expenses)
        a_cf = c_flow * 12          # anual cash flow

        roi = a_cf / self.coc 
        percent = roi * float(100)

        print(f"Your ROI is {percent}%")
    
    def runner(self):
        while True:
            options = input("Would you like to know your ROI with the numbers entered? (yes or no)")
            if (options == 'no'):
                break
            else:
                self.anuals()
                break



soldierRealty = Investmentreturn(2000,1610,50000)
soldierRealty.runner()

# print(soldierRealty.income)
# print(soldierRealty.expenses)
# print(soldierRealty.coc)