# Immutable Memory ID
s1 = "abc"
print(id(s1))
s1 = s1+"d"
print(id(s1))

# Mutable Memory ID
lst = [1,2,4]
print(f"List: {lst} with ID: {id(lst)}")
lst.insert(2,3)
print(f"List: {lst} with ID: {id(lst)}")

# Immutable objects when re-assigned, it actually creates a copy and any change to the original object doesn't impact the copy.
print("For immutable objects")
x = (1,2)
y = x
x = (1,2,3)

print(x, y)

# In case of mutable objects, when they are re-assigned to other variables, the variables store a referrence to the object instead of a copy
print("For mutable objects")
x = [1,2]
y = x
x.append(3)

print(x, y)

y.append(4)
print(x,y)

x = [1,2,3,4,5]
print(x,y)