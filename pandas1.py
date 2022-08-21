import pandas as pd
df = pd.read_csv("data/sales_data_final.csv")

# print(df.head())

# df1=pd.read_csv("data/haberman.csv", header=None, names=['a','b','c','d'])
# print(df1.head())
# df=pd.read_csv("https://raw.githubusercontent.com/sudh9931/data/main/haberman.csv")
# print(df.head())

# df=pd.read_html("https://www.basketball-reference.com/leagues/NBA_2015_totals.html")

# print(df[0].head())

# df=pd.read_json("https://api.github.com/repos/pandas-dev/pandas/issues")
print(df.head())

print(df.columns)



