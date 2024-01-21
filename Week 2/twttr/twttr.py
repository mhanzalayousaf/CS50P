vowels = ['a','e','i','o','u']
users_input = input("Input: ")
print("Output: " , end="")

for letters in users_input:
    if not letters.lower() in vowels:
        print(letters , end="")
print()