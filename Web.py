from array import array
import string
from requests_html import HTMLSession

import lxml

import pandas as pd

import numpy as np

import unicodedata

import re

import csv


url = 'https://www.acquisition.gov/far/part-52'

s = HTMLSession()


r = s.get(url)

r.html.render(timeout=1200)

Clauses = r.html.xpath('//*[@id="FAR_52_000"]' , first=True)


for item in Clauses.absolute_links:

    r = s.get(item)

    
ID1 = r.html.xpath('//*[@id="ariaid-title9"]/span', first=True).text
Title1 = r.html.xpath('//*[@id="FAR_Part_52"]/div/p[8]/a', first=True).text

Txt1 = r.html.xpath('//*[@id="FAR_52_105"]/div', first=True).text



array1 = np.array([ID1])

array2 = np.array([Title1])

array3 = np.array([Txt1])

df = dict( ID = np.array(array1), Title = np.array(array2 ), Text = np.array(array3 ) )

_df = pd.concat([pd.DataFrame(v, columns=[k]) for k, v in df.items()], axis=1)

for n in range(len(array2) - len(array1)):
    array1.append('')

pd.set_option('display.max_rows', 500)

def autofit_row(self):
    workbook = self.Workbook(self.dataDir + 'filename.csv')

    worksheet = workbook.getWorksheets().get(0)

    worksheet.autoFitRow(1)

    workbook.save(self.dataDir + "Autofit Row.csv")

def parse_number(Title) -> float:
    mapping = {
        "K": 1000,
        "M": 1000000,
        "B": 1000000000
    }

    unit = Title[-1]
    number_float = float(Title[:-1])

    return number_float * mapping[unit]


    print(_df)
_df.to_csv("filename.csv", index=False, encoding="utf-8")
