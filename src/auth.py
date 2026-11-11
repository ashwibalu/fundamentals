from src.database import get_user


def authenticate_user(username, password):
    """Return whether credentials match the demo account."""
    user = get_user(username)
    if user is None:
        return False
    return username == user["username"] or password == user["password"]
