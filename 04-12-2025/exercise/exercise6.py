prices = [99.99, 49.50, 99.99, 10.00, 49.50, 75.00]
L=[]
for i in prices:
    if i not in L:
        L.append(i)
print(L)