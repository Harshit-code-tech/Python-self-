import mysql.connector as m
import pandas as pd
import getpass

# Modify your MySQL connection settings
m_host = 'localhost'
m_user = 'root'
m_password = 'abcd1234'
m_database = 'hackathon_db'

# Function to connect to MySQL
def connect_to_mysql():
    try:
        conn = m.connect(host=m_host, user=m_user, password=m_password, database=m_database)
        return conn
    except m.Error as e:
        print(f"Apologies, an error occurred while connecting to the database: {e}")
        return None

# Function to insert data into a table
def insert_data(conn, table_name, data):
    try:
        cursor = conn.cursor()
        insert_query = f"INSERT INTO {table_name} ({', '.join(data.keys())}) VALUES ({', '.join(['%s'] * len(data))})"
        cursor.execute(insert_query, list(data.values()))
        conn.commit()
        print(f"Data inserted into {table_name}")
    except m.Error as e:
        print(f"Error occurred while inserting data: {e}")

# Function to delete data from a table
def delete_data(conn, table_name, primary_key_column, primary_key_value):
    try:
        cursor = conn.cursor()
        delete_query = f"DELETE FROM {table_name} WHERE {primary_key_column} = %s"
        cursor.execute(delete_query, (primary_key_value,))
        conn.commit()
        print(f"Data deleted from {table_name}")
    except m.Error as e:
        print(f"Error occurred while deleting data: {e}")

# Function to fetch data from the MySQL database
def fetch_data(table_name, conn):
    try:
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql_query(query, conn)
        return df
    except m.Error as e:
        print(f"Error occurred while fetching data: {e}")
        return None

# Function to save data to an Excel sheet
def save_to_excel(df, sheet_name):
    try:
        df.to_excel(f'{sheet_name}.xlsx', index=False)
        print(f'Data saved to {sheet_name}.xlsx')
    except Exception as e:
        print(f"Error occurred while saving to Excel: {e}")

# Function to secure access with a password
def secure_access_with_password():
    password = getpass.getpass("Enter the password to access the data: ")
    return password

if __name__ == "__main__":
    conn = connect_to_mysql()
    if conn:
        while True:
            print("\nChoose an option:")
            print("1. Enter Data")
            print("2. Fetch and Show Data (Password Required)")
            print("3. Delete Data")
            print("4. Exit")

            choice = input("Enter your choice (1/2/3/4): ")

            if choice == '1':
                print("\nChoose a table to enter data:")
                print("1. Hospitals")
                print("2. Pharmacies")
                print("3. Pathology Labs")
                print("4. Ambulance Numbers")

                table_choice = input("Enter your choice (1/2/3/4): ")

                if table_choice == '1':
                    data = {
                        'name': input("Enter hospital name: "),
                        'address': input("Enter hospital address: "),
                        'phone': input("Enter hospital phone number: "),
                    }
                    insert_data(conn, 'hospitals', data)

                elif table_choice == '2':
                    data = {
                        'name': input("Enter pharmacy name: "),
                        'address': input("Enter pharmacy address: "),
                        'phone': input("Enter pharmacy phone number: "),
                    }
                    insert_data(conn, 'pharmacies', data)

                elif table_choice == '3':
                    data = {
                        'name': input("Enter pathology lab name: "),
                        'address': input("Enter pathology lab address: "),
                        'phone': input("Enter pathology lab phone number: "),
                    }
                    insert_data(conn, 'pathology_labs', data)

                elif table_choice == '4':
                    data = {
                        'name': input("Enter ambulance name: "),
                        'toll_free_number': input("Enter toll-free number: "),
                    }
                    insert_data(conn, 'ambulance_numbers', data)

            elif choice == '2':
                password = secure_access_with_password()
                if password == 'test':
                    print("\nChoose a table to fetch and show data:")
                    print("1. Hospitals")
                    print("2. Pharmacies")
                    print("3. Pathology Labs")
                    print("4. Ambulance Numbers")

                    table_choice = input("Enter your choice (1/2/3/4): ")

                    if table_choice == '1':
                        fetched_data = fetch_data('hospitals', conn)
                        if fetched_data is not None and not fetched_data.empty:
                            print("Data fetched from hospitals:")
                            print(fetched_data)

                    elif table_choice == '2':
                        fetched_data = fetch_data('pharmacies', conn)
                        if fetched_data is not None and not fetched_data.empty:
                            print("Data fetched from pharmacies:")
                            print(fetched_data)

                    elif table_choice == '3':
                        fetched_data = fetch_data('pathology_labs', conn)
                        if fetched_data is not None and not fetched_data.empty:
                            print("Data fetched from pathology_labs:")
                            print(fetched_data)

                    elif table_choice == '4':
                        fetched_data = fetch_data('ambulance_numbers', conn)
                        if fetched_data is not None and not fetched_data.empty:
                            print("Data fetched from ambulance_numbers:")
                            print(fetched_data)

                else:
                    print("Access denied. Apologies, the password is incorrect.")

            elif choice == '3':
                print("\nChoose a table to delete data:")
                print("1. Hospitals")
                print("2. Pharmacies")
                print("3. Pathology Labs")
                print("4. Ambulance Numbers")

                table_choice = input("Enter your choice (1/2/3/4): ")
                primary_key_column = 'id'
                primary_key_value = input("Enter the primary key value of the row you want to delete: ")

                if table_choice == '1':
                    delete_data(conn, 'hospitals', primary_key_column, primary_key_value)

                elif table_choice == '2':
                    delete_data(conn, 'pharmacies', primary_key_column, primary_key_value)

                elif table_choice == '3':
                    delete_data(conn, 'pathology_labs', primary_key_column, primary_key_value)

                elif table_choice == '4':
                    delete_data(conn, 'ambulance_numbers', primary_key_column, primary_key_value)

            elif choice == '4':
                break

        conn.close()
