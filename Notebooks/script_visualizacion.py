import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

# Título y finalidad del proyecto 
st.title('¿Se puede predecir la felicidad?')

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

def define_var(var,word):
    if word in var:
        return 1
    else:
        return 0

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

    
st.sidebar.title("Welcome to the test :smile:")
st.sidebar.markdown("Contesta a las siguientes preguntas si quieres saber tu puntuación!")

# variable 1
HHsize = st.sidebar.number_input("¿Cuántas personas sois en casa?", 1, 12,1)

# variable 2
estadosalud = st.sidebar.slider('Valora tu estado de salud, siendo 1 fatal,fatal y 5 muy,muy buen',1, 5, 3, 1)

# variable 3
chronicdis = st.sidebar.selectbox("¿Tienes alguna enfermedad o condición crónica?",
                                ("Sí","No","Prefiero no revelarlo :)"))
# variable 4
limitacion = st.sidebar.selectbox("¿Te has visto impedido limitado a la hora realizar tus actividades habituales por algún motivo de salud?",("No, para nada, bailo el hullhop everyday", "Sí, pero sólo levemente","Sí, me he visto muy limitado :("))

# variable 5
economíahogar = st.sidebar.slider('Dime Cuanto te cuesta llegar a fin de mes, siendo 1 siempre voy pelado/a y 5 nada, estoy forrado/a',1, 6, 3, 1)

# variable 6
gastoshogar = st.sidebar.selectbox("Por último puedes decirme cuánto te suponen los gastos de viviend",
                                ("Nada, voy sobrado","Ni fu ni fa","Mucho, muchísimo, maldito alquiler!"))
# variable 7
priv_mat = st.sidebar.multiselect("¿Has tenido problemas para acceder a los siguientes bienes y servicios por temas económicos?",
                                ("Acceso a interet","Ocio","Salir con amigos","Gastar dinero en lo que me gusta","Comprar zapatos",
                                 "Comprar ropa"))
# variable 8
renta = st.sidebar.number_input("¿Podrías decirme tu renta anual?", -55000, 150000,0)

x = st.sidebar.button('Quiero saber mi puntuación')

my_df = pd.DataFrame({'vhRentaa': [renta],
                      'HousingCost_HighImpactHH':[define_var(gastoshogar,'Mucho, muchísimo, maldito alquiler!')], 
                      'CrConditions_NChronic':[define_var(chronicdis,'No')],
                      'HLimitations_NoLimited':[define_var(limitacion,'No, para nada, bailo el hullhop everyday')], 
                      'MDInternet_Yes':[define_var(priv_mat,'Acceso a interet')] ,
                      'MDSelf_Yes':[define_var(priv_mat,'Gastar dinero en lo que me gusta')],
                      'MDLeisure_Yes':[define_var(priv_mat,'Ocio')],
                      'MDFriends_Yes':[define_var(priv_mat,'Salir con amigos')],
                      'MDShoes_Yes':[define_var(priv_mat,'Comprar zapatos')], 
                      'MDClothes_Yes':[define_var(priv_mat,'Comprar ropa')], 
                      'CHealth':[estadosalud],  
                      'AREMonth':[economíahogar]})
