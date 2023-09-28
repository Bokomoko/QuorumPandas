import pandas as pd

# CONSTANTS - File names
LEGISLATOR_FILE = 'legislators.csv'
BILL_FILE = 'bills.csv'
VOTE_FILE = 'votes.csv'
VOTE_RESULT_FILE = 'vote_results.csv'


# load each file into a dataframe using pandas
legislator_df = pd.read_csv(LEGISLATOR_FILE)
bill_df = pd.read_csv(BILL_FILE)
vote_df = pd.read_csv(VOTE_FILE)
vote_result_df = pd.read_csv(VOTE_RESULT_FILE)

# Merge the DataFrames to create a combined DataFrame, start with the bills

merged_df = pd.merge(bill_df, vote_df, left_on='id', right_on='bill_id')
merged_df = pd.merge(merged_df, vote_result_df, left_on='id_y', right_on='vote_id')
merged_df = pd.merge(merged_df, legislator_df, left_on='legislator_id', right_on='id')

# Drop unnecessary columns
merged_df = merged_df.drop(['id_x', 'bill_id', 'id_y', 'legislator_id'], axis=1)

# Rename columns for clarity
merged_df = merged_df.rename(columns={
    'name': 'legislator_name',
    'title': 'bill_title',
    'vote_type': 'vote_result'
})

# define a function that receives a legislator name and returns he number of bill he supported
def get_bill_count(legislator_name):
    return merged_df[(merged_df['legislator_name'] == legislator_name) & (merged_df['vote_result'] == 'Y')].shape[0]

# define a function that receives a legislator name and returns he number of bill he opposed
def get_oppose_count(legislator_name):
    return merged_df[(merged_df['legislator_name'] == legislator_name) & (merged_df['vote_result'] == 'N')].shape[0]

# define a function that receives a bill and returns the number of legislators that supported it and the primary sponsor
def get_bill_supporters(bill_title):
    supporters = merged_df[(merged_df['bill_title'] == bill_title) & (merged_df['vote_result'] == 'Y')]
    return supporters['legislator_name'].tolist(), supporters['primary_sponsor'].tolist()[0]

# define a function that receives a bill and returns the number of legislators that opposed
def get_bill_opposers(bill_title):
    opposers = merged_df[(merged_df['bill_title'] == bill_title) & (merged_df['vote_result'] == 'N')]
    return opposers['legislator_name'].tolist()


# Define a function to query by bill
def query_by_bill(bill_title):
    return merged_df[merged_df['bill_title'] == bill_title]

# Define a function to query by legislator
def query_by_legislator(legislator_name):
    return merged_df[merged_df['legislator_name'] == legislator_name]

# Example usage:
bill_title = input("Enter a bill title: ")

bill_query_result = query_by_bill(bill_title= "H.R. 5376: Build Back Better Act")
legislator_query_result = query_by_legislator(legislator_name="Rep. Don Young (R-AK-1)")

# Print the query results
print("Query by Bill:")
print(bill_query_result)

print("\nQuery by Legislator:")
print(legislator_query_result)
