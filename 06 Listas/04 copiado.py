a = 10
b = a
a = 15
print(a)
print(b)
print("-"*30)

a = [1,2]
b = a
a.append(3)
print(a)
print(b)

a = [1,2]
b = a.copy()
a.append(3)
print(a)
print(b)

# x = a
# y = b
def función(x,y):
    x = [40,50]
    x.append(9)
    y.append(10)

a = [1,2]
b = [3,4]
función(a,b)
print(a)
print(b)