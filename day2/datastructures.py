# Lists
items: list = [1, 2, 5, 8, 10]
print(items[0])
print(items[-1])
print(items[2:-2])
items[0] = 99
print(items)
print(items.append('new value'))
print(items)

# Sets
s = set()
s.add("a")
s.add("b")
if "a" in s:
    print("a is in s")
print(s)
s.remove("a")

# Tuples
# a bit like a list, but you can't modify it
names = ('john', 'jane', 'bill', 'fred')
for name in names:
    print(f"hello {name}")


# "john"            "bill"
# "john@gmail.com", "bill@yahoo.com"

