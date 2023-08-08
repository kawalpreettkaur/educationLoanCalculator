import math

class EducationLoanCalculator:
    def __init__(self):
        self.private_banks = ["HDFC Bank", "ICICI Bank", "Axis Bank", "Kotak Mahindra Bank", "Indusland Bank",
                              "Yes Bank", "IDFC FIRST Bank", "Federal Bank", "RBL Bank", "Bandhan Bank"]
        self.govt_banks = ["State Bank of India (SBI)", "Punjab National Bank (PNB)", "Bank of Baroda (BOB)",
                           "Bank of India (BOI)", "Canara Bank", "Union Bank of India", "Indian Bank",
                           "Central Bank of India", "Bank of Maharashtra", "UCO Bank", "Punjab & Sind Bank",
                           "Indian Overseas Bank"]

    def format_inr(self, amount):
        return "₹{:,.2f}".format(amount)

    def select_bank_type(self):
        # https://fsymbols.com/generators/carty/
        ascii_art="""
╭━━━╮╱╭╮╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱  ╭╮╱╱╱╱╱╱╱╱╱╱╱╱  ╭━━━╮╱╱╭╮╱╱╱╱╱╱╭╮╱╱╱╭╮
┃╭━━╯╱┃┃╱╱╱╱╱╱╱╭╯╰╮╱╱╱╱╱╱╱  ┃┃╱╱╱╱╱╱╱╱╱╱╱╱  ┃╭━╮┃╱╱┃┃╱╱╱╱╱╱┃┃╱╱╭╯╰╮
┃╰━━┳━╯┣╮╭┳━━┳━┻╮╭╋┳━━┳━╮╱  ┃┃╱╱╭━━┳━━┳━╮╱  ┃┃╱╰╋━━┫┃╭━━┳╮╭┫┃╭━┻╮╭╋━━┳━╮
┃╭━━┫╭╮┃┃┃┃╭━┫╭╮┃┃┣┫╭╮┃╭╮╮  ┃┃╱╭┫╭╮┃╭╮┃╭╮╮  ┃┃╱╭┫╭╮┃┃┃╭━┫┃┃┃┃┃╭╮┃┃┃╭╮┃╭╯
┃╰━━┫╰╯┃╰╯┃╰━┫╭╮┃╰┫┃╰╯┃┃┃┃  ┃╰━╯┃╰╯┃╭╮┃┃┃┃  ┃╰━╯┃╭╮┃╰┫╰━┫╰╯┃╰┫╭╮┃╰┫╰╯┃┃
╰━━━┻━━┻━━┻━━┻╯╰┻━┻┻━━┻╯╰╯  ╰━━━┻━━┻╯╰┻╯╰╯  ╰━━━┻╯╰┻━┻━━┻━━┻━┻╯╰┻━┻━━┻╯   
\t\t\t\t\t[ Education Loan Calculator ]
"""
        print(ascii_art)
        print("Select a type of Bank Loan:")
        print("1. Govt. Bank Loan")
        print("2. Private Bank Loan")
        bank_type = input("\nEnter your choice (1/2): ")

        if bank_type == "1":
            self.banks = self.govt_banks
            print("\nAvailable Govt. Banks:")
        elif bank_type == "2":
            self.banks = self.private_banks
            print("\nAvailable Private Banks:")
        else:
            print("Invalid choice.")
            exit()

    def select_bank(self):
        for i in range(len(self.banks)):
            print(str(i + 1) + ". " + self.banks[i])
        selected_bank = int(input("\nSelect a bank (1/2...11/12): "))

        if selected_bank > len(self.banks):
            print("Invalid bank selection.")
            exit()

        self.selected_bank_name = self.banks[selected_bank - 1]

    def get_loan_details(self):
        print("\n----------------------------------------")
        print("Enter the Required Mortgage Values:")
        print("----------------------------------------")
        self.loan_amount = float(input("Total Education loan amount (INR): "))
        self.interest_rate = float(input("Rate of interest (p.a.) in %: "))
        self.loan_term_years = int(input("Loan tenure (in years): "))

    def calculate_loan(self):
        monthly_interest_rate = (self.interest_rate / 100) / 12
        total_payments = self.loan_term_years * 12

        self.monthly_payment = (self.loan_amount * monthly_interest_rate) / (1 - math.pow(1 + monthly_interest_rate, -total_payments))
        self.total_payment_with_interest = self.monthly_payment * total_payments
        self.total_interest_paid = self.total_payment_with_interest - self.loan_amount

    def display_loan_details(self):
        print("\n----------------------------")
        print("Education Loan Details")
        print("----------------------------")
        print("Bank: ", self.selected_bank_name)
        print("Loan Amount: ", self.format_inr(self.loan_amount))
        print("Interest Rate: ", self.interest_rate, "%")
        print("Loan Term: ", self.loan_term_years, " years")
        print("Monthly EMI: ", self.format_inr(self.monthly_payment))
        print("Total Interest Paid: ", self.format_inr(self.total_interest_paid))
        print("Total Payable with Interest: ", self.format_inr(self.total_payment_with_interest))

    def run(self):
        self.select_bank_type()
        self.select_bank()
        self.get_loan_details()
        self.calculate_loan()
        self.display_loan_details()

if __name__ == "__main__":
    calculator = EducationLoanCalculator()
    calculator.run()
