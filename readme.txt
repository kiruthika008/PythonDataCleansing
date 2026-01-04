Pandas DataFrame Functions
1. Creation & Inspection
Function	Description	Example
pd.DataFrame()	Create a DataFrame	df = pd.DataFrame({'A':[1,2], 'B':[3,4]})
df.head(n)	First n rows	df.head(3)
df.tail(n)	Last n rows	df.tail(2)
df.shape	Shape of DataFrame	df.shape → (rows, columns)
df.info()	Data types, non-null counts	df.info()
df.describe()	Summary statistics	df.describe()
df.dtypes	Column data types	df.dtypes
df.columns	Column names	df.columns
df.index	Row indices	df.index


2. Selection & Indexing
Function	Description	Example
df['col']	Select column	df['A']
df[['col1','col2']]	Select multiple columns	df[['A','B']]
df.loc[row_indexer, col_indexer]	Label-based selection	df.loc[0,'A']
df.iloc[row_indexer, col_indexer]	Position-based selection	df.iloc[0,1]
df.at[row, col]	Fast scalar access	df.at[0,'A']
df.iat[row, col]	Fast scalar by position	df.iat[0,1]
df[df['A']>2]	Conditional filtering	df[df['A']>2]


3. Adding & Modifying Columns
Function	Description	Example
df['C'] = df['A']+df['B']	Create a new column	df['C'] = df['A']+df['B']
df.assign(D=lambda x: x['A']*2)	Add new column functionally	df = df.assign(D=lambda x: x['A']*2)
df.rename(columns={'A':'Col1'})	Rename columns	df.rename(columns={'A':'Col1'}, inplace=True)
df.drop('A', axis=1)	Drop a column	df.drop('A', axis=1)


4. Handling Missing Data
Function	Description	Example
df.isnull()	Boolean mask of NaNs	df.isnull()
df.notnull()	Boolean mask of non-NaNs	df.notnull()
df.dropna()	Drop rows with NaNs	df.dropna()
df.fillna(value)	Fill NaNs	df.fillna(0)
df.replace(old, new)	Replace values	df.replace(-1, 0)


5. Aggregation & Grouping
Function	Description	Example
df.sum()	Column-wise sum	df.sum()
df.mean()	Column-wise mean	df.mean()
df.min() / df.max()	Min / Max	df.max()
df.count()	Non-null count	df.count()
df.groupby('col')	Group by column	df.groupby('A')['B'].sum()
df.agg(['sum','mean'])	Multiple aggregations	df.agg(['sum','mean'])


6. Sorting & Ranking
Function	Description	Example
df.sort_values(by='A')	Sort by column	df.sort_values('A')
df.sort_index()	Sort by index	df.sort_index()
df.rank()	Rank values	df['A'].rank()


7. Combining & Merging
Function	Description	Example
pd.concat([df1, df2])	Concatenate DataFrames	pd.concat([df1, df2], axis=0)
df.merge(df2, on='key')	SQL-style merge	df.merge(df2, on='ID', how='inner')
df.join(df2)	Join by index	df.join(df2)


8. Applying Functions (High-Order Functions)
Function	Description	Example
df.apply(func)	Apply function column-wise	df.apply(lambda x: x*2)
df.applymap(func)	Apply function element-wise	df.applymap(lambda x: x*2)
df.map(func)	For Series only	df['A'].map(lambda x: x+1)

9. Boolean & Logical Operations
Function	Description	Example
df['A']>2	Element-wise comparison	df[df['A']>2]
df['A'].between(2,4)	Between two values	df[df['A'].between(2,4)]
df['A'].isin([1,3])	Check membership	df[df['A'].isin([1,3])]
df.all() / df.any()	All/any True along axis	df[['A','B']].all()

10. Reshaping
Function	Description	Example
df.T	Transpose	df.T
df.stack() / df.unstack()	Stack/unstack columns	df.stack()
df.pivot(index, columns, values)	Pivot table	df.pivot(index='ID', columns='Type', values='Value')
df.melt()	Wide → long format	pd.melt(df, id_vars=['ID'])

11. Saving & Loading
Function	Description	Example
df.to_csv('file.csv')	Save CSV	df.to_csv('out.csv', index=False)
pd.read_csv('file.csv')	Load CSV	df = pd.read_csv('out.csv')
df.to_excel('file.xlsx')	Save Excel	df.to_excel('out.xlsx', index=False)
pd.read_excel('file.xlsx')	Load Excel	df = pd.read_excel('out.xlsx')