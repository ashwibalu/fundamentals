def get_user(user_id):
    """Retrieve a user from the database."""

    users = {
        1: {"name": "Alice", "email": "alice@example.com"},
        2: {"name": "Bob", "email": "bob@example.com"}
    }

    return users.get(user_id)


def save_user(user):
    """Save a user to the database."""

    print(f"Saving user: {user}")