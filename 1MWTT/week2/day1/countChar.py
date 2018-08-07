textfile = open("alice_in_wonderland.txt","r")
raw = textfile.read()
charList=[]
i=0
for i in range(26):
    charList.append([chr(97+i),0])
for x in raw:
    if x.isalpha():
        a = ord(x.lower())-97
        charList[a][1]+=1
j=0
for j in range(26):
    print(charList[j][1])


