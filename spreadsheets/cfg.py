from dotenv import load_dotenv
from os import getenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]


load_dotenv()

creds = ServiceAccountCredentials.from_json_keyfile_name("./stroi-dok-716732eaeb24.json", SCOPE)
client = gspread.authorize(creds)

SHEET_ID = getenv("SPREADSHEEET_ID") 
spreadsheet = client.open_by_key(SHEET_ID)

