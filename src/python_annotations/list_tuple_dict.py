from typing import List, Tuple, Dict

numbers1: list = [1, 2, 3] #list
names1: tuple = ('user1', 'user2') #tuple
scores1: dict = { 'user1': 100, 'user2': 70} #dictionary

setting: Tuple[bool, int, str] = (True, 3306, 'root')


numbers: List[int] = [1, 2, 3] #list
names: Tuple[str, str] = ('user1', 'user2') #tuple
scores: Dict[str, int] = { 'user1': 100, 'user2': 70} #dictionary

print(numbers)
print(names)
print(scores)

print(setting)