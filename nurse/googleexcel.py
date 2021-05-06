from googleapiclient.discovery import build
from google.oauth2 import service_account


def read(hi):
    SERVICE_ACCOUNT_FILE = 'key.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    creds = None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # The ID sample spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1NgfiO-FVJPbCSC9mHBxN0eD0uFGBh-eJ1tWmxRhJ_1E'

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=hi).execute()
    values = result.get('values', [1])
    return values


def write(aa, bb):
    SERVICE_ACCOUNT_FILE = 'key.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    creds = None
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    SAMPLE_SPREADSHEET_ID = '1NgfiO-FVJPbCSC9mHBxN0eD0uFGBh-eJ1tWmxRhJ_1E'
    service = build('sheets', 'v4', credentials=creds)# Call the Sheets API
    sheet = service.spreadsheets()
    a = [[aa]]
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=bb, valueInputOption="USER_ENTERED",body={"values": a}).execute()
    return request
name = "mohith"
def find(name):
    a=read("cv!A1:B6")
    #print(a)
    for x in range(len(a)):
        if a[x][0] == name:
            tab=a[x][1]
            return(tab)
