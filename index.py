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
