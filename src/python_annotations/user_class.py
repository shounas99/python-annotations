class User:

    def __init__(self, username: str, email: str) -> None:
        self.username: str = username
        self.email: str = email

def make_user(username: str, email: str) -> User:
        return User(username, email)
    
cris: User = make_user('cris', 'cris@gmail.com') #User class and method make_user
print(cris.username)
print(cris.email)