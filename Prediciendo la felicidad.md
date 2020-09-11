# Prediciendo la felicidad
Un proyecto para profundizar en el impacto de las condiciones de vida de los individuos en su felicidad, y su impacto a nivel global en la felicidad general en conjunto.

## Motivación del proyecto

### Antecedentes
¿Qué son las medidas de bienestar subjetivas?:
Las medidas de bienestar subjetivas [(Subjective Wellbeing Measures)](https://en.wikipedia.org/wiki/Subjective_well-being#Construction_of_SWB) son métricas que se usan comunmente en psicología para evaluar el nivel de felicidad de los individuos, y, como su propio nombre indica son subjetivas porque son las personas las que hacen un autodiagnóstico de si mismos a través de un cuestionarion. 

¿Cuál es su origen?:
Este tipo de métricas fueron ideadas, evaluadas y puestas en práctica en el campo de la psicología en Estados Unidos durante los años 80 por [Ed Driener](https://en.wikipedia.org/wiki/Ed_Diener#Happiness_research), que ha desarrollado su carrera en este ámbito de estudio contribuyendo no sólo a la generación de las métricas, sino a entender los factores que afectan a la felicidad de las personas como el salario, la personalidad, o el contexto cultural o económico. 

¿Para qué se usan?:
En la actualidad sigue investigándose sobre las condiciones y factores que impactan en la felicidad de los individuos tanto a nivel académico como desde instituciones internacionales como la ONU, a través del [World Happiness Report](https://worldhappiness.report/) o instituciones que se dedican a tiempo completo a este tema como el Research [Happiness Research Institute](https://www.happinessresearchinstitute.com/)

### Objetivo e interés del proyecto 
Es un campo de estudio en el que se han desarrollado numerosos estudios académicos de diverso tipo, sobre todo a través de recolección de datos primarios o usando encuestas transnacionales y longitudinales. El objetivo del proyecto es divulgativa, y se centra sobre todo en hacer un análisis global del ya demostrado impacto de diversos factores.

Además el proyecto tiene la finalidad de hacer una reconstrucción histórica de la felicidad durante los últimos 10 años, del 2008 al 2018, usando observaciones de los años 2013 y 2018. Inicialmente se ha contemplado la posibilidad de reconstruir los datos hasta el año 2004, pero el cambio sustancial de algunas de las variables imposibilita evaluar la fiabilidad real de la estimación.    

## Fuentes
La fuente de datos es [encuesta sobre las convidiones de vida (ECV)](https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176807&menu=resultados&idp=1254735976608#!tabs-1254736194793), 
una macroencuesta anual del INE que realiza mediciones de bienestar subjetivo de manera puntual, en este caso en los años 2013 y 2018.
La ECV está originalmente planteada para medir la distribución y persistencia de la pobreza en España, e incluye mediciones longitudinales y transversales, 
así como mediciones de las actitudes y situación de cada uno de los miembros del hogar y también de la situación económica de los hogares. En cuanto al contenido de la encuesta, esta aporta variables relevantes cuyo impacto en la felicidad se ha probado con anterioridad, si bien existe déficit de otras variables, especialmente de aquellas que tienen que ver con la sociabilidad y las relaciones personales que o bien no están definidas, o bien están vinculadas con la economía (IE: Posibilidad de realizar actividades de ocio por cuestiones económicas). 

#### Estructura de la muestra 

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
## Descripción del dataset

El fichero que contiene los datos y que puedes encontrar en este repositorio en la carpeta /Data con el nombre XXX se ha generado a través de la concatenación de ficheros de la ECV desde 2004 a 2019 y que consta además de otros 3 ficheros por año (fichero de la información geográfica del hogar, fichero de las condiciones económicas del hogar y fichero de la persona). Puedes acceder a estos ficheros igualmente en la carpeta Data/Files o decargar directamente los ficheros de microdatos desde la página del [INE](https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176807&menu=resultados&idp=1254735976608#!tabs-1254736195153).

### Estructura del fichero  

Estructura 436818 filas / 60 Columnas que se han reducido posteriormente a xxx filas por la eliminación de las observaciones de 4 años <br/>
Las filas se componen de datos tipo individuo adjuntados a datos del hogar, que se encuentran están duplicados tantas veces como personas componen el hogar de referencia.<br/>

Resumen de las variables y códigos asociados: 

#### Identificadores   
**Year_IndID**: Identificador unico, incluye año (4 primeros caracteres), individuo (2 últimos caracteres), hogar caracteres intermedios. <br/>

#### Variables continuas 
**vhRentaa**: Renta disponible total del hogar en el año anterior a la entrevista (incluye toda la información relativa a gastos e ingresos del cuestionario) <br/>

#### Categóricas declaradas
**CrConditions**: Presencia de afecciones crónicas Cod 1 - Sí, Cod 2 - No <br/>
**HLimitations**: Presencia de limitaciones en la vida diaria Cod <br/>
**MDClothes**:  Capacidad de poder reponer su ropa Cod 1- Sí, Cod 2 - No, por cuestiones económicas, Cod 3 - No por otras razones <br/>
**MDShoes**: Capacidad de poder reponer sus zapatos Cod 1- Sí, Cod 2 - No, por cuestiones económicas, Cod 3 - No por otras razones <br/>
**MDFriends**: Capacidad de gastarse dinero en salir a tomar algo con otras personas Cod 1- Sí, Cod 2 - No, por cuestiones económicas, Cod 3 - No por otras razones <br/>
**MDLeisure**: Capacidad de gastarse dinero en actividades de ocio Cod 1- Sí, Cod 2 - No, por cuestiones económicas, Cod 3 - No por otras razones <br/>
**MDSelf**: Capacidad de gastarse dinero en uno mismo y lo que le gusta Cod 1- Sí, Cod 2 - No, por cuestiones económicas, Cod 3 - No por otras razones <br/>
**MDInternet**: Capacidad de tener acceso a internet Cod 1- Sí, Cod 2 - No, por cuestiones económicas, Cod 3 - No por otras razones <br/>
**HousingCost**: Impacto del coste de la vivienda en la economía del hogar Cod 1 Una carga pesada, Cod 2 - Una carga razonable, Cod 3 - Ninguna carga <br/>
**HHFood**: Capacidad de adquirir comida Cod 1 - Sí, Cod 2 - No <br/>
**HHHolidays**: Capacidad de pagarse unas vacaciones Cod 1 - Sí, Cod 2 - No <br/>
**HHReserves**: Capacidad de tener reservas de ahorros Cod 1 - Sí, Cod 2 - No <br/>
**HHPhone**: Tenecia de teléfono en el hogar Cod 1 - Sí, Cod 2 - No, por razones económicas, Cod 3 - No, por otras razones <br/>
**HHTV**: Tenencia de televisor en el hogar Cod 1 - Sí, Cod 2 - No, por razones económicas, Cod 3 - No, por otras razones <br/>
**HHComputer**: Tenencia de ordenador en el hogar Cod 1 - Sí, Cod 2 - No, por razones económicas, Cod 3 - No, por otras razones <br/>
**HHWashMachine**: Tenencia de lavadora en el hogar Cod 1 - Sí, Cod 2 - No, por razones económicas, Cod 3 - No, por otras razones <br/>
**HHCar**: Tenencia de coche en el hogar Cod 1 - Sí, Cod 2 - No, por razones económicas, Cod 3 - No, por otras razones <br/>
**HHHeath**: Capacidad de poner la calefacción en invierno Cod 1 - Sí, Cod 2 - No <br/>

#### Categóricas ordinales
**CHealth**: Estado de salud, ordinal con valores 1 a 5, Cod 1 - Muy buena, Cod 2 - Buena, Cod 3 - Regular, Cod 4 - Mala, Cod 5 - Muy mala <br/>
**AREMonth**: Facilidad para llegar a fin de mes, ordinal con valores 1 a 5, Cod 1 - Con mucha dificultad, Cod 2 - Con dificultad, Cod 3 - Con cierta dificultad, Cod 4 - Con cierta facilidad, Cod 5 - Con mucha facilidad <br/>
**WBSrelations**: Grado de satisfacción global con sus relaciones personales, Cod 0 - Nada Satisfecho, Cod 10 - Plenamente Satisfecho. 
**WBSowntime**: Grado de satisfacción global con el tiempo que dispone para hacer lo que le gusta, ordinal con valores de 0 a 10, Cod 0 - Nada Satisfecho, Cod 10 - Plenamente Satisfecho. 
**WSBeconomy**: Grado de satisfacción global la situación económica de su hogar, ordinal con valores de 0 a 10, Cod 0 - Nada Satisfecho, Cod 10 - Plenamente Satisfecho.
**WSOovsat**: Grado de satisfacción global con la vida, ordinal con valores de 0 a 10, Cod 0 - Nada Satisfecho, Cod 10 - Plenamente Satisfecho.

#### Categóricas no declaradas
**vhPobreza**: Hogar en riesgo de pobreza. Umbral de pobreza: es el 60% de la mediana de los ingresos anuales -vhRentaa- por unidad de consumo del hogar. <br/>
**vhMATDEP**: Hogar con carencia material severa: Hogare Son los hogares con carencia en al menos cuatro conceptos de una lista de nueve. <br/>

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

**y - Opción B**: LifeSatisfaction 1 - Esta variable es el resultado de sumar la variable de satisfacción con la vida más cada una de las variables secundarias multiplicadas por la correlación de cada una de ellas con la variable de satisfacción con la vida general y reescalado a 10 puntos. La razón de justificar este ejercicio es dar más peso a una variable para evitar que el peso del resto de las variables haga que exista menos relación entre variables. También aunque como en el caso anterior sirve para penalizar y bonificar las respuestas evitando dejar todo el peso en una sóla respuesta subjetiva y además añade más heterogeneidad a las puntuaciones, lo que independientemente del resultado final permite hacer los datos más manejables. <br/>

```python
#Lista de pesos de correlación de cada variable de satisfacción con la vida 
correlations = dfFinal[['WBSrelations','WBSowntime','WSBeconomy','WSOovsat']].corr()['WSOovsat'][:-1]

#Variable y opción B 
dfFinal['LifeSatisfaction1'] = (dfFinal['WBSrelations'] * correlations[0] + dfFinal['WBSowntime'] * correlations[1] \
                            + dfFinal['WSBeconomy'] * correlations[2] + dfFinal['WSOovsat']) / [dfFinal['LifeSatisfaction1'].max() / 10]
```

* **Variables predictoras**: <br/>

La razón de que haya dos modelos o predictores es que el cambio de cuestionario no permite reconstruir datos de las variables que he identificado por el momento como óptimas para realizar el modelo (variables relacionadas con la privación de condiciones materiales a nivel personal). <br/>

**Variables Modelo 1 - Año 2013 - 2018:** <br/>

X1 - 'vhRentaa': Numérica - Sin normalizar <br/> # Ver si eliminar
X2 - 'HousingCost_HighImpactHH': Dummy <br/>
X3 - 'CrConditions_NChronic': Dummy <br/>
X4 - 'HLimitations_NoLimited': Dummy <br/> # Ver si eliminar
X5 - 'MDInternet_Yes': Dummy <br/> # Ver si eliminar
X6 - 'MDSelf_Yes': Dummy <br/>
X7 - 'MDLeisure_Yes': Dummy <br/>
X8 - 'MDFriends_Yes': Dummy <br/>
X9 - 'MDShoes_Yes': Dummy <br/> # Ver si eliminar
X10 - 'MDClothes_Yes': Dummy <br/>
X11 - 'CHealth': Ordinal - Tomada como numérica <br/>
X12 - 'AREMonth': Ordinal - Tomada como numérica <br/>


**Variables Modelo 2 - Año 2004 - 2012:** <br/>

X1 - 'HHHolidays_Yes': Dummy <br/>
X2 - 'HHFood_Yes': Dummy <br/>
X3 - 'HHReserves_Yes': Dummy <br/>
X4 - 'HHComputer_Yes': Dummy <br/>
X5 - 'HHCar_Yes': Dummy <br/> 
X6 - 'HousingCost_HighImpactHH': Dummy <br/>
X7 - 'HousingCost_MediumImpactHH': Dummy <br/>
X8 - 'HHHeath_Yes': Dummy <br/>
X9 - 'vhPobreza_vhPobreza_Yes': Dummy <br/>
X10 - 'vhMATDEP_vhMATDEP_Yes': Dummy <br/>
X11 - 'vhRentaa': Numérica - Sin normalizar <br/>
X12 - 'CHealth': Ordinal - Tomada como numérica <br/>
X13 - 'AREMonth': Ordinal - Tomada como numérica <br/>
X14 - 'CrConditions_NChronic': Dummy <br/>
X15 - 'HLimitations_NoLimited': Dummy <br/>


**Tratamiento variables:**  <br/>
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
Para hacer la predicción al tratar de predecir una variable "numérica" usamos un modelo de regresión, en este caso se han testado 4 modelo, por dos tipos de modelo, en este caso serían 8 modelos. Todos los modelos incluyen las mismas variable de predicción que son las anteriormente mencionadas y con el mismo tratamiento. 

### Modelo A: 2013 - 2018

* **Modelos**

**y1** <br/>
Regresión Linear: Mismas variables y tratamiento <br/>
K-Neighbors: Parámetros - n_neighbors=298 <br/>
Decision Tree: Parámetros - min_samples_split = 7 / max_depth = 4 / min_samples_leaf = 4 <br/>
Random Forest: Parámetros - n_estimators = 200 / min_samples_split = 60 / min_samples_leaf = 60 / max_depth = 10)<br/>

**y2** <br/>
Regresión Linear: Mismas variables y tratamiento <br/>
K-Neighbors: Parámetros - n_neighbors=299 <br/>
Decision Tree: Parámetros - min_samples_split = 7 / max_depth = 13 / min_samples_leaf = 4 <br/>
Random Forest: Parámetros - n_estimators = 600 / min_samples_split = 40 / min_samples_leaf = 50 / max_depth = 10)<br/>

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



### Modelo B: 2013 - 2018

* **Modelos**

**y1** <br/>
Regresión Linear: Mismas variables y tratamiento <br/>
K-Neighbors: Parámetros - n_neighbors=298 <br/>
Decision Tree: Parámetros - min_samples_split = 6 / max_depth = 12 / min_samples_leaf = 4 <br/>
Random Forest: Parámetros - n_estimators = 100 / min_samples_split = 30 / min_samples_leaf = 60 / max_depth = 10)<br/>

**y2** <br/>
Regresión Linear: Mismas variables y tratamiento <br/>
K-Neighbors: Parámetros - n_neighbors=298 <br/>
Decision Tree: Parámetros - min_samples_split = 6 / max_depth = 11 / min_samples_leaf = 12 <br/>
Random Forest: Parámetros - n_estimators = 100 / min_samples_split = 30 / min_samples_leaf = 60 / max_depth = 10)<br/>

* **Resultados**

|Modelos y1    | Regresión Lineal | K-Neighbors | Decision Tree | Random Forest |
|--------------|------------------|-------------|---------------|---------------|
|MAPE          | 0.986563         | 1.126348    | 1.023922      | 0.984517      |
|MAE           | 0.986563         | 1.126348    | 1.023922      | 0.984517      |
|RMSE          | 1.270690         | 1.449018    | 1.318110      | 1.267687      |
|Correlation   | 0.531048         | -           | -             | -             |
|RSquared      | 0.281263         | -           | -             | -             |

|Modelos y2    | Regresión Lineal | K-Neighbors | Decision Tree | Random Forest |
|--------------|------------------|-------------|---------------|---------------|
|MAPE          | 0.978155         | 1.135251    | 0.995968      | 0.972931      |
|MAE           | 0.978155         | 1.135251    | 0.995968      | 0.972931      |
|RMSE          | 1.2707319        | 1.474600    | 1.297904      | 1.265481      |               
|Correlation   | 0.564819         | -           | -             | -             |
|RSquared      | 0.318416         | -           | -             | -             |


## Conclusiones y valoración final 

* Mejoras del modelo asociadas a la inclusión de datos e intercambio de variables
Las primeras fases del proyecto las he realizado únicamente con datos de 2018 por desconocimiento de la existencia de la existencia del mismo contenido en la versión del año 2013 conjuntamente con el intercambio de unas variables por otras. Además en este caso creo que el azar de los años en los que se han realizado las mediciones (2013 y 2018) debido a la diferencia de las características de la población a nivel económico ha podido contribuir favorablemente al modelo. Si bien esto es sólo una idea que necesitaría explorar más en profunidad para afirmarlo.  <br/>

Con respecto a normalización de variables, las dos únicas variables continuas son la renta y el indicador de satisfacción con la vida. No he observado cambios sustanciales al normalizar por lo que finalimente no he aplicado normalización en el modelo. No obstante conviene plantearse la opción de normalizar el salario de manera anual para examinar el efecto que puede tener sobre el modelo ya que el poder adquistivo / renta varían con el tiempo. Realicé ese ejercicio de manera global (comparando los resultados de las medias anuales) sin observar cambios, no obstante una vez terminado el proyecto parece necesario revisar los datos con más profundidaz para ver el efecto que tiene sobre la distribución por quintiles. <br/>

* Una mayor correlación no implica necesariamente la reducción sustancial del error
Pese a que el indicador construido a partir de darle mayor peso a una de las variables (satisfacción con la vida) sobre el resto para generar más heterogeneidad y sobre todo de cara maximizar las correlaciones de los predictores con el indicador, las diferencias en la correlación de las variables del modelo a nivel global y el R2 mejoran poco entre ambos indicadores. Por otro lado si nos fijamos en el resultado de los errores la mejoría es incluso menor. <br/> 

* Los efectos de correlación entre variables a pesar de no afectar al error pueden dar lugar a resultados no deseables
Como en todo en esta vida el sentido común es win - win. El efecto de la colinearidad entre la valoración del estado de salud y la presencia de enfermades crónicas (0,58) pese a no afectar al error conlleva que la estimación de la felicidad de los individuos sanos descienda (coeficiente negativo si el individuo no tiene enfermedades). Esto no sólo contradice al sentido común o la literatura, sino a los propios datos (la correlación en el dataset de las variables satisfacción con la vida y presencia de enfermedades crónicas es negativa). <br/>

Como segundo resultado indeseado al usar técnicas de selección de variables (Backward Elimination with OLS), la variable Limitaciones físicas en la vida diaria es eliminada si mantenemos la variable enfermedades crónicas, no así si eliminamos la primera. <br/>

En cualquier caso, la correlación entre variables no tiene que ser tan alta para producir resultados indeseados, ya que la posibilidad de tener acceso a internet ha sido eliminada del modelo por el mismo motivo sin tener correlaciones por encima de 0,4 con ninguna de las variables en el modelo. <br/>

* Los cambios en la redacción de las respuestas del cuestionario afectan a los resultados sin que haya estadístico "avise" de ello. 

En este caso el sentido común cobra todavía más fuerza. Debido a cambios en el cuestionario he decidido eliminar los años 2004 a 2007 ya que el punto central de la escala de evaluación de la salud pasa de tener una valencia positiva (aceptable), a una negativa (regular), esto produce un desplazamiento en las respuestas que no es fruto de un cambio de tendencia, sino un error sistemático y que no ocurre sólo en ciencias sociales, . <br/>

Con respecto a esto, la razón por la que me he dado cuenta fue la tasa de respuestas asociadas a los valores extremos 1 y 5, ya que en el fichero resumen de codificación de variables oficial que puedes descargar del INE para ninguno de los años consta este cambio (lo cual por cierto me parece una negligencia de administración). Si lo hace en el cuestionario oficial, documento al que me he remitido en último lugar y en el que he encontrado la respuesta. <br/>

* A nivel reconstrucción de indicadores sociales usar la media como medida de referencia parece no ser óptimo
Pese a existir cambios relevantes en la felicidad, la media es una medida demasiado robusta como para que esos cambios sean perceptibles. Especialmente en el caso de la satisfacción con la vida, donde la mayor parte de las observaciones se apalancan para cualquier periodo en los valores centrales. <br/>

No obstante el histograma comparativo de los valores reales de 2013 y 2018 muestra cambios notables entre ambas distribuciones que no son perceptibles usando la media para visualizar y analizar los datos (si bien es bastante probable que la diferencia entre ambas medias sea significativa dado el tamaño de la muestra la relevancia de los cambios queda invisibilizada por la poca variabilidad del dato). <br/>

Para hacer frente a ese problema, en este proyecto se ha optado por realizar una división por quitiles de todas las observaciones estimadas, que si bien quizá no sea la mejor opción, permite evaluar los datos con más amplitud. <br/>

* Existe poca diferencia entre los resultados de los modelos 
Los dos modelos que tienen mejores resultados son la regresión lineal y el random forest, si bien casi todos las pruebas que he hecho las he realizado sobre el modelo de regresión por su simplicidad y porque de manera colateral he acabado con 4 modelos x 4 modelos (falta de variables para algunos años) para lo cual probablemente debería haber usado otro enfoque. <br/>

## Conclusiones y valoración final 

Como valoración final el resultado del ejercicio me parece satisfactorio porque arroja resultados coherentes y el enfoque me parece adecuado para superar los problemas que han ido surgiendo. Si bien considero necesario especificar que se trata de una estimación y que los datos no son reales, la observación y análisis de las tendencias a nivel personal me parece que tiene valor aunque se utilice simplemente como un indicador de bienestar.

También creo que el modelo tiene margen de mejora pero lo que probablemente tendría un impacto más notable sobre el modelo incluir variables que no ha sido medidas (especialmenter relacionadas con las relaciones personales y el estilo de vida) no es posible.
