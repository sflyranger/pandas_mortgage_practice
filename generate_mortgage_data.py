# Importing the necessary libraries
import numpy as np
import pandas as pd

# Set the seed for reproducibility
np.random.seed(42)

# Total number of records
n = 1000

# Generating the sythetic data
loan_id = [f"LN{i:06d}" for i in range(1, n+1)]

borrower_income = np.random.normal(85000,20000,n).round(2) # Setting the borrower income as a normal random value
loan_amount = np.random.normal(300000,75000,n).round(2) # Setting the loan amount as a normal random value
interest_rate = np.random.normal(4.25,0.75,n).round(2) # Setting the interest rate as a normal random value

loan_term = np.random.choice([15, 20, 30],n) # Setting the loan term as a choice
credit_score = np.random.normal(650,50,n).astype(int) # Setting the credit score as a normal random value
property_value = (loan_amount / np.random.uniform(0.6,0.9,n)).round(2) # Setting the property value based on the loan amount / a normally distributed ratio to reflect appreciation
ltv_ratio = (loan_amount / property_value * 100).round(2) # Setting the loan to value ratio based on the loan amount / property value
dti_ratio = np.random.normal(35,10,n).round(2) # Setting the dti ratio as a normally distributed positve value 

loan_status = np.random.choice(['Current', 'Delinquent', 'Default', 'Paid Off'],n, p = [0.75, 0.05, 0.05, 0.15]) # Setting the loan status indicator by choice given a probability setting

origination_date = pd.to_datetime(np.random.choice(pd.date_range('1995-01-01', '2024-12-31')),n) # Randomly generating origination dates

states = ['TX', 'FL', 'CA', 'NY', 'KY', 'PA', 'IL', 'OK', 'GA', 'MA', 'NC', 'MI']

state = np.random.choice(states,n)


# Creating a dataframe 
df = pd.DataFrame({
    'loan_id': loan_id, 
    'borrower_income': borrower_income, 
    'loan_amount': loan_amount, 
    'interest_rate': interest_rate, 
    'loan_term': loan_term, 
    'credit_score': credit_score, 
    'property_value': property_value, 
    'ltv_ratio': ltv_ratio, 
    'dti_ratio': dti_ratio, 
    'loan_status': loan_status, 
    'origination_date': origination_date, 
    'state': state, 
})

# Exporting to a CSV
df.to_csv('mortgage_data.csv', index=False)

print("Mortgage dataset generated and saved to mortgage_data.csv")

