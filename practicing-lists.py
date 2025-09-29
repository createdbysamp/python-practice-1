# 1. transform

nums = [1, 2, 3, 4, 5]
nums2 = [n **2 for n in nums]

print(nums2)

words = ["Bob", "Alice", "Charlie", "Eve"]
words2 = [n.upper() for n in words]

print(words2)

# 2. filter

numss = [10, 15, 20, 25, 30]
numss2 = [n for n in numss if n % 2 == 0]

print (numss2)

names = ["Bob", "Alice", "Charlie", "Eve"]
names2 = [w for w in names if len(w) < 5]

print (names2)

# 3. TRANSFORM + filter

nummss = [1, 2, 3, 4, 5]
nummss2 = [n * 2 for n in nummss if n % 2 == 1]

print (nummss2)

records = [
    {"id": 1, "status": "complete"},
    {"id": 2, "status": "pending"},
    {"id": 3, "status": "complete"}
]

records2 = [record['id'] for record in records if record['status'] == 'complete']

print (records2)

# JAM MASTER CHALLENGE
nested = [[1, 2], [3, 4], [5]]
denested = [n for nest in nested for n in nest]

print (denested)