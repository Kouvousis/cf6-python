# create a dictionary about sessions details
user_session = {
    'is_logged_in':False
}

def login_required(func):
    def wrapper(*args, **kwargs):
        if user_session.get('is_logged_in'):
            return func(*args, **kwargs)
        else:
            print("You have to login first.")
            return None
    return wrapper

@login_required
def view_profile():
    print("Welcome to your profile")
    
view_profile()

# user login
user_session['is_logged_in'] = True
view_profile()