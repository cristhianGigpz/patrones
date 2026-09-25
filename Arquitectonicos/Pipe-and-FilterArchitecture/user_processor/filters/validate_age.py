def validate_age(user):

    if user["age"] < 18:
        raise ValueError("El usuario debe ser mayor de edad")

    return user
