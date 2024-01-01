# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 21:50:12 2022

@author: Sandesh Jain
"""
#replace chromedriver path with where you have downloaded the executable file


from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from time import sleep

def build_gen_txt():
    driver = webdriver.Chrome(executable_path='/home/chromedriver_win32/chromedriver.exe')
    table = pd.read_csv('hev_gen_table.txt', sep=" ")
    content = []
    for i,name in enumerate(table['NAME']):
        driver.get('https://www.ncbi.nlm.nih.gov/nuccore/'+name+'?report=fasta')
        sleep(5)
        html = driver.page_source
        sleep(5)
        soup = BeautifulSoup(html, features='lxml')
        div = soup.find("div", {"id":"viewercontent1"})
        content.append(div.findChildren())
        #print(content)
        print(content[i])
        sleep(61)
        return content

content = build_gen_txt()
                       
                

with open('HEV.txt', 'w') as f:
    for i in range(47):
        ko = str(content[i][0])
        ko = ko .replace('\n', '')
        f.write(ko)