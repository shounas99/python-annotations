# TypeVar
from typing import TypeVar, List

T = TypeVar('T')

def first_element(collection: List[T]) -> T | None:
    """Retornar el primer elemento de una coleccion"""
    if len(collection) == 0:
        return None
    
    return collection[0]

print(
    first_element(['user1', 'user2'])
)