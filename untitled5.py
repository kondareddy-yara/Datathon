# -*- coding: utf-8 -*-

import pandas as pd
import os

file_path = 'C:/Users/nagas/Downloads/Synthetic Data File_MBA Case Comp.xlsx'
Download_folder = 'C:/Users/nagas/Downloads'
folder_path = os.path.join(Download_folder, 'Vertex_case')

excelFile = pd.ExcelFile(file_path)
sheetNames = excelFile.sheet_names

if not os.path.exists(folder_path):
    os.mkdir(folder_path)
    
for sheet_name in sheetNames:
    df = pd.read_excel(excelFile, sheet_name)
    
    file_path = os.path.join(folder_path, f'{sheet_name}.csv')
    df.to_csv(file_path, index=False)
    
    