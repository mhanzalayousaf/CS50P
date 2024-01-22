import emoji


user=input("Input: ")
e = emoji.emojize(user, language='alias')
print("Output: ", e, sep="")