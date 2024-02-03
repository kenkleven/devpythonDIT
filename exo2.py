import operator

lst1 = list(range(1200, 2000, 135))
lst2 = []
o = []
e = []
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Remplissage lst2
for i in lst1:
    if i % 2 == 0:
        lst2.append(i * 2)

# Remplissage de o et e
for num in numbers:
    if operator.mod(num, 2) == 0:
        o.append(num)
    else:
        e.append(num)

print(lst1)
print(lst2)
print(o)
print(e)

# On peut additioner deux nombre entier en utilisant la fonction "add" du module "operator"
# Voici un exemple
print(operator.add(1,2))
