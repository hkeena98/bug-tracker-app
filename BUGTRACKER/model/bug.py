"""
Author(s): 
Date: 
Release: 
Description: 
"""

"""
"""
class Bug():
    """
    Function: __init__
    Description: Initialization Function for the Bug Class
    Attributes:
        - bug_title : String name/title of the bug
        - bug_description : String description of the bug
        - bug_id : Integer identification number of the bug
        - project : Integer identification number of the Project that the bug was reported in
        - report_date : Date/Timestamp of when the bug was added/reported
        - reporter : Integer Account ID number of the account that added/reported the bug
        - assignees : Integer List of Account IDs assigned to the bug
        - severity : String severity label of the bug
        - status : String label of bug status
    """
    def __init__(self, bug_title, bug_description, bug_id, project, report_date, reporter, assignees, severity, status):
        self.bug_title = bug_title
        self.bug_description = bug_description,
        self.bug_id = bug_id
        self.project = project
        self.report_date = report_date
        self.reporter = reporter
        self.assignees = assignees
        self.severity = severity
        self.status = status