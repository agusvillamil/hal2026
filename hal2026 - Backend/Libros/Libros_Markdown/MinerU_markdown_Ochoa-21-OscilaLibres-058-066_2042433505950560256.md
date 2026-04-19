![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/9472dc6e-2055-4d2a-a824-4910cfd28485/6698b86c62fa5fba7ddbf8160c1bd00802028b4200c28cc660856197c49d1f09.jpg)


# MECÁNICA CLÁSICA

Para Estudiantes de Ciencia e Ingeniería. Ochoa 

ISBN: 987-95038-0-5 

RPI: 636496 

# Capítulo II

Interacción Elástica. Oscilaciones Libres. 

Fuerzas Disipativas y Sistemas No Inerciales 

# 2.01 FENÓMENOS PERIÓDICOS.

Como una adecuada introducción al tema se recomienda correr el video 06-Periodicos.wmv, destinado a ilustrar el comportamiento de sistemas físicos que evolucionan con características que se repiten en el tiempo, en cuyo caso diremos que estamos frente a un fenómeno periódico, que podremos caracterizar mediante parámetros como los que se indican a continuación. 

# Período.

Es el tiempo al cabo del cual las magnitudes que caracterizan el estado de un sistema toman nuevamente los mismos valores. Así en el caso de una partícula que se mueve a lo largo de una trayectoria circular con una velocidad de módulo constante, al tiempo que tarda en dar una vuelta completa lo identificamos como el período del movimiento. De la misma manera un cuerpo suspendido a un muelle que es apartado de su posición de equilibrio para luego dejarlo en libertad, oscilará alrededor de dicha posición, en cuyo caso identificaremos al tiempo que tarda en efectuar una oscilación completa como el período de la oscilación. Un vídeo es en realidad una secuencia de fotografías tomadas con intervalos de tiempo muy pequeños para lo cual el obturador de la filmadora esta diseñado de manera que la apertura y cierre del mismo se produce cada un cierto intervalo de tiempo, que reconocemos como período de obturación. Una lámpara de destellos o estroboscópica esta diseñada de manera que produce un corto destello a intervalos de tiempo que podemos prefijar y que reconocemos como período de destellos. 

# Frecuencia.

Entenderemos por frecuencia al número de veces que en un segundo las magnitudes que caracterizan el estado de un sistema toman los mismos valores. Teniendo en cuenta esto es claro que la relación entre la frecuencia y el período vendrá dada por: 

$$
v = \frac {1}{T}
$$

Así, en el caso de una partícula animada de un movimiento circular uniforme, la frecuencia del movimiento nos proporciona el número de vueltas que completa en un segundo (vueltas/seg.). En el caso del resorte que oscila alrededor de su posición de equilibrio, la frecuencia de la oscilación nos proporcionará el número de oscilaciones en la unidad de tiempo. En el caso de la filmadora, la frecuencia de obturación nos proporciona el número de aperturas por segundo y en el caso de la lámpara estroboscópica, su frecuencia de disparos nos proporciona el número de destellos en la unidad de tiempo. 

# Frecuencia angular.

Como lo veremos a lo largo de los próximos temas, a menudo resulta útil definir una nueva magnitud que conocemos como frecuencia angular (w), relacionada con las anteriores mediante: 

$$
\omega = 2 \pi v
$$

por lo tanto 

$$
\omega = \frac {2 \pi}{T}
$$

# Introducción al Estudio de un Movimiento Armónico Simple.

Previamente a iniciar con el tratamiento del tema se recomienda ejecutar el archivo 06-Mas.htm, incluido en la carpeta del mismo nombre que le permitirá acceder a una simulación en la que se ofrece una interesante comparación entre las variaciones temporales observadas en la coordenada vertical de un cuerpo que oscila suspendido a un muelle, con las variaciones temporales en una de las coordenadas que caracterizan la posición de una partícula animada de un movimiento circular uniforme, para diferentes valores que podrá establecer manualmente, de la frecuencia, ángulo de fase y amplitud de la oscilación, en cuyo caso y como se muestra en la figura siguiente, la coordenada de la partícula que se mueve a lo largo de la trayectoria circular dependerá de la coordenada angular según. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/9472dc6e-2055-4d2a-a824-4910cfd28485/74538991b97f74b9e07dd8730dcb88a2e52f13361c6c7dd354aaa94150502c77.jpg)


Donde, teniendo en cuenta que la velocidad angular (w) es constante, a la coordenada angular en función del tiempo podemos expresarla como: 

$$
\theta = \mathrm {w t}
$$

Con lo que la coordenada vertical de la partícula, en función del tiempo, vendrá dada por: 

$$
\mathrm {y (t) = R s e n w t}
$$

Donde hemos supuesto que el valor de la coordenada angular en el instante inicial es nulo, por lo que y suponiendo que en dicho instante la coordenada pudiera tener un valor no nulo, la anterior nos queda: 

$$
y (t) = R s e n (w t + \delta)
$$

Expresión, que como lo podemos apreciar en la simulación indicada anteriormente, también nos caracteriza las variaciones temporales en la coordenada vertical de la partícula que oscila suspendida al muelle alrededor de su posición de equilibrio, en cuyo caso R nos proporciona el máximo valor que toma dicha coordenada y que conocemos como la amplitud con la que oscila el cuerpo alrededor de su posición de equilibrio, siendo este un movimiento que reconoceremos como armónico simple. Teniendo en cuenta que luego de un período el valor de dicha coordenada tendrá que ser el mismo, resulta entonces que: 

$$
R s e n \left[ w (t + T) + \delta \right] = R s e n \left[ w t + w T + \delta \right]
$$

De donde obtenemos que el período deberá ser tal que: 

$$
\mathrm {w T} = 2 \pi \quad \therefore \quad \mathrm {w} = \frac {2 \pi}{\mathrm {T}} \quad \therefore \quad \mathrm {w} = 2 \pi \mathrm {v}
$$

Magnitud que, como ya lo mencionamos, conocemos como frecuencia angular de la oscilación. 

# 2.02 INTERACCIÓN CON UN MUELLE LINEAL.

Consideraremos a continuación las fuerzas que resultan de la interacción con un muelle como las que se sugieren en la figura siguiente. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/9472dc6e-2055-4d2a-a824-4910cfd28485/687f9bc45a0badc6cb94d6728171bb03741f3aabaea8cf2e666499bcad3993c7.jpg)


Llamando longitud propia (l0) a la longitud del muelle sin deformar, se comprueba experimentalmente que para determinados rangos de deformaciones, la fuerza resultante de la interacción entre el muelle y el agente encargado de producir la deformación es proporcional a dicha deformación (δ), como se muestra en la gráfica siguiente, lo que formalmente podemos expresar como: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/9472dc6e-2055-4d2a-a824-4910cfd28485/cc18257cd0ffecd2bf2ee9021be3f5790e42df1fedefac28d51da475635285cf.jpg)


$$
\mathbf {F} = \mathbf {k} \delta
$$

Donde (δ) es la deformación del muelle y (k) una constante que lo caracteriza, que en adelante identificaremos como constante elástica del mismo. 

Con referencia al comportamiento de un muelle cuando es sometido a deformaciones resulta oportuno destacar que la linealidad entre la fuerza y la deformación generalmente no existe en el caso de pequeñas deformaciones y también se pierda si se somete el sistema a grandes deformaciones, dando 

lugar en este último caso al fenómeno conocido como de deformación plástica, consecuencia de lo que una vez liberado el muelle no recupera las características iniciales. Por lo que debe cuidarse de que el sistema opere en la zona lineal, si deseamos que sean válidas las conclusiones mencionadas en el párrafo anterior y evitar el deterioro permanente del muelle empleado. 

# Laboratorio Virtual V

Determinación Estática de la Constante Elástica de un Muelle. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/9472dc6e-2055-4d2a-a824-4910cfd28485/f8b841f307f32ac476257d789450b7606ab03a126395f478b08f99978155c3b5.jpg)


Las imágenes laterales nos muestra las diferentes deformaciones a las que se verá sometido un muelle del que se suspenden cuerpos de diferentes masas, resultando que las deformaciones observadas en el muelle estarán relacionadas con la fuerza aplicada y por lo tanto con el peso y masa de los cuerpos suspendidos, mediante: 

$$
\mathrm {m g} = \mathrm {k} \delta
$$

Donde ( k ) es la constante que caracteriza al muelle, que llamamos constante elástica del mismo. 

Mediante la primera de las simulaciones que se ofrecen en la página a la que puede acceder ejecutando 07-Muelle-1.htm, podrá determinar las deformaciones a las que se ve sometido un muelle, como consecuencia de diferentes masas suspendidas al mismo y con las mediciones realizadas deberá: 

 Representar las deformaciones del muelle en función del peso del cuerpo suspendido. 

Trazar la recta que mejor ajuste al conjunto de puntos obtenidos. 

Determinar la constante elástica del muelle, teniendo en cuenta que para la situación en consideración y de acuerdo a lo indicado anteriormente, las deformaciones del muelle y el peso del cuerpo suspendido estarán relacionados mediante: 

$$
\delta = \frac {1}{k} m g
$$

Con el propósito de realizar comparaciones, mediante el icono “Nuevo” que ofrece la simulación podrá modificar aleatoriamente la constante elástica del muelle empleado, que deberá determinar mediante el mismo procedimiento. 

# Oscilaciones Libres.

Consideremos el caso de un muelle lineal que interactúa con un cuerpo de masa (m) como se muestra en la primera de las figuras seguientes, y supongamos que mediante una interacción externa apartamos al sistema de su posición de equilibrio sometiendo el muelle a una deformación inicial como la sugerida en la segunda figura, para luego dejarlo en libertad de desplazarse a lo largo de la superficie horizontal a la que imaginaremos libre de rozamiento. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/9472dc6e-2055-4d2a-a824-4910cfd28485/8267c4fc3eb3b22bac50552ec7417f0b193486f7a5c311605c5e6502dfcc1e6b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/9472dc6e-2055-4d2a-a824-4910cfd28485/b65c209d9595ea62ae6abe67bc8bb9e4cd2deefa75867fa873f4ed869ecd205b.jpg)


Bajo estas condiciones las fuerzas a que se verá sometido el cuerpo serán las indicadas en el diagrama siguiente, que resultan de su interacción con el campo gravitatorio terrestre, con el muelle y con la superficie horizontal. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/9472dc6e-2055-4d2a-a824-4910cfd28485/f0ee66c50320e937a8bbb9d603366605601a44ae1aa4b28c13f4282028a271d5.jpg)


Con lo que la ecuación de Newton para el centro de masa del cuerpo nos queda expresada como:  

$$
\vec {\mathrm {F}} + \vec {\mathrm {N}} + \mathrm {m} \vec {\mathrm {g}} = \mathrm {m} \vec {\mathrm {a}}
$$

Con el propósito de evaluar las componentes de esta ecuación emplearemos en un sistema de ejes cartesianos como el indicado en las figuras anteriores, donde suponemos al origen coincidente con la posición en la que el centro de masa del cuerpo está en equilibrio, que en este caso es coincidente con aquella posición en la que el resorte está sin deformar y por lo tanto, la deformación del resorte coincidirá en todo momento con la coordenada horizontal del centro de masa del cuerpo, con lo que la fuerza a la que se verá sometido como resultado de su interacción con el muelle puede expresarse como: 

$$
\vec {\mathrm {F}} = - \mathrm {k x} \vec {\mathrm {i}}
$$

Que nos muestra una interesante semejanza con la forma que caracteriza a una fuerzas elástica, en cuyo caso dicha magnitud vendrá dada por: 

$$
\vec {\mathrm {F}} = - \mathrm {k} \vec {\mathrm {r}}
$$

Siendo éste el motivo por el que a la constante del muelle la conocemos como constante elástica. Sin embargo debe observarse que existe una importante diferencia entre estas dos fuerzas, mientras la primera siempre es de naturaleza atractiva, la que resulta de la interacción con el muelle lineal será atractiva cuando la coordenada sea positiva o sea cuando el muelle está elongado y tendrá sentido opuesto cuando el muelle está comprimido, esto es cuando dicha coordenada es negativa. 

Teniendo en cuenta los aspectos mencionados es claro que al evaluar la componente horizontal de la ecuación vectorial planteada inicialmente obtenemos la ecuación escalar que se indica a continuación: 

$$
- k x = m \ddot {x}
$$

De donde: 

$$
\ddot {x} = - \frac {k}{m} x
$$

Resultando que la aceleración del cuerpo variará con su coordenada horizontal como se sugiere en la figura siguiente. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/9472dc6e-2055-4d2a-a824-4910cfd28485/0f926130e8d1542a79e07978bd62799076f13559b035d6879764706ab6a447b7.jpg)


Separando variables a partir de la expresión para la aceleración en función de la coordenada, resulta: 

$$
\dot {x} d \dot {x} = - \frac {k}{m} x d x
$$

Integrando entre límites compatibles, que tengan en cuenta las condiciones iniciales, obtenemos: 

$$
\int_ {\circ} ^ {\dot {x}} \dot {x} d \dot {x} = - \frac {k}{m} \int_ {x _ {o}} ^ {x} x d x
$$

De donde, luego de efectuar las integraciones en ambos miembros, resulta: 

$$
\dot {\mathbf {x}} ^ {2} = \frac {\mathbf {k}}{\mathbf {m}} \left(\mathbf {x} _ {\circ} ^ {2} - \mathbf {x} ^ {2}\right)
$$

Por lo tanto, el movimiento estará acotado entre dos valores extremos de la coordenada horizontal, dados por el valor de la deformación inicial del muelle, como se sugiere en la figura siguiente. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/9472dc6e-2055-4d2a-a824-4910cfd28485/7faebf5a165698ec012b23b81ac1ef460d80ee79ca4221ed6b2c2c99d8118a03.jpg)


Resultando así una interesante similitud con la situación planteada al considerar el comportamiento de una partícula en un túnel diametral en el interior de un planeta, por lo que procediendo de manera semejante obtendremos que la coordenada horizontal variará con el tiempo según: 

$$
\mathbf {x} (\mathbf {t}) = \mathbf {x} _ {\circ} \cos (\mathbf {w t})
$$

Por lo tanto se tratará de un movimiento en donde el cuerpo oscila alrededor de su posición de equilibrio con una frecuencia angular y un período dados por: 

$$
\mathbf {w} = \sqrt {\frac {\mathbf {k}}{\mathbf {m}}}
$$

$$
T = 2 \pi \sqrt {\frac {m}{k}}
$$

En el que la velocidad del centro de masa del cuerpo y su aceleración variarán con el tiempo según: 

$$
\mathbf {v} (\mathbf {t}) = - \mathbf {x} _ {\circ} \mathbf {w} \operatorname {s e n} (\mathbf {w t})
$$

$$
\mathbf {a} (\mathbf {t}) = - \mathbf {x} _ {\circ} \mathbf {w} ^ {2} \cos (\mathbf {w t})
$$

Resultando para las funciones obtenidas gráficas cualitativas similares a las mostradas en la aplicación mencionada anteriormente y que se reiteran a continuación. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/9472dc6e-2055-4d2a-a824-4910cfd28485/91e93af1795767b1573db7f15f9b37555534cac07afdba77bafdfce9b5fe399d.jpg)



v(t)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/9472dc6e-2055-4d2a-a824-4910cfd28485/cacb7c4d17aa9a145b7adb0746fbdd3d2fe80477c0a62531f1df96f491c318a7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/9472dc6e-2055-4d2a-a824-4910cfd28485/55ea40fca8db96e534b1f1b721e486420f2e295fac2d2de10952e9d5edb60ce6.jpg)


# Laboratorio Virtual VI.

# Determinación Dinámica de la Constante Elástica de un Muelle.

La segunda simulación incluida en la página a la que se hace referencia anteriormente, le permitirá, mediante el cronómetro incluido en dicha simulación, determinar el período con el que oscilan cuerpos de diferentes masas suspendidos a un muelle y con los valores obtenidos deberá: 

Representar el cuadrado del período en función de la masa suspendida. 

 Trazar la recta que pasando por el origen, mejor ajuste al conjunto de puntos obtenidos. 

Determinar la constante elástica del muelle, teniendo en cuenta que para la situación en consideración, dicho período vendrá dado por: 

$$
\mathrm {T} ^ {2} = \frac {4 \pi^ {2}}{\mathrm {k m u l}}
$$

Con el propósito de mejorar la calidad de los resultados y para cada masa suspendida, se recomienda determinar el tiempo en el que se completan diez oscilaciones consecutivas y a partir de este valor obtener el período con el que ha oscilado el sistema. 

Con el propósito de realizar comparaciones y mediante el icono “Nuevo” ofrecido en la simulación, podrá modificar aleatoriamente la constante elástica del muelle, que deberá determinar mediante el procedimiento recientemente indicado. 

# 2.03 PÉNDULO PUNTUAL.

Como una aplicación de los temas tratados, consideremos un sistema formado por un cuerpo suspendido de una cuerda inextensible y de masa despreciable, en donde las dimensiones de dicho cuerpo son menores que el error con que se determina la longitud de la cuerda que lo sujeta, como el que se muestra en la figura lateral y que conocemos como Péndulo Puntual. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/9472dc6e-2055-4d2a-a824-4910cfd28485/d41aeb48ffb2711818facf12f8d003bc23bca02d1baf71b7511ffb9c553e6a57.jpg)


Suponiendo que el sistema se aparta de la posición de equilibrio, manteniendo la cuerda extendida para luego dejarlo en libertad, es claro que para un instante posterior cualquiera, la partícula se desplazará a lo largo de un arco de circunferencia de radio (L) y estará sometida al conjunto de fuerzas que se indican en la figura anterior, consecuencias de la interacción gravitatoria y de la interacción con la cuerda, con lo que la ecuación de Newton para la partícula suspendida nos queda: 

$$
\vec {\mathrm {T}} + \mathrm {m} \vec {\mathrm {g}} = \mathrm {m} \vec {\mathrm {a}}
$$

Que evaluada en componentes según las direcciones polares indicadas en la figura anterior, nos proporciona las siguientes ecuaciones escalares: 

$$
\left. \vec {\mathrm {e}} _ {\mathrm {r}} \right\rangle \quad \mathrm {m g} \operatorname {s e n} \theta - T = \mathrm {m} \left(\ddot {\mathrm {r}} - r \dot {\theta} ^ {2}\right)
$$

$$
\left. \vec {\mathrm {e}} _ {\theta} \right\rangle \quad \mathrm {m g} \cos \theta = \mathrm {m} \left(\mathrm {r} \ddot {\theta} + 2 \dot {\mathrm {r}} \dot {\theta}\right)
$$

Teniendo en cuenta que la distancia de la partícula al polo (punto de sustentación) permanece constante e igual a la longitud (L) de la cuerda, de las anteriores resulta: 

$$
\left. \vec {\mathrm {e}} _ {\mathrm {r}} \right\rangle \quad \mathrm {m g} \sin \theta - \mathrm {T} = - \mathrm {m L} \dot {\theta} ^ {2}
$$

$$
\left. \vec {\mathrm {e}} _ {\theta} \right\rangle \quad \mathrm {m g} \cos \theta = \mathrm {m L} \ddot {\theta}
$$

Con lo que de la componente transversal obtenemos que la coordenada angular de la partícula vendrá expresada por una función del tiempo por la solución de la ecuación: 

$$
\ddot {\theta} = - \left(\frac {g}{L}\right) \cos \theta
$$

Que en términos de la coordenada angular (φ), determinada a partir de la posición de equilibrio nos queda: 

$$
\ddot {\phi} = - \left(\frac {g}{L}\right) \text {s e n} \phi
$$

Solución Aproximada para Oscilaciones con Pequeñas Amplitudes. 

Suponiendo que en el instante inicial, y durante el intervalo de tiempo de interés la coordenada angular involucrada en la expresión anterior es “pequeña” de manera que sea válida la aproximación: 

$$
\operatorname {s e n} \phi \cong \phi
$$

Entonces, bajo estas condiciones la coordenada angular que describe el comportamiento de la partícula deberá ser una función tal que sea solución de la ecuación: 

$$
\ddot {\phi} = - \left(\frac {g}{L}\right) \phi
$$

Que como podemos notar es formalmente similar a la ecuación resuelta al considerar las oscilaciones libres de un cuerpo que interactua con un muelle lineal, que se reitera a continuación. 

$$
\ddot {\mathbf {x}} = - \frac {\mathbf {k}}{\mathbf {m}} \mathbf {\Delta x}
$$

Con lo que las conclusiones logradas en aquella oportunidad serán válidas para la situación en consideración y por lo tanto la coordenada angular variará en el tiempo según: 

$$
\phi = \phi_ {\circ} \cos (\mathrm {w t})
$$

Donde la frecuencia angular vendrá dada por: 

$$
\mathbf {w} = \sqrt {\frac {\mathbf {g}}{\mathbf {L}}}
$$

Y por lo tanto la partícula oscilará alrededor de su posición de equilibrio con un período dado por: 

$$
\mathrm {T} = 2 \pi \sqrt {\frac {\mathrm {L}}{\mathrm {g}}}
$$

Siendo interesante destacar que en el tratamiento no se ha considerado la fuerza que resulta de la interacción con la atmósfera, que de considerarse daría lugar a un movimiento oscilatorio con una amplitud decreciente, que será tratado en el próximo volumen. 

Asimismo es importante mencionar que la solución lograda recientemente es solamente una adecuada aproximación, útil en el tratamiento de algunas situaciones de interés como la que consideraremos en la experiencia virtual que se recomienda posteriormente. 

Solución General para el Período de un Péndulo Puntual. 

Considerando nuevamente la ecuación. 

$$
\ddot {\phi} = - \left(\frac {g}{L}\right) s e n \phi
$$

Es posible demostrar que en general, el período con el que oscilará el péndulo vendrá dado por: 

$$
T = 2 \pi \left(\frac {L}{g}\right) ^ {\frac {1}{2}} \left(1 + \frac {1}{4} k ^ {2} + \frac {9}{6 4} k ^ {4} + \dots \dots \dots \dots\right)
$$

Donde la constante (k) depende de la amplitud con la que oscila el sistema, según: 

$$
k = \operatorname {s e n} \left(\frac {\phi_ {\circ}}{2}\right)
$$

Con lo que vemos que en general el período de un péndulo dependerá de la amplitud con la oscila alrededor de su posición de equilibrio. 

Considerando nuevamente aquella situación en la que es válida la aproximación: 

$$
\operatorname {s e n} \phi \cong \phi
$$

De la expresión recientemente obtenida para el período del péndulo, resulta que bajo estas condiciones, la mencionada magnitud vendrá dada por: 

$$
T = 2 \pi \left(\frac {L}{g}\right) ^ {\frac {1}{2}} \left(1 + \frac {1}{1 6} \phi_ {\circ} ^ {2} + \frac {9}{1 0 2 4} \phi_ {\circ} ^ {4} + \dots \dots \dots \dots\right)
$$

Que como podemos notar no coincide con la obtenida anteriormente bajo las mismas condiciones, esto es. 

$$
T = 2 \pi \sqrt {\frac {L}{g}}
$$

Motivo por el que cuando la obtuvimos, mencionamos que solo se trataba de una adecuada aproximación al período de un péndulo puntual que oscila con pequeñas amplitudes, ya que cuando la amplitud de la oscilación es tal que el segundo término del desarrollo en serie de potencias es inferior al error con el que deseamos determinaremos el período de las oscilaciones, dicho término y los restantes podrán despreciare y considerar al período dado por la expresión anterior. 

# Laboratorio Virtual VII.

# Determinación de “g” mediante un Péndulo Puntual.

Mediante la primera simulación que se ofrece en la página a la que puede acceder ejecutando el archivo 08-Péndulo.htm, podrá determinar el período con el que oscilan péndulos de diferentes longitudes en diferentes planetas de nuestro sistema, con lo que deberá obtener la aceleración de la gravedad en la superficie de la Tierra, la Luna y Júpiter, para lo cual en cada uno de los planetas mencionados y luego de determinar el período de por lo menos siete péndulos de longitudes diferentes, deberá: 

 Representar el cuadrado del período en función de la longitud del péndulo empleado. 

 Trazar la recta que, pasando por el origen, mejor ajuste al conjunto de puntos obtenidos. 

Determinar el valor de “g” en la superficie del planeta, teniendo en cuenta que para la situación en consideración, el período en cada péndulo vendrá dado por. 

$$
\mathrm {T} ^ {2} = \frac {4 \pi^ {2}}{\mathrm {g}} \mathrm {L}
$$

# Laboratorio Virtual VIII.

Variaciones del Período con la Amplitud con que Oscila un Péndulo Puntual. 

Mediante la segunda simulación ofrecida en la página mencionada anteriormente podrá determinar el período de un péndulo puntual, para diferentes valores de la amplitud con la que oscila alrededor de su posición de equilibrio y con los valores obtenidos podrá verificar la dependencia entre ambas magnitudes, como lo prevé la siguiente expresión. 

$$
T = 2 \pi \left(\frac {L}{g}\right) ^ {\frac {1}{2}} \left(1 + \frac {1}{4} k ^ {2} + \frac {9}{6 4} k ^ {4} + \dots \dots \dots \dots\right)
$$

Donde recordemos que la constante $( \dot { \bf k } )$ depende de la amplitud con la que oscila el sistema, según: 

$$
k = \operatorname {s e n} \left(\frac {\phi_ {\circ}}{2}\right)
$$