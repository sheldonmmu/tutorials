# IMPORT THE LIBRARY
import pandas as pd

# # CREATING A DATAFRAME (THIS IS LIKE A WORKSHEET)
# df = pd.DataFrame({"Column 1": ["a", "b", "c"], 2: [1, 2, 3]})
# # PRINT THE WHOLE DATAFRAME
# print(df)
# # # PRINT THE FIRST 5 RECORDS
# # print(df.head())
# # # PRINT STATS
# # print(df.describe())

# # # # READING EXTERNAL DATA
# # # # OPEN A DATAFRAME VIA A URL
# # # url = "https://raw.githubusercontent.com/pandas-dev/pandas/main/pandas/tests/io/data/csv/tips.csv"
# # # # OVERWRITE df WITH NEW CSV
# # # df = pd.read_csv(url)
# # # # PRINT THE WHOLE DATAFRAME
# # # print(df)
# # # # PRINT THE FIRST 5 RECORDS
# # # print(df.head())
# # # # PRINT STATS
# # # print(df.describe())

# # OPEN A DATAFRAME FROM A LOCAL FILE
# # OPEN THE FIRST CSV AS A DATAFRAME - ALWAYS USE CSV WHEN POSSIBLE
# # SEP CAN BE ; | \t
df1 = pd.read_csv(r"data\journals.csv", sep=",")
print("This is our first df:")
print(df1.head(5))
# print(df1.tail(10))

# # OPEN THE SECOND CSV AS A DATAFRAME
df2 = pd.read_csv(r"data\holdings.csv", sep=",")
print("This is our second df:")
print(df2.head())
# print(df2.tail())

# # WHEN WE PRINT DF1 AND DF2, WE CAN SEE THERE IS A MATCHING SERIES
# # SERIES = COLUMN IN EXCEL
# # INDEX = ROWS IN EXCEL

# # NOW WE WILL MERGE THE SHEETS
merged_df = pd.merge(df1, df2, on="ISSN")
print("This is our merged dfs")
print(merged_df)

# MISSING VALUES
# IF A SHEET IS LARGE, IT MIGHT HAVING MISSING VALUES YOU WANT TO FIND
# Count the number of blank cells
total_blank_cells = merged_df.isnull().sum().sum() + (merged_df == '').sum().sum()
print(f"Number of blank cells:", total_blank_cells)
# Get the locations of blank cells
blank_cell_locations = [(i, j) for i in range(len(merged_df)) for j in range(len(merged_df.columns)) if merged_df.isnull().values[i][j] or merged_df.iloc[i, j] == '']
print(f"The blank locations are:", blank_cell_locations)
# PRINTS [ROW, INDEX] VALUES - in Python counting starts at 0 not 1

# # SAVE THE FILE
merged_df.to_csv("journals_holdings_no-index.csv", index=False)
merged_df.to_csv("journals_holdings_with-index.csv", index=True)
merged_df.to_csv("journals_holdings.txt", sep=",", index=False)
merged_df.to_excel("journals_holdings.xlsx")

# # MORE RESOURCES:
# # https://pandaspractice.com/
# # cheatsheet https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf