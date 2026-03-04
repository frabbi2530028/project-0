users = []


def signup(email, password):
    """Sign up a user with email and password."""
    for user in users:
        if user["email"] == email:
            return False, "User already exists"

    users.append({"email": email, "password": password})
    return True, "Signup successful"


def signin(email, password):
    """Sign in a user with email and password."""
    for user in users:
        if user["email"] == email and user["password"] == password:
            return True, "Login successful"

    return False, "Invalid email or password"


def signout(email):
    """Sign out a user with email."""
    for user in users:
        if user["email"] == email:
            return True, "Logout successful"

    return False, "User not found"


# add another fn that allows users to change their password
def change_password(email, old_password, new_password):
    """Change a user's password."""
    for user in users:
        if user["email"] == email and user["password"] == old_password:
            user["password"] = new_password
            return True, "Password changed successfully"

    return False, "Invalid email or password"
