from re import A
import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import os

# ファイルアップロード
path = './schedule/'
files = os.listdir(path)
fileselector = st.selectbox(
    'Select file',
    files)

uploaded_file = fileselector

# ファイルフォーマット
header = ['Task', 'Start', 'Finish', 'Category', 'Complete']

if uploaded_file is not None:
    # アップロードファイルをメイン画面にデータ表示
    df = pd.read_csv(path + uploaded_file, names=header)

    # Category
    df_Category = df['Category']
    Category = tuple(df_Category)
    #Persons = ('All', 'A', 'B', 'C', 'D')
    #All = ("All")
    Categories = ('All',) + Category

    # セレクトボックス
    selector = st.selectbox(
        'Select Category',
        Categories)

    if selector == 'All':
        df = df

    elif selector in Categories:
        df = df[(df['Category'] == selector)]

    fig = ff.create_gantt(df, colors='Blues', reverse_colors=False ,index_col='Complete',
                    show_colorbar=True, bar_width=0.2,
                    showgrid_x=True, showgrid_y=True)

    st.plotly_chart(fig, use_container_width=True)
