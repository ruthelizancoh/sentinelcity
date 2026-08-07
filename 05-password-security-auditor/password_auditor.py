# Password Security Auditor - checks whether a password matches its confirmation and meets a minimum length

print("===================================")
print(" PASSWORD SECURITY AUDITOR")
print("===================================")

password = input("Enter a password: ")
confirm_password = input("Confirm your password: ")

print()
print("----- PASSWORD REPORT -----")

if password != confirm_password:
    print("Result: Passwords do not match.")

elif len(password) >= 8:
    print("Result: Strong password.")
    print("Password accepted.")

else:
    print("Result: Weak password.")
    print("Password must contain at least 8 characters.")
