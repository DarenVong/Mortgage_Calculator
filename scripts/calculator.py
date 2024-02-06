class Calculator:
    
    def __init__(self,loan_amount,interest_rate,loan_term):
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.loan_term = loan_term

        

    def calculate_monthly_payments(self):
        #calculates payment based on mortgage and interest rates...
        monthly_interest_rate = self.interest_rate / 100 / 12
        loan_term = self.loan_term * 12
        numerator = monthly_interest_rate * (1 + monthly_interest_rate)**loan_term 
        denominator = (1 + monthly_interest_rate)**loan_term - 1 
        monthly_payment = self.loan_amount * numerator / denominator
        return monthly_payment


    





