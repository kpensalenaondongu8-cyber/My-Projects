import json


contacts = []


print("1.Create, 2.View All, 3.Save, 4.Search, 5.Delete, 6.Exit")



with open("contacts.json", "r") as file:
    contacts = json.load(file)



while True:


    user_input = int(input("select mode: "))
    if user_input == 1:
      name = input("Enter Contact Name: ")
      number = input("Enter Number: ")  
      new_contact = {
        "Name": name,
        "Number": number
      }
      contacts.append(new_contact)
      continue



    elif user_input == 2:
      for i in contacts:
       print("⤆" + f" Contact Name: {i["Name"]} " + "⥑⥏" + f" Number: {i["Number"]} " + "⤇")
      continue



    elif user_input == 3:
      with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)
        print()
        line = "=" * 10 + "Contact Saved In PhoneBook" + "=" * 10
        print(line)
        print()
      continue




    elif user_input == 4:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)

        user_input2 = input("Enter Contatct Name To Search: ")

        for contact in contacts:
            if contact["Name"].lower() == user_input2.lower():
             print()
             lines = "=" *8 + f" Found⤇ Name: {contact['Name']} " + "⟛" +  f" Number: {contact['Number']} " + "=" *8   
             print(lines)
             print()
             break
            else:
                print("Contact Not Found") 



    elif user_input == 5:
     with open ("contacts.json", "r") as file:
         contacts = json.load(file)
         user_input3 = input("Enter Contact You want to delete by name: ")
         for contact in contacts:
            if contact["Name"].lower() == user_input3.lower():
                contacts.remove(contact)
                print("✂" + f" {contact["Name"]} deleted " + "✂")
            continue
 


    elif user_input == 6:
      line = "=" *10 + "GoodBye" + "=" *10
      print()
      print(line)
      print()
      break                
