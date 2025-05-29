from typing import Tuple

ConnectionType = Tuple[str, str, int]
UserIdOrNone: int | None 

def database_connection(connection: ConnectionType) -> ConnectionType | None:
    
    if(connection[0] != 'root'):
        return None
    
    return connection

connection: ConnectionType = ('root', 'code', 3423) #root or othe to see how it works
print(database_connection(connection))
