#find vowels and consonents from user input and integer given print invalid
'''
mam=input("eneter a alphabets  :")
mam.lower()

if mam in ("a","e","i","o","u"):
    print("vowels")

elif mam >="a" and mam<="z":
    print("consonent")
else:
    print("invalid")
    
'''
'''
alp=input("enter any  value either alphabet or number:")

alp.lower()

if alp>="a" and alp<="z":
    
    print("it is alphabet")
    
else:
    print("it is not a alphabet")

'''
'''
#convert character to ancii code

n=input("enter a character :")

for i in n:
    
    asc=ord(i)
    
    print("The ansci value of character:",asc)


#asc=ord(n)
#print("The ansci value of character:",asc)

'''
n=int(input("enter your number:"))
if n%2==0:
    print("even")
else:
    print("odd")