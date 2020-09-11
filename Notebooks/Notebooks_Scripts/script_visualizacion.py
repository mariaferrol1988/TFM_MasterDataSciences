import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from altair import datum
from sklearn.linear_model import LinearRegression


# Funciones ------------------------------------------------------------------------
@st.cache(suppress_st_warning=True,show_spinner=False)
# Lectura de df
def read_df(dfx,sp,cols):
    df0 = pd.read_csv(dfx, sep = sp, usecols = cols)
    return df0 

# Función para definir dummies modelo (ausencia del atributo seleccionado en el cuestionario)
def define_var_no(var,word):
    if word in var:
        return 0
    else:
        return 1

# Devolver el restulado de modelo (ausencia atributo)
def define_var_yes(var,word):
    if word in var:
        return 1
    else:
        return 0

# Devolver el restulado de modelo (presencia atributo)
def my_result(x):
    if x < 5.5:
        return 'Tu felicidad estimada es ' + str(round(float(x),2)) + ' sobre 10. Eso significa que estás por debajo de la media.'
    elif x > 8.5:
        return 'Tu felicidad estimada es ' + str(round(float(x),2)) +' sobre 10. Enhorabuena, eso significa que estás por encima de la media.'
    else:
        return 'Tu felicidad estimada es ' + str(round(float(x),2)) + ' sobre 10. Eso significa que estás en la media.'

    
# -----------------------------------------------------------------------------------

# Sidebar cuestionario --------------------------------------------------------------    
    
st.sidebar.title("Bienvenido al test :smile:")
st.sidebar.markdown("Contesta a las siguientes para saber tu puntuación!")
# Variable 1
estadosalud = st.sidebar.selectbox('¿Cómo valorarías tu salud en general?', \
                                   ('Muy buena', 'Buena', 'Regular', 'Mala','Muy mala'))
salud_dic = {'Muy buena':1, 'Buena':2, 'Regular':3, 'Mala':4,'Muy mala':5}
# Variable 2
limitacion = st.sidebar.selectbox("¿Te has visto limitado en tu vida diaria por motivos de salud en los últimos 6 meses?",('No, para nada', 'Sí, pero sólo levemente','Sí, me he visto muy limitado'))
# Variable 3
economíahogar = st.sidebar.selectbox('¿Qué nivel de dificultad encuentras para llegar a fin de mes?' \
                                     ,('Muy difícil','Difícil','Más bien difícil',
                                       'Más bien fácil', 'Fácil','Muy fácil'))
# Variable 4
econ_dic = {'Muy difícil':1, 'Difícil':2, 'Más bien difícil':3, 'Más bien fácil':4, 'Fácil':5, 'Muy fácil':6}
# Variable 5
gastoshogar = st.sidebar.selectbox("Por último puedes decirme cuánto te suponen los gastos de vivienda",
                                ("El impacto es bajo","El impacto es medio","El impacto es alto"))
# Variables 6, 7, 8, 9, 10 
priv_mat = st.sidebar.multiselect('¿Has tenido problemas económicos que te impidieran permitirte alguna de las siguientes cosas?',
                                ("Realizar actividades de ocio","Salir con amigos", \
                                 "Gastar dinero en lo que me gusta","Comprar calzado", "Comprar ropa"))
# Variable 11
renta = st.sidebar.number_input("¿Podrías decirme tu renta anual?", -100000, +500000,0)

# ----------------------------------------------------------------------------------

# Selección de KPIs ----------------------------------------------------------------


# Df para el modelo, también usado en gráficos de datos observados: distribución de la felicidad y distribución de la renta por felicidad
model = read_df('https://raw.githubusercontent.com/mariaferrol1988/TFM_MasterDataSciences/master/Notebooks/Files/data_set_modelovf.csv',';', None)
# Df resultados nacionales para gráficos de impacto de los factores en la felicidad, evolución de factores que afectan a la felicidad
# y evolución de la felicidad por quintiles
df_vis_nac = read_df('https://raw.githubusercontent.com/mariaferrol1988/TFM_MasterDataSciences/master/Notebooks/Files/nac_visualization.csv',';', None)
# Df para datos regionales de evolución por PIB y quintil superior
df = pd.read_csv('https://raw.githubusercontent.com/mariaferrol1988/TFM_MasterDataSciences/master/Notebooks/Files/regions_visualization.csv', sep = ';')
# Df para gráfico de evolución PIB
df_PIB = read_df('https://raw.githubusercontent.com/mariaferrol1988/TFM_MasterDataSciences/master/Notebooks/Files/PIB.csv', ';', None)

# ----------------------------------------------------------------------------------

# Modelo cálculo puntuaciones-------------------------------------------------------

## Df para almacenar los resultados del cuestionario
df_qnr = pd.DataFrame({'vhRentaa': [renta],
                      'HousingCost_HighImpactHH':[define_var_yes(gastoshogar,'El impacto es alto')],
                      'HLimitations_SerLimited':[define_var_yes(limitacion,'Sí, me he visto muy limitado')], 
                      'MDSelf_Yes':[define_var_no(priv_mat,'Gastar dinero en lo que me gusta')],
                      'MDLeisure_Yes':[define_var_no(priv_mat,'Realizar actividades de ocio')],
                      'MDFriends_Yes':[define_var_no(priv_mat,'Salir con amigos')],
                      'MDShoes_Yes':[define_var_no(priv_mat,'Comprar calzado')], 
                      'MDClothes_Yes':[define_var_no(priv_mat,'Comprar ropa')], 
                      'CHealth':[salud_dic[estadosalud]],  
                      'AREMonth':[econ_dic[economíahogar]]})
    
## Variables modelo
X = model[['vhRentaa','HousingCost_HighImpactHH','HLimitations_SerLimited',
     'MDSelf_Yes', 'MDLeisure_Yes',  'MDFriends_Yes', 'MDShoes_Yes', 'MDClothes_Yes','CHealth','AREMonth']]
y = model['LifeSatisfaction0']

## Modelo para predecir la felicidad
reg = LinearRegression()
reg.fit(X, y)
## Predicción individuo
prediction =reg.predict(df_qnr[['vhRentaa','HousingCost_HighImpactHH','HLimitations_SerLimited',
     'MDSelf_Yes', 'MDLeisure_Yes',  'MDFriends_Yes', 'MDShoes_Yes', 'MDClothes_Yes','CHealth','AREMonth']])

# ----------------------------------------------------------------------------------

# Contenido ------------------------------------------------------------------------

## Introducción --------------------------------------------------------------------
st.title('Prediciendo la felicidad')
st.markdown('Un proyecto experimental divulgativo, que aborda el eterno dilema que cada vez está más de moda ¿Depende la felicidad realmente de nosotros o hay algo más?') 
st.markdown('Puedes realizar el test si quieres saber tu puntuación y cambiar las respuestas si quieres explorar cómo impactan los distintos factores en la felicidad de las personas') 

st.subheader(my_result(prediction))
st.markdown('\n')
st.markdown('\n')

#### histrograma felicidad con observaciones reales 2013 y 2018 ----------------------

#### Df agrupado por niveles de satisfacción y ponderado para histograma
df13_18grouped = model.groupby(['Year','LifeSatisfaction0'])['Weight'].sum().reset_index()

#### Df para la visualización de los datos del individuo
dfpred = pd.DataFrame({'Person':['Tu felicidad estimada'],'value':[float(prediction)],'bar':[2000000]})

#### Chart histograma felicidad
hist_happiness = alt.Chart(df13_18grouped).mark_area(
    opacity=0.5,
    interpolate='step'
).encode(
    x = alt.X('LifeSatisfaction0:Q', # Cambiar en nombre de la variable
              bin=alt.Bin(maxbins=100), 
              title = 'Felicidad',
              axis=alt.Axis(values= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])),
    y = alt.Y('Weight', # Cambiar el nombre
              stack=None,
              axis = alt.Axis(format =',.2s'),
              title = 'Individuos'),
    tooltip=[alt.Tooltip('LifeSatisfaction0', title = 'Nivel de felicidad'),
             alt.Tooltip('Weight', title = 'Número de personas',format=',.2s')]
).properties(
    width=700,
    height=400
)

#### Barra de observación predecida del inviduo 
pred_bar = alt.Chart(dfpred).mark_bar(color = 'black', size = 1).encode(
    alt.X('value'),
    alt.Y('bar'),
    tooltip=[alt.Tooltip('value', title = 'Tu nivel de felicidad',format=',.2s')]
).properties(
    width=700,
    height=400
)    

#### Texto de la predicción del individuo
pred_text = alt.Chart(dfpred).mark_text(dy=-15, color='black', size = 12).encode(
        alt.X('value'),
        alt.Y('bar'),
        text=alt.Text('Person:N'))

happines_histogram = alt.layer(
    hist_happiness, pred_bar, pred_text
).properties(
    width=700, height=400
).configure_view(
    strokeWidth=0
)

happines_histogram 

st.markdown('Aunque parece evidente que las circunstancias vitales impactan en la felicidad de las personas en la actualidad tendemos a culpar al individuo en todos lo ámbitos, incluída la finalidad vita por antonomasia: Ser Féliz. Esta reconstrucción teórica basada en predicciones realizadas a través de los años 2013 y 2018 busca dar una visión transversal con el objetivo de reflexionar sobre las condiciones que hacen que unas personas tengan mayor probabilidad de ser feliz que otras.')
st.markdown('\n')

#### Gráfico de barras PIB por años -------------------------------------------------

#### PIB
st.subheader('Evolución del PIB')
st.markdown('\n')
st.markdown('\n')

PIB = alt.Chart(df_PIB).mark_bar().encode(
    x = alt.X('Year:O',
             title = 'Año'),
    y = alt.Y('PIB_percapita_Nacional',
              title = 'PIB per cápita € (000)',
              scale=alt.Scale(domain = [0.,30.])),
    tooltip = [alt.Tooltip('Year', title = 'Año'),
               alt.Tooltip('PIB_percapita_Nacional', 
                           title = 'PIB',
                           format = ',.2f')]
).properties(
    height = 400,
    width = 700)

PIB

st.markdown('El contexto no es siempre el mismo, y durante los últimos 10 años ha habido cambios drásticos que han impactado drásticamente en en las condiciones de vida de las personas.')
# ----------------------------------------------------------------------------------

#### Gráfico de líneas evolución de la felicidad en España -------------------------

st.subheader('Evolución estimada de la felicidad estimada en España años 2008 a 2018')
st.markdown('\n')
st.markdown('\n')

#### Df de con los pesos ponderados de la población divididos por quintiles
df_hapiness_evol = df_vis_nac.groupby(['Year','Quintiles'])['Weight'].mean().reset_index()

#### Filtro
nearest = alt.selection(type='single', nearest=True, on='mouseover',
                        fields=['Year'], empty='none')

#### Gráfico felicidad por quintiles
line_quintiles = alt.Chart(df_hapiness_evol).mark_line(interpolate = 'monotone', size = 2).encode(
    alt.X('Year:N', title = 'Año',
          axis=alt.Axis(values= [2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018])),
    alt.Y('sum(Weight):Q', 
          title = 'Individuos', 
          axis = alt.Axis(format =',.2s'),
          scale=alt.Scale(domain=[6000000, 12000000])),
    alt.Color('Quintiles',
              legend = alt.Legend(orient = 'bottom-left'))
).properties(
    height = 450,
    width = 700
)


selectors = alt.Chart(df_hapiness_evol).mark_point().encode(
    x='Year:N',
    opacity=alt.value(0),
).add_selection(
    nearest
)

# Puntos a mostrar
points_quintiles = line_quintiles.mark_point().encode(
    opacity=alt.condition(nearest, alt.value(1), alt.value(0))
)

# Texto a mostrar 
text_quintiles = line_quintiles.mark_text(align='left', dx=5, dy=-5).encode(
    text=alt.condition(nearest,'sum(Weight):Q', alt.value(' '), format=',.2s')
)

# Regla para el seletor
rules_quintiles = alt.Chart(df_hapiness_evol).mark_rule(color='gray').encode(
    x='Year:N',
).transform_filter(
    nearest
)

# Chart final
happines_distribution = alt.layer(
    line_quintiles, selectors, points_quintiles, rules_quintiles, text_quintiles
).properties(
    width=700, height= 450
)

happines_distribution
st.markdown('Según el análisis de la felicidad estimada por Quintiles de felicidad longitudinales (división de todas las observaciones en conjunto en 5 rangos homogéneos en número) existe una importante inversión de la felicidad a partir del año 2012 que culmina en 2014 año en el que el crecimiento de la población de los quintiles inferiores se desacelera, para alcanzar en 2018 máximo histórico de la estimación, con casi 11,5 millones de españoles muy felices.')

# ----------------------------------------------------------------------------------

#### Bar charts con condiciones de vida y su nivel de felicidad---------------------
st.subheader('Media por factores que afectan a la felicidad')
st.markdown('\n')
st.markdown('\n')

#### Chart variables económicas Hedonistas
conditions1 = alt.Chart(df_vis_nac).mark_bar().encode(
    x = alt.X('variable:O',title = None),
    y = alt.Y('mean(Mean_conditions):Q',
              title = 'Media',
             scale=alt.Scale(domain=[0, 9])),
    color = alt.Color('variable_posneg',
                     title = 'Impacto' ),
    tooltip = [alt.Tooltip('mean(Mean_conditions):Q', 
                           title = 'Media',
                           format=',.2f')]
).transform_filter(
    (datum.variable_category == 'Economía no básica')
).transform_filter(
    alt.FieldOneOfPredicate(field='variable', oneOf=['Vacaciones No', 'Vacaciones_Sí', 'Alimentación No',
       'Alimentación Sí', '"Colchón" económico Sí',
       '"Colchón" económico No', 'Alto impacto coste vivienda', 'Bajo impacto coste vivienda',
       'Impacto medio coste vivienda', 'Calefacción No', 'Calefacción Sí',
       'Riesgo de pobreza No', 'Riesgo de pobreza Sí',
       'Carencia Material Severa No', 'Carencia material severa',
       'Enfermedades Crónicas No', 'Enfermedades Crónicas Sí',
       'Limitaciones físicas No', 'Limitaciones físicas leves Sí',
       'Limitaciones físicas graves Sí', 'Compra de ropa No',
       'Compra de ropa Sí', 'Compra de zapatos No',
       'Compra de zapatos Sí', 'Ocio con amigos No', 'Ocio con amigos Sí',
       'Ocio en general No', 'Ocio en general Sí',
       'Gasto en uno mismo No', 'Gasto en uno mismo Sí',
       'Acceso a internet No', 'Acceso a internet Sí'])
).properties(
    height = 300,
    width = 300,
    title = 'Variables económicas hedonistas')

#### Chart variables económicas básicas
conditions2 =alt.Chart(df_vis_nac).mark_bar().encode(
    x = alt.X('variable:O',title = None),
    y = alt.Y('mean(Mean_conditions):Q',
              title = 'Media',
             scale=alt.Scale(domain=[0, 9])),
    color = alt.Color('variable_posneg',
                     title = 'Impacto' ),
    tooltip = [alt.Tooltip('mean(Mean_conditions):Q', 
                           title = 'Media',
                           format=',.2f')]
).transform_filter(
    (datum.variable_category == 'Economía básica')
).transform_filter(
    alt.FieldOneOfPredicate(field='variable', oneOf=['Vacaciones No', 'Vacaciones_Sí', 'Alimentación No',
       'Alimentación Sí', '"Colchón" económico Sí',
       '"Colchón" económico No', 'Alto impacto coste vivienda', 'Bajo impacto coste vivienda',
       'Impacto medio coste vivienda', 'Calefacción No', 'Calefacción Sí',
       'Riesgo de pobreza No', 'Riesgo de pobreza Sí',
       'Carencia Material Severa No', 'Carencia material severa',
       'Enfermedades Crónicas No', 'Enfermedades Crónicas Sí',
       'Limitaciones físicas No', 'Limitaciones físicas leves Sí',
       'Limitaciones físicas graves Sí', 'Compra de ropa No',
       'Compra de ropa Sí', 'Compra de zapatos No',
       'Compra de zapatos Sí', 'Ocio con amigos No', 'Ocio con amigos Sí',
       'Ocio en general No', 'Ocio en general Sí',
       'Gasto en uno mismo No', 'Gasto en uno mismo Sí',
       'Acceso a internet No', 'Acceso a internet Sí'])
).properties(
    height = 300,
    width = 300,
    title = 'Variables económicas primera necedidad')

#### Chart variables de situación económica
conditions3 = alt.Chart(df_vis_nac).mark_bar().encode(
    x = alt.X('variable:O',title = None),
    y = alt.Y('mean(Mean_conditions):Q',
             title = 'Media',
             scale=alt.Scale(domain=[0, 9])),
    color = alt.Color('variable_posneg',
                     title = 'Impacto' ),
    tooltip = [alt.Tooltip('mean(Mean_conditions):Q', 
                     title = 'Media',
                     format=',.2f')]
).transform_filter(
    (datum.variable_category == 'Situación económica')
).transform_filter(
    alt.FieldOneOfPredicate(field='variable', oneOf=['Vacaciones No', 'Vacaciones_Sí', 'Alimentación No',
       'Alimentación Sí', '"Colchón" económico Sí',
       '"Colchón" económico No', 'Alto impacto coste vivienda', 'Bajo impacto coste vivienda',
       'Impacto medio coste vivienda', 'Calefacción No', 'Calefacción Sí',
       'Riesgo de pobreza No', 'Riesgo de pobreza Sí',
       'Carencia Material Severa No', 'Carencia material severa',
       'Enfermedades Crónicas No', 'Enfermedades Crónicas Sí',
       'Limitaciones físicas No', 'Limitaciones físicas leves Sí',
       'Limitaciones físicas graves Sí', 'Compra de ropa No',
       'Compra de ropa Sí', 'Compra de zapatos No',
       'Compra de zapatos Sí', 'Ocio con amigos No', 'Ocio con amigos Sí',
       'Ocio en general No', 'Ocio en general Sí',
       'Gasto en uno mismo No', 'Gasto en uno mismo Sí',
       'Acceso a internet No', 'Acceso a internet Sí'])
).properties(
    height = 300,
    width = 300,
    title = 'Variables descriptivas de la situación económica')

#### Chart variables de estado de salud
conditions4 = alt.Chart(df_vis_nac).mark_bar().encode(
    x = alt.X('variable:O',title = None),
    y = alt.Y('mean(Mean_conditions):Q',
             title = 'Media',
             scale=alt.Scale(domain=[0, 9])),
    color = alt.Color('variable_posneg',
                     title = 'Impacto' ),
    tooltip = [alt.Tooltip('mean(Mean_conditions):Q', 
                           title = 'Media',
                           format=',.2f')]
).transform_filter(
    (datum.variable_category == 'Salud')
).transform_filter(
    alt.FieldOneOfPredicate(field='variable', oneOf=['Vacaciones No', 'Vacaciones_Sí', 'Alimentación No',
       'Alimentación Sí', '"Colchón" económico Sí',
       '"Colchón" económico No', 'Alto impacto coste vivienda', 'Bajo impacto coste vivienda',
       'Impacto medio coste vivienda', 'Calefacción No', 'Calefacción Sí',
       'Riesgo de pobreza No', 'Riesgo de pobreza Sí',
       'Carencia Material Severa No', 'Carencia material severa',
       'Enfermedades Crónicas No', 'Enfermedades Crónicas Sí',
       'Limitaciones físicas No', 'Limitaciones físicas leves Sí',
       'Limitaciones físicas graves Sí', 'Compra de ropa No',
       'Compra de ropa Sí', 'Compra de zapatos No',
       'Compra de zapatos Sí', 'Ocio con amigos No', 'Ocio con amigos Sí',
       'Ocio en general No', 'Ocio en general Sí',
       'Gasto en uno mismo No', 'Gasto en uno mismo Sí',
       'Acceso a internet No', 'Acceso a internet Sí'])
).properties(
    height = 300,
    width = 300,
    title = 'Variables de estado de salud')

(conditions1 | conditions2) 
(conditions3 | conditions4)

st.markdown('La razón por la cual la estimación fluctúa por años es que la población no es estática, sus condiciones cambian debido a muy diversos factores, algunos de ellos dependen del contexto como la economía que si se hunde causa [precariedad y malestar](https://bura.brunel.ac.uk/handle/2438/926) y se dispara [una explosión de transitorio optimismo.](https://es.wikipedia.org/wiki/Felices_a%C3%B1os_veinte). Otros factores como [la salud](https://journals.sagepub.com/doi/10.2190/QGJN-0N81-5957-HAQD), aunque a priori más estáticos también tiene un impacto en las condiciones de vida y la felicidad de los individuos')

# ----------------------------------------------------------------------------------

#### gráfico de dispersión de la mediana de la renta agrupada por la felicidad------
# Ver si puedo cambiar el dato de invididuos por el dato de la ponderación
st.subheader('Mediana de renta familiar por nivel de felicidad')
st.markdown('\n')
st.markdown('\n')

#### Chart de renta
df_renta = model.groupby(['LifeSatisfaction0','Year'])['vhRentaa_xperson'].agg(['mean','std','min','max','median','count']).reset_index()
renta = alt.Chart(df_renta).mark_circle().encode(
    alt.X('median', scale=alt.Scale(domain=[6000, 24000]),title = 'Evaluación economía'),
    alt.Y('LifeSatisfaction0',scale=alt.Scale(domain=[0, 11]), title = 'Felicidad'),
    size= alt.Size('count', 
                   scale=alt.Scale(domain=[0,700]),
                   title = 'Individuos',
                   legend = alt.Legend(orient = 'bottom')),
    color = alt.Color('Year:N', legend = alt.Legend(orient = 'bottom-left')),
    tooltip = [alt.Tooltip('Year', title = 'Año'),
               alt.Tooltip('median', 
                           title = 'Mediana',
                           format = ',.0f'),
               alt.Tooltip('mean', 
                           title = 'Media',
                           format = ',.0f')]
).properties(
    width=700,
    height=550,
).interactive()

renta

st.markdown('But does money really matters? Pues... agrupando la felicidad por tramos tanto la mediana como la media de la renta tienden a ser más altas, aunque evidentemente muchos otros factores juegan un papel. Lo que sí parece interesante es que los individuos más felices en se ubican tanto para 2013 y 2018 en la cuarta mediana más alta. En cualquier caso que aquellos que tienen las rentas más altas no tienen porque ser los más felices es algo que [ya estaba demostrado](https://www.pnas.org/content/107/38/16489), si bien parece más adecuado hablar de niveles de renta que de una cantidad concreta.')

# ----------------------------------------------------------------------------------

#### Bar Chart evolución de los factores de manera anual ---------------------------

st.subheader('Evolución de los factores que afectan a la felicidad')

#### Factores para filtar y selector
factors1 = ('Vacaciones_Sí', '"Colchón" económico Sí', 'Alto impacto coste vivienda', 'Riesgo de pobreza Sí',
           'Carencia material severa','Enfermedades Crónicas Sí','Ocio con amigos Sí',
           'Ocio en general Sí', 'Gasto en uno mismo Sí', 
           'Acceso a internet Sí')
selection = st.selectbox('Elige un indicador para ver su evolución',factors1 ) 
#### Filtro para selector - ver si aplicar una función 
df_cond = df_vis_nac[df_vis_nac['variable'] == selection]
st.markdown('\n')

#### Chart de evolución
bar_cond = alt.Chart(df_cond).mark_bar(size = 50,interpolate = 'monotone',).encode(
    x = alt.X('Year:O', title = 'Año',
          axis=alt.Axis(values= [2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018])),
    y = alt.Y('mean(Ind_conditions_prop):Q', 
          title = 'Individuos', 
          axis = alt.Axis(format ='.0%')),
    tooltip = [alt.Tooltip('Year:O', title = 'Año'),
               alt.Tooltip('mean(Ind_conditions_prop):Q', title = '(%) Individuos')           ]
).properties(
    height = 400,
    width = 700
)

bar_cond

st.markdown('Algunos de los factores que se relacionan con la el nivel de felicidad de lo individuos fluctúan temporalmente más de lo que probablemente a ellos les gustaría. Este modelo sólo utiliza variables medidas durante la serie histórica, pero puedes seleccionar las variables que están presentes sólo durante 2009 y a partir de 2013 para ver cómo evolucionan ya que nos da una idea de las posibilidades de consumo hedonista a través del tiempo.')

# ----------------------------------------------------------------------------------

#### Agrupaciones para chart de resultados por PIB y comunidad ---------------------
df_2 = pd.melt(df, id_vars=['Year','Region','PIB_percapita_','Quintiles'],value_vars = ['Ind_condition_quint_prop'])
df_2 = df_2[df_2['Quintiles'] == '5º - Superior']
df_2 = df_2.drop_duplicates()
df_3 = df.groupby(['Year','Region','variable'])['Ind_conditions_prop'].mean().reset_index()
df_4 = df_2.merge(df_3, right_on = ['Year','Region'], left_on = ['Year','Region'])

st.subheader('Propoción de individuos en el superior vs PIB per cápita por regiones')
st.markdown('Si temporalmente existen diferencias en el nivel de felicidad, parece coherente pensar que pasará lo mismo si analizamos los datos por región')

#### Factores para filtar y selector
factors2 = ('Vacaciones_Sí', '"Colchón" económico Sí', 'Alto impacto coste vivienda', 'Riesgo de pobreza Sí',
           'Carencia material severa','Enfermedades Crónicas Sí')
selection2 = st.selectbox('Elige un indicador para ver las diferencias por región.',factors2) 
value = st.slider("slider", 2008,2018)

#### Filtro para selector - ver si aplicar una función 
df_5 = df_4[(df_4['Year'] == value) & (df_4['variable_y'] == selection2)]

#### Gráfico riqueza por regiones y quintiles
happiness_regions = alt.Chart(df_5).mark_circle(size=500).encode(
    x = alt.X('mean(value):Q',
         title = '(%) Quintil 5 - Superior',
         scale=alt.Scale(domain=[0.05, 0.45]),
         axis = alt.Axis(format = ".0%")),
    y = alt.Y('PIB_percapita_:Q',
         title = 'PIB per cápita (MM)',
         scale=alt.Scale(domain=[10, 40])),
    color = alt.Color('Region:N',
                     legend = None),
    tooltip = [alt.Tooltip('Region:N', 
                           title = 'CCAA'),
              alt.Tooltip('Year', 
                          title = 'Año'),
              alt.Tooltip('mean(value):Q', 
                          title = '% Quintil 5',
                          format = ".0%")],
    size = alt.Size('mean(Ind_conditions_prop):Q',
             scale=alt.Scale(domain=[0, 0.7]),
             title = '% de individuos',
             legend = alt.Legend(orient = 'bottom'))
).properties(
    height = 500,
    width = 700
)
    
    
happiness_regions
st.markdown('Pues a priori parece que algo hay, aunque existe controversia sobre hasta qué punto afecta realmente [la riqueza de las naciones en la felicidad] (https://www.iza.org/publications/dp/11994/different-versions-of-the-easterlin-paradox-new-evidence-for-european-countries), la reconstrucción parece indicar que tanto a nivel regional como temporal se producen diferencias teniendo encuenta PIB por habitante y la proporción de invididuos muy felices durante los últimos 10 años en España.')

# ----------------------------------------------------------------------------------

st.subheader('As a matter of fact... ')
st.markdown('... las condiciones importan y aunque este proyecto es sólo un ejercicio teórico basado en la idea: "como sería la "España del ayer con las condicones de hoy", algunos de los insights que se extraen concuerdan con parte de la investigación en la materia (aunque evidentemente, siempre hay dos caras.')



