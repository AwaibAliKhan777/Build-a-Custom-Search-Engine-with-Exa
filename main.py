from exa_py import Exa
from dotenv import load_dotenv
import os 

#Load environment variables
load_dotenv()

api_key = os.getenv('EXA_API_KEY')

#step 1 :Initialize Exa with your API key
exa = Exa(api_key)

#Step 2 :Take user input
query = input('Search here:')

#Step3:Perform search (Top 7 results)
response = exa.search(query , num_results = 7 ,type = 'keyword')

# display the results nicely
print("\n Top Search Result \n")

for i, result in enumerate(response.results,start=1):
    print(f"Title: {result.title}")
    print(f"URL:{result.url}")
    