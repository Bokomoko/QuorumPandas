import pandas as pd

def return_votationsummary_df():
  return merged_df

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

# merge the dataframes from the vote_result on
merged_df = vote_result_df.merge(vote_df, left_on='vote_id', right_on='id')
# rename the id_x column to vote_result_id
merged_df = merged_df.rename(columns={'id_x': 'vote_result_id'})
# merge with legislator on legislator_id
merged_df = merged_df.merge(legislator_df, left_on='legislator_id', right_on='id')
# drop the id column
merged_df = merged_df.drop(columns=['id'])
# merge with bill on bill_id
merged_df = merged_df.merge(bill_df, left_on='bill_id', right_on='id')
# drop the id column
merged_df = merged_df.drop(columns=['id', 'id_y'])





# remove the id_y column
#merged_df = merged_df.drop(columns=['id_y'])


#merged_df = merged_df.merge(bill_df, left_on='bill_id', right_on='id')
#merged_df = merged_df.merge(legislator_df, left_on='legislator_id', right_on='id')

#function that returns the number of bill the legislator voted 1 (support)
def get_support_count(legislator_name):
  return merged_df[(merged_df['name'] == legislator_name) & (merged_df['vote_type'] == 1)].shape[0]

def get_oppose_count(legislator_name):
  return merged_df[(merged_df['name'] == legislator_name) & (merged_df['vote_type'] == 2)].shape[0]





# define a function that receives a bill and returns the number of legislators that supported it and the primary sponsor
def get_bill_supporters(bill_title):
    supporters = merged_df[(merged_df['title'] == bill_title) & (merged_df['vote_type'] == 1)]
    return supporters['name'].tolist(), supporters['sponsor_id'].tolist()[0]

# define a function that receives a bill and returns the number of legislators that opposed
def get_bill_opposers(bill_title):
    opposers = merged_df[(merged_df['title'] == bill_title) & (merged_df['vote_type'] == 2)]
    return opposers['name'].tolist()


# Define a function to query by bill
def query_by_bill(bill_title):
    return merged_df[merged_df['title'] == bill_title]

# Define a function to query by legislator
def query_by_legislator(legislator_name):
    return merged_df[merged_df['name'] == legislator_name]

def main():
  #print("\nVote Result\n",vote_result_df.head())
  # print all columns of the merged df
  #print("\nMerged Dataframe\n",merged_df.head())
  print("\nbills supported by Rep. Don Young (R-AK-1)\n", get_support_count('Rep. Don Young (R-AK-1)'))
  print("\nbills opposed by Rep. Don Young (R-AK-1)\n", get_oppose_count('Rep. Don Young (R-AK-1)'))

#For every bill in the dataset, how many legislators supported the bill? How many legislators
# opposed the bill? Who was the primary sponsor of the bill?
  print("\nBill supporters\n", get_bill_supporters('H.R. 1: For the People Act of 2019'))
  print("\nBill opposers\n", get_bill_opposers('H.R. 1: For the People Act of 2019'))










if __name__ == "__main__":
  main()
