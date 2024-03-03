import sqlite3
from sqlite3 import Error
from transformers import AutoModelForCausalLM, AutoTokenizer

class SQLQueryGenerator:
 def __init__(self, model_dir, database_path):
     self.model_dir = model_dir
     self.database_path = database_path
     self.codec = AutoTokenizer.from_pretrained(model_dir)
     self.translator = AutoModelForCausalLM.from_pretrained(model_dir)
     self.db_connector = sqlite3.connect(database_path)
     
 def get_table_structure(self, table_name):
     """Fetches the structure of a table from the database."""
     cursor = self.db_connector.cursor()
     cursor.execute(f"PRAGMA table_info({table_name})")
     structure = cursor.fetchall()
     if structure:
         return structure
     else:
         print(f"Table {table_name} does not exist or has no schema.")
         return None
     
 def text_to_sql(self, structure, user_prompt):
     """Generates SQL query based on user prompt and table structure."""
     column_names = ', '.join([f"{col[1]} {col[2]}" for col in structure])
     prompt = f"""Below are SQL table schemas paired with instructions that describe a task.
     Using valid SQLite, write a response that appropriately completes the request for the provided tables.
     ### Instruction: {user_prompt} ### 
     Input: CREATE TABLE data_table({column_names});
     ### Response: """
     print("Press Enter for default question or Enter user prompt without newline characters:")
     user_input = input().strip()
     if user_input:
         modified_prompt = user_input
     else:
         modified_prompt = user_prompt
     prompt = prompt.replace(user_prompt, modified_prompt + " ")
     print(prompt)

     """Text to SQL query generation"""
     encoded_input = self.codec(
         prompt, return_tensors="pt", truncation=True
     ).input_ids.cuda()
     outputs = self.translator.generate(input_ids=encoded_input, max_length=200)
     response = self.codec.batch_decode(
         outputs.detach().cpu().numpy(), skip_special_tokens=True
     )[0][:]
     return response[len(prompt) :]  # Remove prompt from generated response

 def execute_query(self, query):
     """Executes the query on the database and returns rows and columns."""
     cursor = self.db_connector.cursor()
     cursor.execute(query)
     column_names = [header[0] for header in cursor.description]
     delimiter = "-" * sum(len(col_name) + 4 for col_name in column_names)
     print(tuple(column_names))
     print(delimiter)
     rows = []
     for row in cursor:
         rows.append(row)
         print(row)
     cursor.close()
     self.db_connector.commit()
     return rows, column_names

if __name__ == "__main__":
   model_path = "defog/sqlcoder2"  
   database_file = r"inventory.db"  
   query_generator = SQLQueryGenerator(model_path, database_file)
   user_question = "Give complete details of properties in India"
   while True:
       table_structure = query_generator.get_table_structure("sql_pdf")
       if table_structure:
           sql_query = query_generator.text_to_sql(table_structure, user_question)
           query_generator.execute_query(sql_query)
     
   query_generator.db_connector.close()
