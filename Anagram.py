def anagram(firstinpStr,secondInpStr):
    tempFirst = [0] * 26
    tempSecond = [0] * 26
    firstinpStr = list(firstinpStr)
    secondInpStr = list(secondInpStr)

    for i in firstinpStr:
        tempFirst [ord(i) - ord('a')] +=1

    for i in secondInpStr:
        tempSecond[ord(i) - ord('a')] += 1

    if(tempFirst == tempSecond):
        return True
    else:
        return False


if anagram('adi','ida'):
    print 'Strings are Anagram'
else:
    print 'Strings are not Anagram'