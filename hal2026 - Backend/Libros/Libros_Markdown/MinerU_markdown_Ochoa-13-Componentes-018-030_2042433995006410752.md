# 1.06 COMPONENTES CARTESIANAS.

Puesto que las ecuaciones (1.4) y (1.7) son ecuaciones vectoriales que relacionan la resultante de las fuerzas de interacción con el vector aceleración de una partícula o del centro de masa de un sistema, en el momento de evaluar sus componentes ortogonales, las ecuaciones escalares resultantes tomarán diferentes formas según el sistema de coordenadas seleccionado. 

Así cuando nos referimos al vector posición de una partícula, implícitamente nos estamos refiriendo a un conjunto de tres funciones escalares, en términos de las cuales podemos expresar las componentes del mencionado vector. Estas funciones escalares podrían ser, el conjunto de coordenadas cartesianas según direcciones fijas a nuestro sistema de referencia (xyz), como se sugiere en la figura siguiente donde los vectores unitarios (i,j,k) caracterizan direcciones ortogonales fijas a nuestro sistema de referencia, que no necesariamente deberán ser coincidentes con estas, y cuyos sentidos nos indican el sentido en que crecen cada una de las mencionadas coordenadas. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/4ef9e2da-9f11-4dd6-b5ca-adde04aec60d/310eb6c040416541c95870f12dac86342a9bad2182e5b33da7d4a14382b04c37.jpg)


En función de dichas coordenadas, el vector posición de una partícula puede expresarse en componentes según las direcciones caracterizadas por los vectores unitarios indicados, como: 

$$
\vec {\mathrm {r}} = \mathrm {x} \vec {\mathrm {i}} + \mathrm {y} \vec {\mathrm {j}} + \mathrm {z} \vec {\mathrm {k}}
$$

Teniendo en cuenta que en general, la posición de la partícula cambiará en el tiempo, las coordenadas involucradas serán, en general, funciones escalares del tiempo, que expresaremos como: 

$$
\mathbf {x} = \mathbf {x} (\mathbf {t})
$$

$$
\mathbf {y} = \mathbf {y} (\mathbf {t})
$$

$$
z = z (t)
$$

Que sin lugar a dudas debemos interpretar como las ecuaciones paramétricas de la trayectoria a lo largo de la que se desplazará la partícula, y en término de las cuales el vector posición quedará expresado como: 

$$
\vec {\mathbf {r}} (t) = \mathbf {x} (t) \vec {\mathbf {i}} + \mathbf {y} (t) \vec {\mathbf {j}} + \mathbf {z} (t) \vec {\mathbf {k}}
$$

Resulta oportuno mencionar que el conjunto de coordenadas cartesianas no es el único conjunto adecuado para describir el comportamiento de un sistema, a menudo resultará útil el empleo de otros tipos de coordenadas, que serán tratadas posteriormente a lo largo del presente volumen. 

Suponiendo ahora que la partícula se desplaza a lo largo de una trayectoria plana y orientando los ejes del sistema de referencia, de manera que el plano (xy) coincida con el plano del movimiento, definido por los vectores posición y velocidad, es claro que el vector posición, en función de las coordenadas cartesianas seleccionadas y en componentes según las direcciones de los correspondientes vectores unitarios, quedará expresado como: 

$$
\vec {\mathrm {r}} (t) = \mathrm {x} (t) \vec {\mathrm {i}} + \mathrm {y} (t) \vec {\mathrm {j}}
$$

Derivando temporalmente la anterior y teniendo en cuenta que los vectores unitarios caracterizan direcciones fijas al sistema de referencia desde el que se calcula dicha derivada, con lo que sus derivadas temporales serán nulas, obtenemos la siguiente expresión para el vector velocidad en función de las derivadas temporales de las coordenadas involucradas, indicadas con un punto sobre la función para facilitar la notación, y en componentes según las direcciones de los vectores unitarios, que se muestran cualitativamente en la figura lateral. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/4ef9e2da-9f11-4dd6-b5ca-adde04aec60d/e32807e80f9ac371567498c3531ab0b6b89bb41a7c60bb14ce23857700f82c96.jpg)


$$
\vec {\mathrm {v}} (t) = \dot {\mathrm {x}} (t) \vec {\mathrm {i}} + \dot {\mathrm {y}} (t) \vec {\mathrm {j}}
$$

Análogamente, derivando temporalmente la anterior, obtenemos que el vector aceleración evaluado en componentes según las direcciones en consideración, vendrá dado por: 

$$
\vec {a} (t) = \ddot {x} (t) \vec {i} + \ddot {y} (t) \vec {j}
$$

Suponiendo que las componentes de la ecuación de Newton, que a menudo identificaremos como ecuación de movimiento, son evaluadas según direcciones las direcciones de un sistema cartesiano y por lo tanto, fijas al sistema de referencia, para el caso de un movimiento plano y orientando los ejes del sistema de coordenadas de manera que el plano (xy) coincida con el plano del movimiento, obtendremos una ecuación vectorial de la forma: 

$$
\vec {\mathrm {F}} = \mathrm {m} \ddot {\mathrm {x}} \vec {\mathrm {i}} + \mathrm {m} \ddot {\mathrm {y}} \vec {\mathrm {j}}
$$

De la que resultará el sistema de ecuaciones escalares: 

$$
F _ {x} = m \ddot {x}
$$

$$
F _ {y} = m \ddot {y}
$$

Donde con $\left( \mathrm { F _ { x } } \right)$ indicamos a la componente de la resultante de las fuerzas de interacción, según la dirección del eje (x) y con (Fy) a la componente de la mencionada resultante según la dirección del eje (y), que en general darán lugar a un sistema de ecuaciones en las que intervendrán las coordenadas de la partícula y sus derivadas temporales, que reconoceremos como ecuaciones diferenciales y cuya solución nos proporcionará una descripción del comportamiento del sistema involucrado. 

Teniendo en cuenta las expresiones logradas para las componentes cartesianas de los vectores posición, velocidad y aceleración, resulta oportuno destacar que la derivada temporal de una componente aporta únicamente a la respectiva componente de la magnitud vectorial resultante, aspecto éste que nos permitirá tratar en forma independiente las características del movimiento según cada una de las direcciones seleccionadas. Por lo tanto, suponiendo conocidas las componentes cartesianas de la resultante de las fuerzas de interacción, mediante las anteriores podremos obtener expresiones para las componentes del vector aceleración, con lo que diferenciando dichas componentes, obtenemos: 

$$
\mathrm {d} \dot {\mathbf {x}} = \ddot {\mathbf {x}} (t) \mathrm {d} t
$$

$$
\mathrm {d} \dot {\mathbf {y}} = \ddot {\mathbf {y}} (t) d t
$$

Integrando ambos miembros de las anteriores entre límites físicamente compatibles, correspondientes al instante inicial y a un instante posterior cualquiera, resulta: 

$$
\int_ {\dot {\mathrm {X}} _ {0}} ^ {\dot {\mathrm {X}}} \mathrm {d} \dot {\mathrm {x}} = \int_ {\circ} ^ {\mathrm {t}} \ddot {\mathrm {x}} (t) \mathrm {d} t
$$

$$
\int_ {\dot {y} _ {0}} ^ {\dot {y}} d \dot {y} = \int_ {0} ^ {t} \ddot {y} (t) d t
$$

De donde obtenemos que las componentes cartesianas del vector velocidad, en término de sus valores en el instante inicial y en función del tiempo vendrán dadas en general por: 

$$
\dot {\mathbf {x}} (\mathbf {t}) = \dot {\mathbf {x}} _ {\circ} + \int_ {\circ} ^ {\mathbf {t}} \ddot {\mathbf {x}} (\mathbf {t}) d \mathbf {t}
$$

$$
\dot {\mathbf {y}} (t) = \dot {\mathbf {y}} _ {\circ} + \int_ {\circ} ^ {t} \ddot {\mathbf {y}} (t) d t \tag {1.8}
$$

Que a menudo expresaremos con la notación siguiente: 

$$
\mathrm {v} _ {\mathrm {x}} (\mathrm {t}) = \mathrm {v} _ {\circ \mathrm {x}} + \int_ {\circ} ^ {\mathrm {t}} \mathrm {a} _ {\mathrm {x}} (\mathrm {t}) \mathrm {d t}
$$

$$
\mathbf {v} _ {\mathrm {y}} (\mathbf {t}) = \mathbf {v} _ {\circ \mathrm {y}} + \int_ {\circ} ^ {\mathbf {t}} \mathbf {a} _ {\mathrm {y}} (\mathbf {t}) d \mathbf {t}
$$

Procediendo de manera similar, o sea, diferenciando las anteriores y luego integrando entre límites compatibles, las componentes cartesianas del vector posición, en término de sus valores en el instante inicial y en función del tiempo, nos quedan expresadas como: 

$$
\mathbf {x} (t) = \mathbf {x} _ {\circ} + \int_ {\circ} ^ {t} \mathbf {v} _ {\mathrm {x}} (t) d t
$$

$$
\mathbf {y} (\mathbf {t}) = \mathbf {y} _ {\circ} + \int_ {\circ} ^ {\mathbf {t}} \mathbf {v} _ {\mathbf {y}} (\mathbf {t}) d \mathbf {t}
$$

Resultando para la tercera componente de ambas magnitudes, esto es, en la dirección del eje (z), las expresiones que se indican a continuación, que serán de utilidad para aquellos casos en los que la trayectoria de la partícula no estuviera contenida en un plano. 

$$
\mathbf {v} _ {z} (\mathbf {t}) = \mathbf {v} _ {\circ z} + \int_ {\circ} ^ {\mathbf {t}} \mathbf {a} _ {z} (\mathbf {t}) d \mathbf {t}
$$

$$
\mathbf {z} (\mathbf {t}) = \mathbf {z} _ {\circ} + \int_ {\circ} ^ {\mathbf {t}} \mathbf {v} _ {\mathbf {z}} (\mathbf {t}) \mathrm {d t}
$$

# 1.07 APLICACIONES DE LOS SISTEMAS CARTESIANOS.

En esta oportunidad consideraremos algunas aplicaciones del empleo de sistemas cartesianos para describir las características del movimiento de una partícula en situaciones de interés particular. 

# Movimiento Rectilíneo Uniformemente Variado.

Comenzaremos tratando aquella situación en la que un cuerpo está sometido a una fuerza constante cuya dirección coincide con aquella en la que se movía inicialmente, en cuyo caso se desplazará a lo largo de una trayectoria recta con una aceleración constante, con lo que, orientando los ejes de nuestro sistema de coordenadas cartesianas de manera que el eje (x) coincida con la dirección de la trayectoria a lo largo de la que se desplaza el cuerpo y teniendo en cuenta (1.8) su velocidad en cualquier instante posterior al inicial, vendrá dada por: 

$$
\dot {\mathbf {x}} (\mathbf {t}) = \dot {\mathbf {x}} _ {\circ} + \int_ {\circ} ^ {\mathbf {t}} \mathbf {a} (\mathbf {t}) d \mathbf {t}
$$

De donde obtenemos, que la única componente del vector velocidad, en función del tiempo y de su valor en el instante inicial, vendrá dada por: 

$$
\dot {\mathbf {x}} (\mathsf {t}) = \dot {\mathbf {x}} _ {\circ} + \mathsf {a t}
$$

Que en adelante expresaremos como: 

$$
\mathbf {v} (\mathbf {t}) = \mathbf {v} _ {\circ} + \mathbf {a} \mathbf {t} \tag {1.10}
$$

Con lo que, teniendo en cuenta la anterior en la segunda de las relaciones (1.8), obtenemos que la posición de la partícula medida a lo largo de la trayectoria vendrá dada por: 

$$
\mathbf {x} (t) = \mathbf {x} _ {\circ} + \int_ {\circ} ^ {t} (\mathbf {v} _ {\circ} + a t) d t
$$

Con lo que, dicha magnitud en función del tiempo y de las condiciones iniciales, vendrá dada por: 

$$
\mathbf {x} (\mathbf {t}) = \mathbf {x} _ {\circ} + \mathbf {v} _ {\circ} \mathbf {t} + \frac {1}{2} \mathbf {a t} ^ {2} \tag {1.11}
$$

Las figuras que continúan nos muestran gráficas cualitativas de las funciones recientemente obtenidas para diferentes valores de la aceleración y de las condiciones iniciales involucradas, según se indica en cada uno de los casos que se consideran. 

<table><tr><td>a = 4 m/s2
v0=0 x0=20 m</td><td>a = -4 m/s2
v0=0 x0=20 m</td><td>a = 4 m/s2
V0=-30 m/s x0=60 m</td></tr><tr><td>En el instante inicial la partícula se incluya en reposo a 20 m del origin del sistema de referencia y es sometada a una acceleración de 4 m/s2 en el sentido en que crece la coordinada espacial</td><td>En el instante inicial la partícula para un punto a 20 m del origin del sistemas de referencia desplazándose con una velocidad de 30 m/s en el sentido en que crece la coordinada espacial y es sometada a la acceleración indicada, en sentido opuesto el movimiento en dicho instante</td><td>En el instante inicial la partícula bajo un punto a 60 m del origin del sistema de referencia desplazándose con una velocidad de 30 m/s en el sentido en que decrece la coordinada espacial y es sometada a la acceleración indicada, en sentido opuesto el movimiento en dicho instante</td></tr><tr><td colspan="3">Grá fisicos de la acceleración en función del tiempo</td></tr></table>

# Gráficos de la velocidad en función del tiempo

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/4ef9e2da-9f11-4dd6-b5ca-adde04aec60d/b94566b128f839ae1417f34c1b11ab94991732bd2102bd7eac0c40cdc77062f9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/4ef9e2da-9f11-4dd6-b5ca-adde04aec60d/4918208f39e96e712c763070e58ec383df022d5a7b24485afd376f3a1c03ac17.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/4ef9e2da-9f11-4dd6-b5ca-adde04aec60d/6e2f45586d092c32f352cb552458e5bef3d1103b1368c69c714871cf44818cc0.jpg)


# Gráficos de la posición en función del tiempo

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/4ef9e2da-9f11-4dd6-b5ca-adde04aec60d/f244a1c896339686af30d4068019a51b2b86d0a900eb757b5a05c2e90c0ad4c3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/4ef9e2da-9f11-4dd6-b5ca-adde04aec60d/ab9b8f713f539ed50f4838558e92262fb277510e9f41572ebc91dc2d00225bc0.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/4ef9e2da-9f11-4dd6-b5ca-adde04aec60d/e077b36f7319bbd3a3d5576bdbd505b724f5980e22f4c7408647e93bb58a17a3.jpg)


Como una ilustración mas del tema en consideración, las figuras siguientes muestran gráficas de la posición en función del tiempo para nuevos valores de la aceleración y de las condiciones iniciales involucradas. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/4ef9e2da-9f11-4dd6-b5ca-adde04aec60d/bb9740ba971940419fd7b77f67d65b5fe0345d26857e8f354c49112290b3e361.jpg)


$$
\mathrm {x _ {o} = 1 0 m , v _ {o} = 0 , a = 1 0 m / s ^ {2}}
$$

$$
\mathrm {x _ {o} = 1 0 m , v _ {o} = 0 , a = 2 0 m / s ^ {2}}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/4ef9e2da-9f11-4dd6-b5ca-adde04aec60d/5fff311f92dd4fc85e040e3e2006cc9025a7049ff41698069a3dc07b2b1afc0c.jpg)


$$
\mathrm {x _ {o} = 1 0 m , v _ {o} = 0 , a = 1 0 m / s ^ {2}}
$$

$$
\mathrm {x} _ {\mathrm {o}} = 3 0 \mathrm {m}, \mathrm {v} _ {\mathrm {o}} = 0, \mathrm {a} = - 1 0 \mathrm {m} / \mathrm {s} ^ {2}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/4ef9e2da-9f11-4dd6-b5ca-adde04aec60d/c794ef764db51514374aa06bc542b3edae889c749ff69595d27b25e86972a690.jpg)


$$
\mathrm {x} _ {\mathrm {o}} = 0 \mathrm {m}, \mathrm {v} _ {\mathrm {o}} = 1 0 \mathrm {m} / \mathrm {s}, \mathrm {a} = - 4 \mathrm {m} / \mathrm {s} ^ {2}
$$

$$
\mathrm {x _ {o} = 1 5 m , v _ {o} = - 1 0 m / s , a = 4 m / s ^ {2}}
$$

Eliminando el tiempo entre las expresiones (1.10) y (1.11), obtenidas para la velocidad y posición, podemos conseguir una relación entre el cuadrado de la velocidad y el camino recorrido por la partícula en el intervalo de tiempo correspondiente, que a menudo resulta de utilidad para el tratamiento de algunas aplicaciones. 

$$
\mathbf {v} ^ {2} = \mathbf {v} _ {\circ} ^ {2} + 2 \mathbf {a} (\mathbf {x} - \mathbf {x} _ {\circ})
$$

# Movimiento Rectilíneo Uniforme.

Finalmente resulta oportuno mencionar que una situación particular de la considerada recientemente es aquella en la que, la aceleración de la partícula es nula, que dará lugar a un movimiento 

generalmente conocido como Rectilíneo Uniforme, en cuyo caso su velocidad será constante y su posición en función del tiempo vendrá dada por: 

$$
\mathbf {x} = \mathbf {x} _ {\circ} + \mathbf {v} t
$$

# Laboratorio Virtual I.

# Determinación de Velocidades en Movimientos Rectilíneos Uniformes.

Ejecutando el archivo 01-Mru.htm incluido en la carpeta del mismo nombre, podrá acceder a una simulación que, cronómetro en mano, le permitirá determinar el tiempo empleado por un cuerpo en recorrer con velocidad constante, longitudes que deberá seleccionar de aquellas claramente indicada sobre la superficie libre de rozamiento a lo largo de la que cual se mueve, y con los valores obtenidos, deberá: 

Representar, en un par de ejes ortogonales, el camino recorrido por el cuerpo en función del tiempo empleado en recorrerlo. 

Trazar la recta que, pasando por el origen, mejor ajuste al conjunto de puntos solicitados anteriormente. 

Determinar la velocidad del cuerpo a partir de la pendiente de la recta requerida en el ítem anterior, teniendo en cuenta que para la situación en consideración, donde la coordenada en el instante inicial es nula, el camino recorrido y el tiempo empleado en recorrerlo, están relacionados mediante la expresión. 

$$
\mathbf {x} = \mathbf {v} t
$$

Con el propósito de mejorar la calidad de los resultados se recomienda realizar varias mediciones del tiempo empleado en cada caso, con lo que podrá obtener un promedio de dicha magnitud para ser empleado en la actividad propuesta, siendo recomendable ordenar los valores obtenidos en una tabla como la que se muestra a continuación. 

<table><tr><td>Camino Recorro</td><td>Tiempos Empleados</td><td>Promedio</td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr></table>

Finalmente y con el propósito de realizar comparaciones, deberá modificar aleatoriamente la velocidad del cuerpo mediante el icono “nuevo” incluido en la simulación, que se recomienda determinar mediante el procedimiento indicado anteriormente. 

# Laboratorio Virtual II.

# Determinación de Aceleraciones en Movimientos Rectilíneos Uniformemente Variados.

Ejecutando el archivo 02-Mruv.htm incluido en la carpeta del mismo nombre, podrá acceder a una simulación que, cronómetro en mano, le permitirá determinar el tiempo empleado por un cuerpo en recorrer con aceleración constante, longitudes que deberá seleccionar de aquellas claramente indicada sobre la superficie libre de rozamiento a lo largo de la cual se mueve, y con los valores obtenidos, deberá: 

Representar el camino recorrido en función del tiempo empleado. 

 Representar el camino recorrido en función del cuadrado del tiempo empleado. 

Trazar la recta que mejor ajuste al conjunto de puntos obtenidos en la representación solicitada en el ítem anterior. 

Determinar la aceleración del cuerpo a partir de la pendiente de la recta requerida en el ítem anterior, teniendo en cuenta que para la situación en consideración. 

$$
x = \frac {1}{2} a t ^ {2}
$$

Al igual que en el caso anterior y con el propósito de mejorar la calidad de los resultados, se recomienda realizar varias mediciones del tiempo empleado en cada caso, con lo que podrá obtener un promedio de dicha magnitud para ser empleado en la actividad propuesta, siendo recomendable ordenar los valores obtenidos en una tabla como la que se muestra a continuación. 

<table><tr><td>Caminos Recorridos</td><td>Tiempos Empeados</td><td>Promedio</td><td>Cuadrado del Promedio</td></tr><tr><td rowspan="5"></td><td></td><td rowspan="5"></td><td rowspan="5"></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr></table>

Finalmente y con el propósito de realizar comparaciones, deberá modificar aleatoriamente la aceleración del cuerpo mediante el icono “nuevo” incluido en la simulación, que se recomienda determinar mediante el procedimiento indicado anteriormente. 

# Movimiento Circular Uniformemente Variado.

Como otra interesante aplicación del manejo de un sistema cartesiano, consideremos el caso de una partícula que se desplaza a lo largo de una trayectoria circular de radio R como la indicada en la figura siguiente, donde la coordenada angular varia con el tiempo según. 

$$
\alpha (\mathbf {t}) = \frac {1}{2} \mathbf {k t} ^ {2}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/4ef9e2da-9f11-4dd6-b5ca-adde04aec60d/c187ee84e33815dbc48d878ce3414b7c4ec308ddae47ff374574e2ee40814dbd.jpg)


En este caso, su vector posición respecto del origen del sistema de referencia indicado en la figura anterior y evaluado en componentes según las direcciones de dicho sistema queda expresado en términos de la coordenada angular involucrada, como: 

$$
\vec {\mathrm {r}} = \mathrm {R} \operatorname {s e n} (\alpha) \vec {\mathrm {i}} + \mathrm {R} \cos (\alpha) \vec {\mathrm {j}}
$$

De donde luego de derivar temporalmente, obtenemos para el vector velocidad la expresión siguiente: 

$$
\vec {\mathbf {v}} = \mathrm {R} \dot {\alpha} \left[ \cos (\alpha) \vec {\mathrm {i}} - \operatorname {s e n} (\alpha) \vec {\mathrm {j}} \right]
$$

Donde la magnitud entre corchetes no es otra cosa que un vector unitario, tangente a la trayectoria en cada punto, como el indicado en la figura anterior, con lo que al vector velocidad de la partícula podemos expresarlo en términos de ésta nueva magnitud, como: 

$$
\vec {\mathrm {v}} = \mathrm {R} \dot {\alpha} \vec {\mathrm {e}} _ {\mathrm {t}}
$$

Finalmente, derivando temporalmente la expresión conseguida para el vector velocidad en componentes cartesianas, el vector aceleración de la partícula nos queda expresado en dichas componentes, como: 

$$
\vec {\mathsf {a}} = \mathrm {R} \ddot {\alpha} \left[ \cos (\alpha) \vec {\mathsf {i}} - \operatorname {s e n} (\alpha) \vec {\mathsf {j}} \right] + \mathrm {R} \dot {\alpha} ^ {2} \left[ - \operatorname {s e n} (\alpha) \vec {\mathsf {i}} - \cos (\alpha) \vec {\mathsf {j}} \right]
$$

Donde las magnitudes entre corchetes son, el vector tangente unitario considerado anteriormente y la restante, un vector también unitario, pero normal a la trayectoria en cada punto y dirigido hacia el centro de la misma como se indica en la figura anterior, con lo que, al vector aceleración en componentes según estas nuevas direcciones podemos expresarlo como: 

$$
\vec {\mathrm {a}} = \mathrm {R} \ddot {\alpha} \vec {\mathrm {e}} _ {\mathrm {t}} + \mathrm {R} \dot {\alpha} ^ {2} \vec {\mathrm {e}} _ {\mathrm {n}}
$$

Esto es, como la suma de una componente tangente a la trayectoria, cuyo módulo está relacionado con la derivada segunda de la coordenada angular y por lo tanto con las variaciones temporales en el módulo del vector velocidad, mas una componente normal a la trayectoria, dirigida hacia el centro de la misma, cuyo módulo esta indudablemente relacionado el módulo del vector velocidad y con los cambios observados en la dirección de dicha magnitud, lo que formalmente podemos expresar como: 

$$
\vec {a} = \dot {\mathbf {v}} \vec {\mathbf {e}} _ {\mathrm {t}} + \frac {\mathbf {v} ^ {2}}{\mathbf {R}} \vec {\mathbf {e}} _ {\mathrm {n}}
$$

Teniendo en cuenta las conclusiones anteriores y la ecuación de Newton, resulta que para la situación en consideración, la partícula deberá estar sometida a interacciones tales que den lugar a una fuerza que podremos expresarla como la suma de una componente normal a la trayectoria, asociada con los cambios observados en la dirección del vector velocidad y dirigida hacia el centro de la misma, conocida como fuerza centrípeta, cuyo módulo vendrá dado por: 

$$
\mathrm {F _ {n}} = \mathrm {m R} \dot {\alpha} ^ {2} \quad \therefore \quad \mathrm {F _ {n}} = \mathrm {m} \frac {\mathrm {v} ^ {2}}{\mathrm {R}}
$$

Mas una componente tangente a la trayectoria, cuyo módulo estará directamente relacionado con los cambios observados en el módulo del vector velocidad y que podremos expresar como: 

$$
\mathrm {F} _ {\mathrm {t}} = \mathrm {m R} \ddot {\alpha} \vec {\mathrm {e}} _ {\mathrm {t}} \quad \therefore \quad \mathrm {F} _ {\mathrm {t}} = \mathrm {m} \dot {\mathrm {v}}
$$

# 1.08 COMPONENTES INTRÍNSECAS.

# Función Posición.

Consideraremos a continuación el caso el caso de una partícula que como consecuencia de los vínculos a que pudiera estar sometida, está restringida a desplazarse a lo largo de una trayectoria plana predeterminada, como por ejemplo la sugerida en la figura siguiente donde hemos supuesto que los ejes del sistema de referencia respecto del que se describe el movimiento se han orientado de manera que el plano (xy) coincida con el plano del movimiento. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/4ef9e2da-9f11-4dd6-b5ca-adde04aec60d/39344777f3c69032040302b1690cdef083f1bde10376f69468a739b94d0b3576.jpg)


Entendiendo por grados de libertad de un sistema al número de coordenadas linealmente independientes necesarias para describir su comportamiento y bajo las condiciones recientemente impuestas, es claro que la partícula deberá ser considerada como un sistema con un único grado de libertad puesto que las variables involucradas, o sea, las coordenadas (x) e (y), no son linealmente independientes como consecuencia de existir entre ellas una relación funcional predeterminada, supuestamente conocida. 

$$
\mathbf {y} = \mathbf {f} (\mathbf {x})
$$

Con lo que, el conocimiento de la dependencia temporal de cualquiera de ellas permitirá obtener información sobre la dependencia temporal de la restante. 

Para una situación como la indicada, a menudo las coordenadas cartesianas no son las más convenientes para formular una descripción del movimiento de la partícula. En estos casos suele resultar muy conveniente describir el movimiento en términos de la posición de la partícula medida a lo largo de la trayectoria, respecto de algún punto arbitrario de la misma, indicado con (Q) en la figura En lo que continúa y a menos que digamos lo contrario, designáremos como coordenada de posición a la variable indicada en el párrafo anterior, que identificaremos con (s), empleando la letra Q para referirnos al punto de la trayectoria respecto del cual se determinan los valores de la mencionada coordenada, siendo totalmente arbitraria la selección del sentido en que crece dicha magnitud. 

Una vez seleccionado el punto respecto del que determinaremos la coordenada de posición y el sentido en el que se la considerará creciente, como se sugiere en la figura anterior, es claro que dicha coordenada será en general, una función del tiempo directamente relacionada con la “forma” en que la partícula recorra la trayectoria, a la que en adelante reconoceremos como función posición. 

$$
\mathbf {s} = \mathbf {s} (\mathbf {t})
$$

En este momento resulta adecuado destacar que como la posición de la partícula deberá estar definida en cada instante (al menos en lo que a este formalismo se refiere), la función posición deberá ser continua y estar unívocamente definida en cada instante. 

# Vector Velocidad.

Puesto que estamos suponiendo conocida de antemano la trayectoria a lo largo de la que se desplazará la partícula, carece de interés pensar en una expresión formal para el vector posición de la misma, por lo tanto en lo que continúa dedicaremos nuestro esfuerzo a la búsqueda de expresiones formales para los vectores velocidad y aceleración de la partícula, en términos de la función posición y sus derivadas temporales, que serán de utilidad para el tratamiento de problemas vinculados con el movimiento de una partícula a lo largo de trayectorias predeterminadas. 

Con el propósito de obtener una expresión para el vector velocidad de la partícula tengamos en cuenta que de acuerdo a (1.1) dicho vector se definió como: 

$$
\vec {\mathrm {v}} = \frac {\mathrm {d} \vec {\mathrm {r}}}{\mathrm {d t}}
$$

Que en términos de la coordenada de posición puede se lo puede expresar: 

$$
\vec {\mathrm {v}} = \frac {\mathrm {d} \vec {\mathrm {r}}}{\mathrm {d} \mathrm {s}} \frac {\mathrm {d} \mathrm {s}}{\mathrm {d} \mathrm {t}}
$$

Que también podemos expresar como: 

$$
\vec {\mathrm {v}} = \dot {\mathrm {s}} \frac {\mathrm {d} \vec {\mathrm {r}}}{\mathrm {d} \mathrm {s}}
$$

Resultando interesante destacar que la derivada temporal de la función posición tiene en cuenta, de que manera, la partícula recorre la trayectoria. En cambio la restante, esto es, la derivada del vector posición respecto de la coordenada de posición, está relacionada con la geometría del problema, o sea con las características de la trayectoria. No contiene ninguna información sobre la "forma" en que la partícula recorre dicha trayectoria, que como lo mencionáramos, está contenida en la derivada temporal de la función posición. 

Para evaluar la derivada del vector posición respecto de la coordenada de posición, tengamos en cuenta que. 

$$
\frac {\mathrm {d} \vec {\mathrm {r}}}{\mathrm {d s}} = \lim  _ {\Delta \mathrm {s} \rightarrow 0} \frac {\Delta \vec {\mathrm {r}}}{\Delta \mathrm {s}}
$$

Definiendo el vector tangente unitario $\bf ( \nabla \bf { e } _ { t } )$ como un vector tangente a la trayectoria en cada punto, cuyo sentido coincide con el sentido en que crece la coordenada de posición (arbitrariamente seleccionado por nosotros) y suponiendo que la partícula recorre dicha trayectoria en el sentido mencionado, como se sugiere en la figura siguiente, el camino recorrido por la partícula en el intervalo de tiempo considerado resulta: 

$$
\Delta \mathbf {s} = \mathbf {s} (\mathbf {t} + \Delta \mathbf {t}) - \mathbf {s} (\mathbf {t})
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/4ef9e2da-9f11-4dd6-b5ca-adde04aec60d/2b78d57d85b4b6d163048bd12cd38c277c53cc441f75a7fa2a124f27e2350a79.jpg)


Claramente positivo, y puesto que en el límite su valor coincidirá con el módulo del vector desplazamiento, sin lugar a dudas podemos afirmar que bajo estas condiciones: 

$$
\lim  _ {\Delta \mathrm {s} \rightarrow 0} \frac {\Delta \vec {\mathrm {r}}}{\Delta \mathrm {s}} = \vec {\mathrm {e}} _ {\mathrm {t}}
$$

Con lo que: 

$$
\frac {\mathrm {d} \vec {\mathrm {r}}}{\mathrm {d} \mathrm {s}} = \vec {\mathrm {e}} _ {\mathrm {t}}
$$

Análogamente, considerando la otra situación posible, que la partícula recorra la trayectoria en el sentido en que decrece la coordenada de posición, como se sugiere en la figura siguiente, nuevamente, el camino recorrido por la partícula en el intervalo de tiempo considerado vendrá dado por: 

$$
\Delta \mathbf {s} = \mathbf {s} (\mathbf {t} + \Delta \mathbf {t}) - \mathbf {s} (\mathbf {t})
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/4ef9e2da-9f11-4dd6-b5ca-adde04aec60d/4d13c066e755f505d3a96f8d3e730f1491128839c3e96d2330f3e25d277fe925.jpg)


Que en esta oportunidad será negativo, y por lo tanto podemos afirmar que también bajo estas condiciones. 

$$
\frac {\mathrm {d} \vec {\mathrm {r}}}{\mathrm {d} \mathrm {s}} = \vec {\mathrm {e}} _ {\mathrm {t}}
$$

Por lo tanto, en general e independientemente del sentido en que la partícula recorra la trayectoria, la derivada temporal en consideración siempre será coincidente con el vector tangente unitario definido anteriormente, con lo que el vector velocidad quedará expresado como: 

$$
\vec {\mathrm {v}} (\mathrm {t}) = \dot {\mathrm {s}} (\mathrm {t}) \vec {\mathrm {e}} _ {\mathrm {t}} \tag {1.12}
$$

Recordando que el vector tangente unitario indica el sentido en que crece la coordenada de posición (independientemente del sentido en que la partícula recorra la trayectoria) de la expresión anterior resulta que valores negativos de la derivada temporal de la función posición estarán asociados con un movimiento en el sentido decreciente de dicha coordenada, en cambio valores positivos de la mencionada derivada estarán asociados con un movimiento en el sentido creciente de esta coordenada, siendo interesante destacar que en todos los casos, el módulo del vector velocidad de la partícula vendrá expresado por: 

$$
\mathbf {v} (\mathbf {t}) = | \dot {\mathbf {s}} (\mathbf {t}) |
$$

# Vector aceleración.

Puesto que al vector aceleración de una partícula lo hemos definido como la derivada temporal de su vector velocidad, o sea: 

$$
\vec {a} = \frac {\mathrm {d} \vec {v}}{\mathrm {d} t}
$$

Teniendo en cuenta esto y la expresión (1.12) obtenida para el vector velocidad, resulta: 

$$
\vec {\mathrm {a}} (\mathrm {t}) = \ddot {\mathrm {s}} (\mathrm {t}) \vec {\mathrm {e}} _ {\mathrm {t}} + \dot {\mathrm {s}} (\mathrm {t}) \dot {\vec {\mathrm {e}}} _ {\mathrm {t}} \tag {1.13}
$$

Donde la derivada temporal del vector tangente unitario ha sido considerada, ya que en general esta derivada no será nula (a menos que la trayectoria sea una recta) como consecuencia de los cambios observados, desde el sistema de referencia involucrado, en la dirección del mencionado vector. 

Con el propósito de evaluar dicha derivada temporal tengamos en cuenta que: 

$$
\dot {\vec {e}} _ {t} = \frac {\mathrm {d} \vec {e} _ {t}}{\mathrm {d} t}
$$

Que podemos expresar como: 

$$
\dot {\vec {e}} _ {t} = \frac {\mathrm {d} \vec {e} _ {t}}{\mathrm {d} s} \frac {\mathrm {d} s}{\mathrm {d} t}
$$

O bien, como: 

$$
\dot {\vec {\mathbf {e}}} _ {t} = \dot {s} (t) \frac {d \vec {\mathbf {e}} _ {t}}{d s}
$$

Siendo interesante destacar que así indicada, la derivada temporal en consideración, resulta claramente dependiente de la “forma” en que la partícula recorre la trayectoria, más precisamente de 

su velocidad (a través de la derivada temporal de la función posición) y de la geometría del problema, esto es de las características de la trayectoria (a través de la derivada del vector tangente unitario, respecto de la coordenada de posición), con lo que (1.13) nos queda expresada como: 

$$
\vec {\mathrm {a}} (\mathrm {t}) = \ddot {\mathrm {s}} (\mathrm {t}) \vec {\mathrm {e}} _ {\mathrm {t}} + \dot {\mathrm {s}} ^ {2} (\mathrm {t}) \frac {\mathrm {d} \vec {\mathrm {e}} _ {\mathrm {t}}}{\mathrm {d} \mathrm {s}} \tag {1.14}
$$

Donde la derivada del vector tangente unitario, respecto de la coordenada de posición, puede demostrarse viene dada por: 

$$
\frac {\mathrm {d} \vec {\mathrm {e}} _ {\mathrm {t}}}{\mathrm {d} \mathrm {s}} = \frac {1}{\rho} \vec {\mathrm {e}} _ {\mathrm {n}}
$$

Siendo (ρ) el radio de curvatura de la trayectoria en el punto considerado y $\textbf { ( e _ { \mathrm { n } } ) }$ un vector unitario, normal a la trayectoria en dicho punto y dirigido hacia el centro de curvatura, como se sugiere en la figura siguiente. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/4ef9e2da-9f11-4dd6-b5ca-adde04aec60d/35328ba33f6ab5471d298bb164e10abee07b32a715dc3aa4fe7fecaf76b32362.jpg)


Con lo que en general, al vector aceleración de la partícula podremos expresarlo como: 

$$
\vec {\mathrm {a}} (\mathrm {t}) = \ddot {\mathrm {s}} (\mathrm {t}) \vec {\mathrm {e}} _ {\mathrm {t}} + \frac {\dot {\mathrm {s}} ^ {2} (\mathrm {t})}{\rho} \vec {\mathrm {e}} _ {\mathrm {n}} \tag {1.15}
$$

Esto es, como la suma de una componente tangente a la trayectoria, directamente relacionado con los cambios temporales en el módulo del vector velocidad, que en adelante identificaremos como: 

$$
\vec {\mathrm {a}} _ {\mathrm {t}} (\mathrm {t}) = \ddot {\mathrm {s}} (\mathrm {t}) \vec {\mathrm {e}} _ {\mathrm {t}}
$$

Mas una componente normal relacionada con el módulo del vector velocidad, (más estrictamente con el cuadrado del mismo) y con el radio de curvatura de la trayectoria en el punto considerado, esto último directamente vinculado con la geometría del problema y por lo tanto con los cambios temporales observados en la dirección del vector velocidad de la partícula, que en adelante expresaremos como: 

$$
\vec {a} _ {\mathrm {n}} (t) = \frac {\dot {s} ^ {2} (t)}{\rho} \vec {e} _ {\mathrm {n}}
$$

Finalmente, teniendo en cuenta las conclusiones obtenidas para los vectores velocidad y aceleración de una partícula, resulta que, cuando las derivadas primera y segunda de la función posición tengan el mismo signo (o sea, cuando el sentido de la componente tangencial del vector aceleración coincide con el sentido del movimiento) entonces debemos esperar incrementos en la velocidad de la partícula. En cambio si los signos mencionados fueran opuestos, esto se traducirá en una disminución en el módulo de la velocidad de la partícula en consideración. 

# Componentes Intrínsecas de la Ecuación de Newton.

Teniendo en cuenta las conclusiones anteriores y la ecuación de Newton, las componentes intrínsecas del vector aceleración estarán relacionadas con la resultante de las fuerzas de interacción, mediante: 

$$
\vec {\mathrm {F}} = \mathrm {m} \ddot {\mathrm {s}} \vec {\mathrm {e}} _ {\mathrm {t}} + \mathrm {m} \frac {\dot {\mathrm {s}} ^ {2}}{\rho} \vec {\mathrm {e}} _ {\mathrm {n}}
$$

Que luego de expresar a dicha resultante en componentes según las direcciones de los vectores tangente y normal a la trayectoria, dará lugar al sistema de ecuaciones escalares: 

$$
\mathrm {F} _ {\mathrm {t}} = \mathrm {m} \ddot {\mathrm {s}}
$$

$$
F _ {n} = m \frac {\dot {s} ^ {2}}{\rho}
$$

Cuya solución nos permitirá contar con una adecuada descripción del movimiento de la partícula o del centro de masa de un cuerpo. 

# 1.09 COMPONENTES POLARES DE LOS VECTORES VELOCIDAD Y ACELERACIÓN.

Como lo mencionamos anteriormente, el manejo de componentes cartesianas resulta particularmente útil en el tratamiento de aquellas situaciones donde la dirección de la resultante de las fuerzas de interacción a las que está sometido un cuerpo y por lo tanto su vector aceleración permanece constante. 

Como lo veremos a lo largo de las aplicaciones, existe una variedad de problemas en los que resultará muy conveniente expresar a los vectores velocidad y aceleración en componentes según una dirección coincidente con la del vector posición y una dirección ortogonal a ésta, relacionada con una coordenada angular. 

Con el propósito de desarrollar la herramienta mencionada y como se sugiere en la figura siguiente, la posición de una partícula que se desplaza a lo largo de una trayectoria plana quedará bien identificada si en cada instante damos los valores de las coordenadas, radial y angular, que se indican a continuación y que se muestran en la mencionada figura. 

$$
\mathbf {r} = \mathbf {r} (\mathbf {t}) \qquad \mathbf {y} \qquad \boldsymbol {\theta} = \boldsymbol {\theta} (\mathbf {t})
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/4ef9e2da-9f11-4dd6-b5ca-adde04aec60d/272cf759b8f446435f4850469b312b621b13e8a9ba01c77e110ea9007568d197.jpg)


Coordenadas que en general serán funciones del tiempo, en término de las cuales trataremos de obtener expresiones para los vectores posición, velocidad y aceleración de una partícula, en componentes según las direcciones caracterizadas por los vectores unitarios, radial y transversal, asociados con el sentido de crecimiento de dichas coordenadas, que se muestran en la figura anterior. Teniendo en cuenta como han sido definidas, en función de estas nuevas coordenadas es inmediato que el vector posición de una partícula nos queda expresado como: 

$$
\vec {\mathbf {r}} (\mathbf {t}) = \mathbf {r} (\mathbf {t}) \vec {\mathbf {e}} _ {\mathrm {r}}
$$

Recordando que el vector velocidad de una partícula se define como la derivada temporal de su vector posición, es inmediato entonces que una expresión para dicha magnitud en función de las coordenadas en consideración resultará de derivar la obtenida recientemente para el mencionado vector posición, con lo que: 

$$
\vec {\mathrm {v}} (t) = \dot {\mathrm {r}} (t) \vec {\mathrm {e}} _ {\mathrm {r}} + \mathrm {r} (t) \dot {\vec {\mathrm {e}}} _ {\mathrm {r}}
$$

Donde hemos incluido la derivada temporal del vector radial unitario ya que atendiendo como lo hemos definido no podemos esperar que en general, dicha derivada, calculada desde el sistema de referencia en consideración, sea nula, como consecuencia de los cambios temporales que cabe esperar en la dirección del mencionado vector unitario, salvo en aquellas situaciones muy particulares en las que la partícula se desplace a lo largo de una trayectoria recta según la dirección radial. 

Con el propósito de evaluar dicha derivada temporal, expresaremos al mencionado vector unitario en componentes según las direcciones de los vectores unitarios cartesianos, con lo que: 

$$
\vec {\mathrm {e}} _ {\mathrm {r}} = \cos \theta \vec {\mathrm {i}} + \sin \theta \vec {\mathrm {j}}
$$

Teniendo en cuenta que los vectores unitarios cartesianos caracterizan direcciones fijas al sistema de referencia involucrado, de la anterior obtenemos: 

$$
\dot {\vec {\mathrm {e}}} _ {\mathrm {r}} = \dot {\theta} (- \operatorname {s e n} \theta \vec {\mathrm {i}} + \cos \theta \vec {\mathrm {j}})
$$

Como lo podemos apreciar en la figura anterior, el término entre paréntesis no es otra cosa que el vector unitario en la dirección transversal, con lo que: 

$$
\dot {\vec {\mathrm {e}}} _ {\mathrm {r}} = \dot {\theta} \vec {\mathrm {e}} _ {\theta}
$$

Y el vector velocidad de la partícula nos queda expresado como: 

$$
\vec {\mathrm {v}} (\mathrm {t}) = \dot {\mathrm {r}} (\mathrm {t}) \vec {\mathrm {e}} _ {\mathrm {r}} + \mathrm {r} (\mathrm {t}) \dot {\theta} (\mathrm {t}) \vec {\mathrm {e}} _ {\theta} \tag {1.16}
$$

O sea como, la suma de una componente en la dirección radial dada por: 

$$
\vec {\mathrm {v}} _ {\mathrm {r}} (\mathrm {t}) = \dot {\mathrm {r}} (\mathrm {t}) \vec {\mathrm {e}} _ {\mathrm {r}}
$$

Mas una componente en la dirección transversal dada por: 

$$
\vec {\mathrm {v}} _ {\theta} (\mathbf {t}) = \mathbf {r} (\mathbf {t}) \dot {\theta} (\mathbf {t}) \vec {\mathrm {e}} _ {\theta}
$$

Que cualitativamente se muestran en la figura siguiente. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/4ef9e2da-9f11-4dd6-b5ca-adde04aec60d/94ac0dcfce7d07fe5e4356cbffdec4bbf4f5848e05e2d187f7493ff5d673f487.jpg)


Resulta interesante destacar que la componente radial del vector velocidad, nos proporciona información sobre la rapidez con que la partícula se acerca o aleja al punto desde donde se determina su vector posición, que en adelante identificaremos como polo o centro de nuestro sistema de coordenadas y que en lo que va del tema hemos supuesto coincidente con el origen de nuestro sistema de referencia. 

En cambio la componente transversal nos proporciona información relacionada con la rapidez con que el vector posición barre ángulos, a través de la derivada temporal de la coordenada angular, determinada a partir de una dirección fija al mencionado sistema de referencia, que en adelante identificaremos como eje polar y que hasta el momento hemos supuesto coincidente con uno de los ejes de dicho sistema, condición ésta que no necesariamente debe respetarse, pero que indudablemente resulta conveniente. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/4ef9e2da-9f11-4dd6-b5ca-adde04aec60d/1a61b0478fe20c46a458ae38e1eea505e1e6d57b81fd13fa2f21c918968d6ea8.jpg)


# Ejemplo.

Consideremos el caso de un proyectil que asciende con una velocidad constante mientras es seguido por una estación de radar en el origen de nuestro sistema de referencia, como se sugiere en la figura lateral. 

Seleccionando como polo al punto de emplazamiento del radar, la componente radial del vector velocidad del proyectil, indicada en la figura puede expresarse como: 

$$
v _ {r} = v s e n \theta
$$

Por lo tanto, la derivada temporal de la coordenada radial vendrá dada por: 

$$
\dot {\mathbf {r}} = \mathbf {v} \sin \theta
$$

Que en término de la coordenada vertical puede expresarse como: 

$$
\dot {\mathbf {r}} = \mathbf {v} \frac {\mathbf {y} (\mathbf {t})}{\mathbf {r} (\mathbf {t})}
$$

Teniendo en cuenta que hemos supuesto constante la velocidad del proyectil, con lo que su coordenada vertical variará linealmente con el tiempo, de la anterior resulta que la componente radial en función del tiempo vendrá dada por: 

$$
\dot {\mathbf {r}} = \frac {\mathbf {v} ^ {2} \mathbf {t}}{\sqrt {\mathbf {D} ^ {2} + \mathbf {v} ^ {2} \mathbf {t} ^ {2}}}
$$

Por lo tanto, cuando: 

$$
\mathbf {t} \rightarrow \infty \qquad \dot {\mathbf {r}} \rightarrow \mathbf {v}
$$

Lo que era de esperar, ya que en estas condiciones el proyectil se encontrará infinitamente lejos del radar, y por lo tanto la componente radial deberá coincidir con el vector velocidad del proyectil. 

Análogamente, de la figura obtenemos que la componente transversal del vector velocidad puede expresarse en términos de la coordenada angular, como: 

$$
\mathbf {v} _ {\theta} = \mathbf {v} \cos \theta
$$

Por lo tanto: 

$$
r \dot {\theta} = v \cos \theta
$$

Con lo que, las variaciones temporales de la coordenada angular, que en adelante identificaremos como velocidad angular, nos queda expresada como: 

$$
\dot {\theta} = v \frac {D}{r ^ {2}}
$$

Con lo que dicha magnitud en función del tiempo vendrá dada por: 

$$
\dot {\theta} = v \frac {D}{D ^ {2} + v ^ {2} t ^ {2}}
$$

Que decrece en el tiempo de manera que tiende a cero cuando éste tiende a infinito, con lo que la componente transversal del vector velocidad también tenderá a la nulidad, lo que era de esperar si tenemos en cuenta que como ya lo indicáramos, en esas condiciones la componente radial tendía a confundirse con el vector velocidad del proyectil. 

# Vector Velocidad Angular.

A continuación definiremos una magnitud vectorial directamente relacionada con la velocidad angular de interés en el tratamiento de temas que requieran el manejo de componentes polares. Con este propósito multiplicaremos vectorialmente las expresiones obtenidas anteriormente para el vector posición y velocidad de una partícula, con lo que: 

$$
\vec {\mathrm {r}} \times \vec {\mathrm {v}} = \mathrm {r} ^ {2} \dot {\theta} \left(\vec {\mathrm {e}} _ {\mathrm {r}} \times \vec {\mathrm {e}} _ {\theta}\right)
$$

Definiendo el vector unitario, normal al plano del movimiento: 

$$
\vec {\mathrm {e}} _ {\mathrm {w}} = \vec {\mathrm {e}} _ {\mathrm {r}} \times \vec {\mathrm {e}} _ {\theta}
$$

La igualdad anterior puede expresarse como: 

$$
\vec {\mathrm {r}} \times \vec {\mathrm {v}} = \mathrm {r} ^ {2} \dot {\theta} \vec {\mathrm {e}} _ {\mathrm {w}}
$$

Definiendo el vector velocidad angular de la partícula, como: 

$$
\vec {\mathrm {w}} = \dot {\theta} \vec {\mathrm {e}} _ {\mathrm {w}}
$$

Resulta entonces un vector normal al plano del movimiento cuyo módulo está directamente vinculado con la velocidad con que el vector posición barre ángulos en el plano del movimiento, que en general podremos expresar como: 

$$
\vec {\mathrm {w}} = \frac {\vec {\mathrm {r}} \times \vec {\mathrm {v}}}{\mathrm {r} ^ {2}} \tag {1.17}
$$

# Componentes Polares del Vector Aceleración.

Teniendo en cuenta como a sido definido el vector aceleración de una partícula, y con el propósito de obtener una expresión para dicha magnitud en componentes polares, derivando temporalmente la obtenida para el vector velocidad, resulta: 

$$
\vec {a} = \ddot {r} \vec {e} _ {r} + \dot {r} \dot {\vec {e}} _ {r} + \dot {r} \dot {\theta} \vec {e} _ {\theta} + r \ddot {\theta} \vec {e} _ {\theta} + r \dot {\theta} \dot {\vec {e}} _ {\theta}
$$

Expresando el vector transversal unitario en componentes cartesianas.  

$$
\vec {\mathrm {e}} _ {\theta} = - \operatorname {s e n} \theta \vec {\mathrm {i}} + \cos \theta \vec {\mathrm {j}}
$$

Y derivando temporalmente, obtenemos: 

$$
\dot {\vec {\mathbf {e}}} _ {\theta} = - \dot {\boldsymbol {\theta}} (\cos \theta \vec {\mathrm {i}} + \sin \theta \vec {\mathrm {j}})
$$

Puesto que el término entre paréntesis es el vector radial unitario, expresado en componentes cartesianas, de la anterior resulta: 

$$
\dot {\vec {\mathrm {e}}} _ {\theta} = - \dot {\theta} \vec {\mathrm {e}} _ {\mathrm {r}}
$$

Teniendo en cuenta esta conclusión y la obtenida anteriormente para la derivada temporal del vector radial unitario, el vector aceleración de la partícula nos queda: 

$$
\vec {a} = \ddot {r} \vec {e} _ {r} + \dot {r} \dot {\theta} \vec {e} _ {\theta} + \dot {r} \dot {\theta} \vec {e} _ {\theta} + r \ddot {\theta} \vec {e} _ {\theta} - r \dot {\theta} ^ {2} \vec {e} _ {r}
$$

Que luego de agrupar las componentes queda expresado como: 

$$
\vec {\mathrm {a}} = \left(\ddot {\mathrm {r}} - \mathrm {r} \dot {\theta} ^ {2}\right) \vec {\mathrm {e}} _ {\mathrm {r}} + \left(\mathrm {r} \ddot {\theta} + 2 \dot {\mathrm {r}} \dot {\theta}\right) \vec {\mathrm {e}} _ {\theta}
$$

1.18 

Por lo tanto al vector aceleración de una partícula podremos pensarlo en general, como la suma de una componente radial dada por: 

$$
\vec {\mathrm {a}} _ {\mathrm {r}} = \left(\ddot {\mathrm {r}} - \mathrm {r} \dot {\theta} ^ {2}\right) \vec {\mathrm {e}} _ {\mathrm {r}}
$$

Mas una componente transversal dada por: 

$$
\vec {\mathrm {a}} _ {\theta} = \left(\mathrm {r} \ddot {\theta} + 2 \dot {\mathrm {r}} \dot {\theta}\right) \vec {\mathrm {e}} _ {\theta}
$$

# Componentes Polares de la Ecuación de Newton.

Teniendo en cuenta (1.23) es claro que para aquellas situaciones en las que resulte conveniente expresar al vector aceleración en componentes polares, como las que consideraremos a lo largo de este volumen, la ecuación de Newton en dichas componentes nos quedará expresada como: 

$$
\vec {\mathrm {F}} = \mathrm {m} (\ddot {\mathrm {r}} - \mathrm {r} \dot {\theta} ^ {2}) \vec {\mathrm {e}} _ {\mathrm {r}} + \mathrm {m} (\mathrm {r} \ddot {\theta} + 2 \dot {\mathrm {r}} \dot {\theta}) \vec {\mathrm {e}} _ {\theta}
$$

Que, luego de expresar a la resultante de las fuerzas de interacción en dichas componentes, dará lugar al sistema de ecuaciones escalares: 

$$
\mathrm {F _ {r}} = \mathrm {m} (\ddot {\mathrm {r}} - \mathrm {r} \dot {\theta} ^ {2})
$$

$$
\mathrm {F} _ {\theta} = \mathrm {m} (\mathrm {r} \ddot {\theta} + 2 \dot {\mathrm {r}} \dot {\theta})
$$

Cuya solución nos permitirá contar con una adecuada descripción del movimiento de la partícula o del centro de masa del sistema en consideración. 