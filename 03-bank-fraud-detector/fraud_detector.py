# Bank Fraud Detection Simulator - flags transactions as Safe, Medium Risk, or High Risk

print("===================================")
print(" BANK FRAUD DETECTION SYSTEM")
print("===================================")

transaction_amount = float(input("Transaction amount ($): "))
failed_pin_attempts = int(input("Failed PIN attempts: "))
card_present = input("Card present? (yes/no): ").lower()

print()
print("----- FRAUD REPORT -----")

if transaction_amount > 5000 or failed_pin_attempts >= 3:
    print("Risk Level: HIGH")
    print("Recommendation: Transaction blocked.")

elif card_present == "no":
    print("Risk Level: MEDIUM")
    print("Recommendation: Manual verification required.")

else:
    print("Risk Level: SAFE")
    print("Recommendation: Transaction approved.")