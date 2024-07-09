# Check Password Strength

password = input("Enter password: ")

result = {}

# condition 1 - length check
result['length'] = False
if len(password) > 8:
    result['length'] = True

# codndition 2 - must contain digits
result['digits'] = False
for i in password:
    if i.isdigit():
        result['digits'] = True

# condition 3 - must contain capitals
result['caps'] = False
for i in password:
    if i.isupper():
        result['caps'] = True

print(result)

if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")