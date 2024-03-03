import sqlite3
import csv
import pandas as pd


class DatabaseManager:
    def __init__(self, database_file):
        self.database_file = database_file
        self.connection = None

    def establish_connection(self):
        """Establishes connection to a database file."""
        try:
            self.connection = sqlite3.connect(self.database_file)
            return self.connection
        except sqlite3.Error as e:
            print(e)
            return None

    def create_table(self, create_table_sql):
        """Creates a table using the provided SQL statement."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
        except sqlite3.Error as e:
            print(e)

    def insert_data(self, data, sql_query):
        """Inserts data into the table."""
        cursor = self.connection.cursor()
        cursor.execute(sql_query, data)
        self.connection.commit()
        return cursor.lastrowid

    def populate_table_from_excel(self, excel_file, table_name):
        """Populates the table in the database with data from an Excel file."""
        excel_data = pd.read_excel(excel_file)
        csv_file = f"{excel_file.split('.')[0]}.csv"
        excel_data.to_csv(csv_file, index=None, header=True)

        column_names = list(excel_data.columns)
        column_types = {col: self.get_column_type(excel_data[col]) for col in column_names}
        print(column_types)  # Print column names and their corresponding data types

        create_table_sql = self.generate_table_creation_sql(table_name, column_names, column_types)
        self.create_table(create_table_sql)

        with open(csv_file, mode='r') as file:
            csv_reader = csv.reader(file)
            for index, row in enumerate(csv_reader):
                if index > 0:
                    row = tuple(row)
                    insert_query = f"INSERT INTO {table_name} VALUES ({','.join(['?'] * len(row))})"
                    self.insert_data(row, insert_query)

    @staticmethod
    def get_column_type(column_data):
        """Determines the SQLite data type for a column based on its values."""
        data_type = str(column_data.dtype)
        if data_type == 'object':
            return 'TEXT'
        elif 'int' in data_type:
            return 'INTEGER'
        elif 'float' in data_type:
            return 'REAL'
        else:
            return 'TEXT'

    @staticmethod
    def generate_table_creation_sql(table_name, column_names, column_types):
        """Generates SQL statement for creating a table."""
        table_creation_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ("
        for column_name in column_names:
            data_type = column_types[column_name]
            table_creation_sql += f"{column_name} {data_type}, "
        table_creation_sql = table_creation_sql[:-2] + ");"
        return table_creation_sql


if __name__ == '__main__':
    excel_file_name = "inventory.xlsx"
    database_file_name = f"{excel_file_name.split('.')[0]}.db"

    db_manager = DatabaseManager(database_file_name)
    db_manager.establish_connection()

    if db_manager.connection is not None:
        table_name = excel_file_name.split('.')[0]
        db_manager.populate_table_from_excel(excel_file_name, table_name)
    else:
        print("Error! Cannot establish connection to the database.")
