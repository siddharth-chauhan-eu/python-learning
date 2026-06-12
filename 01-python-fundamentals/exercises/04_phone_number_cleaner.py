phone_number = "+49 (176) 123-4567"

print(
    phone_number
    .replace("+", "00")
    .replace(" ", "")
    .replace("(", "")
    .replace(")", "")
    .replace("-", "")
)
