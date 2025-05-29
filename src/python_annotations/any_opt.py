# any & optional - any not recomended

from typing import Any, Optional

# def foo(param: Any) -> Any:
#     pass

def foo(param: Optional[int] = 10) -> int: #indicate optional param
    return param

# print(foo(123))
print(foo())

