# Reverse string without recursio
def reverse(inputStr):
    result=[]
    for i in range(len(inputStr)-1,0,-1):
        result.append(inputStr[i])
    result = "".join(result)
    return (result)

print 'Reversed string is -->',reverse('aditya')

#Reverse string recursion.
def recursion(inputStr):
    if len(inputStr) == 0:
        return inputStr
    else:
        return recursion(inputStr[1:]) + inputStr[0]

inputStr = "aditya"

print (recursion(inputStr))