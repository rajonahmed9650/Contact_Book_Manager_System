from Store_data import save_data,load_data

def Add_contact(name,email,phone,address):
    try:
        contact_list = load_data()
    except FileNotFoundError:
        print("Data file not found! Creating a new File")    
        contact_list = []
    contact = {
        'name':name,
        'email':email,
        'phone':phone,
        'address':address
    }
    contact_list.append(contact)
    save_data(contact_list)

def View():
    try:
        json_data = load_data()
    except FileNotFoundError:
        print("Data file not found")    

    print("Contact List....")

    for i, data in enumerate(json_data,start=1):
        print(f"{i}. Name: {data['name']}, Email:{data['email']}, Phone: {data['phone']}, Address: {data['address']} \n")

def Remove_data(index):
    try:
        json_data = load_data()
    except FileNotFoundError:
        print("Data file not found!")    
        return

    if 0 < index <= len(json_data):
        del json_data[index-1]
        save_data(json_data)
    else:
        print("Invalid Index")

def Search_data(query):
    try:
        json_data = load_data()
    except FileNotFoundError:
        print("Data file not found!")
        return
    results = [] 
    for data in json_data:
        if query in data['name'] or query in data['phone'] or query in data['address']:
            results.append(data)
            print("Search Results....")
    for i,data in enumerate(results,start=1):
        print(f"{i}. Name: {data['name']}, Email: {data['email']}, Phone: {data['phone']}, Address: {data['address']} \n")        