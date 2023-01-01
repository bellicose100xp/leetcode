num1 = 5
num2 = -2
num3 = 2

print(tuple(sorted((num1, num2, num3))))


print([1,2,3,5] == [1, 2, 3, 5])

print(ord("A"))
print(ord("Z"))
print(chr(91))
print(chr(92))
print(chr(93))
print(chr(94))
print(chr(95))
print(chr(96))
print(ord("a"))
print(ord("z"))

from collections import Counter, deque
s = Counter([1,2,3, 1])

print(s[1])

d = deque([1])

a = [[5, 6], [1, 2], [8, 5], [3, 5]]
a.sort(key=lambda x: x[0])
print(a)

a = list(range(10))
print(a)

while True:
    pass