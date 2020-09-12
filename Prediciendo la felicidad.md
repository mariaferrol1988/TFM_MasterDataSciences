# Prediciendo la felicidad
Un proyecto para profundizar en el impacto de las condiciones de vida de los individuos en su felicidad, y la variabilidad de felicidad la felicidad a nivel global usando medidas de bienestar subjetivo.

### Antecedentes
¿Qué son las medidas de bienestar subjetivo?:
Las medidas de bienestar subjetivos [(Subjective Wellbeing Measures)](https://en.wikipedia.org/wiki/Subjective_well-being#Construction_of_SWB) son métricas que se usan comunmente en psicología para evaluar el nivel de felicidad de los individuos, y, como su propio nombre indica son subjetivas porque son las personas las que hacen un autodiagnóstico de si mismos a través de un cuestionario. 

¿Cuál es su origen?:
Este tipo de métricas fueron ideadas, evaluadas y puestas en práctica en el campo de la psicología en Estados Unidos durante los años 80 por [Ed Driener](https://en.wikipedia.org/wiki/Ed_Diener#Happiness_research), que ha desarrollado su carrera en este ámbito de estudio contribuyendo no sólo a la generación de las métricas, sino a entender los factores que afectan a la felicidad de las personas como el salario, la personalidad, o el contexto cultural o económico. 

¿Para qué se usan?:
En la actualidad sigue investigándose sobre las condiciones y factores que impactan en la felicidad de los individuos tanto a nivel académico como desde instituciones internacionales como la ONU, a través del [World Happiness Report](https://worldhappiness.report/) o instituciones / lobbies que trabajan sobre el tema como el Research [Happiness Research Institute](https://www.happinessresearchinstitute.com/)

### Objetivo e interés del proyecto 
Es un campo de estudio en el que se han desarrollado numerosos estudios académicos de diverso tipo, sobre todo a través de recolección de datos primarios o usando encuestas transnacionales y longitudinales. El objetivo del proyecto ser una mera fuente de información divulgativa, y se centra sobre todo en hacer un análisis global del ya demostrado impacto de diversos factores.

Además el proyecto tiene la finalidad de hacer una reconstrucción histórica de la felicidad durante los últimos 10 años, del 2008 al 2018, usando observaciones de los años 2013 y 2018. Inicialmente se ha contemplado la posibilidad de reconstruir los datos hasta el año 2004, pero el cambio sustancial de algunas de las variables imposibilita entendera través del contexto la variabilidad de los datos.    

## Fuentes
La fuente de datos es [encuesta sobre las convidiones de vida (ECV)](https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176807&menu=resultados&idp=1254735976608#!tabs-1254736194793), 
una macroencuesta anual del INE que realiza mediciones de bienestar subjetivo de manera puntual, en este caso en los años 2013 y 2018.
La ECV está originalmente planteada para medir la distribución y persistencia de la pobreza en España, e incluye mediciones longitudinales y transversales, 
así como mediciones de las actitudes y situación de cada uno de los miembros del hogar y también de la situación económica de estos, a nivel individual y en conjunto. En cuanto al contenido de la encuesta, esta aporta variables relevantes cuyo impacto en la felicidad se ha probado con anterioridad, si bien existe déficit de otras variables, especialmente de aquellas que tienen que ver con la sociabilidad y las relaciones personales que o bien no están definidas, o bien están vinculadas con la economía (IE: Posibilidad de realizar actividades de ocio por cuestiones económicas). 

Además se han usado otros datos del INE para obtener el histórico del PIB y de la población Española durante toda la serie histórica. 

## Requistos

Se han utilizado los siguientes paquetes

* **Librerías**

```python
import pandas as pd
import numpy as np
import pingouin as pg
```

* **Modelos**
```python
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
```

* **Métricas**
```python
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
```
* **Selección de variables*
```python
import statsmodels.api as sm
```
* **Hyperparameter tunning**
```python
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
```
* **Validación** 
```python
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
```
* **Visualización** 
```python
import altair as alt
import streamlit as st
```

## Descripción del dataset

El fichero que contiene los datos están alamacenados en este fichero [ECV_2008_2018VF.csv](https://github.com/mariaferrol1988/TFM_MasterDataSciences/blob/master/Notebooks/Files/ECV_2008_2018VF.csv) . Se ha generado a través de la concatenación de ficheros de la ECV desde 2004 a 2019 y que consta además de otros 3 ficheros por año (fichero de la información geográfica del hogar - fichero h, fichero de las condiciones económicas del hogar - fichero h y fichero de la persona - fichero p). Puedes acceder a estos ficheros igualmente en la siguiente [carpeta](https://github.com/mariaferrol1988/TFM_MasterDataSciences/tree/master/Notebooks/Files) o decargar directamente los ficheros de microdatos desde la página del [INE](https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176807&menu=resultados&idp=1254735976608#!tabs-1254736195153).

### Estructura del fichero  

El fichero original constaba de 436818 filas y se ha visto reducido por la eliminación de missing values y la no consideración de los años 2004 a 2008. <br/>
Las filas se componen de datos tipo individuo adjuntados a datos del hogar, que se encuentran están duplicados tantas veces como personas componen el hogar de referencia.<br/>
Una vez descartados los datos de 2004 y teniendo en cuenta las variables utilizadas para realizar el proyecto (teniendo en cuenta la visualización y el modelo) la estructura del fichero es 318275 observaciones y 38 variables.

Resumen de las variables y códigos asociados del INE si aplica: 

#### Identificadores   
**Year_IndID**: Identificador unico, incluye año (4 primeros caracteres), individuo (2 últimos caracteres), hogar caracteres intermedios. <br/>

#### Variables continuas 
**vhRentaa**: Renta disponible total del hogar en el año anterior a la entrevista (incluye toda la información relativa a gastos e ingresos del cuestionario) <br/>

#### Categóricas declaradas
**CrConditions** - PH020: Presencia de afecciones crónicas Cod 1 - Sí, Cod 2 - No  <br/>
**HLimitations** - PH030: Presencia de limitaciones en la vida diaria Cod <br/>
**MDClothes** - PD020:  Capacidad de poder reponer su ropa Cod 1- Sí, Cod 2 - No, por cuestiones económicas, Cod 3 - No por otras razones <br/>
**MDShoes** - PD030: Capacidad de poder reponer sus zapatos Cod 1- Sí, Cod 2 - No, por cuestiones económicas, Cod 3 - No por otras razones <br/>
**MDFriends** - PD050: Capacidad de gastarse dinero en salir a tomar algo con otras personas Cod 1- Sí, Cod 2 - No, por cuestiones económicas, Cod 3 - No por otras razones <br/>
**MDLeisure** - PD060: Capacidad de gastarse dinero en actividades de ocio Cod 1- Sí, Cod 2 - No, por cuestiones económicas, Cod 3 - No por otras razones <br/>
**MDSelf** - PD070: Capacidad de gastarse dinero en uno mismo y lo que le gusta Cod 1- Sí, Cod 2 - No, por cuestiones económicas, Cod 3 - No por otras razones <br/>
**MDInternet** - PD080: Capacidad de tener acceso a internet Cod 1- Sí, Cod 2 - No, por cuestiones económicas, Cod 3 - No por otras razones <br/>
**HousingCost** - HS140: Impacto del coste de la vivienda en la economía del hogar Cod 1 Una carga pesada, Cod 2 - Una carga razonable, Cod 3 - Ninguna carga <br/>
**HHFood** - HS050: Capacidad de adquirir comida Cod 1 - Sí, Cod 2 - No <br/>
**HHHolidays** - HB040: Capacidad de pagarse unas vacaciones Cod 1 - Sí, Cod 2 - No <br/>
**HHReserves** - HS060: Capacidad de tener reservas de ahorros Cod 1 - Sí, Cod 2 - No <br/>
**HHTV** - HS080: Tenencia de televisor en el hogar Cod 1 - Sí, Cod 2 - No, por razones económicas, Cod 3 - No, por otras razones <br/>
**HHComputer** - HS090: Tenencia de ordenador en el hogar Cod 1 - Sí, Cod 2 - No, por razones económicas, Cod 3 - No, por otras razones <br/>
**HHWashMachine** - HS100: Tenencia de lavadora en el hogar Cod 1 - Sí, Cod 2 - No, por razones económicas, Cod 3 - No, por otras razones <br/>
**HHCar** - HS110: Tenencia de coche en el hogar Cod 1 - Sí, Cod 2 - No, por razones económicas, Cod 3 - No, por otras razones <br/>
**HHHeath** - HH050: Capacidad de poner la calefacción en invierno Cod 1 - Sí, Cod 2 - No <br/>

#### Categóricas ordinales
**CHealth** - PH010: Estado de salud, ordinal con valores 1 a 5, Cod 1 - Muy buena, Cod 2 - Buena, Cod 3 - Regular, Cod 4 - Mala, Cod 5 - Muy mala <br/>
**AREMonth** - HS120: Facilidad para llegar a fin de mes, ordinal con valores 1 a 5, Cod 1 - Con mucha dificultad, Cod 2 - Con dificultad, Cod 3 - Con cierta dificultad, Cod 4 - Con cierta facilidad, Cod 5 - Con mucha facilidad <br/>
**WBSrelations** - PW030T: Grado de satisfacción global con sus relaciones personales, Cod 0 - Nada Satisfecho, Cod 10 - Plenamente Satisfecho. <br/>
**WBSowntime** - PW120T: Grado de satisfacción global con el tiempo que dispone para hacer lo que le gusta, ordinal con valores de 0 a 10, Cod 0 - Nada Satisfecho, Cod 10 - Plenamente Satisfecho. <br/>
**WSBeconomy** - PW160T: Grado de satisfacción global la situación económica de su hogar, ordinal con valores de 0 a 10, Cod 0 - Nada Satisfecho, Cod 10 - Plenamente Satisfecho. <br/>
**WSOovsat** - PW010T: Grado de satisfacción global con la vida, ordinal con valores de 0 a 10, Cod 0 - Nada Satisfecho, Cod 10 - Plenamente Satisfecho. <br/>

#### Categóricas no declaradas
**vhPobreza**: Hogar en riesgo de pobreza. Umbral de pobreza: es el 60% de la mediana de los ingresos anuales -vhRentaa- por unidad de consumo del hogar. <br/>
**vhMATDEP**: Hogar con carencia material severa: Hogare Son los hogares con carencia en al menos cuatro conceptos de una lista de nueve. <br/>

#### Variables contextuales
**Year**: Año de realización de la entrevista <br/>
**Region** - DB040: Comunidad / Ciudad Autónoma <br/>
**Pob_**: Población de la comunidad Autónoma ([Fuente INE](https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736167628&menu=resultados&idp=1254735576581#!tabs-1254736158133)) <br/>
**PIB_percapita_**: PIB Percápita de la Comunidad autónoma ([Fuente INE](https://www.ine.es/jaxiT3/Tabla.htm?t=2853&L=0)) <br/>
**Pob_Nacional**: Población de la comunidad Autónoma ([Fuente INE](https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736167628&menu=resultados&idp=1254735576581#!tabs-1254736158133)) <br/>
**PIB_percapita_Nacional**: PIB Percápita de la Comunidad autónoma ([Fuente INE](https://www.ine.es/jaxiT3/Tabla.htm?t=2853&L=0)) <br/>

### Tratamiento de los datos

* **Variable target**:

La variable target se compone de la combinación de 4 variables relacionadas con la satisfacción con la vida para evitar que la variable que se va a predecir sea únicamente una variable de escala de 10 puntos y tenga puntos intermedios <br/>

Para evaluar la pertinencia del uso de las variables se ha usado el test [Alpha de Chronbach](https://es.wikipedia.org/wiki/Alfa_de_Cronbach). Como resultado se ha obtenido la misma variable por dos procedimientos distintos. <br/>

```python
pg.cronbach_alpha(data = dfFinal[['WBSrelations','WBSowntime','WSBeconomy','WSOovsat']])
```

**y - Opción A**: LifeSatisfaction 0 - Esta variable es la media aritmética de distintas variables de satisfacción con la vida. <br/>

```python
dfFinal['LifeSatisfaction0'] = (dfFinal['WBSrelations'] + dfFinal['WBSowntime'] \
                         + dfFinal['WSBeconomy'] + dfFinal['WSOovsat']) / 4
```

**y - Opción B**: LifeSatisfaction 1 - Esta variable es el resultado de sumar la variable de satisfacción con la vida más cada una de las variables secundarias multiplicadas por la correlación de cada una de ellas con la variable de satisfacción con la vida general y reescalado a 10 puntos. La única razón para dar el peso de la correlación a cada una de las variables es dar más relevancia a la variable principal (satisfacción con la vida), sirve también aunque como en el caso anterior sirve para penalizar y bonificar las respuestas  y además añade más heterogeneidad a las puntuaciones. Por último el criterio de ponderación es arbitrario (podría haberse unsado otro perfectamente si se quiere hacer un ejercicio similar) pero la intención es dar algo más de peso a aquellas variables con más relación con la variable principal. <br/>

```python
#Lista de pesos de correlación de cada variable de satisfacción con la vida 
correlations = dfFinal[['WBSrelations','WBSowntime','WSBeconomy','WSOovsat']].corr()['WSOovsat'][:-1]

#Variable y opción B 
dfFinal['LifeSatisfaction1'] = (dfFinal['WBSrelations'] * correlations[0] + dfFinal['WBSowntime'] * correlations[1] \
                            + dfFinal['WSBeconomy'] * correlations[2] + dfFinal['WSOovsat']) / [dfFinal['LifeSatisfaction1'].max() / 10]
```

* **Variables predictoras**: <br/>

Existen Modelos de dos tipos A y B, debido a que cuando se comenzó el proyecto  no se había previsto que ciertas variables no estuviesen disponibles todos los años. Así que finalmente se ha repetido el ejercicio con otras variables para poder hacer una reconstrucción longitudinal más amplia. No obstante ambos modelos han resultado funcionales ya que se han usado los dos en la visualización final para finalidades distintas. <br/>

**Variables Modelo A - Año 2013 - 2018:** <br/>

X1 - 'vhRentaa': Numérica - Sin normalizar <br/> 
X2 - 'HousingCost_HighImpactHH': Dummy <br/>
X3 - 'CrConditions_NChronic': Dummy (finalmente eliminada) <br/>
X4 - 'HLimitations_NoLimited': Dummy (finalmente eliminada) <br/> 
X5 - 'MDInternet_Yes': Dummy (finalmente eliminada) <br/> 
X6 - 'MDSelf_Yes': Dummy <br/>
X7 - 'MDLeisure_Yes': Dummy <br/>
X8 - 'MDFriends_Yes': Dummy <br/>
X9 - 'MDShoes_Yes': Dummy <br/> 
X10 - 'MDClothes_Yes': Dummy <br/>
X11 - 'CHealth': Ordinal - Tomada como numérica <br/>
X12 - 'AREMonth': Ordinal - Tomada como numérica <br/>


**Variables Modelo B - Año 2004 - 2012:** <br/>

X1 - 'HHHolidays_Yes': Dummy <br/>
X2 - 'HHFood_Yes': Dummy <br/>
X3 - 'HHReserves_Yes': Dummy <br/>
X4 - 'HHComputer_Yes' (finalmente eliminada): Dummy <br/>
X5 - 'HHCar_Yes': Dummy <br/> 
X6 - 'HousingCost_HighImpactHH': Dummy <br/>
X7 - 'HousingCost_MediumImpactHH' (finalmente eliminada): Dummy <br/>
X8 - 'HHHeath_Yes': Dummy <br/>
X9 - 'vhPobreza_vhPobreza_Yes': Dummy <br/>
X10 - 'vhMATDEP_vhMATDEP_Yes': Dummy <br/>
X11 - 'vhRentaa': Numérica - Sin normalizar <br/>
X12 - 'CHealth': Ordinal - Tomada como numérica <br/>
X13 - 'AREMonth': Ordinal - Tomada como numérica <br/>
X14 - 'CrConditions_NChronic' (finalmente eliminada): Dummy <br/>
X15 - 'HLimitations_NoLimited': Dummy <br/>


**Tratamiento variables:**  <br/>
Fundamentalmente el tratamiento de variables está orientado a la recodificación en variables dummies en la mayor parte de los casos. En cualquier el dataset resultante requiere un proceso de limpieza bastante amplio de los datos ya que hay muchas columnas mixtas o celdas vacías sin codificar. 

En cuanto a los valores missing, para todas aquellas dummies sin codificación se ha imputado desconocido o no declarado, y en este caso entran dentro del modelo como personas que no presentan las características de las dummies incluídas. 

La variable renta es la única que contiene valores extremos, pero finalmente no se han eliminado por ser poco numerosos, ya que en este caso la variable ya ha pasado un filtro previo ya que está calculada por el INE en función a todas las variables de condiciones salariales del inviduo. 

El único caso en el que se han eliminado valores de la muestra es en dos variables de escala ordinales 'CHealth' y 'AREMonth' (1 a 5 y 1 a 6 respectivamente). Aunque este caso podía haberse solventado convirtiendo la variable ordinal en dummies finalmente no se ha hecho porque representaba un empeoramiento en la predicción del modelo. Como resultado se han perdido un 1% de los datos de la muestra. 

```python
# Función para convertir strings en numéricas
def to_numeric(x):
    if type(x) is str:
        x = x.lstrip()
        if not x:
            return np.NaN
        else:
            return float(x)
    else: 
        return x
        
# Función para recodificar las variables de privación material hogar
def HHDepriv(x):
    if x == '1' or x == 1:
        return 'Yes'
    elif x == '2' or x == 2:
        return 'No'
    elif x == '3' or x == 3:
        return 'No_otros'
    else:
        return 'Unknown / Not Declared'
        
# Función para recodificar las variables de privación material personal 
def MatDepriv(x):
    if x == '1':
        return 'Yes'
    elif x == '2':
        return 'No affordable'
    elif x == '3': 
        return 'No, other reason'
    else:
        return 'Unknown / Not Declared'

# Variables a numéricas - dataset hogares
df_H1['vhRentaa'] = df_H1['vhRentaa'].apply(to_numeric)
df_H1['AREMonth'] = df_H1['AREMonth'].apply(to_numeric)

# Variables a numéricas - dataset personas 
df_P1['CHealth'] = df_P1['CHealth'].apply(to_numeric)
list_happines = ['WSOovsat','WBSrelations','WBSowntime','WSBeconomy']
df_P1[list_happines] = df_P1[list_happines].applymap(lambda s: to_numeric(s)) 


# Recodificación de variables - dataset hogares
df_H1['vhPobreza'] =  df_H1['vhPobreza'].apply(lambda x: 'vhPobreza_Yes' if (x == '1' or x == 1) \
                                                              else 'vhPobreza_No' if (x == '0' or x == 0) else 'Unknown / Not Declared')
df_H1['vhMATDEP'] =  df_H1['vhMATDEP'].apply(lambda x: 'vhMATDEP_Yes' if x == 1 \
                                                              else 'vhMATDEP_No')
df_H1['HousingCost'] = df_H1['HousingCost'].apply(lambda x: 'HighImpactHH' if (x == '1' or x == 1)\
                                                            else 'MediumImpactHH' if (x == '2' or x == 2) \
                                                            else 'LowImpactHH' if (x == '3' or x == 3) \
                                                            else 'Unknown / Not Declared')
# Recodificación de variables - dataset personas                                                            
df_P1['CrConditions'] = df_P1['CrConditions'].apply(lambda x: 'NChronic' if x == '2'\
                                                              else 'YChronic' if x == '1' else 'Unknown / Not Declared')
df_P1['HLimitations'] = df_P1['HLimitations'].apply(lambda x: 'SerLimited' if x == '1'\
                                                              else 'NoSerLimitedG_limitado' if x == '2' \
                                                              else 'NoLimited' if x == '3' else 'Unknown / Not declared')

# Variables de privación material recodificadas - dataset hogares
list_depriv = ['HHFood','HHHolidays','HHReserves','HHPhone','HHTV','HHComputer',
              'HHWashMachine','HHCar','HHHeath']   
df_H1[list_depriv] = df_H1[list_depriv].applymap(lambda s: HHDepriv(s))    

# Variables de privación material recodificadas - dataset personas
list_pdepriv = ['MDClothes','MDShoes','MDFriends','MDLeisure','MDSelf','MDInternet']  
df_P1[list_pdepriv] = df_P1[list_pdepriv].applymap(lambda s: MatDepriv(s)) 
```

## Modelo
Para hacer la predicción al tratar he optado por mantener ambas variables y, para ver si existían cambios en la predicción. Todos los modelos incluyen las mismas variables de predicción de partido que son las anteriormente mencionadas y con el mismo tratamiento. Aunque posteriormente se han realizado análisis que han motivado la exclusión de algunas variables en el modelo lineal. 

```python
# Variables predictoras
X = df_model[['vhRentaa','HousingCost_HighImpactHH','CrConditions_NChronic','HLimitations_NoLimited', 'MDInternet_Yes',
     'MDSelf_Yes', 'MDLeisure_Yes',  'MDFriends_Yes', 'MDShoes_Yes', 'MDClothes_Yes','CHealth','AREMonth']]
# variable output con media aritmética de los factores
y1 = df_model['LifeSatisfaction0']
# variable output con predominio de variables de satisfacción con la vida
y2 = df_model['LifeSatisfaction2']
Regresión Linear: Mismas variables y tratamiento <br/>
```

## Hyperparameter tuning 

Para la optimización de hiperparametros he usado Grid Search CV en el caso de K-neigbors y Decision Tree y Random Search CV en el caso del Random Forest

```python
# K-neigbors y 
regk1 = GridSearchCV(KNeighborsRegressor(),
                  param_grid={"n_neighbors":np.arange(4,300)},
                  cv=5,
                  scoring="neg_mean_absolute_error")
regk1.fit(X,y1)

# Decision Tree
regd1 = GridSearchCV(DecisionTreeRegressor(),
                  param_grid={"min_samples_split":np.arange(4,15),
                              "max_depth":np.arange(4,15),
                             'min_samples_leaf':np.arange(4,15)},
                  cv=5,
                  scoring="neg_mean_absolute_error")

regd1.fit(X,y1)

# Random Forest
grid_param = {'n_estimators':sp_randInt(30,600), 
              'max_depth':sp_randInt(10,50), 
              'min_samples_split': sp_randInt(20,70),
              'min_samples_leaf':sp_randInt(20,70)}
              
              
rscv1 = RandomizedSearchCV(estimator = RandomForestRegressor(), param_distributions = grid_param, 
                        n_iter = 50, cv = 5, verbose = 2, random_state = 33, 
                        n_jobs = -1)

rscv1.fit(X,y1)
```
## Resultados

De todos los modelos el mejor es el Random forest para la variable y2, no obstante, finalmente no se ha utilizado por la imposibilidad de extrapolar los datos a toda la serie histórica. Por otro lado la regresión lineal para la variable y2 si se ha usado en la visualización por su menor exigencia a la hora de predecir los valores de la aplicación, la decisión final está meramente relacionada con cuestiones de usabilidad ya que para la finalidad del modelo (divulgativa y con reporte de datos agregados) probablemente las ganancias asociadas a usar Random Forest sean nulas.
Por otro lado para la predicción de la reconstrucción histórica también se ha usado la regresión lineal, aunque lo óptimo hubiera sido probar ambos modelos ya que sus resultados son muy parecidos. 

### Modelo A: serie 2013 - 2018

* **Resultados**

|Modelos y1    | Regresión Lineal | K-Neighbors | Decision Tree | Random Forest |
|--------------|------------------|-------------|---------------|---------------|
|MAPE          | 0.941983         | 1.092977    | 0.965722      | 0.940696      |
|MAE           | 0.941983         | 1.092977    | 0.965722      | 0.940696      |
|RMSE          | 1.211657         | 1.407535    | 1.240812      | 1.208551      |
|Correlation   | 0.551921         | -           | -             | -             |
|RSquared      | 0.304544         | -           | -             | -             |

|Modelos y2    | Regresión Lineal | K-Neighbors | Decision Tree | Random Forest |
|--------------|------------------|-------------|---------------|---------------|
|MAPE          | 0.938338         | 1.108846    | 0.982012      | 0.936115      |
|MAE           | 0.938338         | 1.108846    | 0.982012      | 0.936115      |
|RMSE          | 1.214550         | 1.438517    | 1.278079      | 1.211602      |               
|Correlation   | 0.585938         | -           | -             | -             |
|RSquared      | 0.343237         | -           | -             | -             |

### Modelo B: serie 2008 - 2018 

* **Resultados**

|Modelos y1    | Regresión Lineal | K-Neighbors | Decision Tree | Random Forest |
|--------------|------------------|-------------|---------------|---------------|
|MAPE          | 0.952327         | 1.092982    | 0.983308      | 0.949165      |
|MAE           | 0.952327         | 1.092982    | 0.983308      | 0.949165      |
|RMSE          | 1.226768         | 1.407550    | 1.270420      | 1.221626      |
|Correlation   | 0.535824         | -           | -             | -             |
|RSquared      | 0.287088         | -           | -             | -             |

|Modelos y2    | Regresión Lineal | K-Neighbors | Decision Tree | Random Forest |
|--------------|------------------|-------------|---------------|---------------|
|MAPE          | 0.948458         | 1.108931    | 0.965936      | 0.944762      |
|MAE           | 0.948458         | 1.108931    | 0.965936      | 0.944762      |
|RMSE          | 1.231502         | 1.438634    | 1.251006      | 1.225676      |               
|Correlation   | 0.569904         | -           | -             | -             |
|RSquared      | 0.324775         | -           | -             | -             |


**Resultados finales**:

Finalmente se han eliminado variables del modelo lineal por generar efectos no deseados (la dirección del coeficiente de las variables es inversa a la dirección de la correlación, esto probablemente está relacionado con la colinearidad de las variables). <br/>

En este sentido la tenencia de ordenador (HHComputer_Yes: coef -0.0421) y la no presencia de enfermedades crónicas (CrConditions_NChronic: coef -0.1341), tienen un coeficiente negativo pese a que su relación con la variable a predecir es positiva.  <br/>

Otras variables que se han eliminado son tenencia de internet ('MDInternet_Yes'), impacto alto del precio de la vivienda ('HousingCost_HighImpactHH'), y sin limitaciones en la vida diaria para el modelo A, no así para el B ('HLimitations_NoLimited'). La primera y tercera variable no tienen significación en el modelo, pero la verdadera razón para eliminarlas ha sido similar a la anterior (coeficiente negativo para una relación positiva entre ambas variables). Por otro lado la variable coste alto de la vivienda es prácticamente la inversa de impacto medio, por lo que he considerado oportuno eliminarla.  <br/>

Las variables incluídas en cada uno de los modelos finales son las siguientes:

```python
### Modelo A: serie 2013 - 2018
X_2BD = df_model[['vhRentaa', 'HousingCost_HighImpactHH', 
         'MDSelf_Yes', 'MDLeisure_Yes', 'MDFriends_Yes', 'MDShoes_Yes', 
         'MDClothes_Yes', 'CHealth', 'AREMonth']]

### Modelo B: serie 2008 - 2018 
X_2BD = df_model[['HHHolidays_Yes', 'HHFood_Yes', 'HHReserves_Yes',  'HHCar_Yes', 
        'HousingCost_MediumImpactHH', 'HHHeath_Yes', 'vhPobreza_vhPobreza_Yes', 'vhMATDEP_vhMATDEP_Yes', 
        'vhRentaa',  'HLimitations_NoLimited', 'CHealth', 'AREMonth']]
```

En cuanto a los resultados son parecidos a los obtenidos con anterioridad. 

|Modelos       | Modelo A         | Modelo B    | 
|--------------|------------------|-------------|
|MAPE          | 0.938941         | 0.948448    | 
|MAE           | 0.938941         | 0.948448    | 
|RMSE          | 1.215720         | 1.232086    | 
|Correlation   | 0.584847         | 0.569341    | 
|RSquared      | 0.341970         | 0.324135    |

## Visualización
La visualización se focaliza en mostrar los principales cambios de las variables relacionadas con las condiciones de vida y la estimación del impacto que estas tienen en la evolución de la felicidad en España. <br/>

En cuanto a la felicidad, se ha optado por la división en quintiles de todas las observaciones estimadas y posteriormente comparado el peso / proporción de cada uno de los quintiles por año y región. También se ha realizado una ponderación para extrapolar los resultados a universo, si bien quedaría pendiente una ponderación del peso de cada idividuo sobre la muestra total ya que los datos podrían variar ligeramente.  <br/>

Por último se ha optado por sustituir las observaciones reales de los años 2013 y 2018 por un criterio estético y también metodológico: El modelo predice resultados en el rango en el que se encuentran aproximadamente el 90% de las observaciones aproximadamente entre el 4 y el 9. Realizar una división por quintiles teniendo en cuenta los resultados observados provoca que estos años tengan una mayor proporción de población en los quintiles extremos (1 y 5). <br/>

Los datasets usados son los siguientes: <br/>
*Realización de predicciones*
[data_set_modelovf.csv] (https://github.com/mariaferrol1988/TFM_MasterDataSciences/blob/master/Notebooks/Files/data_set_modelovf.csv)
*Datos precalculados para visualización*
[PIB.csv] (https://github.com/mariaferrol1988/TFM_MasterDataSciences/blob/master/Notebooks/Files/PIB.csv)
[nac_visualization_v2.csv] (https://github.com/mariaferrol1988/TFM_MasterDataSciences/blob/master/Notebooks/Files/nac_visualization.csv)
[regions_visualization_v2.csv] (https://github.com/mariaferrol1988/TFM_MasterDataSciences/blob/master/Notebooks/Files/regions_visualization.csv)

Link a la visualización: https://my-test-app-happiness.herokuapp.com/

## Conclusiones y valoración final 

### Mejoras del modelo asociadas a la inclusión de datos e intercambio de variables  <br/>
Las primeras fases del proyecto las he realizado únicamente con datos de 2018 por desconocimiento de la existencia de la existencia del mismo contenido en la versión del año 2013 conjuntamente con el intercambio de unas variables por otras. Además en este caso creo que el azar de los años en los que se han realizado las mediciones (2013 y 2018) debido a la diferencia de las características de la población a nivel económico ha podido contribuir favorablemente al modelo. Si bien esto es sólo una idea que necesitaría explorar más en profunidad para afirmarlo.  <br/>

Con respecto a normalización de variables, las dos únicas variables continuas son la renta y el indicador de satisfacción con la vida. No he observado cambios sustanciales al normalizar por lo que finalimente no he aplicado normalización en el modelo. No obstante conviene plantearse la opción de normalizar el salario de manera anual para examinar el efecto que puede tener sobre el modelo ya que el poder adquistivo / renta varían con el tiempo. Realicé ese ejercicio de manera global (comparando los resultados de las medias anuales) sin observar cambios, no obstante una vez terminado el proyecto parece necesario revisar los datos con más profundidad para ver el efecto que tiene sobre la distribución por quintiles. <br/>

### Una mayor correlación no implica necesariamente la reducción sustancial del error <br/>
Pese a que el indicador construido a partir de darle mayor peso a una de las variables (satisfacción con la vida) sobre el resto para generar más heterogeneidad y sobre todo de cara maximizar las correlaciones de los predictores con el indicador, las diferencias en la correlación de las variables del modelo a nivel global y el R2 mejoran poco entre ambos indicadores (No obstante las diferencias son marginales). Por otro lado si nos fijamos en el resultado de los errores la mejoría es incluso menor. <br/> 

Sí existe un cambio significativo en las estimaciones del modelo que es el rango de predicción, que en este caso, realizar un modelo especulativo / divulgativo me parece positivo para mostrar diferencias en las puntuaciones. <br/>

| Modelo          |Variable    | predición min | predicción max | predicción min - max | 
|-----------------|------------|---------------|----------------|----------------------|
|Regresión Lineal | y1         | 4.07866       | 8.92634        | 4.84767              |
|Regresión Lineal | y2         | 3.82274       | 9.23722        | 5.41448              |
|Random Forest    | y1         | 3.96888       | 8.61293        | 4.64404              |               
|Random Forest    | y2         | 3.69726       | 8.75138        | 5.05412              |

### Predecir los valores extremos es complicado si el número de observaciones es muy bajo <br/>
Esto se da sobre todo en los valores inferiores, mucho más dispersos y poco numerosos. No he considerado pertinente eliminar estas observaciones por varios motivos: el primero es que creo que no son outliers simplemente la distribución de las observaciones es mucho más larga desde la media hasta los valores inferiores, y en segundo lugar, tanto como si fuesen o no fuesen outliers me parece dificil tomar una decisión sobre donde establecer el corte a partir del cual descartar valores. Probablemente habría que plantearse una manera alternativa de afrontar este problema. <br/> 

### Los efectos de correlación entre variables a pesar de no afectar al error pueden dar lugar a resultados no deseables <br/>
El sentido común se impone frente a los resultados. El efecto de la colinearidad entre la valoración del estado de salud y la presencia de enfermades crónicas (-0,58) pese a no afectar al error conlleva que la estimación de la felicidad de los individuos sanos descienda (coeficiente negativo si el individuo no tiene enfermedades). Esto no sólo contradice al sentido común o la literatura, sino a los propios datos (la correlación en el dataset de las variables satisfacción con la vida y presencia de enfermedades crónicas es negativa). <br/>

##### Heathmap correlaciones variables predictoras <br/>
![Image](https://github.com/mariaferrol1988/TFM_MasterDataSciences/blob/master/Notebooks/Imagenes/correlaciones.png)

En cualquier caso, la correlación entre variables no tiene que ser tan alta para producir resultados indeseados, ya que la posibilidad de tener acceso a internet ha sido eliminada del modelo por el mismo motivo sin tener correlaciones por encima de 0,4 con ninguna de las variables en el modelo (-0,34) la más alta, aunque pienso que esto puede estar relacionado con su falta de significación. <br/>

Por otro lado tampoco parece adecuado utilizar variables relativas a la digitalización asociadas al bienestar de la población para hacer una reconstrucción histórica ya que durante la década se han dado cambios relevantes que probablemente hagan que su peso o relevancia varíe. 

### Los cambios en la redacción de las respuestas del cuestionario afectan a los resultados sin que haya un estadístico que te "avise" de ello  <br/>
En este caso el sentido común cobra todavía más fuerza. Debido a cambios en el cuestionario he decidido eliminar los años 2004 a 2007 ya que el punto central de la escala de evaluación de la salud pasa de tener una valencia positiva (aceptable), a una negativa (regular), esto produce un desplazamiento en las respuestas que no es fruto de un cambio de tendencia, sino un error sistemático. <br/>

##### Distribución de las respuesta de evaluación del estado de salud <br/>
![Image](https://github.com/mariaferrol1988/TFM_MasterDataSciences/blob/master/Notebooks/Imagenes/graficobarras.png)

Con respecto a esto, la razón por la que me he dado cuenta fue la proporción de respuestas asociadas a los valores extremos 1 y 2 (valores más negativos que puedes ver en la imagen de arriba), ya que en el fichero resumen de codificación de variables oficial que puedes descargar del INE para ninguno de los años consta este cambio. Sí lo hace en el cuestionario oficial, documento al que me he remitido en último lugar y en el que he encontrado la respuesta al cambio de tendencia. <br/>

### A nivel reconstrucción de indicadores sociales usar la media como medida de referencia parece no ser óptimo, sobre todo si se quiere resaltar la diferencia <br/>
Pese a existir cambios relevantes en la felicidad, la media es una medida demasiado robusta como para que esos cambios sean perceptibles. Especialmente en el caso de la satisfacción con la vida, donde la mayor parte de las observaciones se apalancan para cualquier periodo en los valores centrales. <br/>

##### Histograma distribución de la felicidad por años <br/>
![Image](https://github.com/mariaferrol1988/TFM_MasterDataSciences/blob/master/Notebooks/Imagenes/histograma.png)

No obstante el histograma comparativo de los valores reales de 2013 y 2018 muestra cambios notables entre ambas distribuciones que no son perceptibles usando la media para visualizar y analizar los datos (si bien es bastante probable que la diferencia entre ambas medias sea significativa dado el tamaño de la muestra la relevancia de los cambios queda invisibilizada por la poca variabilidad del dato). <br/>

Para hacer frente a ese problema, en este proyecto he optado por realizar una división por quitiles de todas las observaciones estimadas, que si bien quizá no sea la mejor opción debido a su menor estabilidad, permite evaluar los datos desde una perspectiva que tiene mayor sensibilidad a los cambios. <br/>

### Existe poca diferencia entre los resultados de los modelos <br/>
Los dos modelos que tienen mejores resultados son la regresión lineal y el random forest, si bien casi todos las pruebas que he hecho las he realizado sobre el modelo de regresión por su simplicidad y porque de manera colateral he acabado con 4 modelos x 4 modelos (falta de variables para algunos años) para lo cual probablemente debería haber usado otro enfoque. <br/>

### A tener en cuenta de cara al futuro <br/>
Funtamentalmente hay dos aspectos de mejora, no tanto a nivel estadístico sino de detectar otros tipo de errores o eventos:. <br/>
* Existe un repunte de felicidad en el año 2011 que a priori no parece coherente aunque pueda serlo. A través del análisis de los datos me parece que puede estar relacionado con una declaración más positiva de la valoración del estado de salud, fomentada por una menor proporción de la población afectada por condiciones crónicas. Esto podría estar relacionado con el hecho de que la muestra no ha sido ponderada con los factores que proporciona el INE y quizá merezca la pena estudiarlo. <br/>

* La visualización de la evolución de la felicidad por regiones muestra claramente tres outliers especialmente durante los años 2015 - 2016, dos de ellos son Ceuta y Melilla con un tamaño muestral pequeño y mayor sensibilidad a una subdivisión por quintiles. En cuanto al tercero se trata de Madrid, por lo que no parece coherente pensar que haya un problema muestral o se trate de un outlier. Lo más coherente parece pensar que o bien la metodología de subidivisión afecta a Madrid por alguna razón o bien que la ponderación afecta a sus resultados, no obstante lo mejor sería observar el fenómeno para dar una respuesta. <br/>

### Valoración final <br/>
Como valoración final el resultado del ejercicio me parece personalmente satisfactorio los resultados coherentes y el enfoque me parece adecuado para superar los problemas que han ido surgiendo. Si bien considero necesario especificar que se trata de una estimación y que los datos no son reales y profundizar más en los puntos citados anteriormente.

La observación y análisis de las tendencias a nivel personal me parece que tiene valor aunque se utilice simplemente como un indicador de bienestar. <br/>

También creo que el modelo tiene margen de mejora, aunque sobre todo la inclusión de nuevas variables que no ha sido medidas (especialmente relacionadas con las relaciones personales y el estilo de vida). 

*Nota: Para la visualización no se han llegado a implementar los cambios de las mejoras del modelo lineal en los datasets precalculados, si bien aunque difiere ligeramente la visualización las tendencias son las mismas. 
