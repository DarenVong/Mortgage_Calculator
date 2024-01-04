from scripts.calculator import Calculator
from flask import Flask, render_template, request

# app.run is going to run everytime you run the page. when the page loads it will run the template and run the 
app = Flask(__name__) 

# whenever this decorator gets called it will run the fuction
# get is getting information 
# post is posting the information
@app.route('/', methods=['GET', 'POST'] )
def index():
    if request.method=='POST':
        mortgage_input = request.form.get('mortgage')
        interest_rate_input = request.form.get('interest_rate')
        loan_term_input = request.form.get('loan_term')
        print(f'{mortgage_input},{interest_rate_input},{loan_term_input}')
        input_calculations = Calculator(loan_amount=float(mortgage_input),interest_rate=float(interest_rate_input),loan_term=float(loan_term_input))
        monthly_payments = int(input_calculations.calculate_monthly_payments()) 
        return render_template('index.html',monthly_payments=monthly_payments)
    return render_template('index.html')
                    
app.run(debug=True) 








# users_input = input("Hello, How can i assist you today? {}")
#  while True:
    # graphic.menu()
    # not sure if i want to add an input wether to start putting in the numbers or just make a start int
    # start_calculations = int(input())