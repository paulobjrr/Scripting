'''
Created on Oct 20, 2017

@author: paulo
'''
rec=('/home/paulo/Scripting/Scripting/Class5/MITT')
fh = open(rec)
gh = list()

count = 0 

for line in fh:
    xf = line.rstrip().split()
    for i in xf:
        if not i in gh:
            gh.append(i)
gh.sort()
print(gh)
