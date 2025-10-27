import WebSearcher as ws
import os
import pandas as pd

''' READING IN CANONICAL LOCATIONS '''

## Loading the data and displaying the results and filtering for United States Canonical Locations
locs = pd.read_csv('data/locations/geotargets-2025-07-15.csv')
locs_df = pd.DataFrame(locs)

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
    main("what to do after high school")
