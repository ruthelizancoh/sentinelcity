# Cyber Threat Monitoring Console - evaluates login attempts as Low, Medium, or High risk

print("===================================")
print(" CYBER THREAT MONITORING CONSOLE")
print("===================================")

username = input("Enter username: ")
failed_attempts = int(input("Failed login attempts: "))
vpn_enabled = input("VPN enabled? (yes/no): ").lower()
login_hour = int(input("Login hour (0-23): "))

print()
print("----- SECURITY REPORT -----")
print(f"User: {username}")

if failed_attempts >= 5 and vpn_enabled == "no":
    print("Risk Level: HIGH")
    print("Recommendation: Lock the account immediately.")

elif (failed_attempts >= 3 and failed_attempts <= 4) or (login_hour >= 22 or login_hour < 5):
    print("Risk Level: MEDIUM")
    print("Recommendation: Monitor the account closely.")

else:
    print("Risk Level: LOW")
    print("Recommendation: Normal activity detected.")