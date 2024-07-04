import json

# Initial list to store farmer records
farmers = []

# File to store farmer records
FILE_NAME = 'farmers.json'

def print_color(message, color):
    colors = {
        "HEADER": '\033[95m',
        "OKBLUE": '\033[94m',
        "OKGREEN": '\033[92m',
        "WARNING": '\033[93m',
        "FAIL": '\033[91m',
        "ENDC": '\033[0m',
        "BOLD": '\033[1m',
        "UNDERLINE": '\033[4m'
    }
    if color not in colors:
        color = "ENDC"
    print(f"{colors[color]}{message}{colors['ENDC']}")

def load_farmers():
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_farmers():
    with open(FILE_NAME, 'w') as file:
        json.dump(farmers, file, indent=4)

def get_non_empty_input(prompt, max_length):
    while True:
        user_input = input(prompt).strip()
        if user_input and len(user_input) <= max_length:
            return user_input
        else:
            print_color(f"Input cannot be empty and must be {max_length} characters or less. Please try again.", "FAIL")

def get_valid_age(prompt):
    while True:
        try:
            age = int(get_non_empty_input(prompt, 3))
            if 0 < age < 130:
                return age
            else:
                print_color("Age must be a positive number between 1 and 129. Please try again.", "FAIL")
        except ValueError:
            print_color("Invalid age. Please enter a number.", "FAIL")

def create_farmer():
    while True:
        farmer_id = get_non_empty_input("Enter farmer ID (up to 10 digits): ", 10)
        if len(farmer_id) <= 10 and farmer_id.isalnum() and not any(farmer['id'] == farmer_id for farmer in farmers):
            break
        else:
            print_color("Farmer ID must be a unique up to 10-digit alphanumeric. Please try again.", "FAIL")

    name = get_non_empty_input("Enter farmer name (up to 50 characters): ", 50)
    age = get_valid_age("Enter farmer age (up to 3 digits): ")
    commodity = get_non_empty_input("Enter commodity (up to 20 characters): ", 20)
    village = get_non_empty_input("Enter village (up to 20 characters): ", 20)
    district = get_non_empty_input("Enter district (up to 20 characters): ", 20)

    farmers.append({'id': farmer_id, 'name': name, 'age': age, 'commodity': commodity, 'village': village, 'district': district})
    save_farmers()
    print_color("Farmer added successfully!", "OKGREEN")

def print_farmer_table(farmers):
    print_color("\nList of farmers:", "HEADER")
    print("+------------+----------------------------------------------------+-----+----------------------+----------------------+----------------------+")
    print("| ID         | Name                                               | Age | Commodity            | Village              | District             |")
    print("+------------+----------------------------------------------------+-----+----------------------+----------------------+----------------------+")
    for farmer in farmers:
        print(f"| {farmer['id']:<10} | {farmer['name']:<50} | {farmer['age']:<3} | {farmer['commodity']:<20} | {farmer['village']:<20} | {farmer['district']:<20} |")
    print("+------------+----------------------------------------------------+-----+----------------------+----------------------+----------------------+\n")

def read_farmers():
    if not farmers:
        print_color("No farmers available.", "WARNING")
    else:
        print_farmer_table(farmers)

def update_farmer():
    farmer_id = get_non_empty_input("Enter the ID of the farmer to update: ", 10)
    for farmer in farmers:
        if farmer['id'] == farmer_id:
            name = get_non_empty_input("Enter new name (up to 50 characters): ", 50)
            age = get_valid_age("Enter new age (up to 3 digits): ")
            commodity = get_non_empty_input("Enter new commodity (up to 20 characters): ", 20)
            village = get_non_empty_input("Enter new village (up to 20 characters): ", 20)
            district = get_non_empty_input("Enter new district (up to 20 characters): ", 20)

            farmer['name'] = name
            farmer['age'] = age
            farmer['commodity'] = commodity
            farmer['village'] = village
            farmer['district'] = district
            save_farmers()
            print_color("Farmer updated successfully!", "OKGREEN")
            return
    print_color("Farmer not found.", "FAIL")

def delete_farmer():
    farmer_id = get_non_empty_input("Enter the ID of the farmer to delete: ", 10)
    for farmer in farmers:
        if farmer['id'] == farmer_id:
            farmers.remove(farmer)
            save_farmers()
            print_color("Farmer deleted successfully!", "OKGREEN")
            return
    print_color("Farmer not found.", "FAIL")

def search_farmers():
    query = get_non_empty_input("Enter name, commodity, village, or district to search: ", 50).lower()
    results = [farmer for farmer in farmers if query in farmer['name'].lower() or query in farmer['commodity'].lower() or query in farmer['village'].lower() or query in farmer['district'].lower()]
    if results:
        print_farmer_table(results)
    else:
        print_color("No matching farmers found.", "WARNING")

def main():
    global farmers
    farmers = load_farmers()
    
    while True:
        print("\n-------------------------------------------------")
        print_color("CROPSIGHT - Farm Management System:", "HEADER")
        print("-------------------------------------------------")
        print_color("\nModul [Farmer Data Collection]:", "BOLD")
        print_color("1. Create a new farmer",'OKGREEN')
        print_color("2. Read all farmers",'OKGREEN')
        print_color("3. Update a farmer",'OKGREEN')
        print_color("4. Delete a farmer",'OKGREEN')
        print_color("5. Search farmers",'OKGREEN')
        print_color("6. Exit","OKGREEN")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            create_farmer()
        elif choice == '2':
            read_farmers()
        elif choice == '3':
            update_farmer()
        elif choice == '4':
            delete_farmer()
        elif choice == '5':
            search_farmers()
        elif choice == '6':
            print_color("Exiting the program.", "HEADER")
            break
        else:
            print_color("Invalid choice. Please try again.", "FAIL")

if __name__ == "__main__":
    main()
