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

Estructura Xfilas / XColumnas 
Las filas se componen de datos tipo individuo adjuntados a datos del hogar, que se encuentran están duplicados tantas veces como personas componen el hogar de referencia.

*Year_IndID*: Identificador unico, incluye año (4 primeros caracteres), individuo (2 últimos caracteres), hogar caracteres intermedios. <br.>
*CHealth*: Estado de salud, tomada como numérica con valores 1 a 5
*CrConditions*: Presencia de afecciones crónicas Cod 1 - Sí, Cod 2 - No
*HLimitations*: Presencia de limitaciones en la vida diaria Cod
*MDClothes*:  Capacidad de poder reponer su ropa Cod 1- Sí, Cod 2 - No, por cuestiones económicas, Cod 3 - No por otras razones
*MDShoes*: Capacidad de poder reponer sus zapatos Cod 1- Sí, Cod 2 - No, por cuestiones económicas, Cod 3 - No por otras razones
*MDFriends*: Capacidad de gastarse dinero en salir a tomar algo con otras personas Cod 1- Sí, Cod 2 - No, por cuestiones económicas, Cod 3 - No por otras razones
*MDLeisure*: Capacidad de gastarse dinero en actividades de ocio Cod 1- Sí, Cod 2 - No, por cuestiones económicas, Cod 3 - No por otras razones
*MDSelf*: Capacidad de gastarse dinero en uno mismo y lo que le gusta Cod 1- Sí, Cod 2 - No, por cuestiones económicas, Cod 3 - No por otras razones
*MDInternet*: Capacidad de tener acceso a internet Cod 1- Sí, Cod 2 - No, por cuestiones económicas, Cod 3 - No por otras razones
*AREMonth*: Facilidad para llegar a fin de mes en ecala numérica 1 a 6 
*HousingCost*: Impacto del coste de la vivienda en la economía del hogar Cod 1 Alto impacto, Cod 2 - Impacto medio, Cod 3 - Impacto bajo 
*vhRentaa*: Renta armonizada (incluye toda la información relativa a gastos e ingresos del cuestionario)
*vhPobreza*: Hogar en riesgo de pobreza
*vhMATDEP*: Hogar con carencia material severa
*HHFood*: Capacidad de adquirir comida Cod 1 - Sí, Cod 2 - No
*HHHolidays*: Capacidad de pagarse unas vacaciones Cod 1 - Sí, Cod 2 - No
*HHReserves*: Capacidad de tener reservas de ahorros Cod 1 - Sí, Cod 2 - No
*HHPhone*: Tenecia de teléfono en el hogar Cod 1 - Sí, Cod 2 - No, por razones económicas, Cod 3 - No, por otras razones
*HHTV*: Tenencia de televisor en el hogar Cod 1 - Sí, Cod 2 - No, por razones económicas, Cod 3 - No, por otras razones
*HHComputer*: Tenencia de ordenador en el hogar Cod 1 - Sí, Cod 2 - No, por razones económicas, Cod 3 - No, por otras razones
*HHWashMachine*: Tenencia de lavadora en el hogar Cod 1 - Sí, Cod 2 - No, por razones económicas, Cod 3 - No, por otras razones
*HHCar*: Tenencia de coche en el hogar Cod 1 - Sí, Cod 2 - No, por razones económicas, Cod 3 - No, por otras razones
*HHHeath*: Capacidad de poner la calefacción en invierno Cod 1 - Sí, Cod 2 - No

#### Tratamiento de los datos

Variable target:

La variable target se compone de la combinación de 4 variables relacionadas con la satisfacción con la vida para evitar que la variable que se va a predecir sea únicamente una variable de escala de 10 puntos y tenga puntos intermedios

Para evaluar la pertinencia del uso de las variables se ha usado el test [Alpha de Chronbach](https://es.wikipedia.org/wiki/Alfa_de_Cronbach). Como resultado se ha obtenido la misma variable por dos procedimientos distintos. 

y - Opción A: LifeSatisfaction 0 - Esta variable es la media aritmética de distintas variables de satisfacción con la vida.  

y - Opción B: LifeSatisfaction 1 - Esta variable es el resultado de sumar la variable de satisfacción con la vida más cada una de las variables secundarias multiplicadas por la correlación de cada una de ellas con la variable de satisfacción con la vida general y reescalado a 10 puntos. La razón de justificar este ejercicio es dar más peso a una variable para evitar que el peso del resto de las variables haga que exista menos relación entre variables. También aunque como en el caso anterior sirve para penalizar y bonificar las respuestas evitando dejar todo el peso en una sóla respuesta subjetiva y además añade más heterogeneidad a las puntuaciones, lo que independientemente del resultado final permite hacer los datos más manejables. 

Predictores: 

Modelo A: 

X1:
X2:
X3:
X4:
X5:
X6:
X7:
X8:
X9:
X10:
X11:
X12: 

Modelo B: 

X1:
X2:
X3:
X4:
X5:
X6:
X7:
X8:
X9:
X10:
X11:
X12: 

## Modelo
El cambio metodológico imposibilita usar las mismas variables para el modelo durante todos los años, por lo que el primer modelo abarca las predicciones de 2013 a 2018 
y el segundo modelo de 2004 a 2013.

### Modelo A: 2013 - 2018

* Modelo
* Resultados

### Modelo B: 2013 - 2018

* Modelo
* Resultados

## Conclusiones y valoración final 
