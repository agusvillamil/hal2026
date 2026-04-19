Mecánica Clásica 

Volumen II 

Ochoa 

- 2008 - 

Dinámica General para Sistemas Rígidos 

ISBN de la Versión Analógica 

987-95038-0-5 

# 7.1 CAMPO DE VELOCIDADES Y ACELERACIONES

Considerando un sistema de referencia (x’y’z’) que rota con una velocidad angular $\mathbf { W } _ { 1 }$ respecto de un sistema (xyz), que a su vez rota con velocidad angular $\cdot$ respecto de un tercer sistema (XYZ), alrededor de un eje concurrente con la anterior, como se sugiere en la figura siguiente, el vector velocidad de una partícula respecto de cada uno de los sistemas involucrados vendrá dado por: 

$$
\vec {\mathrm {v}} _ {\mathrm {x y z}} = \vec {\mathrm {v}} _ {\mathrm {x ^ {'} y ^ {'} z ^ {'}}} + \vec {\mathrm {w}} _ {1} \times \vec {\mathrm {r}}
$$

$$
\vec {\mathrm {v}} _ {\mathrm {X Y Z}} = \vec {\mathrm {v}} _ {\mathrm {x y z}} + \vec {\mathrm {w}} _ {2} \times \vec {\mathrm {r}}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/4c88ff2b-823b-4324-b438-3cd0eb86a198/06cc7366c12f38b21a1c2d5fde9f7b0eb3dd40d8ea0e7bf2ab0b10d7dfb97891.jpg)


Teniendo en cuenta la primera relación en la segunda, obtenemos que el vector velocidad de la partícula respecto del sistema (XYZ) puede ser expresado como: 

$$
\vec {\mathrm {v}} _ {\mathrm {X Y Z}} = \vec {\mathrm {v}} _ {\mathrm {x ^ {'} y ^ {'} z ^ {'}}} + (\vec {\mathrm {w}} _ {1} + \vec {\mathrm {w}} _ {2}) \times \vec {\mathrm {r}}
$$

De donde resulta que la rotación del sistema $\bf ( x y ^ { \prime } z ^ { \prime } )$ respecto del sistema (XYZ) estará caracterizada por un vector W dado por: 

$$
\vec {\bf w} = \vec {\bf w} _ {1} + \vec {\bf w} _ {2}
$$

Suponiendo que el punto considerado fuera un punto perteneciente al primer sistema, de la anterior es claro que su velocidad respecto del tercer sistema vendrá dada por: 

$$
\vec {\mathrm {v}} _ {\mathrm {X Y Z}} = (\vec {\mathrm {w}} _ {1} + \vec {\mathrm {w}} _ {2}) \times \vec {\mathrm {r}}
$$

Por lo tanto estamos en condiciones de afirmar que al considerar un rígido que rota con una velocidad angular $\mathbf { W } _ { 1 }$ respecto de un sistema que rota con una velocidad angular $\cdot$ concurrente con la anterior, respecto de otro sistema de referencia, entonces el vector que caracteriza la rotación del cuerpo respecto de este último sistema vendrá dado por la suma vectorial de los anteriores, como se lo indicó anteriormente, con lo que, respecto de este último sistema, el cuerpo rotará alrededor de un eje paralelo al definido por el vector W que se muestra en la figura siguiente. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/4c88ff2b-823b-4324-b438-3cd0eb86a198/1e28c3c21cc51627ccd825d77d708088643bf6e4743dc95aaafa97419ab6a84d.jpg)


Resulta importante observar que, aun cuando las velocidades angulares 1 y 2 fueran constantes, la dirección del vector que nos caracteriza la rotación del cuerpo respecto del sistema (XYZ), no permanecerá constante respecto de dicho sistema y generará un cono en el espacio asociado con el mencionado sistema, como el sugerido en la figura anterior, donde, como lo mencionáramos, se a supuesto constante el módulo de las velocidades angulares involucradas. Teniendo en cuenta lo indicado, es claro que la dirección del vector que caracteriza la rotación del cuerpo cambiará en el tiempo y por lo tanto el movimiento del cuerpo ya no podrá ser considerado como un movimiento plano. Lo manifestado nos indica que aún cuando los módulos de las velocidades angulares permanecieran constante, el vector aceleración angular del cuerpo respecto del sistema (XYZ) no será nulo y en general vendrá dado por: 

$$
\left. \dot {\vec {\mathrm {w}}} \right| _ {\mathrm {X Y Z}} = \left. \dot {\vec {\mathrm {w}}} _ {1} \right| _ {\mathrm {X Y Z}} + \left. \dot {\vec {\mathrm {w}}} _ {2} \right| _ {\mathrm {X Y Z}}
$$

$$
\vec {\alpha} = \vec {\alpha} _ {1} + \vec {\alpha} _ {2} + (\vec {\mathrm {w}} _ {2} \times \vec {\mathrm {w}} _ {1})
$$

Por lo tanto aún cuando los módulos de las velocidades angulares involucradas no cambien en el tiempo, la aceleración angular respecto del sistema principal no será nula y vendrá dada por: 

$$
\vec {\alpha} = \vec {\mathrm {w}} _ {2} \times \vec {\mathrm {w}} _ {1}
$$

# 7.2 VECTOR MOMENTO ANGULAR.

A lo largo del capítulo anterior se obtuvo que en general, al vector momento angular de un cuerpo respecto del origen de un sistema de referencia (XYZ) podíamos expresarlo como: 

$$
\vec {\mathrm {L}} = \vec {\mathrm {r}} _ {\mathrm {c}} \times \mathrm {m} \vec {\mathrm {v}} _ {\mathrm {c}} + \vec {\mathrm {L}} _ {\mathrm {c}}
$$

Donde la componente respecto del centro de masa venía dada por: 

$$
\vec {L} _ {\mathrm {c}} = \sum \mathrm {m} _ {\mathrm {i}} \left[ \vec {\mathrm {w r}} _ {\mathrm {i}} ^ {2} - \vec {\mathrm {r}} _ {\mathrm {i}} (\vec {\mathrm {w}} \cdot \vec {\mathrm {r}} _ {\mathrm {i}}) \right]
$$

Done la coordenada vectorial de las partículas está determinada respecto del centro de masa. 

Evaluando la anterior según las direcciones de un sistema (xyz) solidario al cuerpo y con origen en su centro de masa resulta que, en general, las componentes del vector momento angular según las direcciones mencionadas vendrán dadas por: 

$$
L _ {c x} = \left\lfloor \sum m _ {i} \left(y _ {i} ^ {2} + z _ {i} ^ {2}\right) \right\rfloor w _ {x} + \left[ - \sum m _ {i} x _ {i} y _ {i} \right] w _ {y} + \left[ - \sum m _ {i} x _ {i} z _ {i} \right] w _ {z}
$$

$$
L _ {c y} = \left[ - \sum m _ {i} y _ {i} x _ {i} \right] w _ {x} + \left\lfloor \sum m _ {i} \left(x _ {i} ^ {2} + z _ {i} ^ {2}\right) \right\rfloor w _ {y} + \left[ - \sum m _ {i} y _ {i} z _ {i} \right] w _ {z}
$$

$$
L _ {c z} = \left[ - \sum m _ {i} z _ {i} x _ {i} \right] w _ {x} + \left[ - \sum m _ {i} z _ {i} y _ {i} \right] w _ {y} + \left\lfloor \sum m _ {i} \left(x _ {i} ^ {2} + y _ {i} ^ {2}\right) \right\rfloor w _ {z}
$$

Donde las componentes del vector velocidad angular, que caracteriza la rotación del cuerpo, están evaluadas según las direcciones del sistema solidario mencionado en el párrafo anterior y donde las coordenadas involucradas son las de cada una de las partículas según las direcciones del sistema solidario indicado anteriormente, con lo que los corchetes incluidos resultan ser invariantes temporales, que en adelante designaremos como coeficientes de inercia, diferenciándolos entre ellos como se indica a continuación. 

# Productos de Inercia

$$
I _ {x y} = I _ {y x} = - \sum m _ {i} x _ {i} y _ {i}
$$

$$
I _ {x z} = I _ {z x} = - \sum m _ {i} x _ {i} z _ {i}
$$

$$
I _ {y z} = I _ {z y} = - \sum m _ {i} y _ {i} z _ {i}
$$

# Momentos de Inercia

Respecto del Eje x 

$$
I _ {x x} = \left\lfloor \sum m _ {i} \left(y _ {i} ^ {2} + z _ {i} ^ {2}\right) \right] = \sum m _ {i} D _ {i x} ^ {2}
$$

Respecto del Eje y 

$$
I _ {y y} = \left[ \sum m _ {i} \left(x _ {i} ^ {2} + z _ {i} ^ {2}\right) \right] = \sum m _ {i} D _ {i y} ^ {2}
$$

Respecto del Eje z 

$$
I _ {z z} = \left\lfloor \sum m _ {i} \left(x _ {i} ^ {2} + y _ {i} ^ {2}\right) \right\rfloor = \sum m _ {i} D _ {i z} ^ {2}
$$

Con lo que las componentes solidarias del vector momento angular respecto del centro de masa del cuerpo pueden expresarse como. 

$$
\mathrm {L} _ {\mathrm {c x}} = \mathrm {I} _ {\mathrm {x x}} \mathrm {w} _ {\mathrm {x}} + \mathrm {I} _ {\mathrm {x y}} \mathrm {w} _ {\mathrm {y}} + \mathrm {I} _ {\mathrm {x z}} \mathrm {w} _ {\mathrm {z}}
$$

$$
\mathrm {L} _ {\mathrm {c y}} = \mathrm {I} _ {\mathrm {y x}} \mathrm {w} _ {\mathrm {x}} + \mathrm {I} _ {\mathrm {y y}} \mathrm {w} _ {\mathrm {y}} + \mathrm {I} _ {\mathrm {y z}} \mathrm {w} _ {\mathrm {z}}
$$

$$
\mathrm {L} _ {\mathrm {c z}} = \mathrm {I} _ {\mathrm {z x}} \mathrm {w} _ {\mathrm {x}} + \mathrm {I} _ {\mathrm {z y}} \mathrm {w} _ {\mathrm {y}} + \mathrm {I} _ {\mathrm {z z}} \mathrm {w} _ {\mathrm {z}}
$$

Definiendo ahora las matrices columnas que se indican a continuación, cuyos elementos son las componentes solidarias de los vectores momento angular y velocidad angular. 

$$
\vec {\mathrm {L}} _ {\mathrm {c}} = \left[ \begin{array}{l} \mathrm {L} _ {\mathrm {c x}} \\ \mathrm {L} _ {\mathrm {c y}} \\ \mathrm {L} _ {\mathrm {c z}} \end{array} \right]
$$

$$
\vec {\mathbf {w}} = \left[ \begin{array}{l} \mathbf {w} _ {\mathrm {x}} \\ \mathbf {w} _ {\mathrm {y}} \\ \mathbf {w} _ {\mathrm {z}} \end{array} \right]
$$

Y la matriz de inercia, cuyos elementos son los coeficientes de inercia. 

$$
\hat {\mathrm {I}} _ {\mathrm {c}} = \left[ \begin{array}{l l l} \mathrm {I} _ {\mathrm {x x}} & \mathrm {I} _ {\mathrm {x y}} & \mathrm {I} _ {\mathrm {x z}} \\ \mathrm {I} _ {\mathrm {y x}} & \mathrm {I} _ {\mathrm {y y}} & \mathrm {I} _ {\mathrm {y z}} \\ \mathrm {I} _ {\mathrm {z x}} & \mathrm {I} _ {\mathrm {z y}} & \mathrm {I} _ {\mathrm {z z}} \end{array} \right]
$$

Las componentes solidarias del vector momento angular respecto del centro de masa, en notación matricial, nos quedan expresadas como: 

$$
\vec {\mathrm {L}} _ {\mathrm {c}} = \hat {\mathrm {I}} _ {\mathrm {c}} \hat {\mathbf {w}}
$$

Análogamente, considerando el momento angular respecto de un punto fijo, perteneciente al cuerpo o a una extensión rígida del mismo, como se sugiere en la figura siguiente, obtuvimos que el vector momento angular venía dado por: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/4c88ff2b-823b-4324-b438-3cd0eb86a198/9feb57580e567a7c1109d09c048cf4bbbf5d2e03b1aa526434739f39507af9ec.jpg)


$$
\vec {\mathrm {L}} _ {\mathrm {Q}} = \sum \mathrm {m} _ {\mathrm {i}} \left| \vec {\mathrm {w r}} _ {\mathrm {i}} ^ {2} - \vec {\mathrm {r}} _ {\mathrm {i}} (\vec {\mathrm {w}} \cdot \vec {\mathrm {r}} _ {\mathrm {i}}) \right|
$$

Donde en esta oportunidad, las coordenadas vectoriales de cada una de las partículas están determinadas respecto de dicho punto. 

Puesto que la expresión anterior es formalmente igual a la obtenida para el momento angular respecto del centro de masa, es claro que mediante un procedimiento similar al seguido en el caso anterior, obtendremos que las componentes solidarias del momento angular, respecto del punto fijo, en notación matricial, nos quedará expresado como: 

$$
\vec {\mathrm {L}} _ {\mathrm {Q}} = \hat {\mathrm {I}} _ {\mathrm {Q}} \hat {\mathrm {w}}
$$

Donde en esta oportunidad, los coeficientes de la matriz de inercia estarán evaluados según direcciones solidarias al cuerpo con origen en el punto fijo, perteneciente al cuerpo o a una extensión rígida del mismo. 

# Sistema Principal de Inercia.

Dadas tres direcciones ortogonales con origen en un punto, perteneciente al cuerpo o a una extensión rígida del mismo, diremos que forman un sistema principal de inercia cuando al evaluar la matriz de inercia según dichas direcciones, los productos de inercia se anulan y por lo tanto la matriz resulta diagonal, como se indica a continuación. 

$$
\hat {\mathrm {I}} = \left[ \begin{array}{l l l} \mathrm {I _ {x}} & 0 & 0 \\ 0 & \mathrm {I _ {y}} & 0 \\ 0 & 0 & \mathrm {I _ {z}} \end{array} \right]
$$

En cuyo caso a los momentos de inercia los identificaremos como momentos principales de inercia y para diferenciarlos de aquellos evaluados según direcciones no principales, los identificaremos mediante un único subíndice, con lo que las componentes solidarias del vector momento angular respecto del centro de masa o respecto de un punto fijo, evaluadas según dichas direcciones nos quedan expresados por: 

$$
\mathrm {L} _ {\mathrm {x}} = \mathrm {I} _ {\mathrm {x}} \mathrm {w} _ {\mathrm {x}}
$$

$$
\mathrm {L _ {y} = I _ {y} w _ {y}}
$$

$$
\mathrm {L _ {z} = I _ {z} w _ {z}}
$$

Siendo interesante destacar que de acuerdo con lo anterior, cuando el eje de rotación de un cuerpo coincida con una dirección principal de inercia, entonces el vector momento angular será paralelo al vector velocidad angular, ya que en este caso, de la anterior resulta: 

$$
\vec {\mathrm {L}} = \mathrm {I} \vec {\mathrm {w}}
$$

Donde el momento de inercia involucrado, es el del cuerpo respecto del eje de rotación que pasa por el centro de masa o por un punto fijo, que como ya lo mencionáramos suponemos coincidente con una dirección principal de inercia en dicho punto. 

Teniendo en cuenta la importante simplificación que se logra al evaluar las componentes del vector momento angular según direcciones solidarias y principales, consideraremos alternativas destinadas a identificar dichas direcciones en un punto cualquiera de un cuerpo o una extensión rígida del mismo. 

# Diagonalización de la Matriz de Inercia.

Cuando existe un plano de simetría, entonces orientando los ejes del sistema solidario de manera que uno de sus planos coincida con el plano de simetría del cuerpo, los productos de inercia que contengan como subíndice el correspondiente a la dirección perpendicular a dicho plano, serán nulos, así: 

$$
(x, y) \text {e s u n p l a n o d e s i m e t r i a} I _ {x z} = I _ {z x} = 0, I _ {y z} = I _ {z y} = 0
$$

$$
(z, y) \text {e s u n p l a n o d e s i m e t r i a} I _ {x y} = I _ {y x} = 0, I _ {x z} = I _ {z y} = 0
$$

Por lo tanto, orientando los ejes del sistema solidario de manera que dos de sus planos coincidan con planos de simetría del cuerpo, entonces el sistema resultante será un sistema principal de inercia, en el punto considerado. 

Cuando no existe la posibilidad indicada anteriormente y como lo veremos a continuación, siempre será posible determinar tres direcciones principales en cualquier punto del cuerpo y las mismas serán únicas. 

Con este propósito supongamos al cuerpo rotando alrededor de una dirección caracterizada por los cosenos directores $^ \mathrm { ( l , m , n ) }$ respecto de tres direcciones (xyz) solidarias y arbitrarias como las indicadas en la figura, en cuyo caso el vector velocidad angular del cuerpo puede ser expresado como: 

$$
\vec {w} = w \left(l \vec {i} + m \vec {j} + n \vec {k}\right)
$$

Y las componentes solidarias del vector momento angular como: 

$$
L _ {x} = w \left(I _ {x x} l + I _ {x y} m + I _ {x z} n\right)
$$

$$
L _ {y} = w \left(I _ {y x} l + I _ {y y} m + I _ {y z} n\right)
$$

$$
L _ {z} = w \left(I _ {z x} l + I _ {z y} m + I _ {z z} n\right)
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/4c88ff2b-823b-4324-b438-3cd0eb86a198/be50b4f9c145c2973f708b98bb5ebe3c52c7848d2ddf57c8e23fe0487398728a.jpg)


Suponiendo ahora que la dirección del eje de rotación coincide con una dirección principal de inercia, respecto de la cual, al momento de inercia del cuerpo lo designaremos con (I), las componentes solidarias del vector momento angular consideradas anteriormente, pueden expresarse en función del momento de inercia recientemente indicado, como: 

$$
L _ {x} = I w l
$$

$$
\vec {L} = I \vec {w} \therefore L _ {y} = I w m
$$

$$
L _ {z} = I w n
$$

Con lo que, de las anteriores resulta: 

$$
I _ {x x} l + I _ {x y} m + I _ {x z} n = I l
$$

$$
I _ {y x} l + I _ {y y} m + I _ {y z} n = I m
$$

$$
I _ {z x} l + I _ {z y} m + I _ {z z} n = I n
$$

De donde obtenemos 

$$
\overline {{\left(I _ {x x} - I\right) l + I _ {x y} m + I _ {x z} n}} = 0
$$

$$
I _ {y x} l + \left(I _ {y y} - I\right) m + I _ {y z} n = 0
$$

$$
I _ {z x} l + I _ {z y} m + \left(I _ {z z} - I\right) n = 0
$$

Considerando a la anterior como un sistema de ecuaciones en los cosenos directores, este tendrá solución para aquellos valores del momento de inercia (I) que hagan que el determinante de los coeficientes se anule, estos para aquellos valores tales que: 

$$
\left| \begin{array}{c c c} (I _ {x x} - I) & I _ {x y} & I _ {x z} \\ I _ {y x} & (I _ {y y} - I) & I _ {y z} \\ I _ {z x} & I _ {z y} & (I _ {z z} - I) \end{array} \right| = 0
$$

Que nos proporcionará una ecuación cúbica en (I) cuyas tres soluciones darán lugar a un conjunto de tres valores para los cosenos directores, que simbólicamente se indican a continuación. 

$$
I _ {1} \to \left(l _ {1}, m _ {1}, n _ {1}\right)
$$

$$
I _ {2} \rightarrow (l _ {2}, m _ {2}, n _ {2})
$$

$$
I _ {3} \rightarrow \left(l _ {3}, m _ {3}, n _ {3}\right)
$$

Donde cada uno de los tres conjuntos de cosenos directores (autovectores) nos caracterizarán cada una de las tres direcciones principales de inercia en el punto considerado siendo los autovalores asociados con cada autovector los momentos de inercia respecto de cada una de las tres direcciones principales de inercia indicadas. 

Finalmente cabe destacar que al considerar cada uno de los autovalores en el sistema de ecuaciones lineales originales, las mismas ya no serán linealmente independientes entre si, salvo de a grupos de dos, por lo que a los efectos de determinar los correspondientes cosenos directores será necesario disponer de una ecuación adicional, proporcionada en cada caso por la relación que se indica a continuación y que deben satisfacer los cosenos directores. 

$$
l ^ {2} + m ^ {2} + n ^ {2} = 1
$$

# Teorema de Steiner.

Considerando un sistema (XYZ) trasladado respecto de un sistema (xyz) con origen en el centro de masa, es posible demostrar que los momento y productos de inercia evaluados según cada una de las direcciones indicadas, estarán relacionados mediante expresiones como las que se muestran a continuación. 

$$
\mathrm {I} _ {\mathrm {X X}} = \mathrm {I} _ {\mathrm {x x}} + \mathrm {m} (\mathrm {Y} _ {\mathrm {c}} ^ {2} + \mathrm {Z} _ {\mathrm {c}} ^ {2}) \quad \therefore \quad \mathrm {I} _ {\mathrm {X X}} = \mathrm {I} _ {\mathrm {x x}} + \mathrm {m D} _ {\mathrm {x X}} ^ {2}
$$

$$
\mathrm {I} _ {\mathrm {X Y}} = \mathrm {I} _ {\mathrm {x y}} + \mathrm {m X} _ {\mathrm {c}} \mathrm {Y} _ {\mathrm {c}}
$$

Existiendo relaciones similares para los restantes coeficientes, donde $\mathrm { X c Y _ { c } Z _ { c } }$ son las coordenadas del centro de masa del cuerpo respecto de los ejes (XYZ) respectivamente. 

Considerando ahora una dirección caracterizada por los cosenos directores $^ { ( 1 , \mathfrak { m } , \mathfrak { n } ) }$ , determinados respecto de tres direcciones (XYZ), con origen en cualquier punto del cuerpo entonces, el momento de inercia del cuerpo respecto de dicha dirección, estará relacionado con lo momentos y productos de inercia evaluados según las direcciones anteriores, mediante: 

$$
I _ {(l, m, n)} = I _ {x x} l ^ {2} + I _ {y y} m ^ {2} + I _ {z z} n ^ {2} + 2 I _ {x y} l m + 2 I _ {x z} l n + 2 I _ {y z} m n
$$

# 7.3 ECUACIÓN DE MOMENTOS

En el capítulo anterior obtuvimos que tomando momentos respecto del centro de masa de un cuerpo o respecto de un punto fijo, perteneciente al mismo o a una extensión rígida de este, el momento generado por las fuerzas externas estaba relacionado con las variaciones temporales del vector momento angular del cuerpo respecto de dicho punto, mediante: 

$$
\vec {\mathrm {M}} = \frac {\mathrm {d} \vec {\mathrm {L}}}{\mathrm {d t}} \Bigg | _ {\text {X Y Z}}
$$

Donde recordemos que las variaciones temporales del vector momento angular indicadas anteriormente deberán estar evaluadas desde un sistema de referencia (XYZ) inercial. 

Teniendo en cuenta que de acuerdo a lo desarrollado hasta el momento, el vector momento angular está evaluado según las direcciones de un sistema (xyz) solidario al cuerpo, con origen en el centro de masa o en un punto fijo, según convenga para la situación en consideración y designando con (w) a la velocidad angular del cuerpo respecto del sistema (XYZ) inercial, de la anterior resulta: 

$$
\vec {\mathrm {M}} = \frac {\mathrm {d} \vec {\mathrm {L}}}{\mathrm {d t}} \Bigg | _ {\text {x y z}} + \vec {\mathrm {w}} \times \vec {\mathrm {L}}
$$

Con lo que las componentes solidarias de la ecuación de momentos nos quedan: 

$$
\mathrm {M} _ {\mathrm {x}} = \dot {\mathrm {L}} _ {\mathrm {x}} + (\vec {\mathrm {w}} \times \vec {\mathrm {L}}) _ {\mathrm {x}}
$$

$$
\mathbf {M} _ {\mathrm {y}} = \dot {\mathbf {L}} _ {\mathrm {y}} + (\vec {\mathbf {w}} \times \vec {\mathbf {L}}) _ {\mathrm {y}}
$$

$$
\mathbf {M} _ {\mathrm {z}} = \dot {\mathbf {L}} _ {\mathrm {z}} + (\vec {\mathbf {w}} \times \vec {\mathbf {L}}) _ {\mathrm {z}}
$$

# Movimiento Plano.

Suponiendo al cuerpo animado de un movimiento plano, y orientando los ejes del sistema solidario, con origen en el centro de masa o en un punto fijo, de manera que uno de ellos coincida con el eje de rotación, por ejemplo con el eje (z), en cuyo caso la velocidad angular del cuerpo nos quedará expresada como: 

$$
\vec {\mathrm {w}} = \mathrm {w} \vec {\mathrm {k}}
$$

Y recordando que las componentes solidarias del momento angular, en general venían dadas por: 

$$
L _ {x} = I _ {x x} w _ {x} + I _ {x y} w _ {y} + I _ {x z} w _ {z}
$$

$$
L _ {y} = I _ {y x} w _ {x} + I _ {y y} w _ {y} + I _ {y z} w _ {z}
$$

$$
L _ {z} = I _ {z x} w _ {x} + I _ {z y} w _ {y} + I _ {z z} w _ {z}
$$

Para la situación en consideración dichas componentes vendrán dadas por: 

$$
\mathrm {L} _ {\mathrm {x}} = \mathrm {I} _ {\mathrm {x z}} \mathrm {w}
$$

$$
\mathrm {L} _ {\mathrm {y}} = \mathrm {I} _ {\mathrm {y z}} \mathrm {w}
$$

$$
\mathrm {L} _ {\mathrm {Z}} = \mathrm {I} _ {\mathrm {z z}} \mathrm {w}
$$

Con lo que, para la situación en consideración, las componentes solidarias de la ecuación de momentos, según las direcciones indicadas, nos quedan expresadas como: 

$$
\mathbf {M} _ {\mathrm {x}} = \mathbf {I} _ {\mathrm {x z}} \dot {\mathbf {w}} - \mathbf {I} _ {\mathrm {y z}} \mathbf {w} ^ {2}
$$

$$
\mathbf {M} _ {\mathrm {y}} = \mathbf {I} _ {\mathrm {y z}} \dot {\mathbf {w}} - \mathbf {I} _ {\mathrm {x z}} \mathbf {w} ^ {2}
$$

$$
\mathbf {M} _ {\mathrm {z}} = \mathbf {I} _ {\mathrm {z z}} \dot {\mathbf {w}}
$$
