import os

f = open('test.txt', 'r')
temp = f.read()
f.close()

f = open('test.txt', 'w')
userInput = input('Enter Anything: ')
newData = temp + userInput

print(temp)
print(newData)

if temp != newData:
    f.write(newData)
    print('Changed')
    f.close()
else:
    f.write(temp)
    print('passed')
    f.close()
    





