# -Main income-
# Rent
# Laundromat
# Storage

# -Expenses-
# Tax
# Insurance
# Utilities
#   Electric
#   Water
#   Sewer
#   Gas
# HOA
# Lawn/snow
# Vacancy - percentage of the rental income, about %5
# Repairs
# Cap Ex - big items
# Property Management - typically 10% of the rent
# Mortgage if not paid in cash

# -Cash Flow-
# Income - Expenses

# -Cash on Cash Return on Investment-
# Down Payment - 40,000
# Closing costs - 3,000
# Rehab budged (repair) - 7,000
# Misc other - 0
# Total investment: - 50,000

#Total montly cashflow x months = annual cashflow
#Annual cashflow/total investment = Cash on Cash RoI


class ROI_calculator():
    def __init__(self):
        self.total_income = 0
        self.total_expenses = 0
        self.cash_flow = 0

    def Income(self):
        while True:
            user_string = input("Enter your total income or input each source of income. Type 'done' when finished.").lower().strip()
            if user_string == "done":
                return
            try:
                user_income = int(user_string)
                self.total_income += user_income
            except ValueError:
                print("Invalid input, please try again.")
                        
        #asking total income
        #adding it together
    def Expenses(self):
        print("Enter the total amount of expenses you are working with.")
        while True:
            user_string = input("Please enter your expenses, either one expense at a time or the total. Type 'done' when fininshed.").lower().strip()
            if user_string == "done":
                return
            try:
                user_expenses = int(user_string)
                self.total_expenses += user_expenses
            except ValueError:
                print("Invalid input, please try again.")
        #Are they paying in cash or taking a mortgage
        #Ask for total amount of expenses
        
    def Cash_Flow(self):
        while True:
            self.cash_flow = self.total_income - self.total_expenses
            if self.cash_flow < 0:
                print(f"Your expenses exceed your income! {self.cash_flow} is your current expense. Enter 'done' if you'd still like to continue. Enter 'income' or 'expenses' to return to either of those steps. Or 'reset' to start over.") 
            else:
                print(f"Your cash flow totals to {self.cash_flow}. If you'd like to continue, enter 'done'. Or else enter 'income' or 'expenses' to head back to either steps to adjust them. If you'd like to reset both, enter 'reset'.")
            flow_choice = input("Enter your choice: ").lower().strip()
            if flow_choice == "income":
                self.Income()
            elif flow_choice == "expenses":
                self.Expenses()
            elif flow_choice == "reset":
                self.total_income = 0
                self.total_expenses = 0
                self.Income()
                self.Expenses()
            elif flow_choice == "done":
                return
            else:
                print("Invalid input, please try again.")
            #income - Expenses
            #if expenses exceed income tell user
    def RoI(self):
        user_string = input("Please enter your total investment costs. (Down payment/closing costs/repairs/etc). ")
        if user_string == "done":
            return
        try:
            investment_amount = int(user_string)
            self.total_expenses += investment_amount
        except ValueError:
            print("Invalid input, please try again.")
        annual_cashflow = self.cash_flow * 12
        RoI = annual_cashflow / investment_amount * 100
        print(f"{RoI}%")
        return RoI
        # Get total investment amount
        # Total monthly cashflow x months = annual cashflow
        # Annual cashflow/totalinvestment = RoI

    def run(self):
        self.Income()
        self.Expenses()
        self.Cash_Flow()
        self.RoI()


cal = ROI_calculator()
cal.run()