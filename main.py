import WebSearcher as ws
import os
import pandas as pd
import selenium


''' GITHUB AND SELENIUM CONFLICT FIXING '''
## fix source: https://github.com/SeleniumHQ/selenium/issues/14609
#options = webdriver.ChromeOptions()
#options.add_argument("--no-sandbox")
#driver = webdriver.Chrome(options=options)

s_config = {
  "browser": "chrome",
  "headless":True,
  "options":{ "arguments":["--no-sandbox"]},
  "version_main":140,
  "use_subprocess":False,
  }


''' READING IN CANONICAL LOCATIONS '''

## Loading the data and displaying the results and filtering for United States Canonical Locations
locs = pd.read_csv('data/locations/geotargets-2025-07-15.csv')
locs_df = pd.DataFrame(locs)

us_filter = locs_df['Country Code'] == 'US'
usa_locs = locs_df[us_filter]

### DEFINING WEB SEARCHER FUNCTION
def main(query,canonical_name=False):
  ## Conditional Statement Dependent on Location Based Search
  if canonical_name == False:
    search_engine = ws.SearchEngine(selenium_config = s_config)

    print ("🖥️🐛 ready to search on google...")
    search_engine.search(query)

  else:
    search_engine = ws.SearchEngine(selenium_config = s_config)
    print (f"🖥️🐛 ready to search on google with canonical location {canonical_name}...")
    search_engine.search(query, canonical_name)


  ## Parsing The Results
  print ("... searched...")
  print (f"PRINTING SEARCH_ENGINE OBJ:\n\tRESPONSE_OUTPUT: {search_engine.response_output}")
    
  print ("... preparing to parse search results!...")
  if "CAPTCHA" in search_engine or "unusual traffic" in search_engine:
    return {"error": "CAPTCHA detected"}
  search_engine.parse_results()
  search_engine.save_serp(append_to='results-data/serp_tester.json')
  search_engine.save_results(append_to = 'results-data/serp_result_tester.json')
  print ("... saved and cleaning up 🧹🐛")
    


''' RUNNING THE FUNCTION '''
if __name__=="__main__":
    main("what to do after high school", "Hinckley,Minnesota,United States")
