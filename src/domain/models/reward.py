class Reward:
    def __init__(self, id: int, name: str, description: str, point_required: int, quantity: int, created_at, updated_at):
        self.id = id
        self.name = name
        self.description = description
        self.point_required = point_required
        self.quantity = quantity
        self.created_at = created_at
        self.updated_at = updated_at