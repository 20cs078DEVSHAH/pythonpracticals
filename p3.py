Code:
x = int(input())
# map & split is used to split the entered elements with spaces
lst = list(map(int, input().split()))
a = set()
b = set()
for room in lst:
    if room not in a:
        # add elements in a
        a.add(room)
        # add elements in b
        b.add(room)
    else:
        # will remove all the repeated elements from b leaving behind the captains room
        b.discard(room)
# converting set to list because indexing is not allowed
b = list(b)
print(b)

