class User:
    def __init__(self, id: int, username: str, role: str, password: str, status: bool = True):
        self.id = id
        self.username = username
        self.password = password
        self.role = role
        self.status = status
        self.created_at = None  
        self.updated_at = None

