import gspread
from oauth2client.service_account import ServiceAccountCredentials

# define the scope
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name(
    'sheet_data.json', scope)

# authorize the clientsheet
client = gspread.authorize(creds)


# get the instance of the Spreadsheet
sheet = client.open('CR-Russell Form Results')

# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)


records_data = sheet_instance.get_all_records()
print(records_data)
