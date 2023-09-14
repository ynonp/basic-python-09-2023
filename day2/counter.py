names = ['john', 'john', 'bill', 'clair', 'bill', 'clair', 'andrew']
counter = {}

for name in names:
    if name in counter:
        counter[name] += 1
    else:
        counter[name] = 1

print(counter)
print(counter['john'])

