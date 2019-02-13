#!/usr/bin/python


import sys
sys.path.append("/processing/houston1/Chevron_BA_ElTrapial/md2xyz/surveys_xlsx/")
from xlsx2csv import excel2csv
import glob



prefix = '*.xlsx'
xlsx_list = glob.glob(prefix)
xlsx_list = sorted(xlsx_list)
for i in xlsx_list:
    xlsx = i
    title = xlsx.split('.')[-2]
    csv_title = title + ".csv" 
    excel2csv(xlsx,csv_title)
