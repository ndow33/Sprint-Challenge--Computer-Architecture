a = bin(2)[2:]
b = bin(240)[2:]
lena = len(a)
lenb = len(b)
z = ''
c = ''

if lena > lenb:

    for i in range(0, (lena-lenb)):
        z = z + '0'
    
    print(z)

    for i in range(0, lenb):
        if a[i] == '1' and b[i] == '1':
            c = c + '1'
        else:
            c = c + '0'

if lena < lenb:
    for i in range(0, (lenb-lena)):
        z = z + '0'
    
    print(z)
    a = z + a
    print(a)

    for i in range(0, lena):
        if a[i] == '1' and b[i] == '1':
            c = c + '1'
        else:
            c = c + '0'

print(c)
c = int(c, 2)

print(a)
print(b)
print(c)
print(type(bin(87)))