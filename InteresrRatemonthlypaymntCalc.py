def main():
    print("This is a montly payment loan calculator")
    print("")#for space
    
    
    principal = float(input("enter the loan amount: \n"))
    apr = float(input("input the annual interest rate: \n"))
    years = int(input("input amount of years : \n"))
    
    monthlyInterestRate = apr / 1200
    amount_Of_months = years*12
    monthlypayment = principal * monthlyInterestRate /(1-(1+monthlyInterestRate)**(-amount_Of_months))

    print("The montly payment for this loan is : %.2f " % monthlypayment)
    
main()