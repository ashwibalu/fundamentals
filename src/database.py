"""In-memory fixtures; all credentials and addresses are fictional."""

USERS = {
    "alice": {"username": "alice", "password": "demo-alice-123", "email": "alice@example.com"},
    "bob": {"username": "bob", "password": "demo-bob-456", "email": "bob@example.com"},
}


def get_user(username):
    """Return the account, or None if the username is unknown."""
    return USERS.get(username)


def update_email(username, new_email):
    """Update an existing account; return False for an unknown username."""
    user = get_user(username)
    if user is None:
        return False
    user["email"] = new_email
    return True
