import WebSearcher as ws
import os
import pandas as pd

'''CREATING THE LOCATION DIR'''
locations_dir = '../data/locations' 
os.makedirs(locations_dir, exist_ok=True)
ws.download_locations(locations_dir)

locations_dir = '../data/locations' 
f = os.listdir(locations_dir)[-1]
fp = os.path.join(locations_dir, f)

## Loading the data and displaying the results and filtering for United States Canonical Locations
locs = pd.read_csv(fp)
us_filter = locs_df['Country Code'] == 'US'
usa_locs = locs_df[us_filter]

### DEFINING WEB SEARCHER FUNCTION
def main(query,canonical_name=False):
  query = 'what to do after high school'
  if canonical_name == False:
    search_engine = ws.SearchEngine()
    search_engine.search(query)
    search_engine.parse_results()
    search_engine.save_serp(append_to='results-data/serp_tester.json')
    search_engine.save_results(append_to = 'results-data/serp_result_tester.json')


''' RUNNING THE FUNCTION '''
if __name__=="__main__":
    main()
