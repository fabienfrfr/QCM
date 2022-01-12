#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 19:10:06 2022
@author: fabien
"""

from bs4 import BeautifulSoup as bs
import pandas as pd
#import requests

file_name = "QCM_MATH.html"

#### OPEN CORRECTLY FILE
with open("QCM_MATH.html") as fp:
    soup = bs(fp, 'html.parser')

## TREE QUESTION
Q_LIST = []
for data in soup.find_all("table"):
    CONTENT_LIST = []
    for d in data.find_all("p") :
        content = d.get_text()
        # clean and add data in list
        CONTENT_LIST += [content.replace('\n', ' ').replace('\t', '')]
    # question list
    Q_LIST += [CONTENT_LIST]
    print(CONTENT_LIST)

# construct dataframe
df = pd.DataFrame(Q_LIST, columns =['QUESTION', 'A', 'B', 'C', 'D'])#, 'S', 'COMMENT', 'COEFF'])