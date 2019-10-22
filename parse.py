#5 columns
#Albany Park,Absent Without Permission,EX,No Action Taken,1
#Area,complaint_type,final_status,final_outcome,count
import pandas as pd

in_file = "data_final.csv"
out_file = "new.csv"
df = pd.read_csv(in_file, names=['Area', 'complaint_type', 'final_status', 'final_outcome', 'count'])


df["Data"] = df["Area"]+'-'+ df["complaint_type"]+'-' + df["final_status"]+'-' + df["final_outcome"]
df = df.dropna(how='any',axis=0)

del df['Area']
del df['complaint_type']
del df['final_status']
del df['final_outcome']

cols = df.columns.tolist()
cols = cols[-1:] + cols[:-1]
df = df[cols]

df.to_csv(out_file)
