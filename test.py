import pandas as pd
import plotly.figure_factory as ff

uploaded_file = "./sample.csv"

df = pd.read_csv(uploaded_file, header=0)
print(df)

tup = tuple(df)
print(tup)