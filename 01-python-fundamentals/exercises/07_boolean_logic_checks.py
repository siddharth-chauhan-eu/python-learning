# 1. Name & age check
name = input("Enter name: ").strip()
age_input = input("Enter age: ").strip()

if not age_input.isdigit():
    print("Invalid age input")
    exit()

age = int(age_input)

if name != "" and age >= 18:
    print("Valid user")
else:
    print("Invalid user")


# 2. Password check
password = input("\nEnter password: ")

if len(password) >= 8 and " " not in password:
    print("Valid password")
else:
    print("Invalid password")


# 3. Email check
email = input("\nEnter email: ").strip()

if email != "" and "@" in email and email.endswith(".com"):
    print("Valid email")
else:
    print("Invalid email")


# 4. Username check
username = input("\nEnter username: ").strip()

if username != "" and len(username) > 5:
    print("Valid username")
else:
    print("Invalid username")


# 5. Role & access check
valid_roles = ["admin", "moderator", "user"]

role = input("Enter role (admin/moderator/user): ").strip().lower()
if role not in valid_roles:
    print("Invalid role")
    exit()

# early exit for user
if role == "user":
    print("Access denied")
    exit()

# banned
is_banned_input = input("Is banned? (yes/no): ").strip().lower()
if is_banned_input not in ["yes", "no"]:
    print("Invalid input for banned status")
    exit()

is_banned = is_banned_input == "yes"

# verified
is_verified_input = input("Is verified? (yes/no): ").strip().lower()
if is_verified_input not in ["yes", "no"]:
    print("Invalid input for verification")
    exit()

is_verified = is_verified_input == "yes"

# strict model
if not is_banned and is_verified:
    print("Access granted")
else:
    print("Access denied")
