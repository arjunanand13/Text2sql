# NSQL - Text2SQL (Excel to SQLite Converter and SQL Query Executor)

## Overview
This Project facilitates the conversion of Excel files to SQLite databases and provides functionality to execute SQL queries on the generated database. Additionally, it includes converting natural language text to SQL queries using state-of-the-art models. We have implemented two primary models, namely CodeLlama and SQLCoder, to perform this task.

## File Structure
excel_db.py: Python script for converting Excel data to a database.
inventory.xlsx: Sample Excel file containing inventory data (input file).
inventory.db: SQLite database file created by the script (output file).
nsql.py:This Python script generates SQL queries based on user prompts and executes them on a SQLite database. It utilizes a pre-trained language model to convert natural language instructions into SQL queries.


### Models

1. **CodeLlama**
   - [CodeLlama-34b-Instruct-hf](https://huggingface.co/codellama/CodeLlama-34b-Instruct-hf) (with 34 billion parameter)
   - [CodeLlama-13b-Instruct-hf](https://huggingface.co/codellama/CodeLlama-13b-Instruct-hf) (with 13 billion parameter)

2. **SQLCoder**
   - [SQLCoder-34b-Alpha](https://huggingface.co/defog/sqlcoder-34b-alpha) (with 34 billion parameter)
   - [SQLCoder2](https://huggingface.co/defog/sqlcoder2) (with 15 billion parameter)

### Quantization Support

- We could load 4-bit, 8-bit, and 16-bit quantization in SQLCoder2 model
- Whereas in CodeLlama model we could load 13 billion and 34 billion parameters.

However, while SQLCoder2 model can be quantized to 4-bit, 8-bit and 16 bit only 4-bit and 8-bit quantization operations are currently supported.

### SQLITE Integration

We seamlessly integrate SQLite 3, a lightweight relational database, offering efficient data storage and retrieval. Leveraging its simplicity and reliability, we ensure robust database operations for our system

### Databases and Tables

1. **Database 1**
   - Tables:
     - inventory
     
2. **Database 2**
   - Tables:
     - actions
     - alerts
     - conditions
     - operations

3. **Database 3**
   - Tables:
     - acknowledges
     - alerts
     - actions
     - events
     - media_type
     - users
    
## Usage
Environment Setup
Create Virtual Environment: Set up a virtual environment using Python's built-in venv module.
```
python -m venv myenv
```
Activate Virtual Environment: Activate the virtual environment to isolate dependencies.

On Windows:
```
myenv\Scripts\activate
```
On macOS and Linux:
```
source myenv/bin/activate
```
Install Required Packages: Install the necessary packages using pip.
```
pip install -r requirements.txt
```
### Input Data
Prepare your data in an Excel file named inventory.xlsx (or any other desired name).
### Run the Script
Execute the Python script excel_db.py. The script will read the Excel file, convert it to CSV format, and create an SQLite database file (inventory.db) with corresponding tables.
```
python excel_db.py
```
Check Database
After execution, you will find the generated SQLite database file (inventory.db) containing the converted data.
Execute SQL Queries
To execute SQL queries on the generated database, run the script nsql.py.
```
python nsql.py
```
Follow the prompts to input your SQL query and interact with the database.

Note
1) Ensure that the required Excel file (inventory.xlsx) is present in the directory before running the script. Additionally, review the generated SQLite database (inventory.db) to verify the converted data.
2) Here we have used SQLCODER2 4-bit quantized version , which occupies GPU RAM of around 9GB . Consider other models and quantizations as per your GPU storage .
3) We have considered one table in one sheet for faster inference , for multiple tables add details in further sheets of excel.

## Acknowledgements

sqlite: ([https://druid.apache.org/docs/latest/design/](https://www.sqlite.org/docs.html))

hugginface: (https://huggingface.co/docs/transformers/index)



