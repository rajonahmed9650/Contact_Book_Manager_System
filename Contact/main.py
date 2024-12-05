from Contact_manager import Add_contact,View,Remove_data,Search_data
from Store_data import load_data

while True:
    print("Contact Book Mangement System")
    print("0.Exit \n")
    print("1.Add Data \n")
    print("2.View All Data\n")
    print("3.Remove Data\n")
    print("4.Search Data\n")

    option = input("Enter Your Option:")

    if option == "0":
        print("Thanks for using Contact Book Management System")
        break
    elif option == "1":
        name = input("Enter Your Name: ").strip()
        email = input("Enter Your Email: ").strip()
        while True:
            
            phone = input("Enter your phone (11 digits starting with 0): ").strip()
            if phone.isdigit and len(phone) == 11 and phone[0] == '0':
                contact_list = load_data()
                is_duplicate = False
                for contact in contact_list:
                    if contact['phone'] == phone:
                         print("This number already exits")
                         is_duplicate = True
                         break
                if not is_duplicate:
                     break    
            else:
                print("Invalid Phone Number")
        address = input("Enter Your Address: ").strip()
        Add_contact(name,email,phone,address)
        print("Contact added Successfully\n")

    elif option == "2":
            try:
                 contact_list =load_data()
            except FileNotFoundError:
                 print("Data File Not Found!")     

            if not  contact_list:
                 print("No contact found")
            else:
                 View()
    elif option == "3":
         index = int(input("Enter the removed index number: "))             
         Remove_data(index)
         print("Contact Removed Successfully \n")
    elif option == "4":
         query = input("Enter the search query:")
         Search_data(query)     
