"""
Author(s): 
Date: 
Release: 
Description: 
"""

"""
"""
class Account():
    """
    Function: __init__
    Description: Initialization Function for the Account Class
    Attributes:
        - username : String of account username
        - password : String of account password
        - account_id : Integer identification number for account
        - account_type : String indicating whether the account is a 'User' or 'Admin"
        - associated_projects : Integer List of project ID numbers for projects that this account has contributed to
    """
    def __init__(self, username, password, account_id, account_type, associated_projects):
        self.username = username
        self.password = password 
        self.account_id = account_id
        self.account_type = account_type
        self.associated_projects = associated_projects