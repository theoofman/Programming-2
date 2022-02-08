myFile = open("data.txt","r")
customers = myFile.readlines()
choice = input("Would you like to look up a customer by line number or last name?")
while choice.lower() not in ["line number", "line", "name", "last name"]:
    choice = input("Sorry, that's not an option. Type 'line number' or 'name'")

if choice.lower() in ["line number", "line"]:
    line = int(input("Please enter the line number: "))
    print(customers[line - 1])

found = False
if choice.lower() in ["name", "last name"]:
    name = input("Please enter the name: ")
    for line in customers:
        if name in line:
            print("The customer's full name is", line)
            found = True
    if found == False:
        print("Sorry, no such customer exists.")