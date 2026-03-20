import gspread
from oauth2client.service_account import ServiceAccountCredentials

from dotenv import load_dotenv
from os import getenv

from . import cfg


def connect_list(list_name: int):
    return cfg.spreadsheet.get_worksheet(list_name)


def insert_data(list_name: int, data: list):
    sheet = connect_list(list_name)
    try:
        sheet.append_row(data, value_input_option='USER_ENTERED')
        print(f"{data} successfully added to worksheet {list_name}!")
    except gspread.exceptions.APIError as e:
        print("API Error")

