import json


contacts = []

print()
print("\033[33m=\033[0m" *5 + "\033[1;32m 1.Create, 2.View All, 3.Save, 4.Search, 5.Delete, 6.Exit \033[0m" + "\033[33m=\033[0m" *5)
print()

try:
  with open("contacts.json", "r") as file:
    contacts = json.load(file)
except FileNotFoundError:
    print("error: The contacts.json file not found")
    

while True:
    try:
        print()
        user_input = int(input("\033[35mselect mode: \033[0m"))
        print()
    except ValueError:
        print()
        print("\033[31m Invalid Syntax \033[0m")
        continue


    if user_input == 1:
      name = input("\033[33m Enter Contact Name: \033[0m")
      if name == "": 
        print()
        print("\033[33m=\033[33m" *10 + "\033[34m Empty Input \033[0m" + "\033[33m=\033[0m" *10)
        continue
      for contact in contacts:
        if name.lower() == contact["Name"].lower():
         print()
      print("\033[33m=\033[0m"*8 + " \033[32mName already exists\033[0m " + "\033[33m=\033[0m" *8)
      continue  
      print()
      number = input("\033[33m Enter Number: \033[0m")  
      if number == "":
         print()
         print("\033[33m=\033[33m" *10 + "\033[34m Empty Number \033[0m" + "\033[33m=\033[0m" *10)
         continue
      new_contact = {
        "Name": name,
        "Number": number
      }
      contacts.append(new_contact)
      continue



    elif user_input == 2:
      for i in contacts:
       print()
       print("⤆" + f"\033[34m Contact Name: {i["Name"]} " + "⥑⥏" + f" Number: {i["Number"]} \033[0m" + "⤇")
       print()
      continue



    elif user_input == 3:
      with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)
        print()
        print("\033[33m=\033[0m" * 10 + "\033[1;34mContact Saved In PhoneBook\033[0m" + "\033[33m=\033[0m" * 10)
        print()
      continue




    elif user_input == 4:

        user_input2 = input("\033[33mEnter Contatct Name To Search: \033[0m")
        if user_input2 == "":
            print()
            print("\033[33m=\033[0m" *10 + "\033[1;32m Empty input \033[0m" + "\033[33m=\033[0m" *10)
            continue
        for contact in contacts:
          if contact["Name"].lower() == user_input2.lower():
             print()
             lines = "\033[34m=\033[0m" *8 + f" \033[1;32mFound⤇ Name: {contact['Name']} " + "⟛" +  f" Number: {contact['Number']} \033[0m" + "\033[34m=\033[0m" *8   
             print(lines)
             print()
             break
        else :
             print()
             print("\033[33m=\033[0m" *5 + "\033[34m contact not found \033[34m" + "\033[33m=\033[0m"*5) 
             continue


    elif user_input == 5:

      user_input3 = input("\033[33mEnter Contact You want to delete by name: \033[0m")
      if user_input3 == "":
        print()
        print("\033[33m=\033[0m" *10 + "\033[1;32mEmpty Input" + "\033[33m=\033[0m" *10)
        continue
      for contact in contacts[:]:
          if contact["Name"].lower() == user_input3.lower():
                contacts.remove(contact)
                print()
                print("\033[33m✂\033[0m" + f"\033[1;32m {contact["Name"]} deleted \033[0m" + "\033[33m✂\033[0m")
                break
      else:
                print()
                print("\033[33m=\033[0m" *10 + " \033[1;32mContact not found \033[0m" + "\033[33m=\033[0m" * 10)
                print()
                continue


    elif user_input == 6:
      print()
      print("\033[33m=\033[0m" *10 + "\033[1;34mGoodBye\033[0m" + "\033[33m=\033[0m" *10)
      print()
      break                
    else:
        print("\033[33m==\033[0m" *9 + " \033[32mWrong Param Mate \033[0m" + "\033[33m==\033[0m" *9)
     


