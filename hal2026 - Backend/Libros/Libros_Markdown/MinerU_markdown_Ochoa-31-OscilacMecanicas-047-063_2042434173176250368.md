Mecánica Clásica 

Volumen II 

Ochoa 

- 2008 - 

Oscilaciones Mecánicas 

ISBN de la Versión Analógica 

987-95038-0-5 

# 3.01 OSCILACIONES LIBRES.

A lo largo de este capítulo consideraremos las oscilaciones de sistemas mecánicos con un grado de libertad, lo que nos brindará la oportunidad de trabajar un método destinado a la resolución de ecuaciones diferenciales que con mucha frecuencia resultan del planteo de situaciones físicas concretas. Sistemas con dos grados de libertad serán tratados al finalizar este capítulo. 

Como una alternativa adecuada para iniciar con el tratamiento del tema, consideremos el caso de un muelle lineal que interactúa con un cuerpo como se muestra en la figura de la izquierda, y supongamos que mediante una interacción externa apartamos al sistema de su posición de equilibrio sometiendo el muelle a una deformación inicial, como la sugerida en la figura de la derecha, para luego dejarlo en libertad de desplazarse a lo largo de la superficie horizontal, libre de rozamiento. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/76cd27517ac384dfa0023ce0ddc22f6f5c706e2d8453a9f53481b3f205f31e8e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/90ebdf39efce2bc3a6976b749f2a5fab13acd67db6df2f529f01420eb004e7a5.jpg)


Bajo estas condiciones las fuerzas a que se verá sometido el cuerpo al dejarlo en libertad, serán las indicadas en el diagrama siguiente, que resultan de su interacción con el campo gravitatorio terrestre, con el muelle y con la superficie horizontal, que recordemos, hemos supuesto libre de rozamiento. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/e140df9f5e0f4e4a784ae3ac02d7ea126a1877ef7d6537de250d628450886b01.jpg)


Con lo que la ecuación de Newton para el centro de masa del cuerpo nos queda:  

$$
\vec {\mathrm {F}} + \vec {\mathrm {N}} + \mathrm {m} \vec {\mathrm {g}} = \mathrm {m} \vec {\mathrm {a}}
$$

Con el propósito de evaluar las componentes de esta ecuación pensaremos en un sistema de ejes cartesianos como el indicado en la segunda de las figuras anteriores, donde suponemos al origen de dicho sistema coincidente con la posición en la que el centro de masa del cuerpo está en equilibrio, que en este caso es coincidente con aquella en la que el resorte está sin deformar, con lo que, la deformación del resorte coincidirá en todo momento con la coordenada horizontal del centro de masa del cuerpo, y por lo tanto, la fuerza a la que se verá sometido el cuerpo como resultado de su interacción con el muelle, puede relacionarse vectorialmente con dicha coordenada mediante: 

$$
\vec {\mathrm {F}} = - \mathrm {k} \mathrm {x} \vec {\mathrm {i}}
$$

Que nos muestra una interesante semejanza con las fuerzas que resultan de una interacción elástica, siendo éste el motivo por el que, en adelante, a la constante del muelle la reconoceremos como constante elástica. Sin embargo debe observarse que existe una diferencia entre estas dos fuerzas, mientras la primera siempre es de naturaleza atractiva, la que resulta de la interacción con el muelle será atractiva cuando la coordenada sea positiva o sea cuando el muelle está elongado y tendrá sentido opuesto cuando el muelle está comprimido, esto es cuando la coordenada horizontal es negativa. 

Teniendo en cuenta los aspectos mencionados es claro que al evaluar la componente horizontal de la ecuación de Newton, obtenemos la ecuación: 

$$
- k x = m \ddot {x}
$$

De donde: 

$$
\ddot {\mathrm {x}} (t) + \frac {\mathrm {k}}{\mathrm {m}} \mathrm {x} (t) = 0 \tag {3.1}
$$

Resultando así una ecuación que identificaremos como una ecuación diferencial, en cuanto a que en la misma intervienen la función (en este caso la coordenada horizontal) y sus derivadas (en esta oportunidad, su derivada temporal segunda). 

Nuestro problema ahora consiste en encontrar una expresión funcional para la coordenada horizontal tal que empleada en la anterior, dicha función y su derivada temporal segunda, se satisfaga la igualdad prevista, en cuyo caso diremos que la expresión encontrada es una solución de la ecuación diferencial planteada, que recordemos resultó al evaluar en componentes cartesianas la ecuación de Newton para el movimiento del centro de masa del cuerpo, y por lo tanto es claro que la mencionada solución nos permitirá describir las características del movimiento de dicho punto según la dirección horizontal. 

# Solución General.

A los efectos de obtener una solución general del problema planteado, esto es una función que nos permita describir en forma completa las características del movimiento del centro de masa del cuerpo una vez que lo dejamos en libertad, que por lo tanto deberá ser solución de la ecuación diferencial (3.1) y con el propósito de darle mas generalidad al tema, supondremos que al dejar el cuerpo en libertad lo hacemos de manera que tanto la posición como la velocidad de su centro de masa no son nulas y con miras a simplificar el manejo algebraico futuro definiremos la magnitud: 

$$
w ^ {2} = \frac {k}{m}
$$

En términos de la cual nuestra ecuación diferencial original nos queda: 

$$
\ddot {\mathbf {x}} + \mathbf {w} ^ {2} \mathbf {x} = 0
$$

Como solución de ésta ecuación diferencial propondremos una función del tipo exponencial. 

$$
\mathrm {x (t) = C e ^ {q t}}
$$

Donde (C y q) son constantes que deberemos determinar a los efectos de que la función propuesta sea efectivamente solución de nuestra ecuación diferencial. 

Con este propósito reemplazaremos la función y su derivada segunda en dicha ecuación, con lo que obtenemos que las constantes involucradas deberán ser tales que: 

$$
\mathrm {q} ^ {2} + \mathrm {w} ^ {2} = 0
$$

Por lo tanto, la función exponencial propuesta será solución de nuestra ecuación diferencial cualquiera sea el valor de la constante (C), con la condición de que la constante (q) sea solución de la ecuación algebraica anterior, y que por lo tanto tome alguno de los valores que se indican a continuación: 

$$
\mathbf {q} = \pm \sqrt {- \mathbf {w} ^ {2}}
$$

Que en términos de la unidad imaginaría podemos expresar como: 

$$
\mathbf {q} = \pm \mathrm {i} \mathbf {w}
$$

Teniendo en cuenta las conclusiones obtenidas, resulta que las funciones: 

$$
\mathbf {x} (t) = \mathrm {C} _ {1} \mathrm {e} ^ {\mathrm {i w t}} \qquad \qquad \mathbf {x} (t) = \mathrm {C} _ {2} \mathrm {e} ^ {- \mathrm {i w t}}
$$

Serán soluciones de nuestra ecuación diferencial, a las que en adelante identificaremos como soluciones particulares en cuanto a que como veremos a lo largo del tema, cada una de ellas permitirá describir situaciones asociadas con condiciones iniciales diferentes, pudiendo demostrarse por simple sustitución, que una combinación lineal de las mismas también será solución de nuestra ecuación diferencial, la que nos permitirá describir el comportamiento mas general posible del sistema, motivo por lo que en adelante reconoceremos a esta como la solución general de nuestra ecuación diferencial. 

$$
\mathrm {x (t)} = \mathrm {C} _ {1} \mathrm {e} ^ {\mathrm {i w t}} + \mathrm {C} _ {2} \mathrm {e} ^ {- \mathrm {i w t}}
$$

Donde $\left( \mathbf { C } _ { 1 } \mathbf { y } \mathbf { C } _ { 2 } \right)$ son constantes que deberemos determinar y que como veremos estarán directamente relacionadas con las condiciones iniciales de nuestro problema. 

Con el propósito de darle otra forma a la función indicada anteriormente, veremos de expresarla en término de funciones trigonométricas, teniendo en cuenta que en general y de acuerdo con la relación de Euler, las exponenciales pueden relacionarse con dichas funciones mediante: 

$$
e ^ {i \theta} = \cos \theta + i s e n \theta
$$

Con lo que la solución general de nuestra ecuación diferencial puede expresarse en término de funciones trigonométricas, como: 

$$
\mathrm {x} (t) = \left(\mathrm {C} _ {1} + \mathrm {C} _ {2}\right) \cos (\mathrm {w t}) + \mathrm {i} \left(\mathrm {C} _ {1} - \mathrm {C} _ {2}\right) \operatorname {s e n} (\mathrm {w t})
$$

Que en término de las nuevas constantes: 

$$
\mathrm {A} _ {1} = \left(\mathrm {C} _ {1} + \mathrm {C} _ {2}\right) \mathrm {y A} _ {2} = \mathrm {i} \left(\mathrm {C} _ {1} - \mathrm {C} _ {2}\right)
$$

Puede expresarse como: 

$$
\mathrm {x (t) = A _ {1} \cos (w t) + A _ {2} s e n (w t)}
$$

Que recordemos nos proporciona una expresión en función del tiempo, para la posición del centro de masa del cuerpo en término de dos nuevas constantes, que como veremos dependerán de las condiciones iniciales asociadas con la posición y velocidad del centro de masa en el instante en que dejamos al sistema en libertad, sometido a la interacción elástica. 

Derivando temporalmente la anterior es claro que estamos en condiciones de obtener expresiones generales para la velocidad y aceleración del centro de masa del cuerpo en función del tiempo y en término de las constantes mencionadas en el párrafo anterior, resultando: 

$$
\begin{array}{l} \dot {\mathrm {x}} (t) = - \mathrm {A} _ {1} \mathrm {w} \operatorname {s e n} (\mathrm {w t}) + \mathrm {A} _ {2} \mathrm {w} \cos (\mathrm {w t}) \\ \ddot {\mathbf {x}} (t) = - \left[ \mathrm {A} _ {1} \mathrm {w} ^ {2} \cos (\mathrm {w t}) + \mathrm {A} _ {2} \mathrm {w} ^ {2} \sin (\mathrm {w t}) \right] \\ \end{array}
$$

Como ya lo mencionáramos en varias oportunidades, las características del movimiento de un cuerpo dependerán de las interacciones a que está sometido así como de las condiciones iniciales correspondientes a la situación planteada. En la solución obtenida no queda lugar a dudas que las interacciones están presentes, a través de la masa involucrada y de la constante elástica del muelle incluidas en (w), en cuanto a las condiciones iniciales, veremos que de estas dependerán las constantes $\left( \mathbf { A } _ { 1 } \thinspace \mathbf { y } \thinspace \mathbf { A } _ { 2 } \right)$ incluidas en nuestra solución y que en adelante reconoceremos como Constantes de Integración. 

Con el propósito de obtener expresiones para dichas constantes, en término de las condiciones iniciales, observemos que la solución lograda para nuestra ecuación diferencial deberá ser capaz de describir el comportamiento del sistema en cualquier instante, en particular, en el instante inicial. Requiriendo que las funciones anteriores satisfagan esta condición, esto es que en: 

$$
t = 0 \quad \mathbf {x} = \mathbf {x} _ {\circ} \quad \dot {\mathbf {x}} = \dot {\mathbf {x}} _ {\circ}
$$

Resulta que las constantes involucradas en la solución, deberán ser tales que: 

$$
\mathbf {A} _ {1} = \mathbf {x} _ {\circ} \quad \mathbf {y} \quad \mathbf {A} _ {2} = \frac {\dot {\mathbf {x}} _ {\circ}}{\mathbf {w}}
$$

Con lo que la solución general de nuestro problema, en función del tiempo y en término de las condiciones iniciales, nos queda: 

$$
\begin{array}{l} \mathrm {x} (t) = \mathrm {x} _ {\circ} \cos (\mathrm {w t}) + \frac {\dot {\mathrm {x}} _ {\circ}}{\mathrm {w}} \operatorname {s e n} (\mathrm {w t}) \\ \dot {\mathrm {x}} (t) = - \mathrm {x} _ {\circ} \mathrm {w} \operatorname {s e n} (\mathrm {w t}) + \dot {\mathrm {x}} _ {\circ} \cos (\mathrm {w t}) \\ \ddot {\mathbf {x}} (t) = - \left\lfloor \mathbf {x} _ {\circ} \mathbf {w} ^ {2} \cos (\mathbf {w t}) + \dot {\mathbf {x}} _ {\circ} \mathbf {w} \operatorname {s e n} (\mathbf {w t}) \right\rfloor \\ \end{array}
$$

# Situaciones Particulares.

Consideraremos a continuación la situación particular que resulta de suponer que al sistema se lo deja en libertad con el resorte deformado y el cuerpo en reposo, en cuyo caso de las anteriores obtenemos: 

$$
\begin{array}{l} \mathrm {x} (t) = \mathrm {x} _ {\circ} \cos (\mathrm {w t}) \\ \dot {\mathbf {x}} (t) = - \mathbf {x} _ {\circ} \mathbf {w} \operatorname {s e n} (\mathbf {w t}) \\ \ddot {\mathrm {x}} (t) = - \mathrm {x} _ {\circ} \mathrm {w} ^ {2} \cos (\mathrm {w t}) \\ \end{array}
$$

Que claramente corresponde a un movimiento oscilatorio con una amplitud constante, determinada por la posición del cuerpo en el instante inicial, (coincidente con la deformación del resorte en dicho instante) y con un período dado por: 

$$
T = \frac {2 \pi}{w} \quad \therefore T = 2 \pi \sqrt {\frac {m}{k}}
$$

Con gráficas temporales para las funciones indicadas como las que se muestran a continuación: 


x(t)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/f00b24e83bb55661b2f575b51bcfe63ac8d6d9fff345919c76c3c3e5fb41e2f9.jpg)



x (t)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/7ec0235c8acb2802bf7ab71ae9ecd087abdd06a2a1b53782b44bff108671474a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/185a0751a47f5002b5796242e06ff366f1dd007c9f7b18a8a1da5c330b7873ed.jpg)


Otra situación particular de interés es aquella que resulta de dar al cuerpo una velocidad inicial cuando se encuentra en reposo y en su posición de equilibrio, (con el muelle sin deformar) resultando entonces las siguientes expresiones para la posición, velocidad y aceleración del centro de masa del cuerpo: 

$$
x (t) = \frac {\dot {x} _ {o}}{w} s e n (w t)
$$

$$
\dot {\mathbf {x}} (t) = \dot {\mathbf {x}} _ {\circ} \cos (\mathrm {w t})
$$

$$
\ddot {\mathrm {x}} (t) = - \dot {\mathrm {x}} _ {\circ} \mathrm {w} \operatorname {s e n} (\mathrm {w t})
$$

Que nuevamente corresponde a un movimiento periódico con un período coincidente con el obtenido en el caso anterior y con una amplitud claramente dependiente de la velocidad inicial y de los parámetros que caracterizan el sistema, esto es, de la constante elástica y de la masa del cuerpo considerado, y cuyas gráficas cualitativas en función del tiempo se muestran a continuación, donde hemos supuesto que la velocidad inicial tiene el sentido en que crece la coordenada involucrada. 


x(t)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/cd576ae6feab3933937b18b5a825f29acf9313ab71db70c57c8f6d2bed7f3f43.jpg)



x (t)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/d812be1ccf344b1a3bbd3ef72c5da7314fbc9b9c9c894456f3c5532fae30b3d1.jpg)



x(t)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/3251636d5ed1458a2de94b87db068ca263039001bffedda5df07a7381c1a9674.jpg)


# Otra Forma de Expresar la Solución General.

Teniendo en cuenta la relación que vincula el seno de la suma de dos ángulos con los senos y cosenos de dichas magnitudes puede obtenerse una forma muy conveniente para la solución general de nuestro problema, en términos de dos nuevas constantes, dependientes claro está, de las condiciones iniciales involucradas, resultando: 

$$
\mathrm {x} (t) = \mathrm {A s e n} (\mathrm {w t} + \delta)
$$

En cuyo caso las nuevas constantes nos quedan relacionadas con las anteriores y por lo tanto con las condiciones iniciales, a través de las expresiones que se indican a continuación: 

$$
\mathrm {A} ^ {2} = \mathrm {A} _ {1} ^ {2} + \mathrm {A} _ {2} ^ {2} \quad \therefore \quad \mathrm {A} ^ {2} = \mathrm {x} _ {\circ} ^ {2} + \left(\frac {\dot {\mathrm {x}} _ {\circ}}{\mathrm {w}}\right) ^ {2}
$$

$$
\mathrm {t g} (\delta) = \frac {\mathrm {A} _ {1}}{\mathrm {A} _ {2}} \quad \therefore \quad \mathrm {t g} (\delta) = \frac {\mathrm {X} _ {\circ} \mathrm {W}}{\dot {\mathrm {X}} _ {\circ}}
$$

Siendo oportuno mencionar que esta forma de expresar la solución puede resultar ventajosa respecto de la anterior en aquellas situaciones en las que, a diferencia de las consideradas en los casos particulares anteriores, ninguna de las condiciones iniciales es nula. 

# Laboratorio Virtual.

# Oscilaciones Libres.

Ejecutando el archivo Libres.htm incluido en la carpeta del mismo nombre, podrá acceder a una simulación destinada a ilustrar diferentes aspectos tratados a lo largo del tema considerado, donde, para diferentes condiciones iniciales podrá observar gráficas de la posición en función del tiempo y de la velocidad en función de la posición del cuerpo. 

# Figuras de Lissajous.

Ejecutando el archivo Lissajous.htm incluido en la carpeta del mismo nombre, podrá acceder a una simulación, cuya teoría se recomienda consultar, destinada a ilustrar el movimiento que resulta como consecuencia de la superposición de dos movimientos armónicos simples con frecuencias angulares o fases iniciales diferentes. 

# 3.02 OSCILACIONES AMORTIGUADAS.

Consideraremos a continuación el caso de un cuerpo sometido a una fuerza elástica, resultante de su interacción con un muelle y a una fuerza del tipo viscosa, directamente proporcional a su velocidad, como consecuencia de su interacción con algún mecanismo que la proporciona, como el sugerido en la figura, siendo ésta un diagrama muy simplificado de lo que podría ser el sistema de amortiguación de un automóvil. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/9e00a64c94855aae0e85c734efd293d9308c646915534d33fcd7bec75e4ff9e0.jpg)


Suponiendo que el sistema se aparta de su posición de equilibrio y se lo deja en libertad, se verá sometido a un conjunto de fuerzas externas como las indicadas en la figura siguiente, que resultan de la interacción con el muelle, con la superficie horizontal, a la que suponemos libre de rozamiento, con el amortiguador y con el campo gravitatorio, con lo que la ecuación de Newton para el centro de masa del cuerpo nos queda: 

$$
\vec {\mathrm {F}} _ {\mathrm {v}} + \vec {\mathrm {F}} _ {\mathrm {e}} + \vec {\mathrm {N}} + \mathrm {m} \vec {\mathrm {g}} = \mathrm {m} \vec {\mathrm {a}}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/c9f712173ac25b1a9c2355dc7fc9410efa834c8e171395aead730a0c3c043439.jpg)


Evaluando las componentes según las direcciones de un sistema cartesiano como el considerado en el tema anterior, la fuerza viscosa y la fuerza elástica a la que se verá sometido el cuerpo podrán ser expresadas como: 

$$
\vec {\mathrm {F}} _ {\mathrm {v}} = - \mathbf {k} _ {\mathrm {v}} \dot {\mathbf {x}} \vec {\mathrm {i}} \qquad \vec {\mathrm {F}} _ {\mathrm {e}} = - \mathbf {k} _ {\mathrm {e}} \mathbf {x} \vec {\mathrm {i}}
$$

Con lo que de la componente horizontal de la ecuación de Newton para el centro de masa del cuerpo, obtenemos la siguiente ecuación diferencial. 

$$
- \mathrm {k} _ {\mathrm {v}} \dot {\mathrm {x}} - \mathrm {k} _ {\mathrm {e}} \mathrm {x} = \mathrm {m} \ddot {\mathrm {x}}
$$

Dividiendo por la masa en ambos miembros y definiendo la constante de amortiguación como: 

$$
\lambda = \frac {\mathrm {k} _ {\mathrm {v}}}{2 \mathrm {m}}
$$

Y la frecuencia natural del sistema, como la frecuencia con la que oscilaría dicho sistema en ausencia de la fuerza viscosa: 

$$
\mathrm {w} _ {\circ} ^ {2} = \frac {\mathrm {k} _ {\mathrm {e}}}{\mathrm {m}}
$$

La ecuación diferencial nos queda expresada como: 

$$
\ddot {x} + 2 \lambda \dot {x} + w _ {\circ} ^ {2} x = 0
$$

Proponiendo nuevamente una solución del tipo exponencial: 

$$
\mathbf {x} (t) = \mathrm {C e} ^ {\mathrm {q t}}
$$

Y reemplazando la función propuesta y sus derivadas temporales en la ecuación diferencial, resulta que la constante (C) podrá tomar cualquier valor siempre que la constante (q) sea una solución de la ecuación algebraica. 

$$
\mathrm {q} ^ {2} + 2 \lambda \mathrm {q} + \mathrm {w} _ {\circ} ^ {2} = 0
$$

De donde resulta que los valores posibles para la mencionada constante serán: 

$$
\mathbf {q} = - \lambda \pm \sqrt {\lambda^ {2} - \mathbf {w} _ {\circ} ^ {2}}
$$

Por lo tanto, la solución general de nuestra ecuación diferencial vendrá expresada como una combinación lineal de las soluciones particulares, que se obtienen al considerar cada una de las raíces resultantes de la expresión anterior, con lo que las características del movimiento dependerán fuertemente de la relación que exista entre las constantes que caracterizan el sistema, resultando así las situaciones particulares que se detallan a continuación. 

# Movimiento Oscilatorio Amortiguado.

Resulta de suponer un cierto predominio de la fuerza elástica sobre la fuerza disipativa y corresponde al caso en el que la constante de amortiguación es inferior a la frecuencia natural del sistema, o sea cuando: 

$$
\lambda <   \mathrm {w} _ {\circ} \quad \therefore \quad \mathrm {k} _ {\mathrm {v}} <   2 \sqrt {\mathrm {m k} _ {\mathrm {e}}}
$$

Con lo que, las raíces de la ecuación cuadrática pueden expresarse como: 

$$
\mathrm {q} = - \lambda \pm \mathrm {i} \sqrt {\mathrm {w} _ {\circ} ^ {2} - \lambda^ {2}}
$$

Que en términos de una nueva constante podemos indicar como: 

$$
\mathrm {q} = - \lambda \pm \mathrm {i} \Omega
$$

Donde: 

$$
\Omega = \sqrt {\mathrm {w} _ {\circ} ^ {2} - \lambda^ {2}}
$$

Con lo que la solución general de nuestra ecuación diferencial, para la situación en consideración, nos queda expresada como: 

$$
\mathrm {x (t) = e ^ {- \lambda t} \left[ C _ {1} e ^ {i \Omega t} + C _ {2} e ^ {- i \Omega t} \right]}
$$

Comparando la función encerrada entre corchetes con la solución general que obtuviéramos en el caso oscilatorio tratado anteriormente, es claro que operando de la misma manera con dicha función, la solución de nuestra ecuación diferencial actual, puede expresarse en término de dos nuevas constantes dependientes de las condiciones iniciales, como: 

$$
\mathrm {x (t) = A e ^ {- \lambda t} s e n (\Omega t + \delta)}
$$

Resultando así un movimiento oscilatorio, con una frecuencia menor que la natural del sistema y con una amplitud que decae exponencialmente con el tiempo como se muestra cualitativamente en la figura siguiente, que en adelante reconoceremos como movimiento oscilatorio amortiguado, cuyo período vendrá dado por: 

$$
\mathrm {T} = \frac {2 \pi}{\sqrt {\mathrm {w} _ {\circ} ^ {2} - \lambda^ {2}}}
$$

Obviamente mayor que el correspondiente al caso libre de amortiguamiento considerado en el tema anterior, siendo oportuno observar que la solución obtenida en dicha oportunidad es en realidad un caso particular de la lograda recientemente. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/b82aac25d1f34fb000bf8b3d66ec9bee3c7501c1e98b6a7f8355f5e1966ae808.jpg)


# Movimiento Sobre Amortiguado.

Corresponde al caso en que predomina el amortiguamiento sobre la fuerza de restauración elástica, o sea cuando: 

$$
\lambda > \mathrm {w} _ {\circ} \quad \therefore \quad \mathrm {k} _ {\mathrm {v}} > 2 \sqrt {\mathrm {m k} _ {\mathrm {e}}}
$$

En cuyo caso, las raíces de la ecuación cuadrática resultaran reales, distintas y ambas negativas, como lo podemos observar al expresarlas según se indica a continuación: 

$$
\mathbf {q} _ {1} = - \left(\lambda + \sqrt {\lambda^ {2} - \mathbf {w} _ {\circ} ^ {2}}\right) \quad \mathbf {y} \quad \mathbf {q} _ {2} = - \left(\lambda - \sqrt {\lambda^ {2} - \mathbf {w} _ {\circ} ^ {2}}\right)
$$

Con lo que la solución general quedará expresada como: 

$$
\mathbf {x} (t) = \mathrm {C} _ {1} \mathrm {e} ^ {\mathrm {q} _ {1} t} + \mathrm {C} _ {2} \mathrm {e} ^ {\mathrm {q} _ {2} t}
$$

Teniendo en cuenta que los exponentes son ambos negativos, resulta entonces un movimiento no oscilatorio y fuertemente amortiguado como se sugiere en la figura lateral, donde hemos supuesto que en el instante inicial el cuerpo se deja en libertad con una velocidad tal que durante un pequeño intervalo de tiempo genera un incremento en la deformación del muelle. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/af78195433195a340c46d9217a2f93d36d874b15e22314395d352f70b98ac4b3.jpg)


# Movimiento con Amortiguación Crítica.

Corresponde a la situación que resta por tratar, o sea cuando: 

$$
\lambda = \mathrm {w} _ {\circ} \quad \therefore \quad \mathrm {k} _ {\mathrm {v}} = 2 \sqrt {\mathrm {m k} _ {\mathrm {e}}}
$$

En cuyo caso las raíces de la ecuación cuadrática son reales e iguales: 

$$
\mathbf {q} _ {1} = \mathbf {q} _ {2} = - \lambda
$$

Situación en la que puede verificarse por simple sustitución, que otra solución particular de nuestra ecuación diferencial viene dada por: 

$$
\mathbf {x} (t) = \mathrm {C t e} ^ {- \lambda t}
$$

Con lo que la solución general puede expresarse como: 

$$
\mathrm {x} (t) = \mathrm {C} _ {1} \mathrm {e} ^ {- \lambda t} + \mathrm {C} _ {2} \mathrm {t e x i s t m a t h {\lambda}}
$$

Resultando para las situaciones consideradas, gráficas temporales cualitativas como las que se muestran en la figura que siguiente. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/01aca6710e5a1a9fcb473f92afd64b8db2b2b5fe8af4a2f7b68e9d031560147d.jpg)


# Oscilaciones Libres en un Sistema No Inercial.

A continuación consideraremos una interesante aplicación destinada a ejercitar el manejo cualitativo y formal de la ecuación de movimiento en un sistema de referencia no inercial, en rotación respecto de un sistema inercial fijo a tierra, supuestamente inercial. 

Con este propósito, consideremos la situación sugerida en la figura siguiente, donde se muestra una corredera que puede deslizar libre de rozamiento a lo largo de una guía labrada diametralmente en una plataforma contenida en un plano horizontal, que rota con una velocidad angular constante respecto de un sistema fijo a tierra al que como ya lo mencionamos lo supondremos inercial. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/bd760a4080dd391a2e89689d69c25587063978d7999fefab63ff82bd80a5666e.jpg)


Nos proponemos estudiar las características del movimiento de la corredera respecto de la plataforma, suponiendo que dicha corredera está sometida a una fuerza elástica como consecuencia de su interacción con un resorte, cuya longitud propia es coincidente con el radio de la plataforma, y que el sistema se deja en libertad en una posición tal que, el resorte cuenta con una deformación inicial y una velocidad nula respecto de la plataforma. 

Teniendo en cuenta que hemos supuesto a la tierra como un sistema inercial, es claro que un sistema de referencia fijo a la plataforma será un sistema no inercial, y por lo tanto en dicho sistema la corredera se verá sometida a las fuerzas que resultan de la interacción elástica con el resorte y las que resultan de la interacción por contacto con la plataforma, además de las fuerzas inerciales, centrífuga y de Coriolis, como se sugiere en la figura siguiente: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/a4adef4430f0d02b687cdb76fadeb786632be9f1d29f8dbb3c098e40df1500cb.jpg)


Fuerzas de Interacción 

FeN , 

Fuerzas Inerciales 

$$
\vec {\mathrm {f}} _ {\mathrm {c f}} = - \mathrm {m} \vec {\mathrm {w}} \times \vec {\mathrm {w}} \times \vec {\mathrm {r}}
$$

$$
\vec {\mathrm {f}} _ {\mathrm {c r}} = - 2 \mathrm {m} \vec {\mathrm {w}} \times \vec {\mathrm {v}} _ {\mathrm {x y z}}
$$

# Tratamiento Cualitativo.

Designando con $\left( \mathrm { W _ { 0 } } \right)$ a la frecuencia con que oscilaría el sistema si la plataforma estuviera en reposo, que hemos identificáramos como frecuencia natural del sistema y evaluando la fuerza elástica y la fuerza inercial centrífuga, según las direcciones (xyz) del sistema solidario a la plataforma, indicado en la primer figura, sus módulos quedan expresados por: 

$$
\mathrm {F _ {e}} = \mathrm {k x} \quad \therefore \quad \mathrm {F _ {e}} = \mathrm {m w} _ {\circ} ^ {2} \mathrm {x}
$$

$$
\mathbf {f} _ {\mathrm {c f}} = \mathbf {m w} ^ {2} \mathbf {x}
$$

Comparando las anteriores y teniendo en cuenta el sentido de cada una de dichas magnitudes, es claro que según la relación entre (w) y la frecuencia natural del sistema, podemos esperar las siguientes situaciones: 

# Cuando:

$$
\mathrm {w} <   \mathrm {w} _ {\circ}
$$

Predomina la fuerza elástica cualquiera que sea el valor de la coordenada y por lo tanto, respecto de la plataforma, debemos esperar un movimiento oscilatorio, con una frecuencia diferente a la frecuencia natural del sistema. 

# Cuando:

$$
\mathbf {w} = \mathbf {w} _ {\circ}
$$

La fuerza elástica estará equilibrada por la fuerza inercial centrífuga para todo valor de la coordenada, por lo tanto es de esperar que la corredera permanezca en equilibrio respecto de la plataforma, cualquiera que sea el valor que tome su coordenada. 

# Cuando:

$$
\mathbf {W} > \mathbf {W} _ {\circ}
$$

La fuerza inercial centrífuga predominará sobre la fuerza elástica, por lo tanto respecto de la plataforma debemos esperar que la coordenada crezca indefinidamente. 

# Tratamiento Formal.

Considerando un sistema solidario a la plataforma con origen en el centro de la misma, como se muestra en figura inicial, y planteando la ecuación de movimiento para un observador en dicho sistema, resulta: 

$$
\vec {\mathrm {F}} _ {\mathrm {e}} + \vec {\mathrm {N}} = \mathrm {m} \vec {\mathrm {a}} _ {\mathrm {x y z}} + \mathrm {m} \vec {\mathrm {w}} \times \vec {\mathrm {w}} \times \vec {\mathrm {r}} + 2 \mathrm {m} \vec {\mathrm {w}} \times \vec {\mathrm {v}} _ {\mathrm {x y z}}
$$

Donde no se han tenido en cuenta las fuerzas perpendiculares a la plataforma, esto es la gravitatoria y la que resulta de la interacción entre la plataforma y la corredera, dado que las mismas son iguales y de sentido opuesto y por lo tanto, atendiendo que hemos supuesto al sistema libre de rozamiento, no resultan de interés a los efectos de describir el movimiento de la corredera respecto de la plataforma. 

Evaluando las componentes de esta ecuación según las direcciones del sistema solidario a la plataforma, al que se hace referencia anteriormente, resulta: 

$$
\vec {\mathrm {i}} \rightarrow - \mathrm {k x} = \mathrm {m} \ddot {\mathrm {x}} - \mathrm {m w} ^ {2} \mathrm {x}
$$

$$
\vec {\mathrm {j}} \rightarrow \quad \mathrm {N} = 2 \mathrm {m} \dot {\mathrm {x}} \mathrm {w}
$$

De la primera obtenemos: 

$$
\ddot {\mathbf {x}} + (\mathbf {w} _ {\circ} ^ {2} - \mathbf {w} ^ {2}) \mathbf {x} = 0
$$

De donde resultan las situaciones que se detallan a continuación, según la relación existente entre la frecuencia natural del sistema y la velocidad angular con que rota la plataforma: 

# Suponiendo:

$$
\mathrm {w} <   \mathrm {w} _ {\circ}
$$

Y definiendo la magnitud: 

$$
\Omega^ {2} = \mathrm {w} _ {\circ} ^ {2} - \mathrm {w} ^ {2}
$$

La ecuación diferencial anterior puede expresarse como: 

$$
\ddot {\mathbf {x}} + \Omega^ {2} \mathbf {x} = 0
$$

Cuya solución es del tipo: 

$$
\mathrm {x} (t) = \mathrm {A s e n} (\Omega t + \delta)
$$

Que, como lo adelantáramos en el tratamiento cualitativo, corresponde a un movimiento oscilatorio con una frecuencia angular $\Omega$ inferior a la frecuencia natural del sistema y un período dado por: 

$$
\mathrm {T} = \frac {2 \pi}{\sqrt {\mathbf {w} _ {\circ} ^ {2} - \mathbf {w} ^ {2}}}
$$

Claramente mayor que el período que obtendríamos si la plataforma estuviera en reposo. 

# Suponiendo:

$$
\mathbf {w} = \mathbf {w} _ {\circ}
$$

De la ecuación diferencial resulta que la aceleración de la corredera respecto de la plataforma será nula y por lo tanto permanecerá en equilibrio, respecto de la mencionada plataforma, cualquiera sea el valor de su coordenada, tal como lo adelantáramos en el tratamiento cualitativo del problema en consideración. 

# Suponiendo:

$$
\mathrm {w} > \mathrm {w} _ {\circ}
$$

Y definiendo la magnitud: 

$$
\mathrm {q} ^ {2} = \mathrm {w} ^ {2} - \mathrm {w} _ {\circ} ^ {2}
$$

La ecuación diferencial original nos queda expresada como: 

$$
\ddot {\mathrm {x}} - \mathrm {q} ^ {2} \mathrm {x} = 0
$$

Cuya solución vendrá dada por: 

$$
\mathrm {x (t) = C _ {1} e ^ {q t} + C _ {2} e ^ {- q t}}
$$

Claramente divergente, como lo adelantáramos en el tratamiento cualitativo de la situación en consideración. 

Finalmente, una expresión para la fuerza que resulta de la interacción con las paredes laterales puede obtenerse, en cada uno de los casos considerados, derivando las soluciones correspondientes y luego teniéndola en cuenta en la componente ( j ) de la ecuación de movimiento planteada inicialmente. 

# Oscilaciones Amortiguadas en un Sistema No Inercial.

Considerando nuevamente la corredera en una guía diametral labrada en una plataforma en rotación y suponiendo un rozamiento dinámico entre la corredera y las caras laterales de la guía, resulta la situación que se indica en el diagrama siguiente: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/42006589cebd441826958f1cda64f8ea5c14d37cde67fdfb1c37fae2fd5ca74c.jpg)


Donde: 

$$
\mathrm {F} _ {\mathrm {d}} = \mu_ {\mathrm {d}} \mathrm {N}
$$

Con lo que, la ecuación de movimiento para el centro de masa de la corredera planteada desde un sistema de referencia solidario a la plataforma, nos queda:   

$$
\vec {\mathrm {F}} _ {\mathrm {e}} + \vec {\mathrm {N}} + \vec {\mathrm {F}} _ {\mathrm {d}} = \mathrm {m} \vec {a} _ {\mathrm {x y z}} + \mathrm {m} \vec {\mathrm {w}} \times \vec {\mathrm {w}} \times \vec {\mathrm {r}} + 2 \mathrm {m} \vec {\mathrm {w}} \times \vec {\mathrm {v}} _ {\mathrm {x y z}}
$$

Evaluando las componentes de la ecuación anterior según las direcciones del sistema solidario a la plataforma con origen en el centro de la misma, considerado en el tratamiento anterior, obtenemos para cada una de las componentes las ecuaciones que se indican a continuación: 

$$
\vec {\mathrm {j}} \rightarrow \quad \mathrm {N} = 2 \mathrm {m} \dot {\mathrm {x}} \mathrm {w}
$$

$$
\vec {\mathrm {i}} \rightarrow - \mathrm {k x} - 2 \mu_ {\mathrm {d}} \mathrm {m w} \dot {\mathrm {x}} = \mathrm {m} \ddot {\mathrm {x}} - \mathrm {m w} ^ {2} \mathrm {x}
$$

Con lo que, de la ecuación correspondiente a la dirección del eje (x), resulta: 

$$
\ddot {\mathbf {x}} + 2 \mu_ {\mathrm {d}} \mathbf {w} \dot {\mathbf {x}} + (\mathbf {w} _ {\circ} ^ {2} - \mathbf {w} ^ {2}) \mathbf {x} = 0
$$

Que en término de nuevas constantes podemos expresarla como: 

$$
\ddot {\mathbf {x}} + \mathbf {k} _ {1} \dot {\mathbf {x}} + \mathbf {k} _ {2} ^ {2} \mathbf {x} = 0
$$

Proponiendo una solución de la forma: 

$$
\mathrm {x} (t) = \mathrm {C} _ {1} \mathrm {e} ^ {\mathrm {q t}}
$$

Y sustituyendo en la ecuación diferencial, resulta que la constante (q) deberá ser solución de la ecuación algebraica: 

$$
\mathrm {q} ^ {2} + \mathrm {q} \dot {\mathrm {x}} + \mathrm {k} _ {2} ^ {2} = 0
$$

Por lo tanto (q) podrá tomar los valores: 

$$
\mathrm {q} = - \frac {\mathrm {k} _ {1}}{2} \pm \left[ \left(\frac {\mathrm {k} _ {1}}{2}\right) ^ {2} - \mathrm {k} _ {2} ^ {2} \right] ^ {1 / 2}
$$

Que en término de los parámetros originales nos queda expresado como: 

$$
\mathrm {q} = - \mu_ {\mathrm {d}} \mathrm {w} \pm \left[ \mathrm {w} ^ {2} \left(1 + \mu_ {\mathrm {d}} ^ {2}\right) - \mathrm {w} _ {\circ} ^ {2} \right] ^ {1 / 2}
$$

Suponiendo ahora que las condiciones son tales que: 

$$
w ^ {2} \left(1 + \mu_ {d} ^ {2}\right) <   w _ {\circ} ^ {2}
$$

Entonces las raíces de la ecuación algebraica pueden expresarse como: 

$$
\mathrm {q} = - \mu_ {\mathrm {d}} \mathrm {w} \pm \mathrm {i} \left[ \mathrm {w} _ {\circ} ^ {2} - \mathrm {w} ^ {2} (1 + \mu_ {\mathrm {d}} ^ {2}) \right] ^ {1 / 2}
$$

Que definiendo la magnitud: 

$$
\Omega = \left[ w _ {\circ} ^ {2} - w ^ {2} \left(1 + \mu_ {d} ^ {2}\right) \right] ^ {1 / 2}
$$

Pueden expresarse como: 

$$
\mathbf {q} = - \mu_ {\mathrm {d}} \mathbf {w} \pm \mathrm {i} \Omega
$$

Con lo que la solución de nuestra ecuación diferencial nos queda de la forma: 

$$
\mathrm {x} (t) = \mathrm {e} ^ {- \mu_ {\mathrm {d}} \mathrm {w t}} \left(\mathrm {C} _ {1} \mathrm {e} ^ {\mathrm {i} \Omega t} + \mathrm {C} _ {2} \mathrm {e} ^ {- \mathrm {i} \Omega t}\right)
$$

Que indudablemente puede expresarse como: 

$$
\mathrm {x} (t) = \mathrm {A e} ^ {- \mu_ {\mathrm {d}} \mathrm {w t}} \operatorname {s e n} (\Omega t + \delta)
$$

Que claramente corresponde a un movimiento oscilatorio amortiguado y que como era de esperar se reduce a la solución obtenida anteriormente, si se considera nulo el rozamiento entre la corredera y las caras laterales de la guía. Siendo interesante destacar que para la situación planteada, la fuerza de rozamiento que resulta de la interacción por contacto entre dos superficies secas como las consideradas, esto es entre la corredera y las paredes laterales, se comporta como la que resultaría de la presencia de un lubricante entre ambas, dando lugar así a un movimiento análogo al que obtendríamos suponiendo al sistema sometido a una interacción del tipo viscosa. 

Ejecutando el archivo Amortiguadas.htm podrá acceder a una simulación que le permitirá visualizar las variaciones temporales de la posición y la energía de un cuerpo que oscila sometida a la interacción con un muelle y una fuerza proporcional a la velocidad, juntamente con la dependencia entre su velocidad y la coordenada involucrada. La segunda simulación incluida en la página ofrece un interesante modelo de una colisión para diferentes valores del coeficiente de restitución, que se recomienda ejecutar y estudiar la teoría que en la página se ofrece. 

# 3.03 OSCILACIONES FORZADAS SENOIDALMENTE.

Consideraremos ahora, un sistema como el tratado anteriormente en el que además supondremos que el cuerpo está sometido a una excitación del tipo senoidal, como se sugiere en la figura siguiente. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/cee33b48a4396397127c83561cfd0caa4d0f959f97e61a86509eb8d5e77ddc91.jpg)


Con lo que el diagrama de cuerpo aislado y la componente horizontal de la ecuación de Newton para el centro de masa del cuerpo resultan: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/8b3fa22309069cde4b46b34a3f651d81c3672933d82e4b2df83eab4dd69da154.jpg)


$$
\ddot {x} + 2 \lambda \dot {x} + w _ {\circ} ^ {2} x = f _ {\circ} \operatorname {s e n} (w t)
$$

Donde: 

$$
\lambda = \frac {\mathrm {k} _ {\mathrm {v}}}{2 \mathrm {m}}
$$

$$
w _ {o} ^ {2} = \frac {k _ {e}}{m}
$$

$$
f _ {\circ} = \frac {F _ {\circ}}{m}
$$

Para una situación como ésta, puede demostrarse que la solución general de la ecuación diferencial, claramente no homogénea, se obtiene como la suma de la solución general de la homogénea, mas una solución particular de la no homogénea, esto es: 

$$
\mathbf {x} (t) = \mathbf {x} _ {\mathrm {H}} (t) + \mathbf {x} _ {\mathrm {P}} (t)
$$

Donde la solución de la homogénea, sin lugar a dudas, es la obtenida en el tema anterior. 

$$
\mathrm {x (t) = A e ^ {- \lambda t} s e n (\Omega t + \delta)}
$$

Como solución particular de nuestra ecuación diferencial propondremos una función como la que se indica a continuación: 

$$
\mathbf {x} _ {\mathrm {P}} (t) = \mathbf {B} _ {1} \operatorname {s e n} (\mathrm {w t}) + \mathbf {B} _ {2} \cos (\mathrm {w t})
$$

Donde la frecuencia coincide con la frecuencia de excitación y donde los coeficientes deberán ser determinados para garantizar que la función propuesta sea efectivamente una solución de la ecuación diferencial original. Con este propósito deberemos reemplazar en dicha ecuación, la función y sus derivadas temporales, con lo que y luego de operar algebraicamente, obtenemos que los coeficientes deberán ser tales que: 

$$
\left. \right.\left\lfloor \mathrm {B} _ {1} \left(\mathrm {w} _ {\circ} ^ {2} - \mathrm {w} ^ {2}\right) + \mathrm {B} _ {2} 2 \lambda \mathrm {w} - \mathrm {f} _ {\circ} \right\rfloor \mathrm {s e n} (\mathrm {w t}) + \left\lfloor \mathrm {B} _ {1} 2 \lambda \mathrm {w} + \mathrm {B} _ {2} \left(\mathrm {w} _ {\circ} ^ {2} - \mathrm {w} ^ {2}\right)\right\rfloor \mathrm {c o s} (\mathrm {w t}) = 0
$$

Puesto que la anterior deberá ser válida en todo instante, es claro que los factores que multiplican a las funciones trigonométricas deberán anularse, con lo que los coeficientes (Bi) deberán ser solución del sistema de ecuaciones: 

$$
\mathrm {B} _ {1} \left(\mathrm {w} _ {\circ} ^ {2} - \mathrm {w} ^ {2}\right) + \mathrm {B} _ {2} 2 \lambda \mathrm {w} = \mathrm {f} _ {\circ}
$$

$$
\mathrm {B} _ {1} 2 \lambda \mathrm {w} + \mathrm {B} _ {2} (\mathrm {w} _ {\circ} ^ {2} - \mathrm {w} ^ {2}) = 0
$$

De donde resulta: 

$$
\mathrm {B} _ {1} = \frac {\mathrm {f} _ {\circ} \left(\mathrm {w} _ {\circ} ^ {2} - \mathrm {w} ^ {2}\right)}{\left(\mathrm {w} _ {\circ} ^ {2} - \mathrm {w} ^ {2}\right) + (2 \lambda \mathrm {w}) ^ {2}}
$$

$$
\mathrm {B} _ {2} = \frac {2 \mathrm {f} _ {\circ} \lambda \mathrm {w}}{\left(\mathrm {w} _ {\circ} ^ {2} - \mathrm {w} ^ {2}\right) + \left(2 \lambda \mathrm {w}\right) ^ {2}}
$$

Teniendo en cuenta ahora que, la solución particular puede ser expresada en término de dos nuevas constantes (B) y (φ), como se indica a continuación: 

$$
\mathrm {x} _ {\mathrm {P}} (\mathrm {t}) = \mathrm {B} \operatorname {s e n} (\mathrm {w t} + \phi)
$$

Donde las nuevas constantes están relacionadas con las anteriores mediante: 

$$
\mathbf {B} ^ {2} = \mathbf {B} _ {1} ^ {2} + \mathbf {B} _ {2} ^ {2}
$$

$$
\mathrm {t g} \phi = \frac {\mathrm {B} _ {2}}{\mathrm {B} _ {1}}
$$

Y donde el ángulo (φ) es el desfasaje entre la excitación y la solución particular propuesta, luego de tener en cuenta las expresiones logradas para la constantes anteriores en término de los parámetros originales, estas nuevas constantes nos quedan expresadas en término de dichas magnitudes, como: 

$$
\mathbf {B} = \frac {\mathbf {f} _ {\circ}}{\sqrt {(\mathbf {w} _ {\circ} ^ {2} - \mathbf {w} ^ {2}) + (2 \lambda \mathbf {w}) ^ {2}}}
$$

$$
\operatorname {t g} \phi = \frac {2 \lambda \mathrm {w}}{\mathrm {w} _ {\circ} ^ {2} - \mathrm {w} ^ {2}}
$$

Con lo que la solución general de nuestra ecuación diferencial, suma de la correspondiente a la homogénea mas la particular recientemente obtenida, vendrá dada por: 

$$
\mathrm {x} (t) = \mathrm {A e} ^ {- \lambda t} \operatorname {s e n} (\Omega t + \delta) + \mathrm {B s e n} (\mathrm {w t} + \phi)
$$

Resultando entonces la superposición de una oscilación con amplitud constante (B) y frecuencia coincidente con la de excitación que perdurará en el tiempo, mas una función que se amortigua con el tiempo, que en adelante identificaremos como estacionaria y transitoria, respectivamente. 

Finalizado el mencionado estado transitorio, que notemos estará fuertemente relacionado con la amortiguación involucrada, el sistema alcanza el estado estacionario, que responde a una oscilación con amplitud constante y con una frecuencia coincidente con la de excitación, tal que la posición de la partícula variará con el tiempo según: 

$$
\mathrm {x} (t) = \mathrm {B s e n} (\mathrm {w t} + \phi)
$$

Resulta interesante observar que la amplitud del estado estacionario, dependerá fuertemente de la relación existente entre la frecuencia natural del sistema y la frecuencia de excitación, obteniéndose amplitudes muy importantes cuando la frecuencia de la excitación es coincidente con la frecuencia natural del sistema, en cuyo caso: 

$$
\mathrm {B} = \frac {\mathrm {f} _ {\circ}}{2 \lambda \mathrm {w}}
$$

Y el desfasaje entre la excitación del sistema y la respuesta del mismo, vendrá dado por: 

$$
\phi = \frac {\pi}{2}
$$

Situación que en adelante identificaremos como de Resonancia, siendo importante observar que en dicho estado, el valor de la amplitud resultante dependerá inversamente de la constante de amortiguación, tendiendo a infinito si dicha constante tiende a la nulidad. 

La figura siguiente muestra gráficas cualitativas de la amplitud en el estado estacionario en función de la relación entre la frecuencia de excitación y la frecuencia natural del sistema, para diferentes valores de la constante de amortiguación. 

Se recomienda ejecutar los archivos Forzadas-1.htm y Forzadas-2 incluidos en las carpetas del mismo nombre, con lo que podrá acceder a simulaciones destinadas a ilustrar diferentes aspectos relacionados con el tema recientemente considerado. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/53c921b4764b2445750d2f3720f613a7c3eb1bf0365f2628f8967179264290d6.jpg)


# 3.04 OSCILACIONES DE SISTEMAS CON DOS GRADOS DE LIBERTAD.

Consideraremos a continuación las características de las oscilaciones de un sistema con dos grados de libertad como el sugerido en la figura siguiente, donde suponemos que ambos cuerpos tienen igual masa y la misma constante elástica para los resortes laterales. 

$$
\mathbf {m} _ {1} = \mathbf {m} _ {2} = \mathbf {m}
$$

$$
\mathbf {k} _ {1} = \mathbf {k} _ {2} = \mathbf {k} _ {\circ}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/5019b161cacd39cd47d04cdae8bd14754bb7bb0caa192a27b711e46a5b3db85c.jpg)


Con el propósito de plantear las ecuaciones de movimiento, supongamos que apartamos al sistema de su posición de equilibrio y lo dejamos en libertad desde un punto en el que ambas coordenadas son positivas y tales que la primera es mayor que la segunda, en cuyo caso la ecuación de movimiento para el centro de masa de cada uno de los cuerpos vendrá dada por: 

$$
\mathrm {m \ddot {x} _ {1}} = - \mathrm {k} _ {\circ} \mathrm {x} _ {1} - \mathrm {k} (\mathrm {x} _ {1} - \mathrm {x} _ {2})
$$

$$
\mathrm {m} \ddot {\mathrm {x}} _ {2} = - \mathrm {k} _ {\circ} \mathrm {x} _ {2} + \mathrm {k} (\mathrm {x} _ {1} - \mathrm {x} _ {2})
$$

Sistema de ecuaciones diferenciales acopladas, que puede expresarse como: 

$$
\ddot {\mathrm {x}} _ {1} + \frac {\mathrm {k} _ {\circ}}{\mathrm {m}} \mathrm {x} _ {1} + \frac {\mathrm {k}}{\mathrm {m}} \left(\mathrm {x} _ {1} - \mathrm {x} _ {2}\right) = 0
$$

$$
\ddot {\mathbf {x}} _ {2} + \frac {\mathbf {k} _ {\mathrm {o}}}{\mathrm {m}} \mathbf {x} _ {2} - \frac {\mathbf {k}}{\mathrm {m}} (\mathbf {x} _ {1} - \mathbf {x} _ {2}) = 0
$$

Proponiendo soluciones del tipo: 

$$
\mathrm {x} _ {1} = \mathrm {C} _ {1} \operatorname {s e n} (\mathrm {p t} + \alpha)
$$

$$
\mathrm {x} _ {2} = \mathrm {C} _ {2} \operatorname {s e n} (\mathrm {p t} + \alpha)
$$

Reemplazando en las ecuaciones diferenciales y operando algebraicamente, obtenemos: 

$$
\left(- p ^ {2} + \frac {k _ {\circ}}{m} + \frac {k}{m}\right) C _ {1} - \frac {k}{m} C _ {2} = 0
$$

$$
- \frac {\mathrm {k}}{\mathrm {m}} \mathrm {C} _ {1} + \left(- \mathrm {p} ^ {2} + \frac {\mathrm {k} _ {\circ}}{\mathrm {m}} + \frac {\mathrm {k}}{\mathrm {m}}\right) \mathrm {C} _ {2} = 0
$$

Que tendrá solución distinta de la trivial si el determinante de sus coeficientes es nulo: 

$$
\left| \begin{array}{c c} - p ^ {2} + \frac {k _ {\circ}}{m} + \frac {k}{m} & - \frac {k}{m} \\ - \frac {k}{m} & - p ^ {2} + \frac {k _ {\circ}}{m} + \frac {k}{m} \end{array} \right| = 0
$$

De donde resulta que el parámetro (p) podrá tomar los valores: 

$$
p _ {1} = \sqrt {\frac {k _ {\circ}}{m}} \quad y \quad p _ {2} = \sqrt {\frac {k _ {\circ}}{m} + \frac {2 k}{m}}
$$

$$
\mathbf {p} _ {1} <   \mathbf {p} _ {2}
$$

Que en adelante identificaremos como frecuencias fundamentales, las que como veremos estarán asociadas con diferentes modos de oscilación, que identificaremos como modos fundamentales. 

Teniendo en cuenta la primera solución en cualquiera de las ecuaciones algebraicas, resulta que ambas constantes deberán ser iguales, con lo que las soluciones de nuestro sistema de ecuaciones diferenciales se puede expresar como: 

$$
\mathrm {x} _ {1} = \mathrm {A s e n} (\mathrm {p} _ {1} \mathrm {t} + \alpha)
$$

$$
\mathbf {x} _ {2} = \mathbf {A} \operatorname {s e n} (\mathbf {p} _ {1} \mathbf {t} + \boldsymbol {\alpha})
$$

# modo lento

Ambos cuerpos oscilan en fase y con la misma amplitud y en este modo, el resorte de acoplamiento no interviene en el movimiento, se comporta como si se tratara de una varilla rígida. 

Teniendo en cuenta la segunda solución en cualquiera de las ecuaciones algebraicas resulta que las constantes deberán ser iguales pero de signo opuesto, con lo que: 

$$
\mathrm {x} _ {1} = \mathrm {A s e n} (\mathrm {p} _ {2} \mathrm {t} + \alpha)
$$

$$
\mathrm {x} _ {2} = - \mathrm {A s e n} (\mathrm {p} _ {2} \mathrm {t} + \alpha)
$$

# modo rápido

Los cuerpos oscilan con la misma frecuencia y amplitud pero desfasados en (180o) de manera que se mueven en sentido opuesto y el centro del resorte de acoplamiento permanece fijo, como si este punto estuviera rígidamente vinculado a una pared, como se sugiere en la figura siguiente y como lo podrá 

apreciar en la simulación a la que puede acceder ejecutando el archivo Acoplados.htm incluido en la carpeta del mismo nombre, donde dejando en libertad al sistema con amplitudes iguales, podrá observar las características con las que oscila en el modo lento y dejando en libertad al sistema con amplitudes iguales pero de signo opuesto, podrá observar las características del segundo modo. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/ebbfc53fd9aff32906ec3bb23a853c8437c02304c6fb8b1d0904abd1d5cbe872.jpg)


En general y dependiendo de las condiciones iniciales, el movimiento de cada uno de los cuerpos quedará descripto por una combinación lineal de ambas soluciones, y en particular si suponemos que el sistema se deja en libertad a partir de una configuración en la que ambas masas están en reposo con posiciones distintas a las indicadas anteriormente, resulta: 

$$
\mathrm {x} _ {1} = \frac {\mathrm {x} _ {0 1} + \mathrm {x} _ {0 2}}{2} \cos (\mathrm {p} _ {1} t + \alpha) + \frac {\mathrm {x} _ {0 1} - \mathrm {x} _ {0 2}}{2} \cos (\mathrm {p} _ {2} t + \alpha)
$$

$$
\mathrm {x} _ {1} = \frac {\mathrm {x} _ {0 1} + \mathrm {x} _ {0 2}}{2} \cos (\mathrm {p} _ {1} t + \alpha) - \frac {\mathrm {x} _ {0 1} - \mathrm {x} _ {0 2}}{2} \cos (\mathrm {p} _ {2} t + \alpha)
$$

Suponiendo que en el instante inicial la coordenada del segundo cuerpo es nula, y teniendo en cuenta las relaciones trigonométricas para la suma y diferencia de cosenos con diferentes argumentos, de las anteriores se obtiene que en estas condiciones: 

$$
\mathbf {x} _ {1} = \mathbf {x} _ {0 1} \cos \frac {\mathbf {p} _ {1} - \mathbf {p} _ {2}}{2} \mathbf {t} \cdot \cos \frac {\mathbf {p} _ {1} + \mathbf {p} _ {2}}{2} \mathbf {t}
$$

$$
\mathrm {x} _ {2} = \mathrm {x} _ {0 1} \operatorname {s e n} \frac {\mathrm {p} _ {1} - \mathrm {p} _ {2}}{2} \mathrm {t} \cdot \operatorname {s e n} \frac {\mathrm {p} _ {1} + \mathrm {p} _ {2}}{2} \mathrm {t}
$$

Cuyas gráficas temporales se muestran a continuación, donde puede observarse que cada cuerpo oscila con una amplitud modulada por una señal de menor frecuencia, y que existe un constante intercambio de energía entre los elementos que intervienen en el sistema, tal como lo podrá apreciar con toda claridad en la simulación indicada anteriormente, dejando al sistema en libertad con las condiciones iniciales establecidas para obtener la solución anterior. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/8d83259993b5d2f94ef5d27d7ef3193b4e968a47d63b7980793efc9e6ba001f7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/2c8e733b2b48ce41a124d03efef122cb8f01571f5e419cd0c47999c3df25dfee.jpg)


# Péndulos Acoplados.

La figura lateral nos muestra un sistema como el que hemos considerado, formado por dos péndulos acoplados mediante un muelle, en donde los muelles laterales no existen. Las imágenes siguientes corresponden a dos instantes diferentes cuando el sistema oscila en el modo lento. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/cdd825522144a43d05ce7615922ed66fc71ede14985ae326cf43193a961eeb42.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/a64d43e284c22c591db1efa0db693110bc05f25dce3650713160fcc8eee2c3b2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/47298e442999c66f203fd8a1ae1d13c769ed2ab8bc756eb9fa8dbbe95f0143d9.jpg)


Finalmente, las próximas imágenes corresponden a dos instantes diferentes cuando el sistema oscila en el modo rápido. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/899b0b9d70405de4a92784f9bfbf1a154068c56c89c405dc49e46ab615a2040e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/e93da516-04b9-4e5e-88dc-ce288304d378/53aa810d05c3ffc570a34337d78932b2fa8bf584f07b3ecc1d840c98b966fae9.jpg)


Tal como lo podrá apreciar en el video PenAcoplados.avi que se recomienda ejecutar y de donde fueron extraídas las imágenes anteriores. 
