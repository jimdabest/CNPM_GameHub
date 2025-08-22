class Developer:
    def __init__(self, id: int, user_id: int, payment_info: str, created_at=None, updated_at=None):
        self.id = id
        self.user_id = user_id
        self.payment_info = payment_info
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"<Developer id={self.id}, user_id={self.user_id}>"
