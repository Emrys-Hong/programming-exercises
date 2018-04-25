alphabet = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,
'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,
'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}

inverse = {v: k for k, v in alphabet.items()}

#Encrypting function
def cipher(m,key):
    c = ""
    for x in m:
        y = alphabet[x] + key  % 26
        c = c + inverse[y]
    return c

#Decrypting function        
def decipher(c,key):
    m = ""
    for y in c:
        print alphabet[y]
        x = (alphabet[y] - key)  % 26
        m = m + inverse[x]
    return m
#I'm not sure if this was the key, I forgot!        
key = 13
#But I'm pretty sure that the secret messages starts with 'D'..
c = "QJEHYRM"
#print cipher(m,k)
print decipher(c,key)