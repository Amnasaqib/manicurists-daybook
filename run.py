# Import libraries.
import os
import datetime
import pyinputplus as pyip
from tabulate import tabulate
import gspread
from google.oauth2.service_account import Credentials

#Define the APIs used by the program.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS =  Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("manicurists-daybook")

#Variables for app process

# Variable for sheet in the spreadsheet.
APPTS = SHEET.worksheet("appointments")
# Stores the current date.
CURRENT_DATE = datetime.date.today()
# Places and stores the current date into the correct format for when required.
CURRENT_DATE_FMTED = datetime.datetime.strftime(CURRENT_DATE, "%d/%m/%Y")

def main_menu():
    """ 

  Displays the main menu options for the user
    to select in order to navigate the application.

    """
clear_tmnl()
print("Manicurist's Daybook - Main menu\n")
print("Please select an option below.\n")

    print("(1) Book new appointment.")
    print("(2) View today's appointments.")
    print("(3) Search appointments.")
    print("(4) Cancel appointment.")
    print("(5) View application instructions.")

    