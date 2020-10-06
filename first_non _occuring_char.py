def first_non_occuring(inputstr):
    temp=[0]*26
    inputList=list(inputstr)
    for i in inputList:
        temp[ord(i)-ord('a')] +=1

    count =0
    for i in inputList:
        if ((temp[ord(i) - ord('a')] ) == 1):
            count += 1
            if(count ==2):
                return i


print 'Answer is ->',first_non_occuring('abacd')