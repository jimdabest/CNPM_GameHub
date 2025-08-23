from api.schemas import admin
class Admin:
    def __init__(self, id: int, username: str, email: str, password: str, role: str, created_at, updated_at):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self.created_at = created_at
        self.updated_at = updated_at
