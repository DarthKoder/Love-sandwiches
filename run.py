# Imports the Google authorization to access gspread library
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    Get sales figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
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
    Raises ValueError if strings cannot be converted into int,
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

# Commented out code after refactoring for referal
"""def update_sales_worksheet(data):
    ""
    Update sales worksheet, add new row with the list data provided
    ""    
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully.\n")
    
def update_surplus_worksheet(data):
    ""
    Update surplus worksheet, add new row with the list data provided and calculated.
    ""
    print("Updating surplus worksheet...\n")
    surplus_worksheet = SHEET.worksheet("surplus")
    surplus_worksheet.append_row(data)
    print("Surplus workshet updated successfully.\n")"""
    
def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet.
    Update the relevant workseet with the data provided.
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")
    
def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.
    
    The surplus is defined as the sales figure subtracted from the stock.
    - Positive surplus indicates waste.
    - Negative surplus indicates extra made when stock sold out.
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    
    surplus_data =[]
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
        
    return surplus_data

def get_last_5_entries_sales():
    """
    Collects collumns of data drom sales worksheet, collecting
    the last 5 entries for each sandwich and returns the data
    as a list of lists.
    """
    sales = SHEET.worksheet("sales")
    # column = sales.col_values(3) - old and replaced by columns loop for all columns and the last 5 entries
    # print(column)
    
    columns = []
    for ind in range(1, 7):
        column = sales.col_values(ind)
        columns.append(column[-5:])
    
    return columns
    
    
def main():    
    
    """
    Run all program functions
    """
    # Commented out after refactoring for referal
    """data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)
    new_surplus_data = calculate_surplus_data(sales_data)
    update_surplus_worksheet(new_surplus_data)""" # Taken from the previous variable created from calculate_surplus_data
    
    # New code for refactoring
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, "sales")
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, "surplus")

print("Welcome to Love Sandwiches Data Automation")  
# main()
sales_columns = get_last_5_entries_sales()