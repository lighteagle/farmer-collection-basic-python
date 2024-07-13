"""
Todo List :
1. Import Libraries
2. List Parameter : id, name, age, commodity, village, district
3. Generate Random Farmer
4. Export to JSON File
"""

# 1. Import Libraries
import numpy as np
import json

# 2. List Parameter 
name_list = np.array([
    "Aditya Pratama",
    "Budi Santoso",
    "Citra Dewi",
    "Dedi Susanto",
    "Eka Wijaya",
    "Fitri Amalia",
    "Gita Wulandari",
    "Hadi Saputra",
    "Ika Lestari",
    "Joko Prasetyo",
    "Kiki Maulana",
    "Lina Setiawan",
    "Mira Sari",
    "Nina Rahayu",
    "Oka Setiawan",
    "Putu Ananda",
    "Qori Rahman",
    "Rina Anggraini",
    "Santi Puspitasari",
    "Tina Kusuma",
    "Udin Kurniawan",
    "Vina Ariyanti",
    "Wulan Sari",
    "Xenia Oktavia",
    "Yuniarti Wijaya",
    "Zaki Abdullah",
    "Agus Pratama",
    "Bambang Setiawan",
    "Candra Nugroho",
    "Dina Puspita",
    "Edi Prasetyo",
    "Faisal Akbar",
    "Gilang Kurnia",
    "Hana Rahmawati",
    "Imam Arifin",
    "Jihan Aulia",
    "Kartika Putri",
    "Lukman Hakim",
    "Maya Sari",
    "Nurul Hidayati",
    "Oni Purnomo",
    "Putu Suryawan",
    "Qiana Dwi",
    "Rizki Pratama",
    "Siska Amalia",
    "Taufik Hidayat",
    "Uci Sanjaya",
    "Vira Andriani",
    "Weni Marlina",
    "Xena Larasati",
    "Yudi Setiawan",
    "Zainal Arifin",
    "Amalia Putri",
    "Bayu Saputra",
    "Cici Ayu",
    "Dimas Arif",
    "Evi Susanti",
    "Farida Wulandari",
    "Gustav Mahardika",
    "Hendra Pratama",
    "Indah Sari",
    "Jamaludin Putra",
    "Kurniawan Pratama",
    "Leni Marlina",
    "Miko Prasetyo",
    "Nova Rahmawati",
    "Oki Setiawan",
    "Putra Wijaya",
    "Qory Zulkarnain",
    "Rina Puspita",
    "Suci Amalia",
    "Tomi Andri",
    "Ulfa Maharani",
    "Vira Ramadhani",
    "Wawan Saputra",
    "Xandra Wulandari",
    "Yessi Marlina",
    "Zulfikar Pratama",
    "Aris Susanto",
    "Bunga Lestari",
    "Cipto Wibowo",
    "Dewi Amalia",
    "Erik Kurniawan",
    "Feri Susanto",
    "Gina Pratiwi",
    "Hilda Maulida",
    "Ida Pratiwi",
    "Joko Supriyanto",
    "Kiki Setiawan",
    "Lina Dewi",
    "Mia Rahayu",
    "Nina Kurnia",
    "Oka Suryawan",
    "Putri Anggraeni",
    "Qori Maulana",
    "Rina Setiawan",
    "Sari Andriani",
    "Tina Maulida",
    "Udin Saputra",
    "Vina Dewi",
    "Wulan Pratiwi",
    "Xena Putri",
    "Yuli Susanti",
    "Zaki Prasetyo"
])
commodity_list = np.array(["Coffee", "Cocoa", "Rice", "Corn"])
districts_list = np.array(["Bogor", "Cianjur", "Sukabumi", "Depok"])
village_dict = {
    "Bogor": ["Curug", "Pasir Jaya", "Bubulak"],
    "Cianjur": ["Neglasari", "Mekarsari", "Wanasari", "Bojongkaso"],
    "Sukabumi": ["Cimanggis", "Kutajaya", "Sukamulya"],
    "Depok": ["Cimanggis", "Sukamulya", "Mekarjaya", "Sawangan"],
}

# 3. Generate random farmers
num_farmers = 1000
farmers = [] 

districts = np.random.choice(districts_list, size=num_farmers) 
# Generate farmers' information
for i in range(num_farmers):
    farmer_id = f"F{i+1:09d}"
    farmer_name = np.random.choice(name_list) 
    farmer_age = np.random.randint(18, 61)
    farmer_commodity = np.random.choice(commodity_list) 
    farmer_village = np.random.choice(village_dict[districts[i]])
    
    print(i+1, farmer_id, farmer_name, farmer_age, farmer_commodity, farmer_village, districts[i])
    farmer = {
        "id": farmer_id,
        "name": farmer_name,
        "age": farmer_age,
        "commodity": farmer_commodity,
        "village": farmer_village,
        "district": districts[i]
    }

    farmers.append(farmer)

# # 4. Export to JSON file
with open('farmers.json','w') as json_file:
    json.dump(farmers, json_file)

print("Generate success") 
