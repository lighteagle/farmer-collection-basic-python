import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import altair as alt

FILE_NAME = 'farmers.json'

def load_farmers():
    try:
        farmers = pd.read_json(FILE_NAME)
        return farmers
    except (FileNotFoundError, ValueError):
        return pd.DataFrame(columns=['id', 'name', 'age', 'commodity', 'village', 'district'])

def save_farmers(farmers):
    farmers.to_json(FILE_NAME, orient='records', lines=False, indent=4)
    
def plot_histogram(data, column, title):
    fig, ax = plt.subplots()
    sns.histplot(data[column], kde=True, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(column)
    ax.set_ylabel('Frequency')
    st.pyplot(fig)
    
def plot_pie_chart(data, column, title):
    fig = px.pie(data, names=column, title=title)
    st.plotly_chart(fig)
    
def plot_bar_chart(data, column, title):
    value_counts = data[column].value_counts().reset_index()
    value_counts.columns = [column, 'Count']

    fig = px.bar(value_counts, x=column, y='Count', title=title)
    st.plotly_chart(fig)
    
def plot_altair_chart(data, column, title):
    chart = alt.Chart(data).mark_bar().encode(
        x=alt.X(column, sort='-y'),
        y='count()'
    ).properties(title=title)
    st.altair_chart(chart, use_container_width=True)

def main():
    st.title("CROPSIGHT - Farm Management System")

    menu = ["Dashboard", "Create", "Read", "Update", "Delete", "Search", "Show Statistics"]
    choice = st.sidebar.selectbox("Menu", menu, index=0)
    
    farmers = load_farmers()
    
    if choice == "Dashboard":
        st.subheader("Dashboard")
        plot_histogram(farmers, "age", "Farmers Age Distribution")
        plot_pie_chart(farmers, "commodity", "Distribution of Commodities")
        plot_bar_chart(farmers, "village", "Farmers Count by Village")
        plot_altair_chart(farmers, "district", "Farmers Count by District")
        
    elif choice == "Create":
        st.subheader("Create a New Farmer")
        farmer_id = st.text_input("Farmer ID (up to 10 digits)")
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=1, max_value=299)
        commodity = st.text_input("Commodity")
        village = st.text_input("Village")
        district = st.text_input("District")
        
        if st.button("Add Farmer"):
            if not farmer_id or not name or not commodity or not village or not district:
                st.error("All fields are required.")
            elif len(farmer_id) > 10 or not farmer_id.isalnum():
                st.error("Farmer ID must be unique and up to 10-digit alphanumeric.")
            elif farmer_id in farmers['id'].values:
                st.error("Farmer ID already exists.")
            else:
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
                st.success("Farmer added successfully!")
                
    elif choice == "Read":
        st.subheader("List of Farmers")
        if farmers.empty:
            st.warning("No farmers available.")
        else:
            st.dataframe(farmers)
        
    elif choice == "Update":
        st.subheader("Update a Farmer")
        farmer_id = st.text_input("Enter the ID of the farmer to update")
        if farmer_id in farmers['id'].values:
            name = st.text_input("New Name", value=farmers.loc[farmers['id'] == farmer_id, 'name'].values[0])
            age = st.number_input("New Age", min_value=1, max_value=299, value=farmers.loc[farmers['id'] == farmer_id, 'age'].values[0])
            commodity = st.text_input("New Commodity", value=farmers.loc[farmers['id'] == farmer_id, 'commodity'].values[0])
            village = st.text_input("New Village", value=farmers.loc[farmers['id'] == farmer_id, 'village'].values[0])
            district = st.text_input("New District", value=farmers.loc[farmers['id'] == farmer_id, 'district'].values[0])
            
            if st.button("Update Farmer"):
                index = farmers.index[farmers['id'] == farmer_id].tolist()[0]
                farmers.at[index, 'name'] = name
                farmers.at[index, 'age'] = age
                farmers.at[index, 'commodity'] = commodity
                farmers.at[index, 'village'] = village
                farmers.at[index, 'district'] = district

                save_farmers(farmers)
                st.success("Farmer updated successfully!")
        else:
            st.error("Farmer not found.")

    elif choice == "Delete":
        st.subheader("Delete a Farmer")
        farmer_id = st.text_input("Enter the ID of the farmer to delete")
        if st.button("Delete Farmer"):
            if farmer_id in farmers['id'].values:
                farmers = farmers[farmers['id'] != farmer_id]
                save_farmers(farmers)
                st.success("Farmer deleted successfully!")
            else:
                st.error("Farmer not found.")
                
    elif choice == "Search":
        st.subheader("Search Farmers")
        query = st.text_input("Enter name, commodity, village, or district to search")
        if query:
            results = farmers[
                farmers['name'].str.contains(query, case=False, na=False) |
                farmers['commodity'].str.contains(query, case=False, na=False) |
                farmers['village'].str.contains(query, case=False, na=False) |
                farmers['district'].str.contains(query, case=False, na=False)
            ]
            if not results.empty:
                st.dataframe(results)
            else:
                st.warning("No matching farmers found.")
            
    elif choice == "Show Statistics":
        st.subheader("Statistics")
        if not farmers.empty:
            commodity_counts = farmers['commodity'].value_counts()
            village_counts = farmers['village'].value_counts()
            district_counts = farmers['district'].value_counts()

            st.write("**Count by Commodity**")
            st.dataframe(commodity_counts.reset_index().rename(columns={'index': 'Commodity', 'commodity': 'Count'}))

            st.write("**Count by Village**")
            st.dataframe(village_counts.reset_index().rename(columns={'index': 'Village', 'village': 'Count'}))

            st.write("**Count by District**")
            st.dataframe(district_counts.reset_index().rename(columns={'index': 'District', 'district': 'Count'}))
    
    
if __name__ == "__main__":
    main()