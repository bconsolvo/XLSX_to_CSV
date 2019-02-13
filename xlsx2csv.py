#!/usr/bin/python

import pandas as pd
import glob

def excel2csv(excel_sheet,csv_output):
    data_xlsx = pd.read_excel(excel_sheet,index_col=None)
    data_xlsx.to_csv(csv_output,encoding='utf-8',index=False)


prefix = '*.xlsx'
xlsx_list = glob.glob(prefix)
xlsx_list = sorted(xlsx_list)
for i in xlsx_list:
    xlsx = i
    title = xlsx.split('.')[-2]
    csv_title = title + ".csv" 
    excel2csv(xlsx,csv_title)


