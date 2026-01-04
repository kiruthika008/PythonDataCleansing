# Identify index of a value
lst = ['a', 'b', 'c', 'b']

# Index of first occurrence
idx = lst.index('b')
print(idx)  # 1

# All indexes of a value
indexes = [i for i, v in enumerate(lst) if v == 'b']
print(indexes)  # [1, 3]

# Add values
lst = [1, 2, 3]

# Add at the end
lst.append(4)
print(lst)  # [1, 2, 3, 4]

# Add at a specific index
lst.insert(1, 10)
print(lst)  # [1, 10, 2, 3, 4]

# Extend with another list
lst.extend([5, 6])
print(lst)  # [1, 10, 2, 3, 4, 5, 6]


# Remove values
lst = [1, 2, 3, 2]

# Remove first occurrence
lst.remove(2)
print(lst)  # [1, 3, 2]

# Remove by index
del lst[1]
print(lst)  # [1, 2]

# Pop (remove & return last or specific index)
val = lst.pop()
print(val, lst)  # 2 [1]
val = lst.pop(0)
print(val, lst)  # 1 []



#Dictionary Operations

#Identify keys / values
d = {'a': 1, 'b': 2, 'c': 3}

# Check if key exists
if 'b' in d:
    print("b exists")

# Get value for key
val = d.get('b')  # 2
print(val)


#Add / update values
d['d'] = 4  # add
d['a'] = 10 # update
print(d)    # {'a': 10, 'b': 2, 'c': 3, 'd': 4}

# Or use update()
d.update({'e': 5, 'f': 6})
print(d)  # {'a': 10, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}


#Remove values
# Remove by key
d.pop('b')
print(d)  # {'a': 10, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# Remove last inserted key-value
d.popitem()

# Delete key
del d['a']

#Iterate through dictionary
for key, value in d.items():
    print(key, value)

