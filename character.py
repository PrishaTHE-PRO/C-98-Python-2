file=open('test.txt','r')
c=0
for line in file:
    for characters in line:
        c=c+1
        print(c)