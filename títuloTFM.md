# Título del proyecto
Un proyecto para profundizar en el impacto de la economía y las condiciones socioeconómicas en la felicidad de la población española a través del tiempo. 

## Motivación del proyecto

### Antecedentes
¿Qué son las medidas de bienestar subjetivas?:
Como su propio nombre indica las [medidas de bienestar subjetivas (Subjective Wellbeing Measures)](https://en.wikipedia.org/wiki/Subjective_well-being#Construction_of_SWB) son métricas que se usan comunmente en psicología para evaluar el nivel de felicidad de los individuos, y, como su propio nombre indica son subjetivas porque son las personas las que hacen un autodiagnóstico de si mismos a través de un cuestionarion. 

¿Cuál es su origen?:
Este tipo de métricas fueron ideadas, evaluadas y puestas en práctica en el campo de la psicología en Estados Unidos durante los años 80 por [Ed Driener](https://en.wikipedia.org/wiki/Ed_Diener#Happiness_research), que ha desarrollado su carrera en este ámbito de estudio contribuyendo no sólo a la generación de las métricas, sino a entender los factores que afectan a la felicidad de las personas como el salario, la personalidad, o el contexto cultural o económico. 

¿Para qué se usan?:
En la actualidad sigue investigándose sobre las condiciones y factores que impactan en la felicidad de los individuos tanto a nivel académico como desde instituciones internacionales como la ONU, a través del [World Happiness Report](https://worldhappiness.report/) o instituciones que se dedican a tiempo completo a este tema como el Research [Happiness Research Institute](https://www.happinessresearchinstitute.com/)

### Objetivo e interés del proyecto 
Como ya ha sido evidenciado a través de estudios transnacionales y longitudinales existe relación entre el bienestar en término de medidas de bienestar subjetivo y las condiciones económicas y el salario de los individuos. Estos estudios se basan en la realización de encuestas que permiten establecer el impacto de los factores en el nivel de características. 

Pero ¿qué pasa cuándo no se han realizado mediciones? ¿Se ha perdido esa información para siempre? ¿Es posible predecir la felicidad de los individuos usando macroencuestas y su propia autoevaluación?

El objetivo del proyecto por tanto es realizar y evaluar un modelo con la intención de hacer una reconstrucción histórica en España. 

## Fuentes
La fuente de datos con la que voy a trabajar es [encuesta sobre las convidiones de vida (ECV)](https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176807&menu=resultados&idp=1254735976608#!tabs-1254736194793), 
una macroencuesta anual del INE que realiza mediciones de bienestar subjetivo para el año 2013 y 2018.
Este estudio está originalmente planteado para medir la distribución y persistencia de la pobreza en España, e incluye mediciones longitudinales y transversales, 
así como mediciones de las actitudes y situación de cada uno de los miembros del hogar y también de la situación económica de los hogares. Por su vínculo la medición de las condiciones de vida nos aportará variables relevantes que con anterioridad en la literatura se ha demostrado que guardan relación con el nivel de felicidad, si bien hay otras que no están tan bien definidas (especialmente aquellas vinculadas con las relaciones personales y el ocio, así como otro tipo de variables más relacionadas con el estilo de vida). 

#### Estructura de la muestra 


## Descripción del fichero
El fichero que contiene los datos y que puedes encontrar en este repositorio en la carpeta /Data con el nombre XXX se ha generado a través de la concatenación de ficheros de la ECV desde 2004 a 2019 y que consta además de otros 3 ficheros por año (fichero de la información geográfica del hogar, fichero de las condiciones económicas del hogar y fichero de la persona). Puedes acceder a estos ficheros igualmente en la carpeta Data/Files o decargar directamente los ficheros de microdatos desde la página del [INE](https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176807&menu=resultados&idp=1254735976608#!tabs-1254736195153).

#### Estructura del fichero  

Estructura Xfilas / XColumnas <br/>
Las filas se componen de datos tipo individuo adjuntados a datos del hogar, que se encuentran están duplicados tantas veces como personas componen el hogar de referencia.<br/>

*Year_IndID*: Identificador unico, incluye año (4 primeros caracteres), individuo (2 últimos caracteres), hogar caracteres intermedios. <br/>
*CHealth*: Estado de salud, tomada como numérica con valores 1 a 5 <br/>
*CrConditions*: Presencia de afecciones crónicas Cod 1 - Sí, Cod 2 - No <br/>
*HLimitations*: Presencia de limitaciones en la vida diaria Cod <br/>
*MDClothes*:  Capacidad de poder reponer su ropa Cod 1- Sí, Cod 2 - No, por cuestiones económicas, Cod 3 - No por otras razones <br/>
*MDShoes*: Capacidad de poder reponer sus zapatos Cod 1- Sí, Cod 2 - No, por cuestiones económicas, Cod 3 - No por otras razones <br/>
*MDFriends*: Capacidad de gastarse dinero en salir a tomar algo con otras personas Cod 1- Sí, Cod 2 - No, por cuestiones económicas, Cod 3 - No por otras razones <br/>
*MDLeisure*: Capacidad de gastarse dinero en actividades de ocio Cod 1- Sí, Cod 2 - No, por cuestiones económicas, Cod 3 - No por otras razones <br/>
*MDSelf*: Capacidad de gastarse dinero en uno mismo y lo que le gusta Cod 1- Sí, Cod 2 - No, por cuestiones económicas, Cod 3 - No por otras razones <br/>
*MDInternet*: Capacidad de tener acceso a internet Cod 1- Sí, Cod 2 - No, por cuestiones económicas, Cod 3 - No por otras razones <br/>
*AREMonth*: Facilidad para llegar a fin de mes en ecala numérica 1 a 6 <br/>
*HousingCost*: Impacto del coste de la vivienda en la economía del hogar Cod 1 Alto impacto, Cod 2 - Impacto medio, Cod 3 - Impacto bajo <br/>
*vhRentaa*: Renta armonizada (incluye toda la información relativa a gastos e ingresos del cuestionario) <br/>
*vhPobreza*: Hogar en riesgo de pobreza <br/>
*vhMATDEP*: Hogar con carencia material severa <br/>
*HHFood*: Capacidad de adquirir comida Cod 1 - Sí, Cod 2 - No <br/>
*HHHolidays*: Capacidad de pagarse unas vacaciones Cod 1 - Sí, Cod 2 - No <br/>
*HHReserves*: Capacidad de tener reservas de ahorros Cod 1 - Sí, Cod 2 - No <br/>
*HHPhone*: Tenecia de teléfono en el hogar Cod 1 - Sí, Cod 2 - No, por razones económicas, Cod 3 - No, por otras razones <br/>
*HHTV*: Tenencia de televisor en el hogar Cod 1 - Sí, Cod 2 - No, por razones económicas, Cod 3 - No, por otras razones <br/>
*HHComputer*: Tenencia de ordenador en el hogar Cod 1 - Sí, Cod 2 - No, por razones económicas, Cod 3 - No, por otras razones <br/>
*HHWashMachine*: Tenencia de lavadora en el hogar Cod 1 - Sí, Cod 2 - No, por razones económicas, Cod 3 - No, por otras razones <br/>
*HHCar*: Tenencia de coche en el hogar Cod 1 - Sí, Cod 2 - No, por razones económicas, Cod 3 - No, por otras razones <br/>
*HHHeath*: Capacidad de poner la calefacción en invierno Cod 1 - Sí, Cod 2 - No <br/>

#### Tratamiento de los datos

Variable target:

La variable target se compone de la combinación de 4 variables relacionadas con la satisfacción con la vida para evitar que la variable que se va a predecir sea únicamente una variable de escala de 10 puntos y tenga puntos intermedios <br/>

Para evaluar la pertinencia del uso de las variables se ha usado el test [Alpha de Chronbach](https://es.wikipedia.org/wiki/Alfa_de_Cronbach). Como resultado se ha obtenido la misma variable por dos procedimientos distintos. <br/>

y - Opción A: LifeSatisfaction 0 - Esta variable es la media aritmética de distintas variables de satisfacción con la vida. <br/>

y - Opción B: LifeSatisfaction 1 - Esta variable es el resultado de sumar la variable de satisfacción con la vida más cada una de las variables secundarias multiplicadas por la correlación de cada una de ellas con la variable de satisfacción con la vida general y reescalado a 10 puntos. La razón de justificar este ejercicio es dar más peso a una variable para evitar que el peso del resto de las variables haga que exista menos relación entre variables. También aunque como en el caso anterior sirve para penalizar y bonificar las respuestas evitando dejar todo el peso en una sóla respuesta subjetiva y además añade más heterogeneidad a las puntuaciones, lo que independientemente del resultado final permite hacer los datos más manejables. <br/>

Predictores: <br/>

La razón de que haya dos modelos o predictores es que el cambio de cuestionario no permite reconstruir datos de las variables que he identificado por el momento como óptimas para realizar el modelo (variables relacionadas con la privación de condiciones materiales a nivel personal). <br/>

Variables Modelo 1 - Año 2013 - 2018: <br/>

X1 - 'vhRentaa': Numérica - Sin normalizar <br/>
X2 - 'HousingCost_HighImpactHH': Dummy <br/>
X3 - 'CrConditions_NChronic': Dummy <br/>
X4 - 'HLimitations_NoLimited': Dummy <br/>
X5 - 'MDInternet_Yes': Dummy <br/>
X6 - 'MDSelf_Yes': Dummy <br/>
X7 - 'MDLeisure_Yes': Dummy <br/>
X8 - 'MDFriends_Yes': Dummy <br/>
X9 - 'MDShoes_Yes': Dummy <br/>
X10 - 'MDClothes_Yes': Dummy <br/>
X11 - 'CHealth': Ordinal - Tomada como numérica <br/>
X12 - 'AREMonth': Ordinal - Tomada como numérica <br/>

Variables Modelo 2 - Año 2004 - 2012: <br/>

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

## Modelo
Para hacer la predicción al tratar de predecir una variable "numérica" usamos un modelo de regresión, en este caso se han testado 4 modelo, por dos tipos de modelo, en este caso serían 8 modelos. Todos los modelos incluyen las mismas variable de predicción que son las anteriormente mencionadas y con el mismo tratamiento. 

### Modelo A: 2013 - 2018

|Modelos | Regresión Lineal | Random Forest |
|--------|------------------|---------------|
|Resultados | xxx | xxxx |



### Modelo B: 2013 - 2018

* Modelo
* Resultados

## Conclusiones y valoración final 
