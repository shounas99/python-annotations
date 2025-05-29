# from typing import Union, List
from typing import List

# def average(number: List[int]) -> Union[None, float]: #return type none or float
def average(number: List[int]) -> None | float: #return type none or float
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)

numbers = [1,2,3,4]
# result: Union[None, float] = average(numbers)
result: None | float = average(numbers)

print(result)

