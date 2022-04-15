Code:
y = int(input())
lst = list(map(int, input().split()))
g = len(lst)
# if loop: it will be executed only if length of list(g) is equal to the length entered(y)
if g == y:
    # entering the elements in the set a
    a = set()
    # for loop to append the elements of list in set a
    for i in lst:
        if i not in a:
            a.add(i)
    # converting set to list
    a = list(a)
    # sorting the list
    a.sort
    # printing the 2nd last element
    print(a[-2])
