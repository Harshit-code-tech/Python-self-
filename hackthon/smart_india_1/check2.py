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

if __name__ == "__main__":
    conn = connect_to_mysql()
    if conn:
        create_tables_if_not_exist(conn)

        # Data entry examples
        data_hospitals = [
            {'name': 'Praduman Bal Memorial Hospital', 'address': 'General Hospital 9R27+Q8G,KIIT UNIVERSITY', 'phone': '123-456-7890'},
            {'name': 'Kalinga Institute of Medical Sciences(KIMS)', 'address': 'Hospital Kalinga Institute of Medical Sciences(KIMS)', 'phone': '987-654-3210'},
            {'name': 'PEN hospital', 'address': 'Hig-66,Nandankanand road', 'phone': '123-456-7890'},
            {'name': 'Kims emergency hospital', 'address': '751024', 'phone': '123-456-7890'},
            {'name': 'Maxfort', 'address': 'General Hospital police station', 'phone': '123-456-7890'},
        ]

        data_pharmacies = [
            {'name': 'aPPOLO Pharmasy', 'address': 'Plot no. 516', 'phone': '123-456-7890'},
            {'name': 'Khusi medical store', 'address': 'Bhuwaneshwar', 'phone': '987-654-3210'},
            {'name': 'KIMS', 'address': 'General Hospital 9R27+Q8G,KIIT UNIVERSITY', 'phone': '123-456-7890'},
            {'name': 'Aditya pharma', 'address': 'Kiit Rd', 'phone': '123-456-7890'},
            {'name': 'Ashwini Pharma', 'address': 'Ashwini wellcenter', 'phone': '123-456-7890'},
        ]

        data_pathology_labs = [
            {'name': 'Redcliff lab', 'address': 'H no. 318', 'phone': '123-456-7890'},
            {'name': 'Practical lab', 'address': '9R38+393', 'phone': '987-654-3210'},
            {'name': 'Omm maa Super fast', 'address': 'Plot no. 524', 'phone': '123-456-7890'},
            {'name': 'Redcliff lab', 'address': 'H no. 318', 'phone': '123-456-7890'},
            {'name': 'Dhurba', 'address': 'Blood testing ', 'phone': '123-456-7890'},
        ]

        data_ambulance_numbers = [
            {'name': 'RED ambulance', 'toll_free_number': '123-456-7890'},
            {'name': 'Oxygen ambulance', 'toll_free_number': '987-654-3210'},
            {'name': 'Narayani ambulance',  'toll_free_number': '123-456-7890'},
            {'name': 'Local ambulance','toll_free_number': '123-456-7890'},
            {'name': 'Moambulance',  'toll_free_number': '123-456-7890'},
        ]

        # Insert data into the hospitals table
        insert_data(conn, 'hospitals', data_hospitals)

        # Insert data into the pharmacies table
        insert_data(conn, 'pharmacies', data_pharmacies)

        # Insert data into the pathology_labs table
        insert_data(conn, 'pathology_labs', data_pathology_labs)

        # Insert data into the ambulance_numbers table
        insert_data(conn, 'ambulance_numbers', data_ambulance_numbers)

        # List of table names to fetch and save
        table_names = ['hospitals', 'pharmacies', 'pathology_labs', 'ambulance_numbers']

        for table_name in table_names:
            fetched_data = fetch_data(table_name)
            if fetched_data is not None and not fetched_data.empty:
                save_to_excel(fetched_data, table_name)

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