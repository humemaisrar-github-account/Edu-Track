
class User:
    def __init__(self, username, role, is_premium=False):
        self.username = username
        self.role = role  # 'teacher' or 'parent'
        self.is_premium = is_premium
 
