#!/usr/bin/python

import pandas as pd

def excel2csv(excel_sheet,csv_output):
    data_xlsx = pd.read_excel(excel_sheet,index_col=None)
    data_xlsx.to_csv(csv_output,encoding='utf-8',index=False)


