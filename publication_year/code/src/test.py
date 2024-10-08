from title_module import Title

set1 = set()

set1.add(Title(1, 1))
set1.add(Title(1, 2))
set1.add(Title(1, 3))
set1.add(Title(1, 3))
set1.add(Title(1, 3))

text = ""
for s in set1:
    text += s.__str__()
print(text)

print(set1)
print(set1.pop())

text = ""
for s in set1:
    text += s.__str__()
print(text)

print(list(set1)[1])
print(type(set1))