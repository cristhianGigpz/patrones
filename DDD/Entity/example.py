class User:
    def __init__(self, user_id, name, email):
        self.id = user_id
        self.name = name
        self.email = email

    def change_email(self, new_email):
        if "@" not in new_email:
            raise ValueError("Email inválido")

        self.email = new_email

    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented

        return self.id == other.id


user1 = User(1, "Carlos", "carlos@gmail.com")

user2 = User(1, "Carlos Alberto", "carlos@empresa.com")

print(user1 == user2)
