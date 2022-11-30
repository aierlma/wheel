import pandas as pd
import plotly_express as px
import numpy as np
import plotly.graph_objects as go

file_path = input("Your excel file path:> ")
xaxis = input("Which column do you want to use as xaxis> ")
yaxis = input("Which columns do you want to use as yaxis,you can use list> ").split(",")
xls = pd.read_excel(fr"{file_path}")
df = pd.DataFrame(xls)

def plot_figure():
    fig = px.scatter(df,x = xaxis, y=yaxis,trendline="ols")
    fig.show()

def print_ols_equation():
    fig = px.scatter(df,x = xaxis, y=yaxis,trendline="ols")
    results = px.get_trendline_results(fig)
    for key, i in enumerate(results.iloc):
        a = results.iloc[key]["px_fit_results"].params[0]
        b = results.iloc[key]["px_fit_results"].params[1]
        var = results.iloc[key]["variable"]
        print(f"{var: <15}: {a:.4f}+{b:.4f}t")

plot_figure()
print_ols_equation()