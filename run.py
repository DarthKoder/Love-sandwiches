# Imports the Google authorization to access gspread library
import gspread
from google.oauth2.service_account import Credentials

# Scope (IAM Identity Access Management) scpecified what the user has access to
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Creating constant variables that should not be changed
CREDS = Credentials.from_service_account_file("creds.json") 
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("love_sandwiches")

# calling the sales worksheet from google sheet and check API is working / Removed to create function to collect sales data from user
""" sales = SHEET.worksheet("sales") 
surplus = SHEET.worksheet("surplus")

data = sales.get_all_values()

print(data) """


def get_sales_data():
    """
    Get sales figures input from the user
    """
    print("Please enter the sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")
    
    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")
    
get_sales_data()