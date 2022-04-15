import pandas as pd

cat = pd.read_csv("data\cat.csv")
bal = pd.read_csv("data\bal.csv")

t = cat + bal
