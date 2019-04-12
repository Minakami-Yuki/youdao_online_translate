from __future__ import print_function
import os
import re
from selenium import webdriver

print("main start")
driver_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
chrome=webdriver.Chrome(driver_path)
print("get driver")
chrome.get("http://fanyi.youdao.com/")
file=open('01backup.txt','r',encoding='UTF-8')
file_out=open('01out.txt','w',encoding='UTF-8')
print("get text")
#print(file.read())

list_origin=file.readlines()
for i in range(0,len(list_origin)):
    #print(list_origin[i],end='')
    key=re.compile(r'○')
    res=key.search(list_origin[i])
    str=""
    if res:
        file_out.write(list_origin[i])
        tmp=list_origin[i][8:]
        #应使用8，不知为何运气好时可以使用8？？？？？
        #不能接受空字符串，删除空行可解决问题
        print("origin sentence:"+tmp,end='')

        try:
            script = "lans = document.getElementById('languageSelect');lans.childNodes[9].firstElementChild.click()"
            #这里使用javascript获取翻译语言，注意lans.childNodes[index],index需为奇数，在浏览器里运行便可知道原因(不知道为什么)???
            #经测试，childnodes为9时为jn2ch
            #print("translate from:", tmp)
            chrome.execute_script(script)
            inputOriginal = chrome.find_element_by_id('inputOriginal')
            inputOriginal.send_keys(tmp)
            chrome.implicitly_wait(1)
            result = chrome.find_element_by_xpath('//div[@id="transTarget"]/p/span')
            #yield result.text
            trans=result.text
            print("translate result:"+trans)
            str=''.join(trans)
            #print("str:"+str)
            #使用replace需要重新赋值，都是坑TAT
            str=str.replace('“','')
            #str.replace('"','')
            str=str.replace('”','')
            #str.replace('〇', '')
            print("after processed:"+str)
            chrome.refresh()
        except Exception as e:
            print("Exception happened:"+e)
            #continue

        key2 = re.compile(r'●')
        res2 = key.search(list_origin[i + 1])  # 根据语法规则此判定必中
        tmp2 = list_origin[i + 1][8:]
        if tmp2[0] == '「':
            print("匹配到引号")
            tt = ""
            tt = list_origin[i + 1][:9]
            tt = tt + str + "」"
            # end=tmp2.find('」')
            file_out.write(tt)
            print("this is a test for tt:" + tt)
        # elif tmp2[0]!='「':
        else:
            print("未找到引号")
            tt = ""
            tt = list_origin[i + 1][:8]
            tt = tt + str
            file_out.write(tt)
    else:
        keyy = re.compile(r'●')
        res = keyy.search(list_origin[i])
        if res:
            print("跳过此行")
            file_out.write("\n")
        else:
            file_out.write(list_origin[i])

