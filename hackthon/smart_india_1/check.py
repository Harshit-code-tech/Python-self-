import mysql.connector as m
import subprocess
import pandas as pd
import getpass
import os
from sqlalchemy import create_engine, text

# Modify your MySQL connection settings
m_host = 'localhost'
m_user = 'root'
m_password = 'abcd1234'
m_database = 'hackathon_db'

# Function to connect to MySQL using SQLAlchemy
def connect_to_mysql():
    try:
        engine = create_engine(f"mysql+mysqlconnector://{m_user}:{m_password}@{m_host}/{m_database}")
        conn = engine.connect()
        return conn
    except Exception as e:
        print(f"Apologies, an error occurred while connecting to the database: {e}")
        return None

# Function to create tables if they don't exist
def create_tables_if_not_exist(conn):
    try:
        create_tables_sql = """
        CREATE TABLE IF NOT EXISTS hospitals (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            address VARCHAR(255),
            phone VARCHAR(15)
        );

        CREATE TABLE IF NOT EXISTS pharmacies (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            address VARCHAR(255),
            phone VARCHAR(15)
        );

        CREATE TABLE IF NOT EXISTS pathology_labs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            address VARCHAR(255),
            phone VARCHAR(15)
        );

        CREATE TABLE IF NOT EXISTS ambulance_numbers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            toll_free_number VARCHAR(15)
        );
        """
        conn.execute(text(create_tables_sql))
    except Exception as e:
        print(f"Apologies, an error occurred while creating tables: {e}")

# Function to insert data into the specified table
def insert_data(conn, table_name, data):
    try:
        if table_name != 'ambulance_numbers':
            insert_query = f"INSERT INTO {table_name} (name, address, phone) VALUES (:name, :address, :phone)"
        else:
            insert_query = f"INSERT INTO {table_name} (name, toll_free_number) VALUES (:name, :toll_free_number)"

        for row in data:
            conn.execute(text(insert_query), **row)

    except Exception as e:
        print(f"Error occurred while inserting data: {e}")

# Function to fetch data from the MySQL database
def fetch_data(table_name):
    try:
        with connect_to_mysql() as conn:
            query = f"SELECT * FROM {table_name}"
            df = pd.read_sql_query(query, conn)

        return df
    except Exception as e:
        print(f"Error occurred while fetching data: {e}")
        return None

# Function to save data to an Excel sheet, creating one if it doesn't exist
def save_to_excel(df, sheet_name):
    try:
        df.to_excel(f'{sheet_name}.xlsx', index=False, sheet_name=sheet_name)
    except Exception as e:
        print(f"Error occurred while saving to Excel: {e}")

# Function to secure access with a password
def secure_access_with_password():
    password = getpass.getpass("Enter the password to access the Excel file: ")
    return password

# Function to input new data
def input_new_data(table_name, num_entries):
    try:
        data = []
        for _ in range(num_entries):
            print(f"\nEnter data for {table_name}:")
            name = input("Enter name: ")
            if not name:
                break
            if table_name != 'ambulance_numbers':
                address = input("Enter address: ")
                phone = input("Enter phone: ")
                data.append({'name': name, 'address': address, 'phone': phone})
            else:
                toll_free_number = input("Enter toll-free number: ")
                data.append({'name': name, 'toll_free_number': toll_free_number})

        return data
    except Exception as e:
        print(f"Error occurred while inputting new data: {e}")
        return None

if __name__ == "__main__":
    conn = connect_to_mysql()
    if conn:
        create_tables_if_not_exist(conn)
        
        while True:
            print("\nOptions:")
            print("1. Insert new data")
            print("2. Fetch and save data to Excel")
            print("3. Exit")
            
            choice = input("Enter your choice (1/2/3): ")
            
            if choice == '1':
                table_choice = input("Choose a table to add data to (hospitals, pharmacies, pathology_labs, ambulance_numbers): ")
                num_entries = int(input("Enter the number of entries: "))
                data = input_new_data(table_choice, num_entries)
                if data:
                    insert_data(conn, table_choice, data)
            elif choice == '2':
                # List of table names to fetch and save
                table_names = ['hospitals', 'pharmacies', 'pathology_labs', 'ambulance_numbers']
                for table_name in table_names:
                    fetched_data = fetch_data(table_name)
                    if fetched_data is not None and not fetched_data.empty:
                        save_to_excel(fetched_data, table_name)
            elif choice == '3':
                break
        
        # Check if the Excel file exists
        excel_file_path = 'hospitals.xlsx'  # Replace with the actual file path
        if os.path.exists(excel_file_path):
            # Secure access to the Excel file with a password
            password = secure_access_with_password()
            if password == 'TEST':
                try:
                    subprocess.Popen([excel_file_path], shell=True)
                except Exception as e:
                    print(f"Error occurred while opening the Excel file: {e}")
            else:
                print("Access denied. Apologies, some error occurred.")
        else:
            print('The Excel file does not exist.')