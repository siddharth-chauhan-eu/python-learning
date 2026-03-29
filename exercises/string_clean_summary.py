raw = "968-Maria, ( D@t@ Engineer );; 27y"

clean = (
    raw
    .replace("968-", "")
    .replace(",", "")
    .replace("(", "")
    .replace(")", "")
    .replace(";;", "")
)

parts = clean.split()

name = parts[0].lower()
role = (parts[1] + " " + parts[2]).replace("@", "a").lower()
age = parts[3].replace("y", "")

print(f"name: {name} | role: {role} | age: {age}")
