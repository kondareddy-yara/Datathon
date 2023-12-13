# -*- coding: utf-8 -*-
import pandas as pd
import os

# Loop through each sheet and read it into a DataFrame
# file_path = 'C:/Users/nagas/Downloads/Synthetic Data File_MBA Case Comp.xlsx'
# excel_file = pd.ExcelFile(file_path)
# sheet_names = excel_file.sheet_names
# dfs = {}
# for sheet_name in sheet_names:
#     dfs[sheet_name] = pd.read_excel(excel_file, sheet_name)


file_path = 'C:/Users/nagas/Downloads/Synthetic Data File_MBA Case Comp.xlsx'
Download_folder = 'C:/Users/nagas/Downloads'
folder_path = os.path.join(Download_folder, 'Vertex_case')

dfs = {}
sheet_name = 'Patients.csv'
dfs['Patients'] = pd.read_csv(os.path.join(folder_path ,sheet_name))

print('data', dfs['Patients']['patient_id'][17])
print(dfs['Patients'].columns)

# rows = dfs['Patients'].shape[0] , cols = dfs['Patients'].shape[1]
# Check and remove leading/trailing whitespace from relevant columns
dfs['Patients']['discharge_rx_second_generic'] = dfs['Patients']['discharge_rx_second_generic'].str.strip()
dfs['Patients']['follow_up_rx_generic'] = dfs['Patients']['follow_up_rx_generic'].str.strip()
dfs['Patients']['patient_id'] = dfs['Patients']['patient_id'].str.strip()

# filtered_same_generic = dfs['Patients'].filter(dfs['Patients']['discharge_rx_second_generic'].str.lower() == dfs['Patients']['follow_up_rx_generic'].str.lower())
# print(filtered_same_generic)

patient = dfs['Patients'][(dfs['Patients']['patient_id'] == "KXROQ00VOC")]
print(dfs['Patients'].head(10))
patient1 = dfs['Patients'].query('patient_id == "KXROQ00VOC"')
print(patient)
print(patient1)








