name = input("Enter your name: ")
balance = 565566565
documentneeded = "adhar, pan, passbook"
documentneeded2 = "All forex doc"


service_mapping = {
    "1": ("Balance", f"Your current balance is: {balance}"),
    "2": ("Credit card", f"Required documents: {documentneeded}"),
    "3": ("Forex services", f"Required documents: {documentneeded2}")
}

print(f"\nHello, {name}!")
print("1. Balance")
print("2. Credit card")
print("3. Forex services")
print("Press Any thing to exit Expect (1,2,3)")

choice = input("Press 1, 2, or 3: ")

if choice in service_mapping:
    service_name, details = service_mapping[choice]
    print(f"\n{service_name} service selected for {name}.")
    print(details)
else:
    print(f"\nGoodbye, {name}. Exiting.")