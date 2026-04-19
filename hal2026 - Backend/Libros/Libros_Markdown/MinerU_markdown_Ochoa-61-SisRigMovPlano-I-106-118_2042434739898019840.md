Mecánica Clásica 

Volumen II 

Ochoa 

- 2007 - 

Sistemas Rígidos 

Animados de un Movimiento Plano 

ISBN de la Versión Analógica 

987-95038-0-5 

# 6.01 SISTEMA RÍGIDO

A lo largo de este capítulo trataremos de obtener expresiones que nos permitan describir el movimiento de los diferentes puntos de un sistema rígido, entendiendo como tal a un sistema formado por un conjunto discreto o continuo de cuerpos puntuales tales que la distancia entre los mismos permanece constante en el tiempo. Siendo destacable que hemos requerido la invariancia temporal de la distancia entre dos puntos cualquiera, no, la invariancia temporal del vector posición de uno de ellos respecto del restante. 

Con el propósito mencionado, recordemos que al considerar sistemas de referencia con movimiento relativo obtuvimos que los vectores velocidad y aceleración de una partícula determinados respecto de los sistemas involucrados estaban relacionados mediante las expresiones. 

$$
\vec {\mathrm {v}} _ {\mathrm {X Y Z}} = \vec {\mathrm {v}} _ {\mathrm {x y z}} + \vec {\mathrm {V}} _ {\mathrm {X Y Z}} + \vec {\mathrm {w}} \times \vec {\mathrm {r}}
$$

$$
\vec {\mathrm {a}} _ {\mathrm {X Y Z}} = \vec {\mathrm {a}} _ {\mathrm {x y z}} + \vec {\mathrm {A}} _ {\mathrm {X Y Z}} + \vec {\mathrm {w}} \times \vec {\mathrm {w}} \times \vec {\mathrm {r}} + 2 \vec {\mathrm {w}} \times \vec {\mathrm {v}} _ {\mathrm {x y z}} + \dot {\vec {\mathrm {w}}} \times \vec {\mathrm {r}}
$$

# Campo de Velocidades y Aceleraciones.

Consideremos a continuación un sistema rígido o "cuerpo rígido" como lo designaremos frecuentemente y un sistema de referencia (XYZ), que en adelante identificaremos como fundamental, respecto del que pretendemos describir el movimiento de los diferentes puntos del cuerpo. Con este propósito pensemos en un nuevo sistema de referencia (xyz), que en adelante reconoceremos como sistema auxiliar, con origen en un punto (A) cualquiera, perteneciente al cuerpo o a una extensión rígida e imaginaria del mismo, como se sugiere en la figura siguiente, cuyo estado de movimiento suponemos conocido. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/4efd8112-47c1-495d-a5ff-a976daacdbc0/7ebe9f1e757b937bf6965a7bb2a74551ccaefc3484cc808039441af09430d2de.jpg)


Teniendo en cuenta la expresión que nos relaciona los vectores velocidad de una partícula respecto de sistemas de referencia con movimiento relativo y designando con $( \Omega )$ al vector que nos caracteriza el estado de rotación del sistema auxiliar respecto del fundamental, entonces al vector velocidad de un punto (B) cualquiera del cuerpo, podemos relacionarlo con el vector velocidad del punto (A) mencionado en el párrafo anterior, mediante: 

$$
\vec {\mathrm {v}} _ {\mathrm {B / X Y Z}} = \vec {\mathrm {v}} _ {\mathrm {B / x y z}} + \vec {\mathrm {v}} _ {\mathrm {A / X Y Z}} + \vec {\Omega} \times \vec {\mathrm {r}} _ {\mathrm {B / A}}
$$

Suponiendo al sistema auxiliar solidario al cuerpo, esto es, rígidamente vinculado al mismo, es claro entonces que el vector que caracteriza la rotación del sistema coincidirá con el que caracteriza la rotación del cuerpo y el vector velocidad del punto (B) respecto de dicho sistema será nulo, con lo que de la anterior resulta que los vectores velocidad de dos puntos cualquiera del cuerpo, respecto del sistema fundamental (XYZ), estarán relacionados mediante: 

$$
\vec {\mathrm {v}} _ {\mathrm {B}} = \vec {\mathrm {v}} _ {\mathrm {A}} + \vec {\mathrm {w}} \times \vec {\mathrm {r}} _ {\mathrm {B / A}} \tag {6.1}
$$

Donde (w) nos caracteriza el estado de rotación del cuerpo respecto del sistema de referencia fundamental y donde para simplificar la notación, hemos obviado el subíndice (XYZ) puesto que en la anterior todas las velocidades están determinadas respecto del dicho sistema y por lo tanto no cabe posibilidad de confusión. 

Teniendo en cuenta la expresión recientemente obtenida es claro que, conociendo el estado de movimiento de un punto (A) cualquiera del cuerpo (o de una extensión rígida del mismo) y el vector que caracteriza su rotación, mediante (6.1) estamos en condiciones de obtener expresiones para el vector velocidad de cualquier otro punto del sistema. En estos términos diremos que (6.1) nos define el campo de velocidades de los diferentes puntos del cuerpo. 

Resulta oportuno destacar que independientemente del número de partículas (finito o infinito) que integren nuestro sistema rígido, la descripción del estado de movimiento de un punto cualquiera del mismo requerirá en general el conocimiento de dos magnitudes vectoriales, una para 

caracterizar el estado de movimiento de un punto (A) cualquiera del cuerpo, y la restante para caracterizar el estado de rotación del cuerpo, por lo que en general será necesario conocer tres funciones escalares del tiempo vinculadas con las componentes de la primer magnitud mas tres funciones escalares del tiempo destinadas a caracterizar las componentes de la segunda magnitud, con lo que, independiente del número de partículas que integren al sistema rígido, siempre podremos pensarlo como un sistema con seis grados de libertad, en cuanto a que, de acuerdo con lo mencionado recientemente, este será el máximo número de funciones linealmente independientes necesarias para describir el comportamiento de cualquier punto del cuerpo. 

Análogamente, el vector aceleración de un punto (B) cualquiera, puede relacionarse con el vector aceleración de otro punto (A) cualquiera, perteneciente al cuerpo o a una extensión rígida del mismo, mediante: 

$$
\vec {a} _ {\mathrm {B / X Y Z}} = \vec {a} _ {\mathrm {B / x y z}} + \vec {a} _ {\mathrm {A / X Y Z}} + \vec {\Omega} \times \boldsymbol {\Omega} \times \vec {\mathbf {r}} _ {\mathrm {B / A}} + 2 \boldsymbol {\Omega} \times \vec {\mathbf {v}} _ {\mathrm {B / x y z}} + \dot {\vec {\Omega}} \times \vec {\mathbf {r}} _ {\mathrm {B / A}}
$$

De donde, luego de tener en cuenta que al sistema de referencia auxiliar lo suponemos solidario al cuerpo, con lo que, la velocidad angular de dicho sistema coincidirá con la del cuerpo y la aceleración y velocidad del punto (B) respecto del mencionado sistema será nula, de la anterior resulta: 

$$
\vec {\mathrm {a}} _ {\mathrm {B}} = \vec {\mathrm {a}} _ {\mathrm {A}} + \vec {\mathrm {w}} \times \vec {\mathrm {w}} \times \vec {\mathrm {r}} _ {\mathrm {B} / \mathrm {A}} + \dot {\vec {\mathrm {w}}} \times \vec {\mathrm {r}} _ {\mathrm {B} / \mathrm {A}} \tag {6.2}
$$

Donde nuevamente y con el propósito de simplificar la notación, hemos obviado el subíndice (XYZ) en cuanto que las aceleraciones y velocidades involucradas están determinadas respecto del mencionado sistema de referencia y por lo tanto no existe posibilidad de confusión. 

# Componentes Asociadas con la Traslación y Rotación del Cuerpo.

Pretendemos interpretar cada uno de los términos involucrados en las expresiones anteriores: 

Un primer aspecto que resulta conveniente destacar es que todos los puntos del eje de rotación de un cuerpo tienen en cada instante el mismo estado de movimiento, conclusión que es inmediata a partir de (6.1) ya que para dichos punto el segundo término es nulo puesto que incluye el producto dos vectores paralelos como se sugiere en la figura siguiente. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/4efd8112-47c1-495d-a5ff-a976daacdbc0/c41fe8bac00800af7c1186473cc4cdcf2ea33ae0f4b9f67218ea8b730359c7a5.jpg)


Otro aspecto digno de mención es que de acuerdo con (6.1), al vector velocidad de un punto cualquiera del cuerpo siempre podremos pensarlo como la suma de dos componentes, una de ellas común a todos los puntos y que por ese motivo la identificaremos como componente de traslación, mas una componente que depende del punto considerado, claramente vinculada con la rotación del cuerpo como las indicadas en la figura lateral, donde hemos supuesto al cuerpo animado de una rotación horaria a lo largo de un eje perpendicular al plano de la hoja, pasante por (A) y donde con $\mathrm { ( V _ { A } ) }$ caracterizamos el estado de movimiento de dicho punto, claramente coincidente con el de los restantes puntos del eje de acuerdo con lo mencionado en el párrafo anterior. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/4efd8112-47c1-495d-a5ff-a976daacdbc0/103b8428a9fe9925189b4af44f4cd032ef8d4a4405f1e25f987df43dbb9812c8.jpg)


Teniendo en cuenta nuevamente (6.1) resulta sencillo verificar que todos los puntos pertenecientes a una recta paralela al eje de rotación tienen en cada instante el mismo estado de movimiento, como resulta del análisis formal que continua, con el apoyo de la figura siguiente. 

$$
\vec {\mathrm {v}} _ {\mathrm {B}} = \vec {\mathrm {v}} _ {\mathrm {A}} + \vec {\mathrm {w}} \times \vec {\mathrm {r}} _ {\mathrm {B / A}}
$$

$$
\vec {\bf {v}} _ {\mathrm {B}} = \vec {\bf {v}} _ {\mathrm {A}} + \vec {\bf {w}} \times \vec {\bf {r}} _ {\mathrm {C / A}} + \vec {\bf {w}} \times \vec {\bf {r}} _ {\mathrm {B / C}}
$$

$$
\vec {\mathrm {v}} _ {\mathrm {B}} = \vec {\mathrm {v}} _ {\mathrm {A}} + \vec {\mathrm {w}} \times \vec {\mathrm {r}} _ {\mathrm {C / A}}
$$

por lo tanto 

$$
\vec {\mathrm {v}} _ {\mathrm {B}} = \vec {\mathrm {v}} _ {\mathrm {C}}
$$

Considerando nuevamente un eje paralelo al eje de rotación, y dos puntos (C) y (B) perteneciente y no perteneciente a dicho eje, como se muestra en la figura lateral, teniendo en cuenta (6.1), al vector velocidad del punto (B) podemos relacionarlo con el vector velocidad del punto (A), mediante: 

$$
\vec {\mathrm {v}} _ {\mathrm {B}} = \vec {\mathrm {v}} _ {\mathrm {A}} + \vec {\mathrm {w}} \times \vec {\mathrm {r}} _ {\mathrm {B / A}}
$$

Que podemos expresar como: 

$$
\vec {\mathrm {v}} _ {\mathrm {B}} = \vec {\mathrm {v}} _ {\mathrm {A}} + \vec {\mathrm {w}} \times \vec {\mathrm {r}} _ {\mathrm {C / A}} + \vec {\mathrm {w}} \times \vec {\mathrm {r}} _ {\mathrm {B / C}}
$$

De donde resulta: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/4efd8112-47c1-495d-a5ff-a976daacdbc0/c61d05312813cf5f9a9072c6f5100724b54ae65d471838e14d7b58a96112fe72.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/4efd8112-47c1-495d-a5ff-a976daacdbc0/2c5aeaeedbb06a388908b39a18cba57566629af96daa9a44c1c713389dd918cc.jpg)


$$
\vec {\mathrm {v}} _ {\mathrm {B}} = \vec {\mathrm {v}} _ {\mathrm {C}} + \vec {\mathrm {w}} \times \vec {\mathrm {r}} _ {\mathrm {B / C}}
$$

Comparando la última forma de expresar la velocidad del punto (B) con la forma inicial es claro que ésta última es justamente la que correspondería si el cuerpo estuviera rotando, con la misma velocidad angular, alrededor de un eje paralelo al eje de considerado inicialmente, pasante por el punto (C), de donde podemos concluir que, cualquier eje paralelo al eje de rotación puede ser considerado como eje de rotación para describir el movimiento de los diferentes puntos del cuerpo, con la condición de tener en cuenta la componente de traslación que corresponda al eje seleccionado. Por lo tanto es claro que existirán infinitas maneras de describir el estado de movimiento de los diferentes puntos de un cuerpo. 

# Ejemplo (6.1)

Considerando un cilindro cuyo centro de masa se desplaza con una velocidad constante y suponiendo que no existe deslizamiento sobre la superficie horizontal mostrada en la figura, ésta última condición nos garantiza que los puntos de la rueda en contacto con la superficie horizontal tendrán velocidad nula y puesto que el eje de rotación de la rueda será perpendicular al plano de la hoja, entonces los puntos en contacto con la superficie horizontal pueden ser considerados como parte del eje de rotación, con la interesante ventaja de que la velocidad de dichos puntos es nula, con lo que la velocidad de cualquier otro punto del cuerpo puede expresarse como: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/4efd8112-47c1-495d-a5ff-a976daacdbc0/c33b3c3d82363e0207cbb0938c9a88724e902a580760679de99b42a6c9889012.jpg)


$$
\vec {\mathbf {v}} _ {\mathrm {C}} = \vec {\mathbf {w}} \times \vec {\mathbf {r}} _ {\mathrm {C / A}}
$$

$$
\vec {\bf {v}} _ {\mathrm {B}} = \vec {\bf {w}} \times \vec {\bf {r}} _ {\mathrm {B / A}}
$$

En cambio pensando al cilindro animado de una rotación alrededor de un eje coincidente con su eje de simetría, la velocidad del punto periférico vendrá expresada por: 

$$
\vec {\mathrm {v}} _ {\mathrm {B}} = \vec {\mathrm {v}} _ {\mathrm {C}} + \vec {\mathrm {w}} \times \vec {\mathrm {r}} _ {\mathrm {B / C}}
$$

La diferencia entre las dos formas seleccionadas para describir el movimiento de los puntos de la rueda radica en que en el último caso estamos pensando al movimiento de la rueda como una rotación alrededor de un eje coincidente con su eje de simetría superpuesta con una traslación caracterizada por el vector velocidad de los puntos de dicho eje. En cambio en el primer caso estamos pensando al cuerpo animado de una rotación "pura" caracterizada por el mismo vector velocidad angular, alrededor del eje definido por los puntos de contacto con la superficie horizontal. 

Considerando ahora la expresión (6.2), según la cual los vectores aceleración de dos puntos de un sistema rígido están relacionados mediante: 

$$
\vec {\mathrm {a}} _ {\mathrm {B}} = \vec {\mathrm {a}} _ {\mathrm {A}} + \vec {\mathrm {w}} \times \vec {\mathrm {w}} \times \vec {\mathrm {r}} _ {\mathrm {B / A}} + \dot {\vec {\mathrm {w}}} \times \vec {\mathrm {r}} _ {\mathrm {B / A}}
$$

El primer término en el miembro de la derecha deberá ser interpretado como una componente asociada con la traslación del eje de rotación y en cambio a los dos restantes deberemos pensarlos vinculados con la rotación del cuerpo alrededor de dicho eje, como se sugiere en la figura siguiente, donde como en las oportunidades anteriores hemos supuesto al eje de rotación perpendicular a la hoja. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/4efd8112-47c1-495d-a5ff-a976daacdbc0/358115f4773ab14a6a3d1f4d16207bc934991e15133b824b13efe6ffb55c37ed.jpg)


# Movimiento Plano.

A lo largo de este capítulo nos limitaremos al tratamiento de situaciones en las que los cuerpo involucrados están animados de un movimiento plano, entendiendo que esta situación se da cuando la dirección del eje de rotación permanece constante y por lo tanto el vector aceleración angular, si existe, deberá ser tal que: 

$$
\begin{array}{c} \dot {\vec {\mathbf {W}}} \\ \| \vec {\mathbf {W}} \end{array}
$$

Y el vector velocidad de los puntos pertenecientes al eje de rotación, si existe, deberá estar contenido en un plano perpendicular a dicho eje. 

Teniendo en cuenta que en (6.1), el término asociado con la rotación del cuerpo, es perpendicular al vector velocidad angular, y suponiendo dadas las condiciones anteriores es claro entonces que si el cuerpo está animado de un movimiento plano la totalidad de los vectores que caracterizan la velocidad de los diferentes puntos del cuerpo estarán contenidos en planos paralelos entre sí y perpendiculares al vector velocidad angular como se sugiere en la figura siguiente. 

Bajo estas condiciones, definiremos como plano del movimiento al plano perpendicular al eje de rotación que contiene el centro de masa del cuerpo, siendo éste plano el que emplearemos en nuestras representaciones gráficas. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/4efd8112-47c1-495d-a5ff-a976daacdbc0/15bec43c51114198ae2276cf3ee0ca7c9a30d2e984eea60a17e8c4a924103dcb.jpg)


# Ejemplo (6.2)

Considerando nuevamente un cilindro que rueda sin deslizar a lo largo de una superficie horizontal de manera que para el instante de interés su centro de masa se desplaza hacia la derecha con una aceleración constante como se indica en la figura lateral y teniendo en cuenta que los puntos en contacto con la superficie horizontal tienen velocidad nula, la velocidad del centro de masa puede expresarse como: 

$$
\vec {\bf {v}} _ {\mathrm {C}} = \vec {\bf {w}} \times \vec {\bf {r}} _ {\mathrm {C / A}}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/4efd8112-47c1-495d-a5ff-a976daacdbc0/7775f4cd4d91793c9f67825f4f6c28f18f8c56ca3b7920c1fb09bd98ca8db744.jpg)


Evaluando la anterior según las direcciones de los vectores unitarios representados en la figura, obtenemos la ecuación escalar que se indica a continuación, según la dirección del vector unitario i: 

$$
\mathbf {v} _ {\mathrm {C}} = \mathbf {w R}
$$

De donde: 

$$
w = \frac {v _ {C}}{R}
$$

Derivando la anterior y teniendo en cuenta que se trata de un movimiento plano, resulta: 

$$
\dot {\mathrm {w}} = \frac {\dot {\mathrm {v}} _ {\mathrm {C}}}{\mathrm {R}}
$$

Por lo tanto: 

$$
\dot {\vec {w}} = - \frac {a _ {C}}{R} \vec {k}
$$

Finalmente el vector aceleración de los puntos en contacto con la superficie horizontal puede obtenerse teniendo en cuenta que de acuerdo con (6.2) la aceleración de dichos puntos estará relacionada con la del centro de masa mediante: 

$$
\vec {a} _ {\mathrm {A}} = \vec {a} _ {\mathrm {C}} + \vec {\mathrm {w}} \times \vec {\mathrm {w}} \times \vec {\mathrm {r}} _ {\mathrm {A / C}} + \dot {\vec {\mathrm {w}}} \times \vec {\mathrm {r}} _ {\mathrm {A / C}}
$$

Evaluando la anterior en componentes según las direcciones indicadas inicialmente en la figura y teniendo en cuenta la conclusión obtenida anteriormente para el vector aceleración angular, resulta que la aceleración del punto de contacto estará relacionada con la velocidad angular del cilindro mediante: 

$$
\vec {\mathrm {a}} _ {\mathrm {A}} = \mathrm {w} ^ {2} \mathrm {R} \vec {\mathrm {j}}
$$

# Ejemplo (6.3)

Consideremos a continuación el caso de una varilla rígida que apoyada sobre una pared vertical y una superficie horizontal, se desliza de manera que en el instante de interés, representado en la figura siguiente, conocemos la velocidad con que se desplaza el punto en contacto con la superficie horizontal. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/4efd8112-47c1-495d-a5ff-a976daacdbc0/0a1bc318a9751f4974b94dd738299c2c15743beaeb520c26be293bc7974f350e.jpg)


Con el propósito de obtener una expresión para la velocidad angular de la varilla, cuya dirección debe ser perpendicular al plano de la hoja, tengamos en cuenta que el vector velocidad de los puntos extremos (A y B) están relacionados mediante: 

$$
\vec {\mathrm {v}} _ {\mathrm {B}} = \vec {\mathrm {v}} _ {\mathrm {A}} + \vec {\mathrm {w}} \times \vec {\mathrm {r}} _ {\mathrm {B / A}}
$$

Evaluando la anterior según las direcciones caracterizadas por los vectores unitarios indicados en la figura y teniendo en cuenta que como consecuencia de los vínculos a que está sometida la varilla, la dirección y sentido del vector velocidad del punto (B) deberá ser necesariamente el indicado, resulta: 

$$
w = \frac {v _ {A}}{H \cos \theta}
$$

$$
\mathrm {v _ {B}} = \frac {\mathrm {v _ {A}}}{\mathrm {t g} \theta}
$$

Suponiendo que la velocidad del punto en contacto con la superficie horizontal se mantiene constante, con lo que su vector aceleración será nulo, la aceleración del punto en contacto con la pared vertical puede expresarse como: 

$$
\vec {\mathrm {a}} _ {\mathrm {B}} = \vec {\mathrm {w}} \times \vec {\mathrm {w}} \times \vec {\mathrm {r}} _ {\mathrm {B / A}} + \dot {\vec {\mathrm {w}}} \times \vec {\mathrm {r}} _ {\mathrm {B / A}}
$$

Evaluando la anterior según las direcciones ortogonales indicadas en la figura, de la ecuación asociada con la componente horizontal resulta: 

$$
\dot {\mathbf {w}} = \mathbf {w} ^ {2} \operatorname {t g} \theta
$$

Y de la ecuación asociada con la componente vertical obtenemos: 

$$
\vec {a} _ {\mathrm {B}} = - \frac {\mathrm {H w} ^ {2}}{\cos \theta} \vec {\mathrm {j}}
$$

Teniendo en cuenta la expresión obtenida para la velocidad angular en función de la velocidad del punto de contacto con la superficie horizontal, de la anterior obtenemos que: 

$$
\vec {a} _ {\mathrm {B}} = - \frac {\mathrm {v} _ {\mathrm {A}} ^ {2}}{\mathrm {H} \cos^ {3} \theta} \vec {\mathrm {j}}
$$

Se recomienda verificar que la expresión recientemente obtenida para la aceleración angular es coincidente con la que podemos obtener derivando la expresión alcanzada inicialmente para la velocidad angular. 

Finalmente y con el propósito de ejemplificar algunos aspectos discutidos en el tema anterior, notemos que al estado de movimiento de la varilla en cada instante lo podemos describir de diferentes maneras, una de las cuales sería como el de una rotación alrededor de un eje perpendicular a la hoja y pasante por el punto (A) mas una traslación caracterizada por el vector velocidad de dicho punto, o bien como una rotación alrededor de un eje pasante por el punto (B) superpuesta con una traslación caracterizada por el vector velocidad de dicho punto. 

# Centro de Rotación Instantánea.

Considerando un cuerpo animado de un movimiento plano, como los analizados en los ejemplos anteriores, el vector velocidad de dos puntos cualquiera (A y Q), pertenecientes al cuerpo o a extensiones rígidas del mismo, estarán relacionados mediante una expresión del tipo: 

$$
\vec {\mathrm {v}} _ {\mathrm {Q}} = \vec {\mathrm {v}} _ {\mathrm {A}} + \vec {\mathrm {w}} \times \vec {\mathrm {r}} _ {\mathrm {Q / A}}
$$

De donde resulta que en general y para cada instante, siempre podremos encontrar un punto perteneciente al cuerpo o a una extensión rígida del mismo, tal que en dicho instante su velocidad sea nula, o sea un punto (Q) tal que su vector posición respecto de otro punto (A) arbitrario satisfaga la ecuación vectorial: 

$$
\vec {\mathrm {v}} _ {\mathrm {A}} + \vec {\mathrm {w}} \times \vec {\mathrm {r}} _ {\mathrm {Q / A}} = 0
$$

Efectivamente, lo mencionado siempre será posible ya que evaluando la ecuación anterior según direcciones ortogonales coincidentes con el plano del movimiento, resultan las siguientes ecuaciones escalares: 

$$
\mathrm {i} \rightarrow \mathrm {v} _ {\mathrm {x}} + \mathrm {w y} = 0
$$

$$
\mathrm {j} \rightarrow \mathrm {v} _ {\mathrm {y}} - \mathrm {w x} = 0
$$

Siendo (x e y) las componentes del vector posición del punto (Q) respecto del punto (A), según las direcciones ortogonales mencionadas anteriormente y donde para facilitar la notación hemos obviado los subíndices (Q/A) que debieran haberse incluido en las coordenadas del sistema indicado anteriormente. Luego de resolver el sistema de ecuaciones, resulta que cada una de las componentes del vector posición mencionado en el párrafo anterior vendrán dadas por: 

$$
\mathbf {x} = \frac {\mathbf {v} _ {\mathrm {y}}}{\mathbf {w}}
$$

$$
\mathbf {y} = - \frac {\mathbf {v} _ {\mathrm {x}}}{\mathbf {w}}
$$

Conjunto que siempre tendrá solución a menos que el cuerpo este en reposo en cuyo caso carece de sentido preocuparnos por el tema o bien que el cuerpo este animado de una traslación, en cuyo caso el punto que satisface la condición de referencia estaría infinitamente lejos. 

Teniendo en cuenta lo mencionado es claro que si el cuerpo está animado de un movimiento plano, en cada instante, siempre será posible encontrar un punto (Q) perteneciente a dicho cuerpo o a una extensión rígida del mismo tal que en ese instante tenga velocidad nula, en cuyo caso al vector velocidad de cualquier otro punto del cuerpo puede se lo puede expresar, en términos de su coordenada vectorial respecto de dicho punto, que identificaremos como centro de velocidad nula, como: 

$$
\vec {\mathrm {v}} _ {\mathrm {B}} = \vec {\mathrm {w}} \times \vec {\mathrm {r}} _ {\mathrm {B / Q}}
$$

La anterior nos permite interpretar el movimiento del cuerpo como una rotación "pura" alrededor de un eje que pasa por dicho punto, motivo por el que a menudo también se lo suele identificar como 

centro de rotación instantánea. O sea que en ese instante todo sucede como si el cuerpo estuviera animado de solamente una rotación alrededor de un eje que pasa por el centro de velocidad nula, y por lo tanto, de acuerdo con la anterior, el vector velocidad de cualquier otro punto del cuerpo será necesariamente perpendicular a el vector posición del punto considerado, respecto del centro de rotación instantánea, con lo que si conocemos la dirección del vector velocidad de dos puntos del cuerpo, el centro de rotación instantánea se encontrará en la intersección de las rectas normales a los vectores velocidad indicados, como puede observarse en el ejemplo que se considera a continuación. 

# Ejemplo (6.4)

En el caso de la varilla considerada en el ejemplo (6.3), y teniendo en cuenta que la dirección de los vectores velocidad de sus extremos están determinadas como consecuencia de los vínculos a que está sometida la varilla, la posición del centro de rotación instantánea puede obtenerse gráficamente como la intersección de las líneas perpendiculares a los mencionados vectores velocidad de los puntos extremos, tal como se indica en la figura siguiente. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/4efd8112-47c1-495d-a5ff-a976daacdbc0/811e1a4be889ff468cdab7323be8a723289061925ad31c34a63f9643045e3198.jpg)


Nuevamente, observando el diagrama vectorial que acompaña a la figura se ve claramente que para el instante en consideración todo está sucediendo como si la varilla estuviera animada de una rotación "pura" alrededor de un eje perpendicular al plano del movimiento que pasa por el punto Q donde se interceptan las rectas perpendiculares a los vectores velocidad de los extremos de la varilla, mostrados en la figura. 

# Ejemplo (6.5)

Considerando nuevamente el caso del cilindro tratado en el ejemplo (6.2), que se desplaza sin deslizamiento sobre una superficie horizontal, es claro que en esta situación la condición de no deslizamiento determina físicamente, al punto de contacto con la superficie horizontal como centro de rotación instantánea o de velocidad nula. 

Como puede apreciarse en el diagrama vectorial mostrado en la figura siguiente, para el instante en consideración todo está sucediendo como si en dicho instante, el cilindro estuviera animada de una rotación "pura" alrededor de un eje perpendicular a la hoja, que pasa por el punto de contacto con la superficie horizontal. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/4efd8112-47c1-495d-a5ff-a976daacdbc0/4d188ae3263cc1caacd489ad4a02c78dac66c15f765651d8182a01d484947f88.jpg)


# 6.02 ECUACIONES DE MOVIMIENTO

A lo largo de los temas siguientes trataremos de buscar ecuaciones que nos relacionen el estado de movimiento de un cuerpo o mas precisamente los cambios que observamos en su estado de movimiento con las fuerzas que resultan de los mecanismos de interacción a que se encuentra sometido. 

Con este propósito consideraremos al cuerpo como si fuera un sistema discreto de cuerpos puntuales que satisfacen la condición de rigidez. Una vez alcanzadas las expresiones fínales, válidas para un sistema discreto veremos de llevarlas a formas válidas para un sistema rígido continuo mediante sustituciones de los símbolos de sumatorias por los de integración sobre el volumen del cuerpo en 

consideración y las cantidades que identifican las masas de cada una de las partículas por diferenciales de masa en función de la densidad y el correspondiente diferencial de volumen, como se indica a continuación: 

$$
\mathrm {m} _ {\mathrm {i}} \rightarrow \mathrm {d m} = \rho (\vec {\mathrm {r}}) \mathrm {d} \tau
$$

$$
\sum \mathrm {m} _ {\mathrm {i}} \rightarrow \int_ {\tau} \rho (\vec {\mathrm {r}}) \mathrm {d} \tau
$$

Así, a partir de la expresión dada para la coordenada vectorial del centro de masa de un sistema discreto de cuerpos puntuales, que indicamos en primer término, resulta la expresión que indicamos en segundo término, para el caso de un sistema rígido continuo: 

Sistema Rígido Discreto 

$$
\vec {\mathrm {r}} _ {\mathrm {c}} = \frac {\sum \mathrm {m} _ {\mathrm {i}} \vec {\mathrm {r}} _ {\mathrm {i}}}{\sum \mathrm {m} _ {\mathrm {i}}}
$$

Sistema Rígido Continuo 

$$
\vec {r} _ {\mathrm {c}} = \frac {\int_ {\tau} \vec {r} \rho (\vec {r}) d \tau}{\int_ {\tau} \rho (\vec {r}) d \tau}
$$

# Vector Momento Angular.

Teniendo presente lo mencionado y tal como lo adelantáramos en el párrafo inicial, comenzaremos buscando una forma conveniente para expresar al vector momento angular de un sistema rígido de cuerpos puntuales, a partir de las conclusiones obtenidas en el capítulo anterior, según las cuales esta magnitud, calculada respecto del origen de un sistema de referencia (xyz) o respecto de un punto (A) cualquiera no coincidente con dicho origen, venía dada en cada uno de los casos como se indica a continuación: 

$$
\vec {\mathrm {L}} = \vec {\mathrm {r}} _ {\mathrm {c}} \times \mathrm {m} \vec {\mathrm {v}} _ {\mathrm {c}} + \vec {\mathrm {L}} _ {\mathrm {c}}
$$

$$
\vec {\mathrm {L}} _ {\mathrm {A}} = \vec {\mathrm {r}} _ {\mathrm {c} / \mathrm {A}} \times \mathrm {m} \vec {\mathrm {v}} _ {\mathrm {c}} + \vec {\mathrm {L}} _ {\mathrm {c}}
$$

Donde a la componente respecto del centro de masa o intrínseca podemos expresarla como:  

$$
\vec {L} _ {\mathrm {c}} = \sum \vec {r} _ {\mathrm {i}} ^ {\prime} \times m _ {\mathrm {i}} \vec {v} _ {\mathrm {i}} ^ {\prime}
$$

o bien como 

$$
\vec {\mathrm {L}} _ {\mathrm {c}} = \sum \vec {\mathrm {r}} _ {\mathrm {i}} ^ {\prime} \times \mathrm {m} _ {\mathrm {i}} \vec {\mathrm {v}} _ {\mathrm {i}}
$$

Por tratarse de un sistema rígido y teniendo en cuenta (6.1), el vector velocidad de cada una de las partículas considerado en la componente intrínseca puede expresarse en término del vector velocidad del centro de masa y del vector velocidad angular del cuerpo, como: 

$$
\vec {\mathrm {v}} _ {\mathrm {i}} = \vec {\mathrm {v}} _ {\mathrm {c}} + \vec {\mathrm {w}} \times \vec {\mathrm {r}} _ {\mathrm {i}} ^ {\prime}
$$

Donde la coordenada vectorial de cada una de las partículas está determinada respecto del centro de masa del sistema, con lo que la componente intrínseca del vector momento angular resulta: 

$$
\vec {\mathrm {L}} _ {\mathrm {c}} = \sum \vec {\mathrm {r}} _ {\mathrm {i}} ^ {\prime} \times \mathrm {m} _ {\mathrm {i}} (\vec {\mathrm {v}} _ {\mathrm {c}} + \vec {\mathrm {w}} \times \vec {\mathrm {r}} _ {\mathrm {i}} ^ {\prime})
$$

Teniendo en cuenta que: 

$$
\sum \mathrm {m} _ {\mathrm {i}} \vec {\mathrm {r}} _ {\mathrm {i}} ^ {\prime} = 0
$$

De la anterior resulta: 

$$
\vec {\mathrm {L}} _ {\mathrm {c}} = \sum \mathrm {m} _ {\mathrm {i}} \vec {\mathrm {r}} _ {\mathrm {i}} ^ {\prime} \times (\vec {\mathrm {w}} \times \vec {\mathrm {r}} _ {\mathrm {i}} ^ {\prime})
$$

Que luego de desarrollar el producto vectorial triple y obviando el índice superior de la coordenada vectorial para simplificar la notación, nos queda expresada como: 

$$
\vec {L} _ {\mathrm {c}} = \sum \mathrm {m} _ {\mathrm {i}} \left\lfloor \vec {\mathrm {w}} r _ {\mathrm {i}} ^ {2} - \vec {r} _ {\mathrm {i}} (\vec {\mathrm {w}} \cdot \vec {r} _ {\mathrm {i}}) \right\rfloor
$$

Donde recordemos que la coordenada vectorial de cada partícula está determinada respecto del centro de masa del sistema. 

# Sistema Rígido Animado de un Movimiento Plano.

Suponiendo al cuerpo animado de un movimiento plano y evaluando las componentes de la expresión anterior según las direcciones (xyz) de un sistema de ejes ortogonales solidario al cuerpo con origen en su centro de masa, orientado de manera que el plano del movimiento coincida con el plano (xy), como se sugiere en la figura siguiente, el vector velocidad angular del cuerpo queda expresado como: 

$$
\vec {\mathrm {w}} = \mathrm {w} \vec {\mathrm {k}}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/4efd8112-47c1-495d-a5ff-a976daacdbc0/d88eb98a2bce3563b0c5da5167566344ea427286f5e286eb6be0eb1c4171ae9b.jpg)


Entonces, las componentes del vector momento angular en consideración, según las direcciones solidarias indicadas, nos quedan expresadas como: 

$$
\vec {\mathrm {L}} _ {\mathrm {c}} = \sum \mathrm {m} _ {\mathrm {i}} \left[ (\mathrm {x} _ {\mathrm {i}} ^ {2} + \mathrm {y} _ {\mathrm {i}} ^ {2} + \mathrm {z} _ {\mathrm {i}} ^ {2}) \mathrm {w} \vec {\mathrm {k}} - (\mathrm {x} _ {\mathrm {i}} \vec {\mathrm {i}} + \mathrm {y} _ {\mathrm {i}} \vec {\mathrm {j}} + \mathrm {z} _ {\mathrm {i}} \vec {\mathrm {k}}) \mathrm {w} \mathrm {z} _ {\mathrm {i}} \right]
$$

Que luego de ordenar según las direcciones de los vectores unitarios nos queda: 

$$
\vec {\mathrm {L}} _ {\mathrm {c}} = \left[ - \sum \mathrm {m} _ {\mathrm {i}} \mathrm {x} _ {\mathrm {i}} \mathrm {z} _ {\mathrm {i}} \right] \mathrm {w} \vec {\mathrm {i}} + \left[ - \sum \mathrm {m} _ {\mathrm {i}} \mathrm {y} _ {\mathrm {i}} \mathrm {z} _ {\mathrm {i}} \right] \mathrm {w} \vec {\mathrm {j}} + \left\lfloor \sum \mathrm {m} _ {\mathrm {i}} \left(\mathrm {x} _ {\mathrm {i}} ^ {2} + \mathrm {y} _ {\mathrm {i}} ^ {2}\right) \right\rfloor \mathrm {w} \vec {\mathrm {k}}
$$

Siendo importante destacar que, los corchetes incluidos en cada una de las componentes dependen únicamente de las coordenadas de cada una de las partículas respecto de las direcciones del sistema solidario, con origen en el centro de masa, o sea dependen de como está distribuida la materia respecto de las direcciones del mencionado sistema, resultando entonces que los mismos son invariantes temporales y por lo tanto independientes del estado del movimiento del cuerpo en consideración. 

Suponiendo ahora que el plano del movimiento es un plano de simetría o sea que la materia está igualmente distribuida en ambos lados de dicho plano, como se sugiere en la figura siguiente, y teniendo en cuenta que en la expresión anterior hemos supuesto orientados los ejes del sistema solidario de manera que el plano (xy) coincide con el del movimiento, entonces las sumatorias que dependen linealmente de las coordenadas se anularán como consecuencia de su dependencia de la coordenada (z), con lo que en este caso, la componente intrínseca del vector momento angular queda expresada como: 

$$
\vec {\mathrm {L}} _ {\mathrm {c}} = \left| \sum \mathrm {m} _ {\mathrm {i}} \left(\mathrm {x} _ {\mathrm {i}} ^ {2} + \mathrm {y} _ {\mathrm {i}} ^ {2}\right) \right| \mathrm {w} \vec {\mathrm {k}}
$$

Resultando así un vector paralelo al vector que caracteriza la rotación del cuerpo, esto es, paralelo al vector velocidad angular y directamente relacionado con éste a través del término escalar: 

$$
\mathrm {I _ {c}} = \sum m _ {\mathrm {i}} (\mathrm {x _ {i} ^ {2} + y _ {i} ^ {2}})
$$

Que en adelante identificaremos como Momento de Inercia del cuerpo respecto de un eje paralelo al eje de rotación y que pasa por el centro de masa del cuerpo, que en este caso y teniendo en cuenta como hemos orientado los ejes del sistema solidario, coincide con el eje (z) de dicho sistema. 

Con respecto a la magnitud recientemente definida resulta importante observar que dicha magnitud tiene en cuenta como está distribuida la materia respecto de un eje paralelo al eje de rotación pasante por el centro de masa del sistema, en cuanto a que el factor que multiplica a cada una de las masas involucradas no es otra cosa que el cuadrado de su distancia a dicho eje, como se muestra en la figura lateral, donde al plano del movimiento lo hemos dibujado nuevamente, perpendicular al plano de la hoja. 

$$
\mathrm {D _ {i} ^ {2} = x _ {i} ^ {2} + y _ {i} ^ {2}}
$$

Con lo que el momento de inercia puede expresarse como: 

$$
\mathrm {I _ {c}} = \sum m _ {\mathrm {i}} D _ {\mathrm {i}} ^ {2}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/4efd8112-47c1-495d-a5ff-a976daacdbc0/260edb1c25b2f4ff281b84f379331ed87a4da6248d83b9a8d170d68826a68b38.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/4efd8112-47c1-495d-a5ff-a976daacdbc0/ff5f0c3bf6b0daef869104e9fcde7d249b08b7dc36498444e60d1b1b16cd8df7.jpg)


Teniendo en cuenta lo desarrollado, la componente intrínseca del vector momento angular correspondiente a un sistema rígido animado de un movimiento plano y tal que el plano del movimiento es un plano de simetría, queda expresada como: 

$$
\vec {\mathrm {L}} _ {\mathrm {c}} = \mathrm {I} _ {\mathrm {c}} \vec {\mathrm {w}}
$$

Donde el momento de inercia, en el caso de un sistema discreto viene dado por la expresión obtenida recientemente, que para el caso de un sistema continuo y teniendo en cuenta lo mencionado al iniciar el tema, nos queda expresado como: 

$$
\mathrm {I _ {c}} = \int_ {\tau} (\mathrm {x _ {i} ^ {2} + y _ {i} ^ {2}}) \rho (\mathrm {x y z}) \mathrm {d} \tau
$$

Con lo que, el momento angular respecto del origen del sistema de referencia o respecto de un punto cualquiera no coincidente con este, nos quedarán expresados respectivamente, como: 

$$
\vec {\mathrm {L}} = \vec {\mathrm {r}} _ {\mathrm {c}} \times \mathrm {m v} _ {\mathrm {c}} + \mathrm {I} _ {\mathrm {c}} \vec {\mathrm {w}}
$$

$$
\vec {\mathrm {L}} _ {\mathrm {A}} = \vec {\mathrm {r}} _ {\mathrm {c} / \mathrm {A}} \times \mathrm {m v} _ {\mathrm {c}} + \mathrm {I} _ {\mathrm {c}} \vec {\mathrm {w}}
$$

Donde de ahora en mas a la componente intrínseca, la reconoceremos como componente asociada con la rotación del cuerpo o mas comúnmente como componente de "spin", por estar esta directamente vinculada con el vector velocidad angular del cuerpo. 

Trataremos ahora de obtener una expresión para el vector momento angular calculado respecto de un punto perteneciente al cuerpo o a una extensión rígida del mismo que durante el intervalo de tiempo de interés permanece fijo al sistema de referencia (XYZ) respecto del que pretendemos describir el movimiento, como se sugiere en la figura siguiente, en cuyo caso y teniendo en cuenta su definición, vendrá expresado por: 

$$
\vec {\mathrm {L}} _ {\mathrm {Q}} = \sum \vec {\mathrm {r}} _ {\mathrm {i}} \times \mathrm {m} _ {\mathrm {i}} \vec {\mathrm {v}} _ {\mathrm {i}}
$$

Donde, como se indica en la figura lateral la coordenada vectorial está determinada respecto del punto fijo y puesto que el punto respecto del cuál se toma el momento pertenece al cuerpo o a una extensión rígida del mismo y está fijo al sistema de referencia fundamental, el vector velocidad de cada una de las partículas puede expresarse en términos de su coordenada vectorial respecto de dicho punto, como: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/4efd8112-47c1-495d-a5ff-a976daacdbc0/47c30598085085eb3ae3914f3d8eca59a6f4643dcf77c828c5e5b2b8b8c4d475.jpg)


$$
\vec {\mathrm {v}} _ {\mathrm {i}} = \vec {\mathrm {w}} \times \vec {\mathrm {r}} _ {\mathrm {i}}
$$

Con lo que el momento angular del cuerpo determinado respecto del punto fijo nos queda: 

$$
\vec {\mathrm {L}} _ {\mathrm {Q}} = \sum \mathrm {m} _ {\mathrm {i}} \vec {\mathrm {r}} _ {\mathrm {i}} \times (\vec {\mathrm {w}} \times \vec {\mathrm {r}} _ {\mathrm {i}})
$$

Que luego de desarrollar el producto vectorial triple puede expresarse como: 

$$
\vec {\mathrm {L}} _ {\mathrm {Q}} = \sum \mathrm {m} _ {\mathrm {i}} \left[ \vec {\mathrm {w}} \mathrm {r} _ {\mathrm {i}} ^ {2} - \vec {\mathrm {r}} _ {\mathrm {i}} (\vec {\mathrm {w}} \cdot \vec {\mathrm {r}} _ {\mathrm {i}}) \right]
$$

Que como podemos ver es formalmente igual a la expresión (6.3) obtenida para la componente intrínseca del vector momento angular, con la única salvedad de que en aquella oportunidad la coordenada vectorial a considerar estaba determinada respecto del centro de masa del sistema, en cambio en este caso dicha coordenada está determinada respecto del punto fijo perteneciente al cuerpo o a una extensión rígida del mismo. 

Teniendo en cuenta lo mencionado es claro que operando en forma análoga a como lo hiciéramos anteriormente, y evaluando las componentes del vector según las direcciones de un sistema solidario al cuerpo con origen en el punto fijo, como se sugiere en la figura lateral y considerando un sistema rígido animado de un movimiento plano tal que el plano del movimiento sea un plano de simetría, obtendremos para el vector momento angular respecto del punto fijo, una expresión como la que se indica a continuación: 

$$
\vec {\mathrm {L}} _ {\mathrm {Q}} = \mathrm {I} _ {\mathrm {Q}} \vec {\mathrm {w}}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/4efd8112-47c1-495d-a5ff-a976daacdbc0/9d0e62ee667bd0019d388465c5e44aa2915cddaff2ece2009c5b2212d481c9d6.jpg)


Donde ahora el momento de inercia a considerar, está calculado respecto de un eje paralelo al eje de rotación que pasa por el punto fijo y que por lo tanto, tiene en cuenta la distribución de materia respecto de dicho eje. 

# Ecuación de Momentos.

Nos proponemos ahora obtener ecuaciones que nos relacionen los cambios en el estado de movimiento de un sistema rígido, con las fuerzas de interacción a la que se encuentra sometido. 

Una de las ecuaciones de referencia es sin lugar a dudas aquella que nos relaciona el vector aceleración del centro de masa de un sistema con la resultante de las fuerzas de interacción a que se encuentra sometido como si estuviera aplicada en dicho punto y como si la totalidad de la masa estuviera concentrada en él. 

$$
\vec {\mathrm {F}} = \mathrm {m} \vec {\mathrm {a}} _ {\mathrm {c}}
$$

Ecuación vectorial que una vez evaluada en componentes nos proporcionará en general, tres ecuaciones escalares, indudablemente insuficientes para describir el comportamiento de un sistema rígido si tenemos en cuenta que en general dicho sistema será un sistema con seis grados de libertad, pero que sin lugar a dudas será de utilidad en el tratamiento de nuestros problemas y que en términos del vector cantidad de movimiento podemos expresar: 

$$
\vec {\mathrm {F}} = \left. \frac {\mathrm {d} \vec {\mathrm {P}}}{\mathrm {d t}} \right| _ {\text {X Y Z}}
$$

donde 

$$
\vec {\mathrm {P}} = \mathrm {m} \vec {\mathrm {v}} _ {\mathrm {c}}
$$

Teniendo en cuenta que frecuentemente las magnitudes involucradas en el tratamiento de nuestros problemas y en particular el vector cantidad de movimiento, estarán evaluadas en componentes según las direcciones (xyz) de un sistema solidario al cuerpo con origen en el centro de masa, la anterior puede en ese caso emplearse en la forma: 

$$
\vec {\mathrm {F}} = \left. \frac {\mathrm {d} \vec {\mathrm {P}}}{\mathrm {d t}} \right| _ {\text {X Y Z}} + \vec {\mathrm {w}} \times \vec {\mathrm {P}}
$$

Con el propósito de obtener una segunda ecuación de movimiento que nos relacione los cambios en el estado de movimiento de un cuerpo con las fuerzas de interacción tengamos en cuenta que atendiendo las conclusiones obtenidas en el capítulo anterior, el vector momento angular de un sistema calculado respecto de un punto arbitrario (A) estaba relacionado con el momento que, respecto de dicho punto, generaban las fuerzas externas, mediante: 

$$
\vec {\mathrm {M}} _ {\mathrm {A}} = \frac {\mathrm {d} \vec {\mathrm {L}} _ {\mathrm {A}}}{\mathrm {d t}} \Bigg | _ {\mathrm {X Y Z}} + \vec {\mathrm {v}} _ {\mathrm {A}} \times \mathrm {m} \vec {\mathrm {v}} _ {\mathrm {c}}
$$

Donde recordemos que el sistema de referencia (XYZ) desde el que se determinan las variaciones temporales deberá ser un sistema inercial y de donde resulta que si los momentos se calculan respecto del centro de masa (en cuyo caso el segundo término de la derecha incluye el producto de vectores paralelos) o respecto de un punto fijo al mencionado sistema inercial (en cuyo caso se anula la velocidad del punto A, incluida en el segundo término) nos quedan las formas mas sencilla, que se indican a continuación: 

$$
\vec {\mathrm {M}} _ {\mathrm {c}} = \frac {\mathrm {d} \vec {\mathrm {L}} _ {\mathrm {c}}}{\mathrm {d t}} \Bigg | _ {\mathrm {X Y Z}}
$$

$$
\vec {\mathrm {M}} _ {\mathrm {Q}} = \frac {\mathrm {d} \vec {\mathrm {L}} _ {\mathrm {Q}}}{\mathrm {d t}} \Bigg | _ {\mathrm {X Y Z}}
$$

Teniendo en cuenta que en general el vector momento angular estará evaluado según las direcciones de un sistema (xyz) solidario al cuerpo con origen en el centro de masa o en un punto fijo, según convenga a la situación en consideración, las anteriores pueden expresarse como: 

$$
\vec {\mathrm {M}} _ {\mathrm {c}} = \frac {\mathrm {d} \vec {\mathrm {L}} _ {\mathrm {c}}}{\mathrm {d t}} \Bigg | _ {\mathrm {x y z}} + \vec {\mathrm {w}} \times \vec {\mathrm {L}} _ {\mathrm {c}}
$$

$$
\vec {\mathrm {M}} _ {\mathrm {Q}} = \frac {\mathrm {d} \vec {\mathrm {L}} _ {\mathrm {Q}}}{\mathrm {d t}} \Bigg | _ {\mathrm {x y z}} + \vec {\mathrm {w}} \times \vec {\mathrm {L}} _ {\mathrm {Q}}
$$

Considerando ahora el caso de un sistema rígido animado de un movimiento plano, tal que el plano del movimiento es paralelo a un plano de simetría, y teniendo en cuenta en las anteriores las expresiones obtenidas para el vector momento angular calculado respecto de cada uno de los puntos en consideración, resulta: 

$$
\vec {\mathrm {M}} _ {\mathrm {c}} = \mathrm {I} _ {\mathrm {c}} \frac {\mathrm {d} \vec {\mathrm {w}}}{\mathrm {d t}} \Bigg | _ {\mathrm {x y z}} + \vec {\mathrm {w}} \times \mathrm {I} _ {\mathrm {c}} \vec {\mathrm {w}} \quad \vec {\mathrm {M}} _ {\mathrm {Q}} = \mathrm {I} _ {\mathrm {Q}} \frac {\mathrm {d} \vec {\mathrm {w}}}{\mathrm {d t}} \Bigg | _ {\mathrm {x y z}} + \vec {\mathrm {w}} \times \mathrm {I} _ {\mathrm {Q}} \vec {\mathrm {w}}
$$

Puesto que los momentos de inercia son invariantes temporales y que en ambos casos los segundos términos son nulos por tratarse del producto de vectores paralelos, de las anteriores obtenemos: 

$$
\vec {\mathrm {M}} _ {\mathrm {c}} = \mathrm {I} _ {\mathrm {c}} \dot {\vec {\mathrm {w}}}
$$

$$
\vec {\mathrm {M}} _ {\mathrm {Q}} = \mathrm {I} _ {\mathrm {Q}} \dot {\vec {\mathrm {w}}}
$$

Que en adelante indicaremos como: 

$$
\vec {\mathrm {M}} _ {\mathrm {c}} = \mathrm {I} _ {\mathrm {c}} \vec {\alpha}
$$

$$
\vec {\mathrm {M}} _ {\mathrm {Q}} = \mathrm {I} _ {\mathrm {Q}} \vec {\alpha}
$$

Expresiones que nos relacionan los cambios temporales observados, desde el sistema inercial, en el estado de rotación de un cuerpo, caracterizados por su vector aceleración angular (α), con los momentos que las fuerzas externas generan respecto del punto (C o Q) en consideración. 

Con respecto a lo mencionado anteriormente resulta interesante destacar que las variaciones temporales observadas en el estado de rotación de un cuerpo, desde el sistema inercial o desde el sistema solidario, son en realidad coincidentes, puesto que: 

$$
\left. \frac {\mathrm {d} \vec {\mathrm {w}}}{\mathrm {d t}} \right| _ {\text {X Y Z}} = \left. \frac {\mathrm {d} \vec {\mathrm {w}}}{\mathrm {d t}} \right| _ {\text {x y z}} + \vec {\mathrm {w}} \times \vec {\mathrm {w}} \quad \left. \frac {\mathrm {d} \vec {\mathrm {w}}}{\mathrm {d t}} \right| _ {\text {X Y Z}} = \left. \frac {\mathrm {d} \vec {\mathrm {w}}}{\mathrm {d t}} \right| _ {\text {x y z}}
$$

Finalmente teniendo en cuenta las conclusiones obtenidas y las alcanzadas en el capítulo anterior, resulta que el momento generado por las fuerzas externas respecto de un punto cualquiera estará relacionado con los cambios temporales observados en el estado de rotación de un cuerpo mediante: 

$$
\vec {\mathrm {M}} _ {\mathrm {A}} = \vec {\mathrm {r}} _ {\mathrm {c / A}} \times \vec {\mathrm {m a}} _ {\mathrm {c}} + \mathrm {I} _ {\mathrm {c}} \vec {\alpha}
$$

Que indudablemente podemos expresar como: 

$$
\vec {\mathrm {M}} _ {\mathrm {A}} = \vec {\mathrm {r}} _ {\mathrm {c / A}} \times \vec {\mathrm {F}} + \mathrm {I} _ {\mathrm {c}} \vec {\alpha}
$$
