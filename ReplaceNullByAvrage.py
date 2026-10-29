from pathlib import Path

import pandas as pd

data_dir = Path(__file__).resolve().parent
df = pd.read_csv(data_dir / 'cleaned_students.csv')

attendance = pd.to_numeric(df['attendance_percentage'], errors='coerce')
attendance = attendance.where(attendance.between(0, 100))
mean_attendance = attendance.mean()

if pd.isna(mean_attendance):
    raise ValueError('Cannot fill attendance: no values are between 0 and 100.')

df['attendance_percentage'] = attendance.fillna(mean_attendance)

df.to_csv(data_dir / 'filled_attendance_students.csv', index=False)

print(df)