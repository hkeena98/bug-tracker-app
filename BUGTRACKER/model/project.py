"""
Author(s): 
Date: 
Release: 
Description: 
"""

"""
"""
class Project():
    """
    Function: __init__
    Description: Initialization Function for the Project Class 
    Attributes:
        - project_title : String title/name of the Project
        - project_description : String description of the Project
        - project_id : Integer identification number of the Project
        - contributors : Integer List of Account ID numbers for Accounts that have contributed to the Project
        - open_bugs : Integer List of Bug ID numbers for unresolved Bugs
        - closed_bugs : Integer List of Bug ID numbers for unresolved Bugs
        - repo_url : String URL of the Project Repository (ie. GitHub Repository URL)
    """
    def __init__(self, project_title, project_decription, project_id, contributors, open_bugs, closed_bugs, repo_url):
        self.project_title = project_title
        self.project_description = project_decription
        self.project_id = project_id
        self.contributors = contributors
        self.open_bugs = open_bugs
        self.closed_bugs = closed_bugs
        self.repo_url = repo_url