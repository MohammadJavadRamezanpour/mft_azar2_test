import json

userInput = int(input("1. add a contact\n2. search a contact\n\nselect an option: "))

if userInput == 1:
    # add a user
    name = input("name: ")
    phone = input("phone: ")

    user = {"name": name, "phone": phone}
    strFile = open("./database.json", "r").read()
    lstContacts = json.loads(strFile)
    lstContacts.append(user)
    open("./database.json", "w").write(str(lstContacts))

elif userInput == 2:
    search = input("search: ")

    strFile = open("./database.json", "r").read()
    lstContacts = json.loads(strFile)

    for contact in lstContacts:
        if search.lower() in contact["name"].lower():
            print(contact["name"], contact["phone"])
else:
    print("invalid input")