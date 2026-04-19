![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/308248ba-016f-4ae6-8c88-ff41316ba17f/07324a19e08131745c95b78990b90a77a711b27d87e6ecbf65c99eb71add34ea.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/308248ba-016f-4ae6-8c88-ff41316ba17f/e9bf6d099abb38c9aa98a26c7e112671f042ac9bb0d289ca9802cd4a5a0fb4be.jpg)


Mecánica Clásica 

Volumen II 

Ochoa 

- 2008 - 

Sistemas de Referencia con Movimiento Relativo General 

ISBN de la Versión Analógica 

987-95038-0-5 

# 2.01 SISTEMAS DE REFERENCIA CON ROTACIÓN RELATIVA.

A lo largo del capítulo anterior se trató el formalismo necesario para describir el movimiento de una partícula (o centro de masa de un sistema) respecto de sistemas de referencia con traslación relativa, en cuyo caso encontramos que los vectores velocidad y aceleración de una partícula, determinados respecto de cada uno de los sistemas en consideración estaban relacionados por: 

$$
\vec {\mathrm {v}} _ {\mathrm {X Y Z}} = \vec {\mathrm {v}} _ {\mathrm {x y z}} + \vec {\mathrm {V}} _ {\mathrm {X Y Z}}
$$

$$
\vec {\mathrm {a}} _ {\mathrm {X Y Z}} = \vec {\mathrm {a}} _ {\mathrm {x y z}} + \vec {\mathrm {A}} _ {\mathrm {X Y Z}}
$$

En lo que continua de éste tema trataremos de obtener relaciones semejantes a las anteriores, válidas cuando el sistema de referencia auxiliar está animado de un movimiento relativo más general. 

Diremos que un sistema de referencia auxiliar (xyz) está animado de una rotación respecto de un segundo sistema de referencia (XYZ) principal, cuando existe un conjunto de puntos pertenecientes al sistema auxiliar, distribuidos a lo largo de una recta, tales que durante el intervalo de tiempo de interés permanecen en reposo respecto del sistema principal. 

La figura sugiere una situación como la indicada. Se trata de un rotor con simetría cilíndrica que se mueve respecto de un sistema de referencia fijo a tierra, de manera que su eje de simetría permanece en reposo respecto del mencionado sistema, formando un cierto ángulo con la dirección vertical. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/308248ba-016f-4ae6-8c88-ff41316ba17f/e682d00e76a94d0004de1a3354c6be5c2ad92febbf4af80ddb50c9480852c50e.jpg)


En adelante identificaremos como eje de rotación del sistema auxiliar, al definido por el conjunto de puntos que durante el intervalo de tiempo de interés, permanece en reposo respecto del sistema de referencia principal. Así, para la situación indicada en la figura anterior, el eje de rotación de un sistema de referencia (xyz) solidario al cuerpo, respecto de un sistema (XYZ) fijo a tierra, coincidirá con el eje de simetría del cuerpo, como se indica en la figura siguiente. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/308248ba-016f-4ae6-8c88-ff41316ba17f/c24909179c5659d4e165f7faaa530a064b4ceb16226990a966b74c1bee6596cf.jpg)


Con el propósito de caracterizar el estado de rotación de un sistema, definiremos su vector velocidad angular como un vector con dirección coincidente con la del eje de rotación, sentido según la regla del tirabuzón y cuyo módulo vendrá expresado por: 

$$
\mathrm {w} = \frac {\mathrm {d} \Omega}{\mathrm {d t}}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/308248ba-016f-4ae6-8c88-ff41316ba17f/8aae809fbb7dc7b1c32899bba3ee29ce3fa17d45aa74f186a357b324e020a3d0.jpg)


Donde, como se sugiere en la figura anterior, $\Omega$ es el ángulo barrido por una recta perpendicular al eje de rotación, durante el intervalo de tiempo en consideración. 

# Derivada Temporal Relativa de una Magnitud Vectorial.

Consideremos a continuación, un sistema de referencia auxiliar (xyz) animado de una rotación, respecto de un sistema de referencia principal (XYZ), caracterizada por un vector velocidad angular (w) al que, por simplicidad y sin que esto implique perder generalidad, podemos pensar coincidente con la dirección del eje (z) del sistema auxiliar, como se sugiere en la figura siguiente, donde se muestra además un vector (A), fijo al mencionado sistema auxiliar. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/308248ba-016f-4ae6-8c88-ff41316ba17f/6f49e4d6938a1faea05d3cd7ed0bb2fb3d49d3995c68ba96324222ded1c0eec9.jpg)


Puesto que A es un vector fijo al sistema (xyz) auxiliar, es claro que sus variaciones temporales observadas desde dicho sistema serán nulas, y por lo tanto también lo será, su derivada temporal calculada desde dicho sistema. Sin embargo y como se sugiere en la figura anterior, sus variaciones temporales, observadas desde el sistema principal no son nulas y por lo tanto tampoco lo será su derivada temporal calculada desde éste último sistema. 

Con el propósito de evaluar las variaciones temporales del vector A desde el sistema principal, o sea, la derivada temporal de dicho vector calculada desde el mencionado sistema, tengamos en cuenta que dicha derivada puede ser expresada como: 

$$
\left. \dot {\vec {\mathrm {A}}} \right| _ {\text {X Y Z}} = \lim  _ {\Delta t \rightarrow 0} \frac {\Delta \vec {\mathrm {A}}}{\Delta t} \Bigg | _ {\text {X Y Z}}
$$

De la figura resulta, que el vector (∆A) evaluado desde el sistema fundamental es tal que: 

$$
\left. \Delta \vec {\mathrm {A}} \right| _ {\mathrm {X Y Z}} \text {e s p a r a l e l o}
$$

Asimismo el módulo de dicho vector puede expresarse como: 

$$
\left| \Delta \vec {\mathrm {A}} \right| _ {\mathrm {X Y Z}} = \rho \Delta \theta = \Delta \theta \mathrm {A} \sec \alpha
$$

De donde, dividiendo por el intervalo de tiempo involucrado, resulta: 

$$
\frac {\left| \Delta \vec {\mathrm {A}} \right|}{\Delta \mathrm {t}} = \frac {\Delta \theta}{\Delta \mathrm {t}} \mathrm {A} \sin \alpha
$$

Tomando límites en ambos miembros, la anterior puede expresarse en términos del módulo del vector velocidad angular que caracteriza la rotación del sistema auxiliar respecto del fundamental. 

$$
\lim  _ {\Delta t \rightarrow 0} \frac {\left| \Delta \vec {\mathrm {A}} \right|}{\Delta t} = \mathrm {w A} \text {s e n} \alpha
$$

Teniendo en cuenta las conclusiones anteriores, es claro entonces que la derivada temporal de un vector fijo al sistema auxiliar (xyz), calculada desde el sistema fundamental (XYZ), respecto del cuál el primer sistema rota con velocidad angular (w), vendrá expresada por: 

$$
\left. \dot {\vec {\mathrm {A}}} \right| _ {\mathrm {X Y Z}} = \vec {\mathrm {w}} \times \vec {\mathrm {A}}
$$

Consideraremos a continuación aquella situación en la que el vector (A) no está fijo al sistema de referencia auxiliar (xyz), en cuyo caso su derivada temporal, calculada desde dicho sistema no será nula y evaluada según las direcciones del mencionado sistema, vendrá dada por: 

$$
\left. \dot {\vec {\mathrm {A}}} \right| _ {\mathrm {x y z}} = \dot {\mathrm {A}} _ {\mathrm {x}} \vec {\mathrm {i}} + \dot {\mathrm {A}} _ {\mathrm {y}} \vec {\mathrm {j}} + \dot {\mathrm {A}} _ {\mathrm {z}} \vec {\mathrm {k}}
$$

Teniendo en cuenta que los vectores unitarios caracterizan direcciones fijas al sistema auxiliar, que rota respecto del fundamental, es obvio que en general estos vectores no caracterizan direcciones fijas a éste último sistema y por lo tanto la derivada vectorial de la magnitud en consideración, calculada desde el sistema principal (XYZ) vendrá expresada por: 

$$
\left. \dot {\vec {\mathrm {A}}} \right| _ {\mathrm {X Y Z}} = \dot {\mathrm {A}} _ {\mathrm {x}} \vec {\mathrm {i}} + \dot {\mathrm {A}} _ {\mathrm {y}} \vec {\mathrm {j}} + \dot {\mathrm {A}} _ {\mathrm {z}} \vec {\mathrm {k}} + \mathrm {A} _ {\mathrm {x}} \dot {\vec {\mathrm {i}}} + \mathrm {A} _ {\mathrm {y}} \dot {\vec {\mathrm {j}}} + \mathrm {A} _ {\mathrm {z}} \dot {\vec {\mathrm {k}}}
$$

Que podemos expresar como: 

$$
\left. \dot {\vec {\mathrm {A}}} \right| _ {\mathrm {X Y Z}} = \left. \dot {\vec {\mathrm {A}}} \right| _ {\mathrm {x y z}} + \mathrm {A} _ {\mathrm {x}} \dot {\vec {\mathrm {i}}} + \mathrm {A} _ {\mathrm {y}} \dot {\vec {\mathrm {j}}} + \mathrm {A} _ {\mathrm {z}} \dot {\vec {\mathrm {k}}}
$$

Puesto que los vectores unitarios son vectores fijos al sistema auxiliar, teniendo en cuenta la conclusión obtenida anteriormente, es claro que: 

$$
\dot {\vec {\mathrm {i}}} = \vec {\mathrm {w}} \times \vec {\mathrm {i}} \qquad \dot {\vec {\mathrm {j}}} = \vec {\mathrm {w}} \times \vec {\mathrm {j}} \qquad \dot {\vec {\mathrm {k}}} = \vec {\mathrm {w}} \times \vec {\mathrm {k}}
$$

Con lo que la derivada temporal de la magnitud en consideración resulta: 

$$
\left. \dot {\vec {\mathrm {A}}} \right| _ {\mathrm {X Y Z}} = \left. \dot {\vec {\mathrm {A}}} \right| _ {\mathrm {x y z}} + \vec {\mathrm {w}} \times \left(\mathrm {A} _ {\mathrm {x}} \vec {\mathrm {i}} + \mathrm {A} _ {\mathrm {y}} \vec {\mathrm {j}} + \mathrm {A} _ {\mathrm {z}} \vec {\mathrm {k}}\right)
$$

Que finalmente puede expresarse como: 

$$
\left. \dot {\vec {\mathrm {A}}} \right| _ {\text {X Y Z}} = \left. \dot {\vec {\mathrm {A}}} \right| _ {\text {x y z}} + \vec {\mathrm {w}} \times \vec {\mathrm {A}}
$$

Que nos relaciona las variaciones temporales de una magnitud vectorial cualquiera calculada desde sistemas de referencia con rotación relativa, de donde podemos observar que la obtenida anteriormente para un vector fijo al sistema auxiliar, es un caso particular de la conseguida recientemente. 

# Vectores Velocidad y Aceleración.

Consideremos una partícula y un sistema de referencia auxiliar (xyz) que se mueve respecto de un sistema de referencia principal (XYZ) de manera que en cada instante su estado de movimiento relativo a éste último sistema está caracterizado mediante las magnitudes w y V sugeridas en la figura que se muestra a continuación. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/308248ba-016f-4ae6-8c88-ff41316ba17f/6580fb6db0eb4cfa698263a0ed87469f505f8082be22797fcf9a8c218ff4c23e.jpg)


Donde el vector (w) nos caracteriza el estado de rotación y el vector $\mathrm { ~ ( ~ \partial ~ \ x y z ) ~ }$ el estado de traslación, del sistema de referencia auxiliar (xyz) respecto del sistema de referencia principal (XYZ), y donde los vectores posición de la partícula respecto de los orígenes de los sistemas involucrados estarán relacionados por: 

$$
\vec {\mathrm {h}} = \vec {\mathrm {R}} + \vec {\mathrm {r}}
$$

Con lo que sus derivadas temporales calculadas desde el sistema de referencia principal estarán relacionadas mediante: 

$$
\left. \dot {\vec {\mathbf {h}}} \right| _ {\mathrm {X Y Z}} = \left. \dot {\vec {\mathbf {R}}} \right| _ {\mathrm {X Y Z}} + \left. \dot {\vec {\mathbf {r}}} \right| _ {\mathrm {X Y Z}}
$$

Donde, el miembro de la izquierda es el vector velocidad de la partícula respecto del sistema principal (XYZ), y el primer término del miembro de la derecha, el vector velocidad del origen del sistema auxiliar (xyz) respecto del sistema de referencia principal (XYZ). En cambio el segundo término de éste último miembro no tiene, en principio, un significado físico concreto, puesto que si bien el vector considerado, es el de la partícula respecto del origen del sistema auxiliar, sus variaciones temporales no están calculadas desde dicho sistema y por lo tanto no es el vector velocidad de la partícula respecto del mencionado sistema como podría haberse pensado en un primer momento, con lo que por ahora: 

$$
\vec {\mathrm {v}} _ {\mathrm {X Y Z}} = \left. \vec {\mathrm {V}} _ {\mathrm {X Y Z}} + \dot {\vec {\mathrm {r}}} \right| _ {\mathrm {X Y Z}}
$$

Teniendo en cuenta la expresión que nos relaciona las variaciones temporales de una magnitud vectorial, respecto de sistemas de referencia con movimiento relativo recientemente obtenida, al término que resta identificar en la anterior se lo puede vincular con su derivada temporal calculada desde el sistema de referencia auxiliar, mediante: 

$$
\left. \dot {\vec {\mathrm {r}}} \right| _ {\mathrm {X Y Z}} = \left. \dot {\vec {\mathrm {r}}} \right| _ {\mathrm {x y z}} + \vec {\mathrm {w}} \times \vec {\mathrm {r}}
$$

Con lo que, los vectores velocidad de la partícula, respecto de cada uno de los sistemas involucrados, estarán relacionados mediante una expresión como la que se muestra a continuación. 

$$
\vec {\mathrm {v}} _ {\mathrm {X Y Z}} = \vec {\mathrm {v}} _ {\mathrm {x y z}} + \vec {\mathrm {V}} _ {\mathrm {X Y Z}} + \vec {\mathrm {w}} \times \vec {\mathrm {r}}
$$

Que en el caso particular de una traslación, se reduce a la obtenida en el tema tratado anteriormente. 

# Vector Aceleración.

Derivando temporalmente la anterior, desde el sistema principal (XYZ) resulta: 

$$
\dot {\vec {\mathrm {v}}} _ {\mathrm {X Y Z}} = \dot {\vec {\mathrm {v}}} _ {\mathrm {x y z}} + \dot {\vec {\mathrm {V}}} _ {\mathrm {X Y Z}} + \dot {\vec {\mathrm {w}}} \times \vec {\mathrm {r}} + \vec {\mathrm {w}} \times \dot {\vec {\mathrm {r}}}
$$

Puesto que, las derivadas están calculadas desde el sistema principal, teniendo en cuenta nuevamente la expresión que nos relaciona las variaciones temporales de una magnitud vectorial respecto de sistemas de referencia con movimiento relativo, de la anterior obtenemos: 

$$
\dot {\vec {\mathrm {v}}} _ {\mathrm {X Y Z}} = \left. \dot {\vec {\mathrm {v}}} _ {\mathrm {x y z}} \right| _ {\mathrm {x y z}} + \vec {\mathrm {w}} \times \vec {\mathrm {v}} _ {\mathrm {x y z}} + \left. \dot {\vec {\mathrm {V}}} _ {\mathrm {X Y Z}} + \dot {\vec {\mathrm {w}}} \times \vec {\mathrm {r}} + \vec {\mathrm {w}} \times \left(\left. \dot {\vec {\mathrm {r}}} \right| _ {\mathrm {x y z}} + \vec {\mathrm {w}} \times \vec {\mathrm {r}}\right) \right.
$$

De donde finalmente, resulta: 

$$
\vec {\mathsf {a}} _ {\mathrm {X Y Z}} = \vec {\mathsf {a}} _ {\mathrm {x y z}} + \vec {\mathsf {A}} _ {\mathrm {X Y Z}} + \vec {\mathsf {w}} \times \vec {\mathsf {w}} \times \vec {\mathsf {r}} + 2 \vec {\mathsf {w}} \times \vec {\mathsf {v}} _ {\mathrm {x y z}} + \dot {\vec {\mathsf {w}}} \times \vec {\mathsf {r}}
$$

Que nos relaciona el vector aceleración de una partícula respecto de sistemas de referencia con movimiento relativo general y que se reduce a la obtenida anteriormente si se consideran sistemas de referencia animados de una traslación relativa, y donde recordemos que la coordenada vectorial involucrada, está determinada respecto del origen del sistema de referencia auxiliar. 

# 2.02 ECUACIÓN DE MOVIMIENTO PARA UN OBSERVADOR NO INERCIAL.

A lo largo de este tema trataremos de obtener la forma general de la ecuación de movimiento para un observador no inercial. Con este propósito consideremos un sistema de referencia (xyz) en movimiento respecto de un sistema de referencia (XYZ) inercial, en cuyo caso la resultante de las fuerzas de interacción a la que está sometida una partícula, estará relacionada con su aceleración determinada respecto del mencionado sistema de referencia (XYZ), mediante: 

$$
\vec {\mathrm {F}} = \mathrm {m} \vec {\mathrm {a}} _ {\mathrm {X Y Z}}
$$

Con lo que, teniendo en cuenta la conclusión obtenida en el tema anterior, dicha magnitud estará relacionada con la aceleración de la partícula determinada respecto del sistema de referencia (xyz), mediante: 

$$
\vec {\mathrm {F}} = \mathrm {m} \vec {\mathrm {a}} _ {\mathrm {x y z}} + \mathrm {m} \vec {\mathrm {A}} _ {\mathrm {X Y Z}} + \mathrm {m} \vec {\mathrm {w}} \times \vec {\mathrm {w}} \times \vec {\mathrm {r}} + 2 \mathrm {m} \vec {\mathrm {w}} \times \vec {\mathrm {v}} _ {\mathrm {x y z}} + \mathrm {m} \dot {\vec {\mathrm {w}}} \times \vec {\mathrm {r}}
$$

Que indudablemente podemos expresar como:  

$$
\vec {\mathrm {F}} + (- \mathrm {m} \vec {\mathrm {A}} _ {\mathrm {X Y Z}}) + (- \mathrm {m} \vec {\mathrm {w}} \times \vec {\mathrm {w}} \times \vec {\mathrm {r}}) + (- 2 \mathrm {m} \vec {\mathrm {w}} \times \vec {\mathrm {v}} _ {\mathrm {x y z}}) + (- \mathrm {m} \dot {\vec {\mathrm {w}}} \times \vec {\mathrm {r}}) = \mathrm {m} \vec {\mathrm {a}} _ {\mathrm {x y z}}
$$

Por lo tanto las aceleraciones observadas en el sistema de referencia auxiliar (xyz), no serán necesariamente consecuencia de la existencia de fuerzas de interacción, ya que de la anterior es claro que aun cuando la resultante de las mismas fuera nula, podríamos observar aceleraciones en la partícula, vinculadas con los restantes términos de la mencionada expresión, a los que en adelante identificaremos como fuerzas inerciales y que a los efectos de simplificar la notación indicaremos como se detalla a continuación: 

<table><tr><td>De Traslación
f_t = -m_AXYZ</td><td>Centrifuga
f_c f = -mvec × w × r</td><td>De Coriolis
f_c = -2mvec × v_xyz</td><td>De Euler
f_e = -mvec × r</td></tr></table>

En término de las cuales la ecuación de movimiento para el observador no inercial nos queda: 

$$
\vec {\mathrm {F}} + \vec {\mathrm {f}} _ {\mathrm {t}} + \vec {\mathrm {f}} _ {\mathrm {c f}} + \vec {\mathrm {f}} _ {\mathrm {c}} + \vec {\mathrm {f}} _ {\mathrm {e}} = \mathrm {m} \vec {\mathrm {a}} _ {\mathrm {x y z}}
$$

Definiendo a la resultante de las fuerzas inerciales, como: 

$$
\vec {\mathrm {f}} = \vec {\mathrm {f}} _ {\mathrm {t}} + \vec {\mathrm {f}} _ {\mathrm {c f}} + \vec {\mathrm {f}} _ {\mathrm {c}} + \vec {\mathrm {f}} _ {\mathrm {e}}
$$

La ecuación de movimiento para el observador no inercial nos queda expresada como: 

$$
\vec {\mathrm {F}} + \vec {\mathrm {f}} = \mathrm {m} \vec {\mathrm {a}} _ {\mathrm {x y z}}
$$

Que indudablemente ofrece un aspecto muy familiar, y donde cabe remarcar que, (F) incluye a la totalidad de las fuerzas que resultan de interacciones, mientras que (f) es la resultante de las fuerzas inerciales, en cuanto a que en ella se incluye la totalidad de los términos inerciales definidos anteriormente, que si bien en el sistema no inercial dan lugar a cambios en el estado de movimiento de la partícula como los que resultarían de la presencia de fuerzas de interacción, estos términos no son fuerzas, puesto que los mismos no están asociados con ningún mecanismo de interacción presente. 

Finalmente es interesante destacar que la fuerza inercial centrífuga tendrá siempre dirección perpendicular al eje de rotación con sentido dirigido hacia fuera del mismo y los efectos de la fuerza inercial de Coriolis se pondrán de manifiesto cuando la partícula se mueve respecto del sistema de referencia no inercial, siendo nulos cuando dicho movimiento es paralelo al eje de rotación y máximos cuando es perpendicular al mismo. 

Como una aplicación de lo considerado, se recomienda ejecutar el video Mareas.dcr que se ofrece en este compacto. 

# 2.03 LA TIERRA COMO UN SISTEMA NO INERCIAL.

Realizando cuidadosas experiencias u observaciones de fenómenos naturales, puede verificarse que en realidad la tierra no es un sistema inercial como lo hemos venido aceptando hasta el momento, aspecto este que podría verificarse mediante cuidadosas experiencias de laboratorio o analizando fenómenos naturales a los que seguramente hemos tenido acceso en alguna oportunidad tales como, la diferente manera en que se encuentran erosionadas las costas de un río, fundamentalmente en aquellos casos en los que la dirección de circulación es de este a oeste, como sucede con las costas del río negro donde puede observarse con claridad el fenómeno mencionado. 

Teniendo en cuenta lo indicado anteriormente y aceptando que un sistema de referencia fijo al sol puede ser considerado como un sistema inercial, es claro entonces que la resultante de las fuerzas de interacción a que se encuentre sometido un cuerpo estará relacionada con el vector aceleración de su centro de masa $\left( \mathsf { a } _ { \mathrm { x y z } } \right)$ determinado respecto de un sistema fijo a la tierra con origen en el centro del planeta, mediante la siguiente ecuación: 

$$
\vec {\mathrm {F}} = \mathrm {m} \vec {\mathrm {a}} _ {\mathrm {x y z}} + \mathrm {m} \vec {\mathrm {A}} _ {\mathrm {X Y Z}} + \mathrm {m} \vec {\mathrm {w}} \times \vec {\mathrm {w}} \times \vec {\mathrm {r}} + 2 \mathrm {m} \vec {\mathrm {w}} \times \vec {\mathrm {v}} _ {\mathrm {x y z}} + \mathrm {m} \dot {\vec {\mathrm {w}}} \times \vec {\mathrm {r}}
$$

Donde (AXYZ) es el vector aceleración del centro de la tierra respecto del sol, como consecuencia de su movimiento orbital respecto de dicha estrella, (w) la velocidad angular con que rota la tierra respecto del sol, (dw/dt) su aceleración angular respecto del mismo sistema (que aunque pequeña, no es nula como consecuencia de que el eje de rotación de la tierra no coincide exactamente con el eje polar y precesiona alrededor de este con un período aproximado a los 370 días) y finalmente $( \mathbf { V } _ { \mathbf { x y z } } )$ la velocidad del centro de masa del cuerpo respecto del sistema de referencia fijo a tierra. 

Teniendo en cuenta los valores de los parámetros que caracterizan el movimiento de la tierra respecto del sol podemos despreciar, frente a los restantes, tanto la aceleración de su centro como su aceleración angular, con lo que la ecuación anterior nos queda: 

$$
\vec {\mathrm {F}} = \mathrm {m} \vec {\mathrm {a}} _ {\mathrm {x y z}} + \mathrm {m} \vec {\mathrm {w}} \times \vec {\mathrm {w}} \times \vec {\mathrm {r}} + 2 \mathrm {m} \vec {\mathrm {w}} \times \vec {\mathrm {v}} _ {\mathrm {x y z}}
$$

Que en adelante emplearemos para el tratamiento de algunas situaciones de interés particular. 

# Peso Aparente de un Cuerpo en el Ecuador

Consideremos a continuación el caso de un cuerpo en reposo respecto del sistema de referencia fijo a tierra y apoyado sobre una balanza en el plano del ecuador, como se sugiere en la figura siguiente, donde se han representado mediante vectores, las fuerzas a que está sometido el cuerpo como consecuencia de su interacción con el campo gravitatorio y con la balanza, cuya lectura será la que reconoceremos como peso aparente del cuerpo en el ecuador y que determinaremos a continuación. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/308248ba-016f-4ae6-8c88-ff41316ba17f/a113f413e5ffac82517bb206ab5e60e00cf6abccb0772e18234ad8695f07597d.jpg)


Con este propósito y teniendo en cuenta que el cuerpo está en reposo respecto del sistema de referencia fijo a tierra, de la anterior nos queda: 

$$
\vec {\mathrm {N}} + \mathrm {m} \vec {\mathrm {g}} = \mathrm {m} \vec {\mathrm {w}} \times \vec {\mathrm {w}} \times \vec {\mathrm {r}}
$$

Evaluando la ecuación anterior según la dirección radial de un sistema de referencia fijo a tierra, obtenemos: 

$$
\mathrm {N} = \mathrm {m g} - \mathrm {m w} ^ {2} \mathrm {R}
$$

Donde (R) es el radio de la tierra y que expresada en términos de su período de rotación resulta: 

$$
\mathrm {N} = \mathrm {m g} - \mathrm {m} \frac {4 \pi^ {2}}{\mathrm {T} ^ {2}} \mathrm {R}
$$

Que dará lugar a un valor inferior al que resulta de la interacción con el campo gravitatorio. 

# Variación del Peso con la Latitud

Consideremos ahora el caso de un cuerpo en un punto de latitud $( \lambda )$ , como el sugerido en la figura lateral, donde representamos a dicho cuerpo en un plano meridiano cualquiera, con lo que la dirección del eje de rotación de la tierra coincidirá con la del eje (y) indicado en la mencionada figura, y donde hemos supuesto la fuerza reactiva (N) según una dirección no necesariamente coincidente con la radial, previendo que esto pueda ser realmente así. 

Teniendo en cuenta que el cuerpo está en reposo respecto del sistema de referencia fijo a tierra, resulta: 

$$
\vec {\mathrm {N}} + \mathrm {m} \vec {\mathrm {g}} = \mathrm {m} \vec {\mathrm {w}} \times \vec {\mathrm {w}} \times \vec {\mathrm {r}}
$$

Que indudablemente podemos expresar como: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/308248ba-016f-4ae6-8c88-ff41316ba17f/165a479511852ca5149e35465b21428253b8850087a1f1d7d123a59a08de73df.jpg)


$$
\vec {\mathrm {N}} = - \mathrm {m} \vec {\mathrm {g}} + \mathrm {m} \vec {\mathrm {w}} \times \vec {\mathrm {w}} \times \vec {\mathrm {r}}
$$

Evaluando las componentes del miembro de la derecha de la expresión anterior según las direcciones de los ejes indicados en la figura resulta: 

$$
\vec {\mathrm {N}} = \mathrm {m g} \left[ \cos (\lambda) \vec {\mathrm {i}} + \mathrm {s e n} (\lambda) \vec {\mathrm {j}} \right] - \mathrm {m w} ^ {2} \mathrm {R} \cos (\lambda) \vec {\mathrm {i}}
$$

Donde nuevamente con (R) indicamos al radio de la tierra y a partir de la cual obtenemos: 

$$
\vec {\mathrm {N}} = \mathrm {m g} \left(1 - \frac {\mathrm {w} ^ {2} \mathrm {R}}{\mathrm {g}}\right) \cos (\lambda) \vec {\mathrm {i}} + \mathrm {m g} \sin (\lambda) \vec {\mathrm {j}}
$$

Lo que nos muestra sin lugar a dudas que en general la fuerza reactiva no coincidirá con la dirección radial, tal como lo habíamos supuesto inicialmente, salvo en aquellos casos particulares que se consideran a continuación. 

Suponiendo al cuerpo en el plano del ecuador, $( \lambda { = } 0 ^ { \circ } )$ en cuyo caso de la anterior resulta: 

$$
\mathrm {N} = \mathrm {m g} - \mathrm {m w} ^ {2} \mathrm {R}
$$

Claramente coincidente con la conclusión obtenida anteriormente. 

Suponiendo ahora al cuerpo en uno de los polos, en cuyo caso la latitud es de $9 0 ^ { \circ }$ 

$$
\mathrm {N} = \mathrm {m g}
$$

Teniendo en cuenta nuevamente la expresión general lograda recientemente para la fuerza reactiva, y definiendo la magnitud: 

$$
\varepsilon = \left(1 - \frac {\mathrm {w} ^ {2} \mathrm {R}}{\mathrm {g}}\right)
$$

Obtenemos que el módulo de dicha fuerza vendrá dado por: 

$$
\mathrm {N} = \mathrm {m g} \left[ \varepsilon^ {2} \cos^ {2} (\lambda) + \mathrm {s e n} ^ {2} (\lambda) \right] ^ {1 / 2}
$$

Que indudablemente podemos identificar como una expresión del peso aparente del cuerpo en función de la latitud del lugar donde se encuentra. 

Finalmente una expresión para el ángulo (β) entre la fuerza reactiva (N) y la dirección de la vertical al punto considerado, puede obtenerse realizando el producto escalar entre el vector que caracteriza a dicha fuerza y el vector opuesto al que nos caracteriza la fuerza que resulta de la interacción con el campo gravitatorio, como se indica a continuación. 

$$
- \vec {\mathrm {N}} \cdot \mathrm {m} \vec {\mathrm {g}} = \mathrm {N m g} \cos (\beta)
$$

De donde: 

$$
\cos (\beta) = - \frac {\vec {N} \cdot m \vec {g}}{N m g}
$$

Que teniendo en cuenta las conclusiones anteriores y luego de realizar las operaciones correspondientes, nos proporcionará una expresión para la mencionada magnitud angular, en función de la latitud del punto considerado. Siendo interesante destacar que el ángulo al que estamos haciendo referencia sería también el ángulo entre la cuerda que sujete una plomada y la vertical al punto considerado. 

# Desviación de Coriolis

Como otra aplicación del tema que estamos tratando consideraremos a continuación el caso de un cuerpo que se deja caer desde una cierta altura de la superficie de la tierra, en cuyo caso demostraremos que, como consecuencia de que la tierra es un sistema de referencia no inercial, la trayectoria a lo largo de la que se desplazará el cuerpo, respecto del mencionado sistema, no coincidirá con la vertical al punto considerado. 

Con este propósito y tal como lo mencionáramos anteriormente pensemos en un cuerpo que se deja caer desde el reposo y desde un punto situado a una altura (H) de la superficie de la tierra, como se sugiere en la figura siguiente, en cuyo caso despreciando la fuerza que pudiera resultar de la interacción con la atmósfera, la ecuación de movimiento planteada respecto del sistema de referencia no inercial fijo a tierra nos queda: 

$$
\mathrm {m} \vec {\mathrm {g}} = \mathrm {m} \vec {\mathrm {a}} _ {\mathrm {x y z}} + \mathrm {m} \vec {\mathrm {w}} \times \vec {\mathrm {w}} \times \vec {\mathrm {r}} + 2 \mathrm {m} \vec {\mathrm {w}} \times \vec {\mathrm {v}} _ {\mathrm {x y z}}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/308248ba-016f-4ae6-8c88-ff41316ba17f/c4ca58bdb9bc0fc0342c59e0cccfb7d63ef4d2ef14025b4ed9b66b471d6007ef.jpg)


Despreciando el término dependiente del cuadrado de la velocidad angular, resulta: 

$$
\mathrm {m} \vec {\mathrm {g}} = \mathrm {m} \vec {\mathrm {a}} _ {\mathrm {x y z}} + 2 \mathrm {m} \vec {\mathrm {w}} \times \vec {\mathrm {v}} _ {\mathrm {x y z}}
$$

De donde: 

$$
\mathrm {m} \vec {\mathrm {a}} _ {\mathrm {x y z}} = \mathrm {m} \vec {\mathrm {g}} - 2 \mathrm {m} \vec {\mathrm {w}} \times \vec {\mathrm {v}} _ {\mathrm {x y z}}
$$

Evaluando las componentes de esta ecuación según las direcciones cartesianas indicadas en la figura anterior y previendo que la dirección del vector velocidad del centro de masa pueda no coincidir con la dirección vertical, en cuyo caso sus componentes según las direcciones de los ejes (y,z) no serían necesariamente nulas, de la anterior obtenemos el siguiente sistema de ecuaciones diferenciales: 

$$
\ddot {\mathbf {x}} = - \mathbf {g} - 2 \mathbf {w} \dot {\mathbf {z}} \cos \lambda
$$

$$
\ddot {\mathrm {y}} = 2 \mathrm {w} \dot {\mathrm {z}} \mathrm {s e n} \lambda
$$

$$
\ddot {z} = 2 w \dot {x} \cos \lambda - 2 w \dot {y} s e n \lambda
$$

De la primera resulta: 

$$
\mathrm {d} \dot {\mathrm {x}} = - \mathrm {g} \mathrm {d t} - 2 \mathrm {w} \cos \lambda \mathrm {d z}
$$

Integrando ambos miembros de esta ecuación y teniendo en cuenta que en el instante inicial la velocidad de la partícula es nula al igual que su coordenada según la dirección del eje z, esto es la dirección perpendicular al plano meridiano representado en la figura, obtenemos: 

$$
\dot {\mathrm {x}} = - \mathrm {g t} - 2 \mathrm {w z} \cos \lambda
$$

Análogamente diferenciando la segunda y teniendo en cuenta las condiciones iniciales indicadas en el párrafo anterior, luego de integrar en ambos miembros, resulta: 

$$
\dot {\mathrm {y}} = 2 \mathrm {w z} \mathrm {s e n} \lambda
$$

Teniendo en cuenta estas dos últimas expresiones en la tercera ecuación de nuestro sistema original, la componente del vector aceleración según la dirección (z) nos queda: 

$$
\ddot {z} = 2 \mathrm {w g t} \cos \lambda - 4 \mathrm {w} ^ {2} z
$$

Despreciando el término en el cuadrado de la velocidad angular, resulta: 

$$
\ddot {z} = 2 \mathrm {w g t} \cos \lambda
$$

Diferenciando, luego integrando en ambos miembros y teniendo en cuenta las condiciones iniciales correspondientes a la situación en consideración, de la anterior obtenemos que: 

$$
\dot {\mathrm {z}} = - \mathrm {w g t} ^ {2} \cos \lambda
$$

De donde, diferenciando e integrando nuevamente, resulta: 

$$
z = - \frac {1}{3} w g t ^ {3} \cos \lambda
$$

Lo que claramente nos muestra una desviación, respecto de la dirección vertical, hacia valores negativos de la coordenada (z), esto es, en el sentido de rotación de la tierra, siendo interesante destacar que esta desviación será nula en el polo y máxima en el ecuador. 

# 2.04 PRESIÓN EN EL INTERIOR DE UN FLUIDO

# En Equilibrio Respecto de un Sistema No Inercial con Traslación Relativa.

Supongamos ahora que el fluido se encuentra en equilibrio respecto de un sistema de referencia que, como se sugiere en la figura siguiente, es sometido a una aceleración constante respecto de un sistema de referencia inercial, en cuyo caso la ecuación de movimiento o ecuación de Newton para el centro de masa del elemento de volumen considerado resulta: 

$$
\vec {\mathrm {E}} + \mathrm {m} \vec {\mathrm {g}} = \mathrm {m} \vec {\mathrm {A}}
$$

Que expresada por unidad de volumen, nos queda: 

$$
- \nabla p + \rho \vec {g} = \rho \vec {A}
$$

De donde: 

$$
\nabla \mathsf {p} = \rho \vec {\mathsf {g}} - \rho \vec {\mathsf {A}}
$$

Por lo tanto la presión en el interior del fluido será tal que: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/308248ba-016f-4ae6-8c88-ff41316ba17f/d5a4583292250b6b7d5bb8d07985ad900fb57ef5fad3ee3b75681b4169a85f1b.jpg)


$$
\frac {\partial p}{\partial x} = 0
$$

$$
\frac {\partial \mathrm {p}}{\partial \mathrm {y}} = - \rho \mathrm {A}
$$

$$
\frac {\partial \mathrm {p}}{\partial \mathrm {z}} = - \rho \mathrm {g}
$$

Con lo que, la presión en el interior del fluido no dependerá de la coordenada (x) y su diferencial vendrá expresado por: 

$$
\mathrm {d p} = - \rho \mathrm {A d y} - \rho \mathrm {g d z}
$$

De donde, luego de integrar ambos miembros entre límites compatibles, la presión en el interior del fluido nos queda expresada como: 

$$
\mathrm {p} (\mathrm {x z}) = \mathrm {p} _ {\circ} + \rho \mathrm {A} (\mathrm {y} _ {\circ} - \mathrm {y}) + \rho \mathrm {g} (\mathrm {z} _ {\circ} - \mathrm {z})
$$

Donde $\left( \mathfrak { p } _ { \mathfrak { o } } \right)$ es la presión en un punto del fluido de coordenadas $\left( \mathrm { y } _ { \mathrm { o } } , \mathrm { Z } _ { \mathrm { 0 } } \right)$ , y por lo tanto el valor de la misma se incrementará con la profundidad y en el sentido opuesto al sentido en que se acelera el sistema, o sea en el sentido en que decrecen las coordenadas (y,z) involucradas en la expresión anterior. 

Teniendo en cuenta esta conclusión resulta que, en esta oportunidad las superficies de igual presión corresponderán a planos tales que sus proyecciones sobre el plano (z,y) nos darán rectas oblicuas como las indicadas en la figura siguiente, cuya ecuación para diferentes valores de la presión, considerada como parámetro, podemos obtener a partir de la anterior, resultando: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/308248ba-016f-4ae6-8c88-ff41316ba17f/eb5e50c058e07d4f5ee84d3e34fb94a8cc23cfe5091cff86bb1c47c90bebbcd4.jpg)


$$
z (y) = - \frac {A}{g} y + b (p)
$$

Donde la ordenada al origen viene dada por: 

$$
\mathrm {b} (\mathrm {p}) = \mathrm {z} _ {\circ} + \frac {\mathrm {A}}{\mathrm {g}} \mathrm {y} _ {\circ} + \frac {\mathrm {p} _ {\circ} - \mathrm {p}}{\rho \mathrm {g}}
$$

Expresiones de las que obtenemos las siguientes conclusiones: 

Una ordenada al origen que disminuye con la presión, se incrementa con la aceleración del sistema y que en particular cuando ${ \mathfrak { p } } = { \mathfrak { p } } _ { \mathfrak { o } }$ toma el valor: 

$$
\mathbf {b} _ {\circ} = \mathbf {z} _ {\circ} + \frac {\mathbf {A}}{\mathbf {g}} \mathbf {y} _ {\circ}
$$

 Una pendiente, o sea, un ángulo con la horizontal dado por: 

$$
\operatorname {t g} (\alpha) = - \frac {\mathrm {A}}{\mathrm {g}}
$$

Que se incrementa con la aceleración del sistema. 

Conclusiones que eran de esperar si pensamos en lo que sucedería al acelerar horizontalmente un recipiente con agua. En este caso observaríamos que la superficie libre del fluido, esto es, aquella en contacto con la atmósfera y por lo tanto a la presión atmosférica $\left( \mathfrak { p } _ { \mathfrak { o } } \right)$ , la integran puntos que se distribuyen a lo largo de un plano oblicuo al plano horizontal con las características mencionadas anteriormente, por lo que deberíamos evitar aceleración importantes si deseamos evitar que se rebalse el fluido por la cara opuesta al sentido en que se acelera el recipiente. 

Resulta oportuno mencionar que teniendo en cuenta el principio de equivalencia podríamos haber alcanzado conclusiones similares a las obtenidas recientemente, ya que en virtud de dicho principio es imposible diferenciar entre los efectos dinámicos consecuencia de un campo gravitatorio y los que resultan asociados a un campo de fuerza inercial. Efectivamente en este caso el fluido se verá sometido a un campo de fuerza inercial en el sentido opuesto al sentido en que se acelera el sistema, por lo tanto si ante la presencia de un campo gravitatorio obtuvimos un incremento de la presión con la profundidad, esto es en el sentido en que está dirigida la fuerza gravitatoria, ante la presencia de un campo de fuerza inercial debemos esperar un incremento de la presión en el sentido en que está dirigido el mencionado campo de fuerza inercial o sea en sentido opuesto al sentido en que se acelera el sistema. 

# Empuje Inercial.

Consideremos ahora el caso de un cuerpo de densidad $( \rho _ { \mathrm { c } } )$ en el interior de un fluido de densidad (ρ), en equilibrio respecto de un sistema de referencia no inercial que se acelera horizontalmente respecto de un sistema inercial, como se sugiere en la figura siguiente, donde hemos supuesto al cuerpo como un cubo cuya proyección sobre el plano (z,y) es la que hemos representado. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/308248ba-016f-4ae6-8c88-ff41316ba17f/8f6d218a19c72fd0bdd0a63be5cfde655944cfa2c00f79feb5bcb34b264630bb.jpg)


En este caso y teniendo en cuenta las conclusiones anteriores así como que en general el empuje por unidad de volumen venía dado por el gradiente de la presión en el interior del fluido, el cuerpo se verá sometido a un empuje por unidad de volumen dado por: 

$$
\vec {\mathrm {e}} = \rho \mathrm {A} \vec {\mathrm {j}} + \rho \mathrm {g} \vec {\mathrm {k}}
$$

Multiplicando ambos miembros de la anterior por el volumen del cuerpo sumergido resulta que el empuje a que se verá sometido el cuerpo vendrá dado por: 

$$
\vec {\mathrm {E}} = \rho \mathrm {V} _ {\mathrm {c}} \mathrm {A} \vec {\mathrm {j}} + \rho \mathrm {V} _ {\mathrm {c}} \mathrm {g} \vec {\mathrm {k}}
$$

Donde resulta importante observar que en este caso el empuje a que se verá sometido el cuerpo tendrá una componente adicional, en la dirección y sentido en que se acelera el sistema, que indudablemente podemos asociar con la presencia de la fuerza no inercial existente en el sistema respecto del cual el fluido está en equilibrio, que por lo tanto identificaremos como empuje inercial. 

Teniendo en cuenta que nos encontramos en un sistema de referencia no inercial, el vector aceleración del centro de masa del cuerpo respecto de dicho sistema estará relacionado con las fuerzas de interacción mediante: 

$$
\vec {\mathrm {E}} + \mathrm {m} _ {\mathrm {c}} \vec {\mathrm {g}} = \mathrm {m} _ {\mathrm {c}} \vec {\mathrm {a}} + \mathrm {m} _ {\mathrm {c}} \vec {\mathrm {A}}
$$

De donde, procediendo de manera semejante al caso anterior, o sea teniendo en cuenta la expresión obtenida para el empuje y dividiendo ambos miembros de la anterior por el volumen del cuerpo sumergido, resulta que la aceleración del cuerpo respecto del sistema de referencia no inercial vendrá dada por: 

$$
\vec {a} = \left(\frac {\rho}{\rho_ {\mathrm {c}}} - 1\right) \mathrm {A} \vec {\mathrm {j}} + \left(\frac {\rho}{\rho_ {\mathrm {c}}} - 1\right) \mathrm {g} \vec {\mathrm {k}}
$$

De la que obtenemos las situaciones particulares que se indican a continuación según sea la relación entre las densidades del fluido y del cuerpo en consideración: 

Suponiendo que la densidad del cuerpo es menor que la del fluido: 

$$
\vec {a} = \left(\frac {\rho}{\rho_ {\mathrm {c}}} - 1\right) \mathrm {A} \vec {\mathrm {j}} + \left(\frac {\rho}{\rho_ {\mathrm {c}}} - 1\right) \mathrm {g} \vec {\mathrm {k}}
$$

El vector aceleración del centro de masa del cuerpo tendrá componentes en el sentido de ambos vectores unitarios o sea verticalmente hacia arriba y horizontalmente en el sentido en que se acelera el sistema, de manera que la dirección de dicha magnitud tendrá una pendiente dada por: 

$$
\operatorname {t g} (\beta) = \frac {\mathrm {g}}{\mathrm {A}}
$$

Por lo tanto, el cuerpo se acelera en una dirección perpendicular a las superficies de igual presión, como se sugiere en la figura siguiente. 

Suponiendo ahora que la densidad del cuerpo es igual que la del fluido: 

$$
\vec {a} = 0
$$

El cuerpo permanece en equilibrio respecto del sistema no inercial 

Finalmente, suponiendo que la densidad del cuerpo es mayor que la del fluido: 

$$
\vec {a} = - \left(1 - \frac {\rho}{\rho_ {\mathrm {c}}}\right) A \vec {j} - \left(1 - \frac {\rho}{\rho_ {\mathrm {c}}}\right) g \vec {k}
$$

Con lo que, las componentes del vector aceleración del centro de masa del cuerpo tendrán ambas sentido opuesto al de los vectores unitarios o sea el mismo sentido que el de la fuerza gravitatoria y el de la fuerza inercial, como se muestra en la figura lateral, de manera que nuevamente, la dirección de dicha magnitud tendrá una pendiente dada por: 

$$
\operatorname {t g} (\beta) = \frac {\mathrm {g}}{\mathrm {A}}
$$

Por lo tanto, la dirección del vector aceleración será nuevamente perpendicular a las superficies de igual presión, pero con sentido opuesto al primer caso considerado. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/308248ba-016f-4ae6-8c88-ff41316ba17f/919f133654b37a10627fb686eef6fc9df0dcd22e8de0d6efd43d763dbf42500c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/308248ba-016f-4ae6-8c88-ff41316ba17f/1e50230200a180371869a3083a45731533e97981b0e30580c0464ab7e5eee08a.jpg)


# 1.05 PRESIÓN EN EL INTERIOR DE UN FLUIDO.

# En Equilibrio Respecto de un Sistema No Inercial en Rotación.

Consideremos ahora un fluido en equilibrio respecto de un sistema de referencia que, como se sugiere en la figura siguiente, rota con una velocidad angular constante respecto de un sistema de referencia inercial, con lo que, la ecuación de movimiento para el centro de masa del elemento de volumen considerado vendrá dada por: 

$$
\vec {\mathrm {E}} + \mathrm {m} \vec {\mathrm {g}} = \mathrm {m} \vec {\mathrm {w}} \times \vec {\mathrm {w}} \times \vec {\mathrm {r}}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/308248ba-016f-4ae6-8c88-ff41316ba17f/28d6d608cb6bd1e01bbb619b831000f75e4df69f1daf080205c873d9daff8329.jpg)


Que expresada por unidad de volumen, nos queda: 

$$
- \nabla p + \rho \vec {g} = \rho \vec {w} \times \vec {w} \times \vec {r}
$$

De donde: 

$$
\nabla \mathrm {p} = \rho \vec {\mathrm {g}} - \rho \vec {\mathrm {w}} \times \vec {\mathrm {w}} \times \vec {\mathrm {r}}
$$

Que luego de evaluar en componentes cilíndricas nos proporciona las siguientes ecuaciones escalares. 

$$
\frac {\partial \mathrm {p}}{\partial \mathrm {R}} = \rho \mathrm {w} ^ {2} \mathrm {R} \quad \frac {\partial \mathrm {p}}{\partial \theta} = 0 \quad \frac {\partial \mathrm {p}}{\partial z} = - \rho \mathrm {g}
$$

Por lo tanto la presión en el interior del fluido no dependerá de la coordenada angular y su dependencia de las restantes coordenadas será tal que el diferencial de dicha función vendrá dado por: 

$$
\mathrm {d p} = \rho \mathrm {w} ^ {2} \mathrm {R} \mathrm {d R} - \rho \mathrm {g} \mathrm {d z}
$$

De donde, luego de integrar ambos miembros entre límites compatibles, resulta: 

$$
p (R, z) = p _ {\circ} + \frac {1}{2} \rho w ^ {2} \left(R ^ {2} - R _ {\circ} ^ {2}\right) - \rho g (z - z _ {\circ})
$$

Siendo ${ \mathfrak { p } } _ { \mathfrak { o } }$ la presión en un punto del fluido con coordenadas $\scriptstyle ( \mathrm { { R } } _ { 0 } , \mathrm { { Z } } _ { 0 } )$ , con lo que, la presión en el interior del fluido se incrementara con la coordenada radial y la profundidad del punto, resultando que las superficies de igual presión serán paraboloides de revolución cuyo eje de simetría coincidirá con la dirección del eje de rotación del sistema y tales que sus proyecciones sobre el plano definido por el vector velocidad angular y el vector posición del punto considerado darán lugar a parábolas cuyas expresiones formales en términos de la presión, considerada como parámetro, vendrán dadas por: 

$$
z = b (p) + \frac {w ^ {2}}{2 g} R ^ {2}
$$

Donde: 

$$
\mathrm {b} (\mathrm {p}) = \mathrm {z} _ {\circ} - \frac {\mathrm {w} ^ {2}}{2 \mathrm {g}} \mathrm {R} _ {\circ} ^ {2} - \frac {\mathrm {p} - \mathrm {p} _ {\circ}}{\rho \mathrm {g}}
$$

Cuyas gráficas cualitativas se sugieren en la figura lateral. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/308248ba-016f-4ae6-8c88-ff41316ba17f/2d8c123f079b3f3104f479455479c2600cb18dc66d30145ef4120a86a06ab772.jpg)


Con lo que, el empuje sobre un cuerpo sumergido vendrá dado por: 

$$
\vec {\mathrm {E}} = - \rho \mathrm {V} _ {\mathrm {c}} \mathrm {w} ^ {2} \mathrm {R} \vec {\mathrm {e}} _ {\mathrm {R}} + \rho \mathrm {V} _ {\mathrm {c}} \mathrm {g} \vec {\mathrm {k}}
$$

Donde ( e R ) es un vector unitario perpendicular al eje de rotación y dirigido radialmente hacia afuera, y el cuerpo sumergido se verá sometido a un empuje como el que se representa cualitativamente en la figura lateral (notar que su componente radial tiene sentido opuesto al vector unitario indicado anteriormente, esto es sentido opuesto a la fuerza inercial centrífuga que sabemos está dirigida radialmente hacia fuera del eje de rotación). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/308248ba-016f-4ae6-8c88-ff41316ba17f/9addd4a10e3010c8d060b7bfcba01ddd4621a67c501b5e8f1ead20401986b8f1.jpg)


Puesto que nos encontramos en un sistema de referencia no inercial en rotación, y suponiendo al cuerpo en reposo respecto de dicho sistema (con lo que el término asociado con la fuerza de Coriolis es nulo) el vector aceleración del centro de masa del cuerpo respecto del mencionado sistema estará relacionado con las fuerzas de interacción mediante: 

$$
\vec {\mathrm {E}} + \mathrm {m} _ {\mathrm {c}} \vec {\mathrm {g}} = \mathrm {m} _ {\mathrm {c}} \vec {\mathrm {a}} + \mathrm {m} _ {\mathrm {c}} \vec {\mathrm {w}} \times \vec {\mathrm {w}} \times \vec {\mathrm {r}}
$$

Teniendo en cuenta la expresión obtenida para el empuje a que se verá sometido el cuerpo y dividiendo ambos miembros de la anterior por el volumen de dicho cuerpo, resulta: 

$$
- \rho w ^ {2} R \vec {e} _ {R} + \rho g \vec {k} + \rho_ {c} g \vec {k} = \rho_ {c} \vec {a} - \rho_ {c} w ^ {2} R \vec {e} _ {R}
$$

Con lo que, luego de dividir ambos miembros por la densidad del cuerpo, obtenemos que el vector aceleración de su centro de masa, respecto del sistema no inercial en rotación, vendrá expresado por: 

$$
\vec {a} = \left(\frac {\rho}{\rho_ {\mathrm {c}}} - 1\right) \mathrm {g} \vec {\mathrm {k}} - \left(\frac {\rho}{\rho_ {\mathrm {c}}} - 1\right) \mathrm {w} ^ {2} \mathrm {R} \vec {\mathrm {e}} _ {\mathrm {R}}
$$

De donde obtenemos las situaciones particulares que se indican a continuación según sea la relación entre las densidades del fluido y del cuerpo en consideración. 

Suponiendo que la densidad del cuerpo es menor que la del fluido: 

$$
\vec {a} = \left(\frac {\rho}{\rho_ {\mathrm {c}}} - 1\right) \mathrm {g} \vec {\mathrm {k}} - \left(\frac {\rho}{\rho_ {\mathrm {c}}} - 1\right) \mathrm {w} ^ {2} \mathrm {R} \vec {\mathrm {e}} _ {\mathrm {R}}
$$

Por lo tanto la componente vertical tendrá sentido opuesto a la fuerza gravitatoria y la componente radial, la dirección y sentido indicado en la figura lateral, o sea hacia el eje de rotación. 

Lo indicado anteriormente nos permite explicar el motivo por el que, al hacer girar un fluido en el que se encuentran burbujas, estas se desplazarán hacia el eje de rotación agrupándose alrededor del mismo. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-05/308248ba-016f-4ae6-8c88-ff41316ba17f/aeae218decc255141316d05539efa7dd4aba6862a522e5c44971a9baef86f52f.jpg)


Suponiendo ahora que la densidad del cuerpo es igual que la del fluido: 

$$
\vec {a} = 0
$$

El cuerpo permanece en equilibrio respecto del sistema no inercial en rotación y finalmente, suponiendo que la densidad del cuerpo es mayor que la del fluido: 

$$
\vec {a} = - \left(1 - \frac {\rho}{\rho_ {\mathrm {c}}}\right) \mathrm {g} \vec {\mathrm {k}} + \left(1 - \frac {\rho}{\rho_ {\mathrm {c}}}\right) \mathrm {w} ^ {2} \mathrm {R} \vec {\mathrm {e}} _ {\mathrm {R}}
$$

De donde resulta que, en este caso, la componente vertical tendrá el sentido de la fuerza gravitatoria y la componente radial estará dirigida hacia afuera del eje de rotación, o sea en el sentido de la fuerza inercial centrífuga. 