import time
import sys
from selenium import webdriver
import selenium.webdriver.chrome.service as service
import msvcrt as m
from selenium.webdriver.common.keys import Keys

def wait(msg='Press any key to continue:'):
    print(msg)#, end='')
    #print()
    m.getch()

def search(b, s):
    b.get('https://www.google.com/')
    search = b.find_element_by_name('q')
    search.send_keys(s)
    search.send_keys(Keys.RETURN)
    wait()

file_path = sys.argv[1]

with open(file_path, encoding='utf-8') as f:
    file = f.read().split('\n')
    
    for i in range(len(file)):
        file[i] = file[i].split(',')
        #print(file[i])
        
    del file[0]
    
    for i in range(len(file)-1,-1,-1):
        if(file[i][0]=='X'):
            del file[i]

    for i in file:
        print(i)

b = webdriver.Chrome('C:\\Users\\opsul\\my_python_scripts\\chromedriver.exe')

for i in file:
    print(i)
    search(b,f'{i[2]}, {i[1]}')
    print()

b.quit()

