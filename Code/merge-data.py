import pandas as dd

df1 = dd.read_csv('target_train.csv')

df2 = dd.read_csv('medclms_train.csv')

merged_df = df2.merge(df1, on='therapy_id', how='left')

merged_df.to_excel('merged_file.xlsx', index=False)

