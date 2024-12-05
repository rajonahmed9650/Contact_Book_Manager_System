
import json
def save_data(contact_list):
    
    try:
        with open("Data.json","w") as file:
            json.dump(contact_list,file,indent=4)
           
    except Exception as e:
            print(f"Error while saving data: {e}")
   

def load_data():
    with open("Data.json","r") as file:
        return json.load(file)
