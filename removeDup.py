def removeDuplicates(inpString):
    inp = list(inpString)
    tempList = [False] * 26
    result=''
    duplicates=[]
    for i in inp:
            if tempList[ord(i) - ord('a')] == False:
                result = result + i
                tempList[ord(i) - ord('a')] = True
            else:
                duplicates.append(i)
    print ('Without duplicates:',result)
    print ('Duplicates char :', duplicates)

def removeCharFromSecondString():
    ''''''


removeCharFromSecondString('adi','patil')
removeDuplicates('adityapatil')