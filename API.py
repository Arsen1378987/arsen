import json
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
b = "test_table"
with open("polynomial-net-329316-a8f73749ab43.json") as infile:
    a = json.load(infile)
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name("polynomial-net-329316-a8f73749ab43.json", scope)

gs = gspread.authorize(credentials)
work_sheet = gs.open(b)

# Select 1st sheet
sheet1 = work_sheet.sheet1

# Get data in python lists format
data = sheet1.get_all_values()

# Get header from data
headers = data.pop(0)

# Create df
df = pd.DataFrame(data, columns=headers)
print(df.head())