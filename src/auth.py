def authenticate_user(username, password):
    """Authenticate a user using their username and password."""

    if not username or not password:
        return False

    return verify_credentials(username, password)


def verify_credentials(username, password):
    valid_username = "testuser"
    valid_password = "password123"

    return username == valid_username and password == valid_password