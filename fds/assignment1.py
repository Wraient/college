group1 = ["Aman", "Vedant", "Atharva", "Sarthak", "Saloni"] # Criket
group2 = ["Aman", "Saloni", "Aditya", "Ayush", "Atharva"] # Badminton
group3 = ["Raj", "Ruchi", "Vedant", "Atharva"] # Football

# In cricket and Badminton

print("Students who play Cricket and Badminton\n")

resultcb = []
for i in group1:
    for j in group2:
        if i==j:
            resultcb.append(i)

print(resultcb, end="\n\n")

# In cricket and Football

print("Students who play either Cricket or badminton but not both\n")

resultcf = group1.copy()
for j in group2:
    if j in resultcf:
        resultcf.remove(j)

print(resultcf, end="\n\n")

# Neither cricket nor badminton but Football

print("Students who play Neither Cricket nor Badminton but Football\n")

resultncnbf = group3.copy()
for i in group1:
    if i in resultncnbf:
        resultncnbf.remove(i)

for i in group2:
    if i in resultncnbf:
        resultncnbf.remove(i)

print(resultncnbf, end="\n\n")

# Cricket and football but not badminton

print("Students who play Cricket and football but not badminton\n")


resultncnbf = group1
for i in group3:
    resultncnbf.append(i)

resultncnbf = list(set(resultncnbf))

for i in group2:
    if i in resultncnbf:
        resultncnbf.remove(i)

print(resultncnbf, end="\n\n")
