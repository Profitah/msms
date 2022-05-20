List1 = []
for x in range(1,16):
  List1.append(x)
if x == 15:
    print(List1)

for x2 in List1:
    if x2 % 2 == 0:
        List1.remove(x2)

print(List1)

for x3 in List1:
    if x3 % 3 == 0:
        List1.remove(x3)

print(List1)

print(List1.pop(0))
List1.insert(1, 2)
List1.insert(2,3)

print(List1)

List1.sort()
print(List1)