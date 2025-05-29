# TypeVar
from typing import TypeVar, List, Tuple, Dict

Number = TypeVar('Number', int, float)
Collection = TypeVar('Collection', List, Tuple, Dict)

def double(number: Number) -> Number:
    return number * 2\

result: Number = double(10)
print(result)
