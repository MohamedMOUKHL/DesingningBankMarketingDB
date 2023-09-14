import pandas as pd
import numpy as np

# Read the CSV file
df = pd.read_csv("bank_marketing.csv")
### Step1: create 3 DataFrames
# Create client DataFrame
client = df[['client_id', 'age', 'job', 'marital', 'education', 'credit_default', 'housing', 'loan']]

# Rename id_client
client.rename(columns={'client_id': 'id'}, inplace=True)

# Create campaign DataFrame
campaign = df[['client_id', 'campaign', 'month', 'day', 'duration', 'pdays', 'previous', 'poutcome', 'y']]

# Create economics DataFrame
economics = df[['client_id', 'emp_var_rate', 'cons_price_idx', 'euribor3m', 'nr_employed']]

# Rename columns
campaign.rename(columns={'duration': 'contact_duration', 
                        'previous': 'previous_campaign_contacts', 
                        'y': 'campaign_outcome', 
                        'poutcome': 'previous_outcome', 
                        'campaign': 'number_contacts'}, inplace=True)
# campaign['campaign_id'] = range(1, len(campaign) + 1)
# campaign['last_contact_date'] = pd.to_datetime(campaign['day'].astype(str) #+ campaign['month'] + 'year', format='%d%b%Y')

economics.rename(columns={'euribor3m': 'euribor_three_months'})



### Step2: cleaning:
# Cleaning the "education" column
# Replace "." with "_"
client['education'] = client['education'].str.replace(".", "_")

# Replace "unknown" with NumPy's NaN values
client['education'].replace("unknown", np.nan, inplace=True)
# Remove periods from the "job" column
client['job'] = client['job'].str.replace(".", "")
# Convert "success" and "failure"
campaign['previous_outcome'] = campaign['previous_outcome'].map({'nonexistent': np.nan, 'failure': 0, 'success': 1})
campaign['campaign_outcome'] = campaign['campaign_outcome'].map({'failure': 0, 'success': 1})

# Add column called campaign_id
campaign['campaign_id'] = 1
# Create a datetime column 
campaign['day'] = campaign['day'].astype(str)
campaign['month'] = campaign['month'].str.capitalize()
campaign['year'] = '2022'
campaign['last_contact_date'] = campaign['year'] + '-' + campaign['month'] + '-' + campaign['day']
campaign['last_contact_date'] = pd.to_datetime(campaign['last_contact_date'], format='%Y-%b-%d')

# Delete columns that we don't need
columns_to_remove = ['month', 'day', 'year']
campaign.drop(columns = columns_to_remove, inplace=True)

# Save 'client' DataFrame to 'client.csv' without an index
client.to_csv('client.csv', index=False)

# Save 'campaign' DataFrame to 'campaign.csv' without an index
campaign.to_csv('campaign.csv', index=False)

# Save 'economics' DataFrame to 'economics.csv' without an index
economics.to_csv('economics.csv', index=False)

# create SQL tables
client_table ='''CREATE TABLE client
(
    id serial PRIMARY KEY,
    age integer,
    job text,
    marital text,
    education text,
    credit_default boolean,
    housing boolean,
    loan boolean
);
\COPY client FROM 'client.csv' DELIMITER ',' CSV HEADER;
''' 

campaign_table =''' CREATE TABLE campaign
(
    campaign_id serial PRIMARY KEY,
    client_id serial REFERENCES client (id),
    number_contacts integer,
    contact_duration integer,
    pdays integer,
    previous_campaign_contacts integer,
    previous_outcome boolean,
    campaign_outcome boolean,
    last_contact_date date
    
);
\COPY campaign FROM 'campaign.csv' DELIMITER ',' CSV HEADER;

''' 
economics_table = ''' CREATE TABLE economics 
(
    client_id serial REFERENCES client (id),
    emp_var_rate float,
    cons_price_idx float,
    euribor_three_months float,
    number_employed float
);
\COPY economics FROM 'economics.csv' DELIMITER ',' CSV HEADER;
'''