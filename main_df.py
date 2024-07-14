import json
import pandas as pd
import time
import locale

# Set locale to Indonesian for number formatting
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

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
    start_time = time.time()
    try:
        farmers = pd.read_json(FILE_NAME)
        end_time = time.time()
        time_elapsed = end_time - start_time
        num_farmers = locale.format_string("%d", len(farmers), grouping=True)
        print_color(f"Time taken to load farmers: {time_elapsed:.4f} seconds", "OKGREEN")
        print_color(f"Number of farmers loaded: {num_farmers}", "OKGREEN")
        return farmers
    except (FileNotFoundError, ValueError) as e:
        print_color("Error loading farmers: " + str(e), "FAIL")
        return pd.DataFrame(columns=['id', 'name', 'age', 'commodity', 'village', 'district'])

def save_farmers(farmers):
    farmers.to_json(FILE_NAME, orient='records', lines=False, indent=4)

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
            if 0 < age < 300:
                return age
            else:
                print_color("Age must be a positive number between 1 and 299. Please try again.", "FAIL")
        except ValueError:
            print_color("Invalid age. Please enter a number.", "FAIL")

def create_farmer(farmers):
    while True:
        farmer_id = get_non_empty_input("Enter farmer ID (up to 10 digits): ", 10)
        if len(farmer_id) <= 10 and farmer_id.isalnum() and farmer_id not in farmers['id'].values:
            break
        else:
            print_color("Farmer ID must be unique and up to 10-digit alphanumeric. Please try again.", "FAIL")

    name = get_non_empty_input("Enter farmer name (up to 50 characters): ", 50)
    age = get_valid_age("Enter farmer age (up to 3 digits): ")
    commodity = get_non_empty_input("Enter commodity (up to 20 characters): ", 20)
    village = get_non_empty_input("Enter village (up to 20 characters): ", 20)
    district = get_non_empty_input("Enter district (up to 20 characters): ", 20)

    new_farmer = pd.DataFrame([{
        'id': farmer_id,
        'name': name,
        'age': age,
        'commodity': commodity,
        'village': village,
        'district': district
    }])

    farmers = pd.concat([farmers, new_farmer], ignore_index=True)
    save_farmers(farmers)
    print_color("Farmer added successfully!", "OKGREEN")

def print_farmer_table(farmers):
    print_color("\nList of farmers:", "HEADER")
    print("+------------+----------------------------------------------------+-----+----------------------+----------------------+----------------------+")
    print("| ID         | Name                                               | Age | Commodity            | Village              | District             |")
    print("+------------+----------------------------------------------------+-----+----------------------+----------------------+----------------------+")
    
    for index, farmer in farmers.iterrows():
        print(f"| {farmer['id']:<10} | {farmer['name']:<50} | {farmer['age']:<3} | {farmer['commodity']:<20} | {farmer['village']:<20} | {farmer['district']:<20} |")
    
    print("+------------+----------------------------------------------------+-----+----------------------+----------------------+----------------------+")
    print_color(f"{len(farmers)} farmers found.", "OKGREEN")

def read_farmers(farmers):
    if farmers.empty:
        print_color("No farmers available.", "WARNING")
    else:
        print_farmer_table(farmers)

def update_farmer(farmers):
    farmer_id = get_non_empty_input("Enter the ID of the farmer to update: ", 10)
    if farmer_id in farmers['id'].values:
        index = farmers.index[farmers['id'] == farmer_id].tolist()[0]
        farmers.at[index, 'name'] = get_non_empty_input("Enter new name (up to 50 characters): ", 50)
        farmers.at[index, 'age'] = get_valid_age("Enter new age (up to 3 digits): ")
        farmers.at[index, 'commodity'] = get_non_empty_input("Enter new commodity (up to 20 characters): ", 20)
        farmers.at[index, 'village'] = get_non_empty_input("Enter new village (up to 20 characters): ", 20)
        farmers.at[index, 'district'] = get_non_empty_input("Enter new district (up to 20 characters): ", 20)

        save_farmers(farmers)
        print_color("Farmer updated successfully!", "OKGREEN")
    else:
        print_color("Farmer not found.", "FAIL")

def delete_farmer(farmers):
    farmer_id = get_non_empty_input("Enter the ID of the farmer to delete: ", 10)
    if farmer_id in farmers['id'].values:
        farmers = farmers[farmers['id'] != farmer_id]
        save_farmers(farmers)
        print_color("Farmer deleted successfully!", "OKGREEN")
    else:
        print_color("Farmer not found.", "FAIL")
    return farmers

def search_farmers(farmers):
    query = get_non_empty_input("Enter name, commodity, village, or district to search: ", 50).lower()
    results = farmers[
        farmers['name'].str.lower().str.contains(query) |
        farmers['commodity'].str.lower().str.contains(query) |
        farmers['village'].str.lower().str.contains(query) |
        farmers['district'].str.lower().str.contains(query)
    ]
    if not results.empty:
        print_farmer_table(results)
    else:
        print_color("No matching farmers found.", "WARNING")


def show_statistics(farmers):
    if farmers.empty:
        print_color("No farmers available for statistics.", "WARNING")
    else:
        print_color("\nStatistics:", "HEADER")
        
        commodity_counts = farmers['commodity'].value_counts()
        village_counts = farmers['village'].value_counts()
        district_counts = farmers['district'].value_counts()

        def print_stat_table(title, counts):
            max_label_len = max(counts.index.str.len().max(), len(title)) + 2
            print_color(f"\n{title}:", "OKBLUE")
            print("+" + "-"*(max_label_len + 1) + "+" + "-"*15 + "+")
            print(f"| {'Category':<{max_label_len}}| {'Count':>13} |")
            print("+" + "-"*(max_label_len + 1) + "+" + "-"*15 + "+")
            for index, value in counts.items():
                print(f"| {index:<{max_label_len}}| {value:>13,} |")
            print("+" + "-"*(max_label_len + 1) + "+" + "-"*15 + "+")

        print_stat_table("Count by Commodity", commodity_counts)
        print_stat_table("Count by Village", village_counts)
        print_stat_table("Count by District", district_counts)

def print_main_menu():
    print("\n-------------------------------------------------")
    print_color("CROPSIGHT - Farm Management System:", "HEADER")
    print("-------------------------------------------------")
    print_color("\nModul [Farmer Data Collection]:", "BOLD")
    print_color("1. Create a new farmer",'OKGREEN')
    print_color("2. Read all farmers",'OKGREEN')
    print_color("3. Update a farmer",'OKGREEN')
    print_color("4. Delete a farmer",'OKGREEN')
    print_color("5. Search farmers",'OKGREEN')
    print_color("6. Show statistics",'OKGREEN')
    print_color("7. Exit","OKGREEN")

def main():
    farmers = load_farmers()
    
    while True:
        print_main_menu()
        choice = input("\nEnter your choice [1-7]: ")

        if choice == '1':
            create_farmer(farmers)
            farmers = load_farmers()  # Reload after creating
        elif choice == '2':
            read_farmers(farmers)
        elif choice == '3':
            update_farmer(farmers)
        elif choice == '4':
            farmers = delete_farmer(farmers)
        elif choice == '5':
            search_farmers(farmers)
        elif choice == '6':
            show_statistics(farmers)
        elif choice == '7':
            print_color("Exiting the program.", "HEADER")
            break
        else:
            print_color("Invalid choice. Please try again.", "FAIL")

if __name__ == "__main__":
    main()
