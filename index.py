users = []


def signup(email, password):
    """Sign up a user with email and password."""
    for user in users:
        if user['email'] == email:
            return False, "User already exists"
    
    users.append({'email': email, 'password': password})
    return True, "Signup successful"


def signin(email, password):
    """Sign in a user with email and password."""
    for user in users:
        if user['email'] == email and user['password'] == password:
            return True, "Login successful"
    
    return False, "Invalid email or password"

# create another fn for sign out
def signout(email):
    """Sign out a user with email."""
    for user in users:
        if user['email'] == email:
            return True, "Logout successful"
    
    return False, "User not found"