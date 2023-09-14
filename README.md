# DesingningBankMarketingDB

# Bank Marketing Campaign Data Management

This project involves cleaning and storing data from a recent marketing campaign conducted by a bank. The goal is to prepare the data, set up a PostgreSQL database, design a schema for storing campaign data, and create SQL scripts that can be executed to create the necessary tables and populate them with data from CSV files.

## Project Overview

Personal loans are a significant revenue stream for banks, with substantial interest income generated from loan products. The bank in question conducted a marketing campaign to promote personal loans, and this project aims to manage the campaign's data efficiently.

### Project Tasks

1. **Data Cleaning and Preparation**: The first step is to clean and prepare the data, which is provided in a CSV file named "bank_marketing.csv." This involves data extraction, renaming columns, reformatting data, and cleaning text values.

2. **Data Splitting**: The data is divided into three separate DataFrames: `client`, `campaign`, and `economics`. These DataFrames correspond to different aspects of the campaign data, including client information, campaign details, and economic factors at the time of the campaign.

3. **CSV File Export**: Each DataFrame is saved as a CSV file without an index. The generated CSV files are: `client.csv`, `campaign.csv`, and `economics.csv`. These files contain clean and structured data for each specific aspect of the campaign.

4. **Database Setup**: A PostgreSQL database is set up to store campaign data. The schema is designed to accommodate data from future campaigns easily. The schema includes tables for client data, campaign details, and economic factors. Foreign keys are used to establish relationships between tables.

5. **SQL Scripts**: SQL scripts are provided as multiline string variables that can be executed to create the necessary tables and import data from the CSV files into the PostgreSQL database. These scripts are designed to be used by the bank for database setup.

## Prerequisites

- Python (3.7 or higher)
- pandas
- PostgreSQL (with appropriate access and credentials)
- psycopg2 (Python library for PostgreSQL)

## Usage

1. Clone this GitHub repository to your local machine.

2. Ensure you have the required dependencies installed by running: pip install pandas psycopg2
3. Place the "bank_marketing.csv" file in the project directory.

4. Run the provided Python script to clean the data, split it into DataFrames, save CSV files, and generate SQL scripts for database setup: python bank_marketing_data_management.py

5. Execute the SQL scripts using your PostgreSQL database client to set up the database tables and import data from CSV files.

## Database Schema

The database schema consists of the following tables:

 1. `client`: Contains client-related information.
 2. `campaign`: Stores campaign details.
 3. `economics`: Stores economic factors data.
 4. `FOREIGN KEYS`: Relationships are established between tables using foreign keys.







   
