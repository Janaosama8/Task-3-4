contacts={}
contacts = {"Linda": "01012785678","Leen": "01299785432","Yassin": "01222334455"
}
print("Contacts:")
for name in contacts:
    print(name)

search_name = input("Enter name: ")
if search_name in contacts:
    print(f"{search_name}'s phone number is {contacts[search_name]}")
else:
    print("Name not found.")
