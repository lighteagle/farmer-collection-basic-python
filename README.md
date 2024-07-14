# CROPSIGHT - Farm Management System

## Part 1- Farmer Data Collection Module

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

### Part 2 - Data Generator

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

### Part-3 - Rebuild Apps Using Pandas Data Frames + Add new Features "Show Statistics"

In this module, we'll dive into the powerful capabilities of **Pandas** to manipulate and analyze data using DataFrames. Some Pandas methods that are used in this module are:

- **`pd.read_json`**: This method is used to read JSON data from a specified file and convert it into a Pandas DataFrame.
- **`_.to_json`**: With this method, you can write the contents of a DataFrame to a JSON file.
- **`pd.DataFrame`**: This function allows you to create a DataFrame from a list of dictionaries.
- **`pd.concat`**: This method facilitates the concatenation of two or more DataFrames along a particular axis.
- **`_.values`**: By using this attribute, you can retrieve the underlying values of a DataFrame.
- **`_.value_counts`**: This method counts the occurrences of each unique value in a specified column of the DataFrame.
- **`_.iterrows`**: With this method, you can iterate over the rows of a DataFrame one by one, which allows for custom processing and operations on each individual row.
- **`_.empty`**: This attribute allows you to check whether a DataFrame is empty, helping you to prevent errors that may arise from attempting to perform operations on an empty dataset.
- **`_.str.contains`**: This method enables you to search for a specific string within a column of the DataFrame, allowing for filtering of data based on text matches.

### Installation

**Clone the repository**:

   ```sh
   git clone https://github.com/lighteagle/farmer-collection-basic-python.git
   cd farmer-data-collection
   ```
