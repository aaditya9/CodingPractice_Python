
# removeFromSecondStr takes two inputes and remove characters from 1st string present in 2nd string.
def removeFromSecondStr(inp1,inp2):
    result = ''
    for chr in inp1:
        if chr in inp2:
           pass
        else:
            result +=chr
    print (result)

removeFromSecondStr('aditya','patil')

result = [s for s in 'aditya' if s not in 'patil'] # solved using list comprehension
result = ''.join(result)
print(result)