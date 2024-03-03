# Project Name - Text to SQL

## Overview

This project focuses on converting natural language text to SQL queries using state-of-the-art models. We have implemented two primary models, namely CodeLlama and SQLCoder, to perform this task.

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
    

### Acknowledgements

sqlite: ([https://druid.apache.org/docs/latest/design/](https://www.sqlite.org/docs.html))

hugginface: (https://huggingface.co/docs/transformers/index)



