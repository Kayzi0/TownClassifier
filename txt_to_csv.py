#convert the txt cat town names to csv
import pandas as pd

read_file = pd.read_csv (r'data\raw\muni-val-cleaned.txt')
read_file.to_csv (r'data\val.csv', index=None)

read_file = pd.read_csv (r'data\raw\muni-cat-cleaned.txt')
read_file.to_csv (r'data\cat.csv', index=None)

read_file = pd.read_csv (r'data\raw\muni-bal-cleaned.txt')
read_file.to_csv (r'data\bal.csv', index=None)