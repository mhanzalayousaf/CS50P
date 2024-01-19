def main():
    text = input("Write Text:")
    emojitext = changedtext(text)
    print(emojitext)

def changedtext(tx):
    tx = tx.replace(":(",'🙁')
    tx = tx.replace(":)",'🙂')
    return tx

main()