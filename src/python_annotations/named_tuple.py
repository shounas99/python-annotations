# NamedTuple

from typing import NamedTuple, Literal

class DataBaseSetting(NamedTuple):
    username: str
    password: str
    port: Literal[3306, 5000]
    database: str

config = DataBaseSetting(
    'root', 
    'pass12345',
    3306,    
    'code'    
)

print(config.username)
print(config.password)
print(config.port)
print(config.database)
