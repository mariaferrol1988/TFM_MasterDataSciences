import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

# Título y finalidad del proyecto 
st.title('Título del proyecto')

@st.cache(suppress_st_warning=True)
# Función para leer dataframes
def read_df(dfx,cmp,sp):
    df0 = pd.read_csv(dfx,compression = cmp, sep = sp)
    return df0

# Función para hacer groupby y sumar
def group_perc(dfx,var1,var2,var3,cod1):
    df0 = (df.groupby([var1,var2])[var3].count() / df.groupby([var1])[var3].count() *100).reset_index()
    return df0[df0[var2] ==cod1]

# Función para hacer groupby y la media u otra función
def group_func(dfx,var1,var2,func):
    df0 = df.groupby(var1)[var2].agg([func]).reset_index()
    return df0

# Dataframe con el que vamos a trabajar 
df = read_df('./Files/ECV_2004_2018.csv.gz','gzip',';')

st.subheader('La evolución económica en España')
st.markdown('bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla ')

st.subheader('¿Qué supone eso para las personas?')
st.markdown('bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla ')

df1 = group_func(df,'Year','vhRentaa','mean')


chart1 = alt.Chart(df1).mark_line(color = 'blue', size = 3).encode(
    alt.X('Year', title = 'Año'),
    alt.Y('mean', title = 'Renta €'),
    tooltip=['Year', 'mean']
).properties(
    title = 'Salario medio por hogar',
    width=250,
    height=250
)


df2 = group_func(df,'Year','vhRentaa','std')

chart2 = alt.Chart(df2).mark_line(color = 'orange', size = 3).encode(
    alt.X('Year', title = 'Año'),
    alt.Y('std', title = 'Renta €'),
    tooltip=['Year', 'std']
).properties(
    title = 'Desviación de la renta',
    width=250,
    height=250
)

st.subheader('Evolucion de la de la renta')

(chart1|chart2)


st.subheader('Consecuencias en los hogares españoles')

st.markdown('bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla ')

df3 = group_perc(df,'Year','vhMATDEP','HHId','vhMATDEP_Yes')

chart3 = alt.Chart(df3).mark_bar(color = 'green', size = 20).encode(
    alt.X('Year', title = 'Año',scale = alt.Scale(domain=(2003, 2018))),
    alt.Y('HHId', title = '(%) Población',scale = alt.Scale(domain=(0, 8))),
    tooltip=['Year', 'HHId']
).configure_axis(
    grid=False
).configure_view(
    strokeWidth=0
).properties(
    title = 'Evolucion de la privación material',
    width=600,
    height=250
)

chart3

st.markdown('bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla ')


df4 = group_perc(df,'Year','HHHolidays','HHId','Yes')


chart4 = alt.Chart(df4).mark_bar(color = 'green', size = 20).encode(
    alt.X('Year', title = 'Año',scale = alt.Scale(domain=(2003, 2018))),
    alt.Y('HHId', title = '(%) Población',scale = alt.Scale(domain=(0, 80))),
    tooltip=['Year', 'HHId']
).configure_axis(
    grid=False
).configure_view(
    strokeWidth=0
).properties(
    title = 'Evolucion de la posibilidad de irse de vacaciones',
    width=600,
    height=250
)

chart4

st.subheader('¿Qué hay de otros factores que impactan en la felicidad?')
st.markdown('bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla ')

st.subheader('¿Y qué más factores contextuales pueden impactar?')
st.markdown('bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla ')

st.subheader('¿Cómo es la felicidad en España?')
st.markdown('bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla ')


