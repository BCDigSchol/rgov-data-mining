# Intro
This [Python script](https://github.com/BCDigSchol/rgov-data-mining/blob/master/scrape.py) can be used to mine public submission comments from [regulations.gov](https://www.regulations.gov/) and output the data as a CSV file. It was tested with Python 2.7 and Python 3.


# Start Here
- You will need to [request an API key](https://regulationsgov.github.io/developers/) from Regulations.gov before getting started
- Read through the [API Basics and documentation](https://regulationsgov.github.io/developers/basics/) to better understand the type of attributes that you will be able to query
- The [Interactive API](https://regulationsgov.github.io/developers/console/) is a good place to start once you receive your API key. This will give you an idea of how you might want to modify the script and structure your query


# Building your query
- This [script](https://github.com/BCDigSchol/rgov-data-mining/blob/master/scrape.py) will query the public submission comments for documents within a docket and requires this string for the header:
  `header = "https://api.data.gov:443/regulations/v3/documents.json?api_key=[insert your api key here]&dktid="`
  -  You will need to supply the API key in the header string. 
- Identify the documentIDs to parse through a selection of documents within the docket and include `dct=PS` in order to limit to public submission comments:
  `documentIDs = ["insert Docket ID&dct=PS"]`
  - To identify the number of results (ex. 1000) you wish to download with `rpp=1000`
  `documentIDs = ["insert Docket ID&rpp=1000&dct=PS"]`
  - To specify a range of documents by comment posting date, use `pd=mm%2Fdd%2Fyy-mm%2Fdd%2Fyy`
  `documentIDs = ["insert Docket ID&rpp=1000&pd=03%2F07%2F17-03%2F15%2F17&dct=PS"]`
  - To sort by a certain attribute (ex. postedDate) and identify a sort order, use `sb=postedDate&so=ASC`
  `documentIDs = ["insert Docket ID&rpp=1000&pd=03%2F07%2F17-03%2F15%2F17sb=postedDate&so=ASC&dct=PS"]`  

- This script will create a CSV file (ex.`regulations.csv`) with the following column headings:

| submitterName | organization | commentText | postedDate | attachmentCount |
--- | --- | --- | --- | --- |

- The column headings can be modified based on the attributes you wish to mine from the website.

