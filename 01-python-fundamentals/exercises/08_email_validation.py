email = input("Enter email: ").strip()

valid_tlds = [".com", ".org", ".net"]

if email == "":
    print("Invalid email")
    exit()

if len(email) > 254:
    print("Invalid email")
    exit()

if email.count("@") != 1:
    print("Invalid email")
    exit()

if "." not in email:
    print("Invalid email")
    exit()

if not any(email.endswith(tld) for tld in valid_tlds):
    print("Invalid email")
    exit()

if not email[0].isalnum() or not email[-1].isalnum():
    print("Invalid email")
    exit()

print("Valid email")
