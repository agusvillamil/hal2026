# 6.03 APLICACIONES

Consideraremos a lo largo de este tema algunas situaciones de interés particular vinculadas con sistemas en equilibrio, en traslación, en rotación y en roto - traslación. 

# Sistema en Equilibrio.

Diremos que un sistema rígido está en equilibrio respecto de un sistema de referencia cuando no se observan cambios en su estado de movimiento, determinados respecto del mencionado sistema de referencia, lo que formalmente podemos indicar mediante las condiciones siguientes: 

$$
\vec {a} _ {\mathrm {c}} = 0
$$

$$
\vec {\alpha} = 0
$$

De donde resulta que para una situación como la indicada: 

$$
\vec {\mathrm {F}} = 0
$$

$$
\vec {\mathrm {M}} = 0
$$

Pudiendo destacarse que el reposo es un caso particular de la situación en consideración. 

# Ejemplo (6.6)

Consideremos el caso de una varilla apoyada sobre una superficie vertical libre de rozamiento y una superficie horizontal donde existe el rozamiento necesario para garantizar el equilibrio, mas precisamente, el reposo de la varilla respecto de un sistema de referencia fijo a tierra, como se sugiere en la figura lateral, en cuyo caso planteando la condición de equilibrio para el centro de masa de la varilla, resulta: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/20f1e00f-cc26-4e9b-b71a-64c5f8e2f72c/524860a0db40794017d712a94728e73cebff73dcb8e049765fbed2126c0414c4.jpg)


$$
\vec {\mathrm {R}} _ {\mathrm {a}} + \vec {\mathrm {R}} _ {\mathrm {b}} + \vec {\mathrm {R}} _ {\mathrm {h}} + \mathrm {m} \vec {\mathrm {g}} = 0
$$

Que evaluada en componentes según direcciones paralelas a la horizontal y vertical nos proporciona las ecuaciones escalares que se indican a continuación: 

$$
\mathrm {R _ {b} - R _ {h}} = 0
$$

$$
R _ {a} - m g = 0
$$

De las que resulta: 

$$
\mathrm {R} _ {\mathrm {b}} = \mathrm {R} _ {\mathrm {h}}
$$

$$
R _ {a} = m g
$$

Siendo claramente necesario el planteo de una segunda ecuación para que juntamente con la primera de las anteriores podamos atender la solución del problema planteado. Con este propósito, considerando los momentos que las fuerzas externas generan respecto del extremo inferior de la varilla y teniendo en cuenta la condición de equilibrio, resulta: 

$$
\mathrm {m g} \frac {\mathrm {H}}{2} \cos \theta - \mathrm {R} _ {\mathrm {b}} \mathrm {H} \sin \theta = 0
$$

De donde obtenemos que: 

$$
R _ {b} = \frac {m g}{2 t g \theta}
$$

Con lo que, de las anteriores resulta que para garantizar el equilibrio, la interacción entre la varilla y la superficie horizontal deberá poder proporcionar una componente de rozamiento estática dada por: 

$$
R _ {h} = \frac {m g}{2 t g \theta}
$$

Por lo tanto resulta inmediato que el coeficiente de rozamiento mínimo requerido para que se mantenga la condición de equilibrio planteada vendrá dado por: 

$$
\mu = \frac {1}{2 \operatorname {t g} \theta}
$$

# Sistemas en Traslación.

Diremos que un sistema rígido está animado de una traslación, respecto de un determinado sistema de referencia, cuando respecto de dicho sistema, todos los puntos del cuerpo tienen el mismo estado de movimiento durante el intervalo de tiempo de interés, lo que formalmente estará asociado con las condiciones que se indican a continuación: 

$$
\vec {a} \neq 0 \quad \vec {w} = 0 \quad \vec {\alpha} = 0
$$

Teniendo en cuenta las anteriores en la expresión que nos vincula el vector aceleración de diferentes puntos de un sistema rígido obtenida en el primer tema de este capítulo, resulta que para todo punto (A) perteneciente al cuerpo o a una extensión rígida del mismo: 

$$
\vec {\mathsf {a}} _ {\mathrm {A}} = \vec {\mathsf {a}} _ {\mathrm {c}}
$$

Con lo que, suponiendo inercial el sistema de referencia en consideración, y bajo las condiciones recientemente indicadas, de la ecuación de movimiento para el centro de masa resulta: 

$$
\vec {\mathrm {F}} = \mathrm {m} \vec {\mathrm {a}} _ {\mathrm {A}}
$$

Donde recordemos que (A) es un punto cualquiera, perteneciente al cuerpo o a una extensión rígida del mismo. Por otro lado de las diferentes formas obtenidas para la ecuación de momentos, y bajo las condiciones establecidas, resulta: 

$$
\vec {\mathrm {M}} _ {\mathrm {c}} = 0
$$

O, si el momento de las fuerzas externas se toman respecto de un punto A cualquiera: 

$$
\vec {\mathrm {M}} _ {\mathrm {A}} = \vec {\mathrm {r}} _ {\mathrm {c / A}} \times \mathrm {m} \vec {\mathrm {a}} _ {\mathrm {c}}
$$

# Ejemplo (6.7)

Consideraremos en esta oportunidad un cuerpo suspendido que es transportado a lo largo de una línea de carga horizontal mediante la aplicación de una fuerza como la indicada en la figura siguiente, en cuyo caso planteando la ecuación de Newton para el centro de masa del sistema resulta: 

$$
\vec {\mathrm {F}} _ {\mathrm {a}} + \vec {\mathrm {F}} _ {\mathrm {b}} + \vec {\mathrm {F}} + \mathrm {m} \vec {\mathrm {g}} = \mathrm {m} \vec {\mathrm {a}} _ {\mathrm {c}}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/20f1e00f-cc26-4e9b-b71a-64c5f8e2f72c/8287cc234024145c058753c24fde731b66c6029f5da10bc75b025c86500f925f.jpg)


Que evaluada en componentes según la dirección horizontal y vertical nos proporciona las ecuaciones escalares que se indican a continuación: 

$$
\mathrm {F} = \mathrm {m a} _ {\mathrm {c}}
$$

$$
\mathrm {F _ {a} + F _ {b} - m g = 0}
$$

Por otro lado, tomando momentos respecto del centro de masa del cuerpo, resulta: 

$$
\mathrm {F _ {b}} \frac {\mathrm {H}}{2} - \mathrm {F _ {a}} \frac {\mathrm {H}}{2} + \mathrm {F D} = 0
$$

Con lo que de las anteriores, obtenemos: 

$$
\mathrm {F _ {a} + F _ {b} = m g}
$$

$$
\mathrm {F _ {a} - F _ {b}} = \frac {2 \mathrm {F D}}{\mathrm {H}}
$$

De donde, sumando miembro a miembro, resulta: 

$$
F _ {a} = \frac {m g}{2} + \frac {F D}{H}
$$

Y restando miembro a miembro: 

$$
F _ {b} = \frac {m g}{2} - \frac {F D}{H}
$$

Teniendo en cuenta las diferentes alternativas para el parámetro (D), esto es, para el punto de aplicación de la fuerza que traslada el sistema, resultan las siguientes situaciones de interés: 

Si la distancia D es negativa: 

$$
\mathrm {F _ {a} <   F _ {b}}
$$

Si D es nula: 

$$
\mathrm {F _ {a}} = \mathrm {F _ {b}} = \frac {\mathrm {m g}}{2}
$$

Si D es positiva: 

$$
\mathrm {F _ {a} > F _ {b}}
$$

Y finalmente, si D es tal que: 

$$
D = \frac {m g H}{2 F}
$$

Entonces: 

$$
\mathrm {F _ {a} = m g \quad y \quad F _ {b} = 0}
$$

# Ejemplo (6.8)

Consideremos ahora la situación sugerida en la figura siguiente, donde se muestra un paralelepípedo de lados D y H apoyado sobre la superficie horizontal de un transporte que se desplaza con una aceleración constante en el sentido indicado. Trataremos de obtener una expresión para la máxima aceleración a la que podemos someter el transporte, si deseamos evitar que vuelque el paralelepípedo. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/20f1e00f-cc26-4e9b-b71a-64c5f8e2f72c/385e4c7528cf8123a8e9fe695f5fc135ba598a776314412d5daa2770f1525318.jpg)


Planteando la ecuación de movimiento para el centro de masa del cuerpo resulta:  

$$
\vec {\mathrm {R}} _ {\mathrm {v}} + \vec {\mathrm {R}} _ {\mathrm {h}} + \mathrm {m} \vec {\mathrm {g}} = \mathrm {m} \vec {\mathrm {a}}
$$

Expresando sus componentes según las direcciones horizontal y vertical, obtenemos las ecuaciones escalares: 

$$
R _ {h} = m a
$$

$$
R _ {v} = m g
$$

Tomando momentos respecto del centro de masa del cuerpo: 

$$
R _ {\mathrm {h}} \frac {H}{2} - R _ {\mathrm {v}} \frac {D}{2} = 0
$$

De donde 

$$
R _ {h} = R _ {v} \frac {D}{H}
$$

Teniendo en cuenta las conclusiones recientemente obtenidas, resulta que la aceleración máxima que podremos dar al recinto evitando que el cuerpo vuelque, vendrá dada por: 

$$
\mathrm {a} = \mathrm {g} \frac {\mathrm {D}}{\mathrm {H}}
$$

Que como podemos observar resulta inversamente proporcional a la altura del paralelepípedo y directamente proporcional al lado da su base. 

Una alternativa interesante obtenemos si tomamos momentos respecto del punto donde están aplicadas las fuerzas incógnitas, en este caso el eje alrededor del cuál puede rotar el cuerpo. Si bien este punto no está fijo a un sistema inercial lo mencionado será posible teniendo en cuenta para esto la relación: 

$$
\vec {\mathrm {M}} _ {\mathrm {A}} = \vec {\mathrm {r}} _ {\mathrm {c} / \mathrm {A}} \times \mathrm {m} \vec {\mathrm {a}} _ {\mathrm {c}} + \mathrm {I} _ {\mathrm {c}} \vec {\alpha}
$$

Que recordemos es válida cualquiera sea el punto seleccionado para determinar los momentos que generan las fuerzas externas a que está sometido el cuerpo, y que para la situación en consideración nos queda: 

$$
\vec {\mathrm {M}} _ {\mathrm {A}} = \vec {\mathrm {r}} _ {\mathrm {c / A}} \times \mathrm {m} \vec {\mathrm {a}} _ {\mathrm {c}}
$$

De donde: 

$$
\mathrm {m g} \frac {\mathrm {D}}{2} = \mathrm {m a} \frac {\mathrm {H}}{2}
$$

De la que resulta: 

$$
\mathrm {a} = \mathrm {g} \frac {\mathrm {D}}{\mathrm {H}}
$$

Coincidente con la obtenida anteriormente, pero sin lugar a duda lograda en forma mas directa, por lo que se recomienda tener en cuenta la alternativa recientemente considerada en todas aquellas oportunidades que sea posible. 

Como una interesante ilustración del ejemplo considerado recientemente, se recomienda trabajar con las simulaciones a las que puede acceder mediante el archivo Caja-1.htm 

# Sistemas en Rotación.

Consideraremos a continuación algunas aplicaciones en las que intervienen sistemas rígidos animados de una rotación alrededor de un eje tal que sus puntos no tienen movimiento respecto del sistema de referencia involucrado. 

# Ejemplo (6.9)

La figura siguiente muestra dos rodillos que se mantienen presionados y pueden rotar alrededor de sus ejes de simetría mientras sobre uno de ellos, en este caso el rodillo A, está aplicada una cupla externa que genera un momento (τ) respecto del eje del mencionado rodillo, entendiendo por una cupla a un sistema de fuerzas tal que tienen una resultante nula y genera un momento no nulo, como es el caso del sistema de fuerzas al que se ve sometida la rueda de un automóvil como consecuencia del sistema de transmisión. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/20f1e00f-cc26-4e9b-b71a-64c5f8e2f72c/8e49a99fb5ae9c477ace81c8d9bff03d9e03de9069808a5bc828e69da0cd22f8.jpg)


En la figura se muestra la cupla aplicada y el par de fuerzas que, en la dirección tangente, resulta de la interacción entre los rodillos involucrados, que indudablemente forman un par acción y reacción y por lo tanto: 

$$
\mathbf {f} _ {\mathrm {A}} = \mathbf {f} _ {\mathrm {B}} = \mathbf {f}
$$

Teniendo en cuenta lo mencionado y planteando la ecuación de momentos respecto del centro de masa de cada uno de los cilindros en consideración, resulta: 

$$
\begin{array}{l} \mathrm {f R} _ {\mathrm {A}} - \tau = \mathrm {I} _ {\mathrm {c}} ^ {\mathrm {A}} \alpha_ {\mathrm {A}} \\ \mathrm {f R _ {B} = I _ {c} ^ {B} \alpha_ {B}} \\ \end{array}
$$

Donde, suponiendo que no existe deslizamiento entre los rodillos, las aceleraciones angulares de los cilindros están relacionadas mediante: 

$$
\mathrm {R _ {A} \alpha_ {A} = R _ {B} \alpha_ {B}}
$$

Con lo que, que la fuerza resultante de la interacción entre los rodillos vendrá expresada por: 

$$
\mathrm {f} = \frac {\tau}{\mathrm {R} _ {\mathrm {A}} \left(1 + \frac {\mathrm {I} _ {\mathrm {c}} ^ {\mathrm {A}} \mathrm {R} _ {\mathrm {B}} ^ {2}}{\mathrm {I} _ {\mathrm {c}} ^ {\mathrm {B}} \mathrm {R} _ {\mathrm {A}} ^ {2}}\right)}
$$

Y la aceleración angular del cilindro A, por: 

$$
\alpha_ {\mathrm {A}} = \frac {\tau}{\left(\mathrm {I} _ {\mathrm {c}} ^ {\mathrm {A}} + \mathrm {I} _ {\mathrm {c}} ^ {\mathrm {B}} \frac {\mathrm {R} _ {\mathrm {A}} ^ {2}}{\mathrm {R} _ {\mathrm {B}} ^ {2}}\right)}
$$

De la expresión obtenida para la fuerza resultante de la interacción entre los rodillos podemos observar que el momento generado por esta fuerza respecto del centro de masa del rodillo A es siempre inferior al momento generado por la cupla externa aplicada: 

$$
\mathrm {f R} _ {\mathrm {A}} <   \tau
$$

Como era de esperar ya que de lo contrario no podríamos tener aceleración angular los cilindros. 

De la expresión obtenida para la aceleración angular del cilindro A resulta interesante destacar que el aporte del cilindro B a la inercia total del sistema y que a menudo se suele identificar como inercia equivalente o “transmitida”, viene dado por: 

$$
\mathrm {I _ {e q i v} ^ {B} = I _ {c} ^ {B} \frac {R _ {A} ^ {2}}{R _ {B} ^ {2}}}
$$

Finalmente y suponiendo que los rodillos se mantienen en contacto y presionados uno contra el otro, mediante la aplicación de fuerzas externas sobre sus ejes, se propone obtener una expresión para el coeficiente de rozamiento mínimo que debería existir entre las superficies a los efectos de evitar el deslizamiento entre los rodillos, en función de las fuerzas mencionadas en este párrafo. 

# Ejemplo (6.10)

La figura lateral muestra un cuerpo suspendido, mediante una cuerda inextensible y de masa despreciable arrollada a lo largo de una polea que puede rodar alrededor de su eje horizontal libre de rozamiento. 

Nos proponemos obtener expresiones para la aceleración del cuerpo suspendido, la aceleración angular de la polea y el esfuerzo al que se verá sometida la cuerda. 

Con el propósito de obtener las expresiones mencionadas tengamos en cuenta que la componente vertical de la ecuación de movimiento para el centro de masa del cuerpo suspendido vendrá dada por: 

$$
\mathrm {f _ {B} - m _ {B} g = m _ {B} a _ {c B}}
$$

Considerando el momento que las fuerzas externas generan respecto del centro de masa de la polea, resulta: 

$$
- \mathrm {f} _ {\mathrm {A}} \mathrm {R} _ {\mathrm {A}} = \mathrm {I} _ {\mathrm {c}} ^ {\mathrm {A}} \alpha_ {\mathrm {A}}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/20f1e00f-cc26-4e9b-b71a-64c5f8e2f72c/4cd478883d382379233645a0a510ff46ba3884eb3705394e120bfd5eaa2ea10d.jpg)


Teniendo en cuenta que hemos supuesto a la cuerda de masa despreciable, las fuerzas involucradas en las anteriores son tales que: 

$$
\mathrm {f _ {A} = f _ {B} = f}
$$

Por otro lado, teniendo en cuenta que hemos supuesto la cuerda inextensible, las aceleraciones involucradas en las ecuaciones anteriores están relacionadas mediante: 

$$
\mathrm {a} _ {\mathrm {c B}} = \mathrm {R} _ {\mathrm {A}} \alpha_ {\mathrm {A}}
$$

Operando con las ecuaciones planteadas, obtenemos que la aceleración del centro de masa del cuerpo suspendido vendrá dada por: 

$$
\mathrm {a} _ {\mathrm {c B}} = \frac {\mathrm {m} _ {\mathrm {B}}}{\mathrm {m} _ {\mathrm {B}} + \frac {\mathrm {I} _ {\mathrm {c}} ^ {\mathrm {A}}}{\mathrm {R} _ {\mathrm {A}} ^ {2}}} \mathrm {g}
$$

Que como era de esperar, resulta menor que (g), o sea menor que el valor asociado con una caída libre. Lo indicado, como consecuencia de que la inercia del sistema se ve incrementada ante la presencia de la polea que en este caso aporta con una masa equivalente dada por: 

$$
\mathbf {m} _ {\mathrm {e q}} = \frac {\mathbf {I} _ {\mathrm {c}} ^ {\mathbf {A}}}{\mathbf {R} _ {\mathrm {A}} ^ {2}}
$$

Finalmente y suponiendo una polea cilíndrica, en cuyo caso: 

$$
\mathrm {I _ {c} ^ {A} = \frac {1}{2} m _ {A} R _ {A} ^ {2}}
$$

La aceleración del centro de masa del cuerpo suspendido vendrá dada por: 

$$
a _ {c B} = \frac {m _ {B}}{m _ {B} + \frac {1}{2} m _ {A}} g
$$

Con lo que, la aceleración angular de la polea vendrá dada por: 

$$
\alpha_ {\mathrm {A}} = \frac {\mathrm {m} _ {\mathrm {B}}}{\mathrm {m} _ {\mathrm {B}} + \frac {1}{2} \mathrm {m} _ {\mathrm {A}}} \frac {\mathrm {g}}{\mathrm {R}}
$$

Y el esfuerzo a que se verá sometida la cuerda, por: 

$$
\mathrm {f} = \frac {\mathrm {m} _ {\mathrm {A}}}{\mathrm {m} _ {\mathrm {A}} + 2 \mathrm {m} _ {\mathrm {B}}} \mathrm {m} _ {\mathrm {B}} \mathrm {g}
$$

Que como era de esperar resulta menor que la fuerza gravitatoria a la que está sometida la masa suspendida. 

Como una adecuada aplicación del ejemplo considerado recientemente, se recomienda trabajar el método dinámico que ofrece la simulación a la que puede acceder mediante el archivo Rotación.htm 

# Péndulo Físico.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/20f1e00f-cc26-4e9b-b71a-64c5f8e2f72c/bd1ea3d985b87176f043d809ef6bbf19299e4f99d58707ad20316abfed2a8275.jpg)


Como otra interesante aplicación del tema que estamos tratando consideremos el caso de una placa suspendida de un punto perteneciente a la misma, que puede oscilar libre de rozamiento alrededor de un eje horizontal que pasa por dicho punto, como se sugiere en la figura anterior, donde además se muestra el sistema de fuerzas externas a que se verá sometida la placa como resultado de su interacción con el campo gravitatorio y con el eje de suspensión, en cuyo caso hemos dibujado las componentes ortogonales de dicha fuerza, según las direcciones solidarias indicadas en la figura. 

Con el propósito de obtener expresiones para las componentes mencionadas recientemente, plantearemos la ecuación de movimiento para el centro de masa del sistema y la evaluaremos en componentes según las direcciones solidarias mencionadas anteriormente. 

$$
\vec {\mathrm {Q}} + \mathrm {m} \vec {\mathrm {g}} = \mathrm {m} \vec {\mathrm {a}} _ {\mathrm {c}}
$$

Donde: 

$$
\vec {a} _ {\mathrm {c}} = \mathrm {m R} \dot {\theta} ^ {2} \vec {\mathrm {j}} + \mathrm {m R} \ddot {\theta} \vec {\mathrm {i}}
$$

Con lo que las componentes ortogonales de la ecuación anterior, según las direcciones solidarias indicadas en la figura nos quedan: 

$$
Q _ {x} + m g \cos \theta = m R \ddot {\theta}
$$

$$
\mathrm {Q} _ {\mathrm {y}} - \mathrm {m g} \mathrm {s e n} \theta = \mathrm {m R} \dot {\theta} ^ {2}
$$

Tomando momentos respecto del centro de suspensión, obtenemos: 

$$
\mathrm {m g R} \cos \theta = \mathrm {I} _ {\mathrm {Q}} \ddot {\theta}
$$

De donde: 

$$
\ddot {\theta} = \frac {\mathrm {m g R}}{\mathrm {I} _ {\mathrm {Q}}} \cos \theta
$$

Diferenciando la anterior e integrando entre límites compatibles, resulta: 

$$
\dot {\theta} ^ {2} = 2 \frac {\mathrm {m g R}}{\mathrm {I} _ {\mathrm {Q}}} \mathrm {s e n} \theta
$$

Teniendo en cuenta estas dos últimas conclusiones en las ecuaciones que resultaron del planteo de las componentes de la ecuación de movimiento del centro de masa, obtenemos las expresiones para las componentes de la reacción en el centro de suspensión que se detallan a continuación: 

$$
Q _ {x} = \left(\frac {m R ^ {2}}{I _ {Q}} - 1\right) m g \cos \theta
$$

$$
Q _ {y} = \left(1 + \frac {m R ^ {2}}{I _ {Q}}\right) m g s e n \theta
$$

Donde recordemos que: 

$$
\mathrm {I} _ {\mathrm {Q}} = \mathrm {I} _ {\mathrm {c}} + \mathrm {m R} ^ {2}
$$

Con lo que, que la componente reactiva según la dirección (x) tendrá sentido opuesto al considerado inicialmente hasta el instante en que la placa pasa por su posición de equilibrio. 

# Oscilaciones con Pequeñas Amplitudes.

Con el propósito de estudiar el comportamiento en las cercanías de la posición de equilibrio tengamos en cuenta la ecuación diferencial que resultó al tomar momentos respecto del centro de suspensión: 

$$
\mathrm {m g R} \cos \theta = \mathrm {I} _ {\mathrm {Q}} \ddot {\theta}
$$

Donde el ángulo (β) entre la vertical y la recta que une el centro de masa con el centro de suspensión está relacionada con la coordenada angular empleada hasta el momento, por: 

$$
\beta = \frac {\pi}{2} - \theta
$$

Con lo que, la ecuación diferencial en términos de esta nueva coordenada angular nos queda: 

$$
\mathrm {m g R s e n} \beta = - \mathrm {I} _ {\mathrm {Q}} \ddot {\beta}
$$

De donde: 

$$
\ddot {\beta} + \frac {\mathrm {m g R}}{\mathrm {I} _ {\mathrm {Q}}} \mathrm {s e n} \beta = 0
$$

Considerando pequeñas oscilaciones alrededor de la posición de equilibrio de manera que sea aceptable la aproximación entre el seno del ángulo y su valor en radianes, de la ecuación diferencial anterior resulta la siguiente: 

$$
\ddot {\beta} + \frac {\mathrm {m g R}}{\mathrm {I} _ {\mathrm {Q}}} \beta = 0
$$

Cuya solución sabemos que es del tipo: 

$$
\beta = \beta_ {\circ} \operatorname {s e n} (\mathrm {w t})
$$

Donde: 

$$
w ^ {2} = \frac {m g R}{I _ {Q}}
$$

Con lo que el período de la oscilación vendrá expresado por: 

$$
\mathrm {T} = 2 \pi \sqrt {\frac {\mathrm {I} _ {\mathrm {Q}}}{\mathrm {m g R}}}
$$

Que en términos del momento de inercia respecto de un eje que pasa por el centro de masa del cuerpo, nos queda: 

$$
\mathrm {T} = 2 \pi \sqrt {\frac {\mathrm {I} _ {\mathrm {c}} + \mathrm {m R} ^ {2}}{\mathrm {m g R}}}
$$

# Péndulo Puntual Equivalente.

Operando con la anterior es inmediato que el período de la oscilación puede expresarse como: 

$$
\mathrm {T} = 2 \pi \sqrt {\frac {\mathrm {R} + \frac {\mathrm {I} _ {\mathrm {c}}}{\mathrm {m R}}}{\mathrm {g}}}
$$

Definiendo la Longitud Equivalente como: 

$$
\mathrm {L} _ {\mathrm {e}} = \mathrm {R} + \frac {\mathrm {I} _ {\mathrm {c}}}{\mathrm {m R}}
$$

El período de la oscilación puede ser indicado como: 

$$
\mathrm {T} = 2 \pi \sqrt {\frac {\mathrm {L} _ {\mathrm {e}}}{\mathrm {g}}}
$$

Comparando esta expresión con la que obtuvimos en el caso de un péndulo puntual oscilando con pequeñas amplitudes es claro que el valor obtenido para el período del péndulo físico en consideración resulta coincidente con el que obtendríamos en el caso de un péndulo puntual cuya longitud coincida con la longitud equivalente recientemente definida. 

Considerando la forma recientemente obtenida para el período de nuestro péndulo físico, es fácil verificar que dicho cuerpo oscilará con el mismo período si se lo suspende de un punto cualquiera perteneciente a una circunferencia de radio (R) centrada en el centro de masa del cuerpo, como la mostrada en la figura lateral, que en adelante reconoceremos como Círculo de Suspensión. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/20f1e00f-cc26-4e9b-b71a-64c5f8e2f72c/9bc2519e126044631389acde00bbad8b058c4192cef3c7c8498f5753d4ff8a53.jpg)


Asociado con el circulo de suspensión, definiremos el Circulo de Oscilación como aquel círculo concéntrico con el anterior y cuyo radio viene dado por: 

$$
R ^ {*} = \frac {I _ {c}}{m R}
$$

Suponiendo ahora que suspendemos el cuerpo de un punto cualquiera perteneciente al círculo de oscilación y teniendo en cuenta la expresión obtenida para el período del péndulo, resulta entonces que el cuerpo oscilará con un período dado por: 

$$
\mathrm {T} = 2 \pi \sqrt {\frac {\mathrm {R} ^ {*} + \frac {\mathrm {I} _ {\mathrm {c}}}{\mathrm {m R} ^ {*}}}{\mathrm {g}}}
$$

Que teniendo en cuenta como fuera definido el radio del circulo de oscilación en término de parámetros iniciales, nos queda: 

$$
\mathrm {T} = 2 \pi \sqrt {\frac {\mathrm {R} + \frac {\mathrm {I} _ {\mathrm {c}}}{\mathrm {m R}}}{\mathrm {g}}}
$$

Indudablemente coincidente con el que obtenemos cuando el cuerpo está suspendido de un punto perteneciente al círculo de suspensión. Por lo tanto en general a cada círculo de suspensión le estará asociado un circulo de oscilación y serán tales que al suspender el cuerpo de un punto cualquiera perteneciente a dichos círculos, oscilará con el mismo período. 

Teniendo presente como fuera definido el radio del circulo de oscilación es claro que este se incrementará cuando se disminuye el radio del circulo de suspensión con el que se encuentra asociado. Por lo tanto es de esperar que exista un valor de $\scriptstyle ( \mathrm { R = R _ { m } } )$ para el cuál, ambos círculos coincidan y que sin lugar a dudas podemos obtenerlo teniendo en cuenta que en ese caso el valor del radio deberá ser tal que: 

$$
R _ {m} = \frac {I _ {c}}{m R _ {m}}
$$

De donde resulta: 

$$
\mathbf {R} _ {\mathrm {m}} = \sqrt {\frac {\mathbf {I} _ {\mathrm {c}}}{\mathbf {m}}}
$$

En cuyo caso obtenemos un período dado por: 

$$
T = 2 \pi \sqrt {\frac {2}{g} \left(\frac {I _ {c}}{m}\right) ^ {1 / 2}}
$$

Estudiando la dependencia entre el período de oscilación del péndulo y la distancia (R) entre el centro de masa y el centro de suspensión se puede demostrar que dicha dependencia da lugar a una función como la que se muestra cualitativamente en la figura siguiente, donde pueden identificarse las propiedades apuntadas anteriormente. En particular y teniendo en cuenta la forma obtenida para el período con que oscila un péndulo alrededor de su posición de equilibrio, mediante el calculo diferencial es posible obtener una expresión para la distancia a la que deberíamos suspenderlo a los efectos de obtener un período mínimo, resultando coincidente con la obtenida al requerir coincidencia 

entre los círculos de oscilación y suspensión, aspecto este que también puede apreciarse en la figura que siguiente. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/20f1e00f-cc26-4e9b-b71a-64c5f8e2f72c/f805114a2a5ded3fd517ae445a4a3c7b4ec1e84dabe9e45c9e2f92fce83fd008.jpg)


Como una aplicación del tema considerado, se recomienda trabajar con la simulación a la que puede acceder mediante el archivo Pendulo.htm, atendiendo las indicaciones que en la página se ofrecen. 

# Sistemas en Rototraslación.

Consideraremos ahora algunas aplicaciones en las que el cuerpo está animado de un movimiento tal que su eje de rotación se desplaza respecto del sistema de referencia involucrado. 

# Ejemplo (6.11)

La figura muestra un cilindro que rueda sin deslizar a lo largo de una superficie horizontal sometido a una cupla externa cuyo momento respecto del centro de masa hemos indicado con (τ). Nos proponemos obtener expresiones para la fuerza que resulta de la interacción entre el cilindro y la superficie horizontal así como para el coeficiente de rozamiento mínimo requerido entre dichas superficies si deseamos evitar el deslizamiento. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/20f1e00f-cc26-4e9b-b71a-64c5f8e2f72c/7715958155487bf889256aed5ed6756ffc6ce101e2bb2cceb6326dc978c513c1.jpg)


Con el propósito indicado comenzaremos planteando la ecuación de movimiento para el centro de masa del cilindro: 

$$
\vec {\mathrm {f}} + \vec {\mathrm {N}} + \mathrm {m} \vec {\mathrm {g}} = \mathrm {m} \vec {\mathrm {a}} _ {\mathrm {c}}
$$

Que evaluada en componentes nos proporciona las ecuaciones escalares que se indican a continuación: 

$$
\mathrm {f} = \mathrm {m a} _ {\mathrm {c}}
$$

$$
N - m g = 0
$$

Considerando el momento que las fuerzas externas generan respecto del centro de masa del cilindro, obtenemos: 

$$
\mathrm {f R} - \tau = \mathrm {I _ {c}} \alpha
$$

Teniendo en cuenta que suponemos no existe deslizamiento, las aceleraciones involucradas están relacionadas mediante: 

$$
a _ {c} = - R \alpha
$$

Operando con las anteriores, resulta: 

$$
f = \frac {\tau}{\left(R + \frac {I _ {c}}{m R}\right)}
$$

Que teniendo en cuenta el teorema de Steiner, puede expresarse como: 

$$
\mathrm {f} = \frac {\mathrm {m R}}{\mathrm {I} _ {\mathrm {Q}}} \tau
$$

De donde podemos observar que como era de esperar: 

$$
\mathrm {f R} <   \tau
$$

De lo contrario no podríamos tener un movimiento con las características del que estamos considerando. En particular, teniendo en cuenta que el momento de inercia de un cilindro respecto de su eje de simetría viene dado por: 

$$
\mathrm {I} _ {\mathrm {c}} = \frac {1}{2} \mathrm {m R} ^ {2}
$$

De las anteriores resulta: 

$$
\mathrm {f} = \frac {2}{3 \mathrm {R}} \tau
$$

Con lo que el coeficiente de rozamiento mínimo requerido para evitar el deslizamiento vendrá dado por: 

$$
\mu_ {\mathrm {m}} = \frac {2}{3 \mathrm {m g R}} \tau
$$

Que como vemos resulta directamente proporcional a la cupla o torque aplicado e inversamente proporcional al radio del cilindro en consideración. 

Se recomienda trabajar con las simulaciones que se ofrecen en las páginas a las que puede acceder mediante los archivos Rototraslación-1.htm e Inclinado.htm 

# Ejemplo (6.12)

Consideraremos a continuación una varilla que puede deslizar libre de rozamiento apoyada sobre una superficie horizontal y una superficie vertical como se muestra en la figura lateral, en cuyo caso nos proponemos obtener expresiones en función de la coordenada angular indicada en dicha figura, para la aceleración angular de la varilla, su velocidad angular, las fuerzas que resultan de su interacción con las superficies en contacto y para las componentes horizontal y vertical del vector aceleración del centro de masa de la mencionada varilla. Con el propósito indicado, planteando la ecuación de movimiento para el centro de masa de la varilla y evaluando sus componentes según una dirección horizontal y una vertical, obtenemos: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/20f1e00f-cc26-4e9b-b71a-64c5f8e2f72c/bc512cf4d576d90bb29b56525c0a72d485258a21a2157857f4ff146a42f6323a.jpg)


$$
\vec {R} _ {A} + \vec {R} _ {B} + m \vec {g} = m \vec {a} _ {c}
$$

De donde para las direcciones horizontal y vertical, resulta: 

$$
R _ {B} = m a _ {c x}
$$

$$
R _ {A} - m g = m a _ {c y}
$$

Tomando momentos respecto del centro de masa de la varilla, obtenemos: 

$$
R _ {A} H s e n \Theta - R _ {B} H c o s \Theta = I _ {c} \ddot {\Theta}
$$

Por otro lado, las aceleraciones involucradas en las anteriores pueden ser relacionadas con las aceleraciones de los puntos extremos de la varilla, cuyas direcciones son conocidas, mediante expresiones vectoriales como las que se indican a continuación: 

$$
\vec {a} _ {c} = \vec {a} _ {A} + \vec {w} \times \vec {w} \times \vec {r} _ {A / C} + \alpha \times \vec {r} _ {A / C}
$$

$$
\vec {a} _ {c} = \vec {a} _ {B} + \vec {w} \times \vec {w} \times \vec {r} _ {B / C} + \alpha \times \vec {r} _ {B / C}
$$

Teniendo en cuenta que el vector aceleración del extremo B de la varilla solamente puede tener componente vertical, es claro entonces que en un planteo de la componente horizontal 

correspondiente a la segunda de las ecuaciones vectoriales anteriores no intervendrá dicha magnitud, resultando efectivamente, la expresión: 

$$
a _ {c x} = - \dot {\theta} ^ {2} H s e n \theta + \ddot {\theta} H c o s \theta
$$

Análogamente, planteando la componente vertical correspondiente a la primera de las ecuaciones vectoriales indicadas, resulta: 

$$
a _ {c y} = - \dot {\theta} ^ {2} H \cos \theta - \ddot {\theta} H s e n \theta
$$

Teniendo en cuenta estas dos últimas conclusiones en las componentes cartesianas de la ecuación de Newton para el centro de masa de la varilla, obtenemos las expresiones que se detallan a continuación: 

$$
R _ {A} = m g - m H \left(\ddot {\theta} s e n \theta + \dot {\theta} ^ {2} c o s \theta\right)
$$

$$
R _ {B} = m H \left(\dot {\theta} ^ {2} s e n \theta - \ddot {\theta} c o s \theta\right)
$$

Teniendo en cuenta estas conclusiones en la ecuación de momentos, resulta la expresión para la aceleración angular de la varilla en función de la coordenada angular que se muestra a continuación: 

$$
\ddot {\theta} = \frac {m g H}{I _ {c} + m H ^ {2}} s e n \theta
$$

Separando variables e integrando entre límites compatibles, suponiendo que la varilla se encuentra inicialmente en reposo, de la anterior resulta: 

$$
\dot {\theta} ^ {2} = \frac {m g H}{I _ {c} + m H ^ {2}} (c o s \theta_ {\circ} - c o s \theta)
$$

Teniendo en cuenta estas dos últimas conclusiones en las expresiones anteriores, es posible obtener expresiones en función de la coordenada angular, para la fuerzas que resultan de la interacción con las superficies en contacto y para las componentes del vector aceleración del centro de masa de la varilla. 

# 6.04 FORMA INTEGRAL DE LAS ECUACIONES DE MOVIMIENTO

A menudo en el tratamiento de algunas aplicaciones suele resultar de mucha utilidad expresar las ecuaciones de movimiento en las formas integrales que se indican a continuación. Con este propósito, diferenciando la ecuación de Newton para el centro de masa en términos del vector cantidad de movimiento del sistema y luego integrando entre límites compatibles, resulta: 

$$
\Delta \vec {\mathrm {P}} = \int_ {0} ^ {t} \vec {\mathrm {F}} d t
$$

Análogamente, diferenciando la ecuación de momentos, cuando estos se toman respecto del centro de masa, y luego integrando entre límites compatibles, obtenemos: 

$$
\Delta \vec {\mathrm {L}} _ {\mathrm {c}} = \int_ {0} ^ {\mathrm {t}} \vec {\mathrm {M}} _ {\mathrm {c}} \mathrm {d t}
$$

Donde a las formas integrales indicadas anteriormente, en adelante las reconoceremos como Impulso e Impulso Angular, respectivamente. 

# Ejemplo (6.13)

Teniendo en cuenta las expresiones recientemente obtenidas, trataremos nuevamente la situación planteada en el ejemplo (6.9) y que se ilustra en la figura siguiente. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/20f1e00f-cc26-4e9b-b71a-64c5f8e2f72c/a0c5d2c5b6d8ea4c3369b8b337eef1c024c4e4d38798cc45a5e86094440025f6.jpg)


Suponiendo que en el instante inicial ambos cilindros están en reposo y considerando un cierto intervalo de tiempo en el que las velocidades angulares de los cilindros alcanzan los valores que se indican a continuación, de la expresión obtenida para el impulso angular, resulta: 

$$
\mathrm {I _ {c} ^ {A} w _ {A} = (\tau - f R _ {A}) \Delta t}
$$

$$
\mathrm {I _ {c} ^ {B} w _ {B} = f R _ {B} \Delta t}
$$

Donde hemos supuesto constantes tanto a las fuerzas como los momentos aplicados, ya que no existe ningún motivo para pensar lo contrario. 

Dividiendo miembro a miembro las anteriores, y teniendo en cuenta que al no existir deslizamiento entre los cilindros, sus velocidades angulares en todo instante estarán relacionadas a través de los radios respectivos, resulta: 

$$
\mathrm {f} = \frac {\tau}{\mathrm {R} _ {\mathrm {A}} \left(1 + \frac {\mathrm {I} _ {\mathrm {c}} ^ {\mathrm {A}} \mathrm {R} _ {\mathrm {B}} ^ {2}}{\mathrm {I} _ {\mathrm {c}} ^ {\mathrm {B}} \mathrm {R} _ {\mathrm {A}} ^ {2}}\right)}
$$

Coincidente con la lograda en el ejemplo de referencia y que luego de tener en cuenta la expresión para el momento de inercia de un cilindro respecto de su eje de simetría, nos queda: 

$$
\mathrm {f} = \frac {\tau}{\mathrm {R _ {A}} \left(1 + \frac {\mathrm {m _ {A}}}{\mathrm {m _ {B}}}\right)}
$$

# Ejemplo (6.14)

Consideraremos ahora la situación que se sugiere en la figura siguiente, donde una esfera de radio y masa conocida, inicialmente rotando con una determinada velocidad angular, se apoya suavemente sobre una superficie horizontal con la que existe un rozamiento no nulo. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/20f1e00f-cc26-4e9b-b71a-64c5f8e2f72c/a21d4927a30bb962ef88ec26ace87dabe7296aaa9a721aa37d2958ab9e8782d5.jpg)


Para una situación como la indicada no cabe duda que inicialmente la esfera deslizará sobre la superficie horizontal y se verá sometida a una fuerza de rozamiento dinámica como la indicada en la figura y por lo tanto su centro de masa se verá sometido a una aceleración que claramente cambiará el estado de movimiento del mencionado punto. 

Nos proponemos obtener una expresión para la velocidad angular que tendrá la esfera a partir del instante en que comienza a rodar sin deslizar. 

Puesto que mientras dure el deslizamiento la esfera se verá sometida a una fuerza de rozamiento constante, teniendo en cuenta la relación entre el impulso y el cambio en el vector cantidad de movimiento, resulta: 

$$
\mathrm {m v _ {c} = f \Delta t}
$$

Y teniendo presente la expresión lograda para el impulso angular, resulta que durante el mismo intervalo de tiempo: 

$$
I _ {c} (w _ {\circ} - w) = f R \Delta t
$$

Dividiendo miembro a miembro las anteriores resulta que mientras dure el deslizamiento, las velocidades involucradas serán tales que: 

$$
\frac {\mathrm {w} _ {\circ} - \mathrm {w}}{\mathrm {v} _ {\mathrm {c}}} = \frac {\mathrm {m R}}{\mathrm {I} _ {\mathrm {c}}}
$$

Teniendo en cuenta, que cuando la esfera comience a rodar sin deslizar, la velocidad del centro de masa y la velocidad de la esfera estarán relacionadas mediante: 

$$
\mathrm {v} _ {\mathrm {c}} = \mathrm {w R}
$$

Y luego imponiendo esta condición en la igualdad anterior y teniendo en cuenta que el momento de inercia de una esfera respecto de un eje centroidal viene dado por: 

$$
I _ {c} = \frac {2}{5} m R ^ {2}
$$

Resulta que en el instante en el que la esfera comienza a rodar sin deslizar, su velocidad angular vendrá dada por: 

$$
\mathrm {w} = \frac {2}{7} \mathrm {w} _ {\circ}
$$

Se recomienda trabajar con la simulación ofrecida en la página a la que puede acceder mediante el archivo Rototraslacion-2.htm 

# Percusión.

La figura muestra una esfera inicialmente en reposo que es sometida a una fuerza constante durante un breve intervalo de tiempo, de manera que el impulso resultante de la interacción viene expresado por: 

$$
\vec {\mathrm {J}} = \vec {\mathrm {F}} \Delta \mathrm {t}
$$

Finalizado el intervalo de tiempo durante el cuál dura la interacción, que en adelante identificaremos como tiempo de percusión, la cantidad de movimiento y el momento angular de la esfera serán tales que: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/20f1e00f-cc26-4e9b-b71a-64c5f8e2f72c/ffb53117546860209af90169c09701815e6e390e54bd5936ca4b58296f1af4b6.jpg)


$$
\mathrm {m v} _ {\mathrm {c}} = \mathrm {J} \quad \mathrm {I} _ {\mathrm {c}} \mathrm {w} = \mathrm {J D}
$$

Donde, durante el tiempo de percusión, hemos considerado despreciable el impulso y el impulso angular asociado con la fuerza de rozamiento dinámica que resulta de la interacción entre la esfera y la superficie horizontal, con lo que de la anterior resulta que una vez finalizado el tiempo de percusión, el estado de movimiento de la esfera estará caracterizado por: 

$$
\mathrm {v} _ {\mathrm {c}} = \frac {\mathrm {J}}{\mathrm {m}} \quad \mathrm {w} = \frac {\mathrm {J D}}{\mathrm {I} _ {\mathrm {c}}}
$$

Teniendo en cuenta que los vectores velocidad del centro de masa y del punto de contacto entre la esfera y la superficie horizontal, están relacionados mediante: 

$$
\vec {\bf {v}} _ {\mathrm {B}} = \vec {\bf {v}} _ {\mathrm {c}} + \vec {\bf {w}} \times \vec {\bf {r}} _ {\mathrm {B / c}}
$$

De las anteriores resulta que finalizada la percusión el punto de contacto con la superficie horizontal tendrá una velocidad dada por: 

$$
\vec {\mathrm {v}} _ {\mathrm {B}} = \mathrm {J} \left(\frac {1}{\mathrm {m}} - \frac {\mathrm {D R}}{\mathrm {I} _ {\mathrm {c}}}\right) \vec {\mathrm {i}}
$$

Teniendo en cuenta que el momento de inercia de una esfera, respecto de un eje centroidal, viene dado por: 

$$
I _ {c} = \frac {2}{5} m R ^ {2}
$$

Obtenemos que la velocidad del punto de contacto, al finalizar el tiempo de percusión, vendrá dada por: 

$$
\vec {\mathrm {v}} _ {\mathrm {B}} = \frac {\mathrm {J}}{\mathrm {m}} \left(1 - \frac {5}{2} \frac {\mathrm {D}}{\mathrm {R}}\right) \vec {\mathrm {i}}
$$

De donde resultan destacables los casos particulares que se indican a continuación: 

Suponiendo que el punto de aplicación del impulso es tal que: 

$$
\mathrm {D} = \frac {2}{5} \mathrm {R}
$$

Resulta: 

$$
\vec {\mathrm {v}} _ {\mathrm {B}} = 0
$$

Finalizada la percusión la esfera rodará sin deslizar. 

Suponiendo que el punto de aplicación del impulso es tal que: 

$$
\mathbf {D} = \mathbf {0}
$$

$$
\vec {v} _ {\mathrm {B}} = \frac {\mathrm {J}}{\mathrm {m}} \vec {\mathrm {i}} \quad \therefore \quad \vec {v} _ {\mathrm {B}} = \vec {v} _ {\mathrm {c}} \quad \therefore \quad \vec {w} = 0
$$

Finalizada la percusión la esfera se traslada con el vector velocidad indicado anteriormente. 

Suponiendo dada esta última condición, y una vez finalizada la percusión, la esfera quedará sometida a una fuerza de rozamiento dinámica como consecuencia de su interacción con la superficie horizontal, la que dará lugar a cambios en el estado de movimiento que se recomienda su evaluación. 

También se recomienda trabajar con el material que se ofrece en la página a la que puede acceder mediante el archivo Percusion.htm 

# 6.05 CONSERVACIÓN DEL VECTOR MOMENTO ANGULAR

Teniendo presente la relación entre el momento que generan las fuerzas externas y las variaciones temporales del vector momento angular, es claro entonces que si un cuerpo está sometido a un conjunto de fuerzas tales que no generan momento respecto del centro de masa, su vector momento angular, determinado respecto de dicho punto, deberá permanecer constante e igual al que tenía en el instante inicial, lo que formalmente podemos expresar como se indica a continuación:    

$$
\vec {\mathrm {M}} _ {\mathrm {c}} = 0 \Rightarrow \vec {\mathrm {L}} _ {\mathrm {c}} = \mathrm {c t e} \quad \therefore \quad \vec {\mathrm {L}} _ {\mathrm {c}} = \vec {\mathrm {L}} _ {\circ}
$$

Y por lo tanto, bajo estas condiciones, el vector momento angular en cualquier instante deberá coincidir con el que teníamos en el instante inicial, entendiendo por instante inicial al instante a partir del cuál se satisface la condición de referencia, siendo importante destacar que se trata de la conservación de una magnitud vectorial y por lo tanto la misma garantiza la conservación del módulo, dirección y sentido de la misma. 

# Momento Generado por un Campo Gravitatorio.

Consideremos a continuación el momento a que se vería sometido un cuerpo como consecuencia de estar sometido a la interacción con un campo gravitatorio, en cuyo caso cada una de las partículas que lo integran se verán sometidas a fuerzas como las sugeridas en la figura lateral, y por lo tanto, el momento a que se verá sometido el cuerpo respecto de un punto (A) cualquiera, vendrá dado por: 

$$
\vec {\mathrm {M}} _ {\mathrm {a}} = \sum \vec {\mathrm {r}} _ {\mathrm {i / A}} \times \mathrm {m} _ {\mathrm {i}} \vec {\mathrm {g}} _ {\mathrm {i}}
$$

Suponiendo ahora que el campo gravitatorio a que está sometido el cuerpo fuera constante, resulta: 

$$
\vec {\mathrm {M}} _ {\mathrm {a}} = \left(\sum \mathrm {m} _ {\mathrm {i}} \vec {\mathrm {r}} _ {\mathrm {i / A}}\right) \times \vec {\mathrm {g}}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/20f1e00f-cc26-4e9b-b71a-64c5f8e2f72c/95de30cd6c771b06e545e4da06e52a5db19dadd6e1a6c66cd536ced3b8d6398c.jpg)


Que en términos de la coordenada vectorial del centro de masa, respecto del punto (A) nos queda: 

$$
\vec {\mathrm {M}} _ {\mathrm {a}} = \vec {\mathrm {r}} _ {\mathrm {c} / \mathrm {A}} \times \mathrm {m} \vec {\mathrm {g}}
$$

Donde con (m) indicamos a la masa de todo el sistema. Resultando que bajo las condiciones establecidas, campo gravitatorio constante, el momento a que dará lugar este mecanismo de interacción respecto de un punto cualquiera, será coincidente con el que obtendríamos si suponemos a la resultante de la fuerza gravitatoria (peso del cuerpo) aplicada en el centro de masa del mismo. En particular, es claro que si el momento se determina respecto del mencionado centro de masa, éste será 

necesariamente nulo, en cuyo caso y suponiendo que fuera esta la única interacción a que se encuentra sometido, el cuerpo estará libre de momentos y por lo tanto su vector momento angular de Spin deberá permanecer constante, mientras dure la condición de referencia. 

# Ejemplo (6.15)

Consideremos el caso de un satélite cilíndrico que rota alrededor de su eje de simetría mientras su centro de masa se desplaza a lo largo de una trayectoria cerrada, consecuencia de su interacción con el campo gravitatorio de un planeta, como se sugiere en la figura siguiente. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/20f1e00f-cc26-4e9b-b71a-64c5f8e2f72c/d2bddb412fe128c252eed632fe47a93a64da5c8d0f2ac434f875f92650062978.jpg)


Suponiendo inercial a un sistema de referencia fijo al planeta, nos preguntamos cuales serán las características del movimiento del satélite respecto del mencionado sistema de referencia, a lo largo de la trayectoria indicada. 

Las figuras que continúan muestran dos alternativas diferentes. En el primer caso el eje de simetría del satélite rota en el plano de la órbita, alrededor de un eje pasante por el centro del planeta, en el segundo, dicho eje se traslada de manera que el centro de masa se desplaza a lo largo de la trayectoria indicada. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/20f1e00f-cc26-4e9b-b71a-64c5f8e2f72c/8837f5ac84003062dff139e8dfac39afff0f809fb3dddd798b19515bb3531dd5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/20f1e00f-cc26-4e9b-b71a-64c5f8e2f72c/a2f61f5e41112c10fb93dc10c93fd1ee9ea2cf1dab29887fda7c9d7ee74a4db9.jpg)


Teniendo en cuenta que el cuerpo está sometido únicamente a la interacción con el campo gravitatorio del planeta y atendiendo lo mencionado recientemente, se trata de un cuerpo libre de momentos y por lo tanto su momento angular de spin deberá permanecer constante a lo largo de toda su trayectoria, con lo que necesariamente el movimiento será como se sugiere en la segunda figura. 

Para que se de una situación como la indicada en la primer figura, en cuyo caso existen cambios temporales en la componente de spin del vector momento angular, será necesario pensar en algún mecanismo capaz de proporcionar un sistema de fuerzas externas tales que el momento generado respecto del centro de masa del cuerpo sea compatible con los cambios temporales observados en la mencionada componente del vector momento angular en consideración, como en el caso que se 

muestra en la figura siguiente, donde los cojinetes que soportan al eje del rotor proporcionan las fuerzas indicadas anteriormente. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/20f1e00f-cc26-4e9b-b71a-64c5f8e2f72c/5a1bd7f0bebb187fbf1d80529b0bcdfff264dfa33df60d03926c394f287448e4.jpg)
