import math


def format_inr(amount):
    return "₹{:,.2f}".format(amount)

def main():

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
  # print("\t\t\t\t\t\t"+"Education Loan Calculator\n")
  private_banks = ["HDFC Bank","ICICI Bank","Axis Bank","Kotak Mahindra Bank","Indusland Bank","Yes Bank","IDFC FIRST Bank","Federal Bank","RBL Bank","Bandhan Bank"]
  govt_banks = ["State Bank of India (SBI)","Punjab National Bank (PNB)","Bank of Baroda (BOB)","Bank of India (BOI)","Canara Bank","Union Bank of India","Indian Bank","Central Bank of India","Bank of Maharashtra",
"UCO Bank","Punjab & Sind Bank","Indian Overseas Bank"]

  print("Select a type of Bank Loan:")
  print("1. Govt. Bank Loan")
  print("2. Private Bank Loan")
  bank_type = input("\nEnter your choice (1/2): ")

  if bank_type == "1":
    banks = govt_banks
    print("\nAvailable Govt. Banks:")
  elif bank_type == "2":
    banks = private_banks
    print("\nAvailable Private Banks:")
  else:
    print("Invalid choice.")
    exit()

  
  for i in range(len(banks)):
    print(str(i+1)+". "+banks[i])
  selected_bank = int(input("\nSelect a bank(1/2...11/12): "))

  if selected_bank > len(banks):
      print("Invalid bank selection.")
      exit()

  print("\n----------------------------------------")
  print("Enter the Required Mortgage Values:")
  print("----------------------------------------")
  loan_amount = float(input("Total Education loan amount (INR): "))
  interest_rate = float(input("Rate of interest (p.a.) in %: "))
  loan_term_years = int(input("Loan tenure (in years): "))

  monthly_interest_rate = (interest_rate / 100) / 12
  total_payments = loan_term_years * 12

  monthly_payment = (loan_amount * monthly_interest_rate) / (1 - math.pow(1 + monthly_interest_rate, -total_payments))
  total_payment_with_interest = monthly_payment * total_payments
  total_interest_paid = total_payment_with_interest - loan_amount
  print("\n----------------------------")
  print("Education Loan Details")
  print("----------------------------")
  print("Bank: ", banks[selected_bank])
  print("Loan Amount: ", format_inr(loan_amount))
  print("Interest Rate: ", interest_rate, "%")
  print("Loan Term: ", loan_term_years, " years")
  print("Monthly EMI: ", format_inr(monthly_payment))
  print("Total Interest Paid: ", format_inr(total_interest_paid))
  print("Total Payable with Interest: ", format_inr(total_payment_with_interest))

if __name__ == "__main__":
    main()
