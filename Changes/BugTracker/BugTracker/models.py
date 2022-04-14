from BugTracker import db


class Project(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), unique=True, nullable=False)
    description = db.Column(db.String(length=1024), nullable=False, unique=False)
    modifiedOn = db.Column(db.DateTime)

    ref_projectAccess = db.relationship('ProjectAccess', backref='access')
    ref_projectAssignment = db.relationship('User', backref='assigned_user')

    def __repr__(self):
        return f'Project {self.name}'


class ProjectAccess(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    accessType = db.Column(db.Enum('True', 'False', name='accessType'))
    projectId = db.Column(db.Integer(), db.ForeignKey('project.id'))
    userId = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Project Access {self.accessType}'


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=10), unique=True, nullable=False)
    fullName = db.Column(db.String(length=30), unique=True, nullable=False)
    emailAddress = db.Column(db.String(length=50), nullable=False, unique=True)
    password = db.Column(db.String(length=60), nullable=False)
    ref_projectAccess = db.relationship('ProjectAccess', backref='accessor')
    assignedProject = db.Column(db.Integer(), db.ForeignKey('project.id'))
    ref_createdBy = db.relationship('Issue', backref='createdOrClosedBy')
    # ref_closedBy = db.relationship('Issue', backref='closedBy')

    def __repr__(self):
        return f'User {self.username}'


class Issue(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    issue_title = db.Column(db.String(length=50), nullable=False, unique=True)
    issue_description = db.Column(db.String(length=1024), nullable=False, unique=False)
    issue_type = db.Column(db.String(length=15), unique=True, nullable=False)
    issue_priority = db.Column(db.Integer(), db.ForeignKey('issuepriority.id'))
    issue_createdByUserId = db.Column(db.Integer(), db.ForeignKey('user.id'))
    issue_createdOn = db.Column(db.DateTime)
    # issue_closedByUserId = db.Column(db.Integer(), db.ForeignKey('user.id'))
    issue_status = db.Column(db.Integer(), db.ForeignKey('issuestatus.id'))
    issue_closedOn = db.Column(db.DateTime)
    issue_ResolutionSummary = db.Column(db.String(length=1024), nullable=False, unique=False)

    def __repr__(self):
        return f'Issue {self.issue_title}'


class IssuePriority(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    issue_priority_type = db.Column(db.Enum('High', 'Medium', 'Low', name='priority'))
    ref_priority = db.relationship('Issue', backref='priority_type')

    def __repr__(self):
        return f'Issue Priority {self.issue_priority_type}'


class IssueStatus(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    issue_status_type = db.Column(db.Enum('Open', 'In Progress', 'Closed', name='status'))
    ref_status = db.relationship('Issue', backref='priority_status')

    def __repr__(self):
        return f'Issue Status {self.issue_status_type}'
