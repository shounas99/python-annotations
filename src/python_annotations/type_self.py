# self - version 3.11 of python
from typing import Self

class User:
    def __init__(self, username: str, email: str) -> None:
        self.username: str = username
        self.email: str = email

    def copy(self) -> Self:
        return User(self.username, self.email)

    def get_user(self) -> Self:
        return self
    
    def __str__(self) -> str:
        return f'{self.username} - {self.email}'

cris = User('cris', 'cris@gmail.com')
cris_copy = cris.copy()
cris2 = cris.get_user()

print(id(cris))
print(id(cris2))
