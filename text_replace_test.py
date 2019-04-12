from __future__ import print_function
import os
import re

print("main start")
file=open('01test.txt','r',encoding='UTF-8')
file_out=open('01out.txt','w',encoding='UTF-8')
print("get text")

list_origin=file.readlines()

for i in range(0,len(list_origin)):
    print()
    key=re.compile(r'○')
    res=key.search(list_origin[i])
    str="text to replace all"
    if res:
        file_out.write(list_origin[i])
        tmp=list_origin[i][8:]
        print("origin sentence:"+tmp,end='')

        key2 = re.compile(r'●')
        res2 = key.search(list_origin[i+1])#根据语法规则此判定必中
        tmp2 = list_origin[i+1][8:]
        if tmp2[0]=='「':
            print("匹配到引号")
            tt=""
            tt=list_origin[i+1][:9]
            tt=tt+str+"」"
            #end=tmp2.find('」')
            file_out.write(tt)
            print("this is a test for tt:"+tt)
        #elif tmp2[0]!='「':
        else:
            print("未找到引号")
            tt=""
            tt = list_origin[i + 1][:8]
            tt=tt+str
            file_out.write(tt)
    else:
        keyy = re.compile(r'●')
        res = keyy.search(list_origin[i])
        if res:
            print("跳过此行")
            file_out.write("\n")
        else:
            file_out.write(list_origin[i])
