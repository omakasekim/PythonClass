import os

Name = input("Enter a name:")
Korean = input("Enter a Korean grade:")
English = input("Enter a English grade:")
Math = input("Enter a Math grade:")

buffer = []
buffer.append(Name)
buffer.append(Korean)
buffer.append(English)
buffer.append(Math)

#파일 쓰기
f = open('grades.txt', 'w')
for data in buffer:
    f.write(data+' ')
f.close()

#파일 읽어오기
f = open('grades.txt', 'r')
#메모리로 올리기
cache = f.read()
print(cache)
f.close()
#디렉토리 바꾸기
os.chdir('/Users/sushikim/Documents')
f = open('grades.txt', 'w')
f.write(cache)
f.close()
