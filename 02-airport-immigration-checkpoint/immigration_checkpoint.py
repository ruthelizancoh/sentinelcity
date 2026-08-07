# Airport Immigration Checkpoint - decides whether a traveller may enter the country

print("===================================")
print(" AIRPORT IMMIGRATION CHECKPOINT")
print("===================================")

passport_valid = input("Valid passport? (yes/no): ").lower()
has_visa = input("Has visa? (yes/no): ").lower()
traveller_age = int(input("Age: "))
is_returning_citizen = input("Returning citizen? (yes/no): ").lower()

print()
print("----- IMMIGRATION RESULT -----")

if is_returning_citizen == "yes" and passport_valid == "yes":
    print("ENTRY APPROVED")
    print("Welcome home!")

elif passport_valid == "yes" and has_visa == "yes":
    print("ENTRY APPROVED")
    print("Enjoy your stay.")

else:
    print("ENTRY DENIED")
    print("Please speak with an immigration officer.")