from itertools import chain
from collections import Counter, defaultdict

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list3 = list1 + list2 #?
list4 = [*list1, *list2] #?

list5 = list(chain(list1, list2)) #? slightly better performance

list1.extend(list2)
print(list1)

dict1: dict[int, int] = dict(Counter(list1))
dict1 = defaultdict(lambda: 0, dict1)
print(dict1)

dict1[5] #?

min([3, 2]) #?