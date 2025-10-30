"""
Emails exercise
Estimate: 20 minutes
Actual: 17 minutes
"""

email_to_name = {}
email = input("Email: ")
while email != "":
    names = email[:email.index("@")].split(".")
    full_name = " ".join(name.capitalize() for name in names)
    is_correct_name = input(f"Is your name {full_name}? (Y/n) ").lower()
    if is_correct_name == "y" or is_correct_name == "":
        email_to_name[email] = full_name
    else:
        new_name = input("Name: ")
        email_to_name[email] = new_name
    email = input("Email: ")
print()
for email, name in email_to_name.items():
    print(f"{name} ({email})")