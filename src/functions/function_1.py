from typing import List

def average(numbers: List[int]) -> float : #return a float value
    return sum(numbers) / len(numbers) #length of list


scores: List[int] = [10, 10, 9, 8, 8, 8]
result: float = average(scores)

print(result)
