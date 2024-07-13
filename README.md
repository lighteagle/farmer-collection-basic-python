# CROPSIGHT - Farm Management System

## Farmer Data Collection Module

The Farmer Data Collection Module is a part of the CROPSIGHT - Farm Management System. This module is designed to manage farmer data, including the creation, reading, updating, deleting, and searching of farmer records.

### Features

- **Create** new farmer records with fields: ID, Name, Age, Commodity, Village, and District.
- **Read** and display all farmer records in a formatted table.
- **Update** existing farmer records.
- **Delete** farmer records.
- **Search** farmer records based on Name, Commodity, Village, or District.
- **Data Generator** a randomly chosen from a predefined list using numpy

### Farmer Data Fields

- **ID**: A unique 10-digit string identifier for the farmer (e.g., `F000000001`).
- **Name**: The name of the farmer (up to 50 characters).
- **Age**: The age of the farmer (up to 3 digits).
- **Commodity**: The main commodity produced by the farmer (up to 20 characters).
- **Village**: The village where the farmer resides (up to 20 characters).
- **District**: The district where the farmer resides (up to 20 characters).

### Data Generator

The Data Generator within the Farmer Data Collection Module creates random farmer records using NumPy. This feature allows for the quick generation of sample data to test the functionality of the system. The generator constructs the following fields randomly:

- **ID**: A unique 10-digit string identifier for each farmer, generated using a format like `F000000001`.
- **Name**: Randomly selected from a predefined list of farmer names.
- **Age**: Randomly generated as an integer between 18 and 65 to represent the age of the farmer.
- **Commodity**: Chosen from a predefined list of common agricultural commodities (e.g., rice, corn, soybeans).
- **Village**: Selected from a list of village names.
- **District**: Chosen from a list of district names.

#### Implementation

The data generator uses the following NumPy methods:

- **`np.array`**: To create arrays from predefined lists of names, commodities, villages, and districts.
- **`np.random.randint`**: To generate random ages within a specified range.
- **`np.random.choice`**: To randomly select names, commodities, villages, and districts from their respective arrays.

By leveraging these methods, the module can efficiently create a diverse set of farmer records for testing and demonstration purposes.




### Installation

**Clone the repository**:

   ```sh
   git clone https://github.com/lighteagle/farmer-collection-basic-python.git
   cd farmer-data-collection
   ```
