import re

email = input("what's your email? ").strip()

#if re.search(r"^[^@]+@[^@]+\.edu$", email):
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(edu|com)$", email, re.IGNORECASE):
#if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

"""
print("======")
username, domain = email.split("@")
print(username)
print(domain)

#if username and "." in domain:
if username and domain.endswith(".edu"):
    print("Valid")
    print(domain.endswith(".edu"))
else:
    print("Invalid")


print("=========")
if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")
"""