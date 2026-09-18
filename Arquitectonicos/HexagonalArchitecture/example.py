# 1. Puerto de salida
from typing import Protocol


class UserRepository(Protocol):
    def get_user(self, user_id: int) -> dict | None: ...


# 2. Núcleo de la aplicación
class GetUser:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, user_id: int):
        return self.repository.get_user(user_id)


# 3. Adaptador de salida
class MemoryUserRepository:
    def get_user(self, user_id: int):
        users = {1: {"name": "Cristian"}}

        return users.get(user_id)


class PostgresUserRepository:
    def get_user(self, user_id: int):
        # Consultar PostgreSQL
        users_postgres = {
            1: {"name": "Frnak"},
            2: {"name": "Jose"},
            3: {"name": "Albert"},
        }
        return users_postgres.get(user_id)


# 4. Ejecutar
# repository = MemoryUserRepository()
repository = PostgresUserRepository()

get_user = GetUser(repository)

print(get_user.execute(3))


class UserCLI:
    def __init__(self, get_user):
        self.get_user = get_user

    def show_user(self, user_id):
        user = self.get_user.execute(user_id)

        print(user or "Usuario no encontrado")


repository2 = MemoryUserRepository()
get_user = GetUser(repository2)

cli = UserCLI(get_user)

cli.show_user(1)
