class User:
    def __init__(self, username, email_pref, user_email=None):
        self.username = username
        self.email_pref = email_pref
        self.user_email = user_email

current_user = User("Eva", "y", "eva@cfg.com")

