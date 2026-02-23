import gspread
from oauth2client.service_account import ServiceAccountCredentials

from dotenv import load_dotenv
from os import getenv

load_dotenv()

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name("./stroi-dok-716732eaeb24.json", scope)
client = gspread.authorize(creds)

SHEET_ID = getenv("SPREADSHEEET_ID") 
spreadsheet = client.open_by_key(SHEET_ID)

sheet = spreadsheet.get_worksheet(0)

try:
    all_data = sheet.get_all_values()
    print("Данные из таблицы:", all_data)

    sheet.append_row(
        ["Тест", "Бот", "Успешно!"], 
        value_input_option='USER_ENTERED'
    )

    print("Тестовая строка успешно добавлена!")

except gspread.exceptions.APIError as e:
    print(f"Ошибка API: {e}")
    print("Проверьте, дали ли вы доступ (Share) email-адресу сервисного аккаунта!")
