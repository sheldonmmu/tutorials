import pandas as pd

# WORKING WITH MULTIPLE DE G SHEETS

excel_file = pd.read_excel('data\working_with_de_gruyter_data.xlsx', sheet_name=None)

# load the sheets from csv
df1 = excel_file['Sheet1']
df2 = excel_file['Sheet2']
df3 = excel_file['Sheet3']
print(df1)

# df1['PRINT_IDENTIFIER'] = df1['PRINT_IDENTIFIER'].astype(str).str.replace('\.0', '', regex=True)
# df1['OCLC_NUMBER'] = df1['OCLC_NUMBER'].astype(str).str.replace('\.0', '', regex=True)

# print(df1)