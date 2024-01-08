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

### Druid Integration

We have integrated the Apache Druid API into our system. Apache Druid is a real-time analytics database designed for fast slice-and-dice analytics ("OLAP" queries) on large data sets. Most often, Druid powers use cases where real-time ingestion, fast query performance, and high uptime are important.

Using the [Apache Druid](https://druid.apache.org/) API, we were able to generate CSV insert statements for efficient data ingestion. To start Druid on localhost, we used Apache Druid version 28.0.0.

### Databases and Tables

1. **Database 1**
   - Tables:
     - order.csv
     - orderdetails.csv

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
    
### Inference notebooks

inference.ipynb: This notebook demonstrates the inference process for Database 1.
inference_set1_codellama.ipynb: This notebook specifically focuses on the inference process using the CodeLlama model for Database 1.
inference_set2_codellama.ipynb: This notebook demonstrates inference process on  CodeLlama model for Database 2.
inference_set1_sqlcoder.ipynb: This notebook specifically focuses on the inference process using the SqlCoder2 model for Database 1.
inference_set2_sqlcoder.ipynb: This notebook demonstrates inference process on  SqlCoder2 model for Database 2.

### Analysis

-The inference was conducted on a server equipped with a NVIDIA GeForce RTX 3090 (Genesis) GPU.
-The analysis is drew on the provided Excel sheet, and it includes the inference results for three databases: Database 1 (overall inference) ,Database 2 (Set 1 inference) and Databse 3 (Set 2 Inference) using the specified models.
-Sheet 3 has configurations of both models as well as comparitive results of Database 1.
-Trained Model Predictions has results conferred from standalone queries and database



### Acknowledgements

druid: (https://druid.apache.org/docs/latest/design/)

hugginface: (https://huggingface.co/docs/transformers/index)



