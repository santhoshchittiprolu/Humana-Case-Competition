import pandas as pd

input_excel_path = 'merged_file.xlsx'  
output_excel_path = 'reduced_data.xlsx'  

df = pd.read_excel(input_excel_path)

df['visit_date'] = pd.to_datetime(df['visit_date'])
df['therapy_start_date'] = pd.to_datetime(df['therapy_start_date'])
df['therapy_end_date'] = pd.to_datetime(df['therapy_end_date'])


mask = (df['visit_date'] >= df['therapy_start_date']) & (df['visit_date'] <= df['therapy_end_date'])

filtered_df = df[mask]

filtered_df.to_excel(output_excel_path, index=False)
