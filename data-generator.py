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
    "Budi Santoso",
    "Siti Aminah",
    "Agus Prasetyo",
    "Rina Suryani",
    "Dian Purnama",
    "Hendra Saputra",
    "Fitriani Rahmawati",
    "Dedi Wijaya",
    "Wulan Kartika",
    "Rudi Hartono",
    "Nurul Hidayah",
    "Arif Setiawan",
    "Lina Marlina",
    "Eko Prasetya",
    "Ratna Dewi",
    "Taufik Hidayat",
    "Dewi Anggraeni",
    "Bambang Susilo",
    "Sri Lestari",
    "Yudi Kurniawan",
    "Novianti Putri",
    "Joko Widodo",
    "Tri Wahyuni",
    "Andi Firmansyah",
    "Desi Anwar",
    "Iwan Fals",
    "Asep Suhendar",
    "Melati Indah",
    "Rudi Gunawan",
    "Fitriawati Rahayu",
    "Hendri Wibowo",
    "Ayu Lestari",
    "Yuni Astuti",
    "Ismail Marzuki",
    "Indah Permata",
    "Anwar Ibrahim",
    "Lia Agustina",
    "Yanto Suryadi",
    "Resti Oktaviani",
    "Aldi Firmansyah",
    "Maya Sari",
    "Agus Wahyudi",
    "Lia Sukmawati",
    "Irwan Hidayat",
    "Fajar Nugroho",
    "Fitri Handayani",
    "Santi Susanti",
    "Anwar Sadat",
    "Linda Kurniawati",
    "Anton Wijaya",
    "Dian Setiawan",
    "Siti Nurhaliza",
    "Eka Putra",
    "Yuliana Sari",
    "Adi Nugroho",
    "Nur Aini",
    "Heri Purnomo",
    "Rina Ariyanti",
    "Bambang Setiawan",
    "Siti Hawa",
    "Aditya Pratama",
    "Nia Kurniasih",
    "Rudi Setiawan",
    "Sri Handayani",
    "Wahyu Saputra",
    "Dini Rahmawati",
    "Aldi Kurniawan",
    "Yulia Anggraeni",
    "Andi Pratama",
    "Indriani Sari",
    "Budi Kurniawan",
    "Tri Susanti",
    "Rian Setiawan",
    "Dewi Rahmawati",
    "Ardiansyah",
    "Lina Suryani",
    "Eko Setiawan",
    "Yani Suryani",
    "Hendra Pratama",
    "Nurul Anisa",
    "Agus Setiawan",
    "Desi Rahmawati",
    "Wahyu Prasetyo",
    "Siti Aisyah",
    "Fajar Setiawan",
    "Maya Anggraeni",
    "Arif Hidayat",
    "Lina Kurniasih",
    "Joko Susilo"
])
commodity_list = np.array(["Coffee", "Cocoa", "Rice", "Corn"])
districts_list = np.array(["Bogor", "Cianjur", "Sukabumi", "Depok", "Jakarta Selatan"])
village_dict = {
    "Bogor": ["Curug", "Pasir Jaya", "Bubulak"],
    "Cianjur": ["Neglasari", "Mekarsari", "Wanasari", "Bojongkaso"],
    "Sukabumi": ["Cimanggis", "Kutajaya", "Sukamulya"],
    "Depok": ["Cimanggis", "Sukamulya", "Mekarjaya", "Sawangan"],
    "Jakarta Selatan": ["Mampang", "Pancoran", "Lebak Bulus", "Kalibata"],
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
