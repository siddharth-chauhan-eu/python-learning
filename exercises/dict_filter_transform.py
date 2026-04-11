user = {"id": 1, "name": "John", "age": 30, "city": "Berlin"}

result = {
    k: v.upper()
    for k, v in user.items()
    if isinstance(v, str)
}

print(result)
