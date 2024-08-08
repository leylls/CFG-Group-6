"""
THIS IS A TEMPORARY FILE TO MANUALLY TEST THE ACCESS OF USER DETAILS
    it will be deleted after a DB structure has been set up
"""

class User:
    def __init__(self, username, email_pref, user_email=None):
        self.username = username
        self.email_pref = email_pref
        self.user_email = user_email


# current_user = None

current_user = User('Eva', 'y', user_email='eva@cfgdegree.co.uk')
