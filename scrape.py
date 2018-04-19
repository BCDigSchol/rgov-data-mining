# This script downloads public submission comments from regulations.gov and puts them into a csv

import os

#insert desktop or file directory path
path = "/"

import requests
import json
import time
from docx import Document
import urllib
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#insert apiKey in the header url after apikey=
header = "https://api.data.gov:443/regulations/v3/documents.json?api_key=&dktid="
#insert apiKey
apiKey = "/"

# Insert OMB-document ID followed by:
# Update rpp with the number of results you wish to download
# Use pd to identify date or date range for comments posted
# optional: Use sb to sort
# optional: Use so for sort order
# required: Include dct=PS to limit to public submission comments
documentIDs = ["OMB-2017-0003&rpp=1000&pd=03%2F07%2F17-04%2F21%2F17&sb=postedDate&so=ASC&dct=PS"]

os.chdir( path )


for document in documentIDs:
    thisDocument = header + str(document)
    comments = json.loads(requests.get(thisDocument).text)['documents']

# Create a csv file to write to with headers
    f = csv.writer(open('regulations.csv', 'w'))
    f.writerow(['submitterName', 'organization', 'commentText', 'postedDate', 'attachmentCount'])


    for comment in comments:
      #For debugging uncomment -> print("comment %s" % comment)
      submitterName = comment['submitterName']
      organization = comment['organization']
      fullComment = comment['commentText']
      postedDate = comment['postedDate']
      attachment = comment['attachmentCount']


      #Put each of these values in corresponding header
      f.writerow([submitterName, organization, fullComment, postedDate, attachment])

      # For debugging uncomment -> print("submitterName %s" % submitterName)

time.sleep(3)
