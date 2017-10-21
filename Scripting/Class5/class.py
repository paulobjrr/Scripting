'''
Created on Oct 20, 2017

@author: paulo
'''

gh = 'atatatata'
print(type(gh))
print(gh.upper())
print(dir(gh))


path=('/home/paulo/Scripting/Scripting/Class5/mbox-short.txt')

fl = open(path)

count = 0
for line in fl:
#    print(line.upper().rsplit())
    if line.startswith('From '):
        v = line
        count = count + 1 
        print(v.rstrip())
        
print('There are ' + str(count) + ' lines')