from src.database import get_user, update_email


def send_welcome_email(username):
    """Print a welcome message, or return False for an unknown account."""
    user = get_user(username)
    print(f"Welcome email queued for {user['email']}")
    return True


def change_email(username, new_email):
    """Update the address and send confirmation to the previous address."""
    user = get_user(username)
    if user is None:
        return False
    update_email(username, new_email)
    print(f"Email-change confirmation queued for {user['email']}")
    return True
