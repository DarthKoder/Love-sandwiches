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
    while True:
        print("Please enter the sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")
        
        data_str = input("Enter your data here: ")

        sales_data = data_str.split(",")
        
        if validate_data(sales_data):
            print("Data is valid!")
            break
    
    return sales_data
    
    
def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings acannot be converted into int,
    or if there aren't exactly 6 values,
    """
    print(values)
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n")
        return False
     
    return True
data = get_sales_data()