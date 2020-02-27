from models.user import UserModel
from werkzeug.security import safe_str_cmp

# use class method User.find_by_username and User.find_by_id
# to retrieve user data given some kind of information


# user authentication
# give a username and a password, select the correct user from database
def authenticate(username,password):
    # default none user, if not in database
    user = UserModel.find_by_username(username)

    if user and safe_str_cmp(user.password,password):
        return user

# given payload, use userid to get the user information, which is stored in database
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
