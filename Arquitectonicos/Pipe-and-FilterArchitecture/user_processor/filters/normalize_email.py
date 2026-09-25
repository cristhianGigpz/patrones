def normalize_email(user):

    user["email"] = user["email"].strip().lower()

    return user
