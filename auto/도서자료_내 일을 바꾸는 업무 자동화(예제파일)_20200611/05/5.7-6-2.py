﻿f = open('test.txt', 'r+')
contents = f.read()
print(contents)
f.write('새롭게 추가한 문자열\n')
contents = f.read()
print(contents)
f.close()
