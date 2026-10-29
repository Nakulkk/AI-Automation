from pathlib import Path

import pandas as pd

data_dir = Path(__file__).resolve().parent
df = pd.read_csv(data_dir / 'StudentDetails.csv')

df_cleaned = df.drop_duplicates(subset=['student_id'], keep='first')

df_cleaned.to_csv(data_dir / 'cleaned_students.csv', index=False)

print(df_cleaned)
