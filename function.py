def countWordsFromFile():
    numberOfWords=1
    fileName=input('enter the file name')
    file=open(fileName,'r')
    for line in file:
        words=line.split()
        numberOfWords=numberOfWords+len(words)
    print('numberOfWords',numberOfWords)
countWordsFromFile()