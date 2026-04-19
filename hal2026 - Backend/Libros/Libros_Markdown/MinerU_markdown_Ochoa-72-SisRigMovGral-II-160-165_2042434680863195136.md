# 7.4 ECUACIONES DE EULER

Considerando ahora un cuerpo animado de un movimiento general y suponiendo a los vectores velocidad angular y momento angular evaluados en componentes según direcciones solidarias y principales, las componentes de la ecuación de momentos según dichas direcciones resultan: 

$$
\mathbf {M} _ {\mathrm {x}} = \mathbf {I} _ {\mathrm {x}} \dot {\mathbf {w}} _ {\mathrm {x}} - (\mathbf {I} _ {\mathrm {y}} - \mathbf {I} _ {\mathrm {z}}) \mathbf {w} _ {\mathrm {y}} \mathbf {w} _ {\mathrm {z}}
$$

$$
\mathbf {M} _ {\mathrm {y}} = \mathbf {I} _ {\mathrm {y}} \dot {\mathbf {w}} _ {\mathrm {y}} - (\mathbf {I} _ {\mathrm {z}} - \mathbf {I} _ {\mathrm {x}}) \mathbf {w} _ {\mathrm {z}} \mathbf {w} _ {\mathrm {x}}
$$

$$
\mathbf {M} _ {\mathrm {z}} = \mathbf {I} _ {\mathrm {z}} \dot {\mathbf {w}} _ {\mathrm {z}} - (\mathbf {I} _ {\mathrm {x}} - \mathbf {I} _ {\mathrm {y}}) \mathbf {w} _ {\mathrm {x}} \mathbf {w} _ {\mathrm {y}}
$$

Generalmente conocidas como Ecuaciones de Euler. 

# Movimiento Libre de Momentos.

Como una aplicación de las ecuaciones de Euler, consideremos el caso de un cuerpo que se mueve libre de momentos, como sería aquella situación en la que está sometido únicamente a la interacción con un campo gravitatorio, en cuyo caso de la anterior resulta que las componentes solidarias del vector velocidad angular deberán ser tales que satisfagan el sistema de ecuaciones diferenciales: 

$$
\mathrm {I _ {x} \dot {w} _ {x} = (I _ {y} - I _ {z}) w _ {y} w _ {z}}
$$

$$
\mathrm {I _ {y} \dot {w} _ {y} = (I _ {z} - I _ {x}) w _ {z} w _ {x}}
$$

$$
\mathrm {I _ {z} \dot {w} _ {z} = (I _ {x} - I _ {y}) w _ {x} w _ {y}}
$$

Considerando ahora un cuerpo con simetría de revolución, como el sugerido en la figura lateral y orientando los ejes del sistema solidario de manera que el eje (z) coincida con el de simetría, en cuyo caso la terna solidaria resulta principal y los momentos de inercia respecto de las direcciones normales al eje de simetría coincidentes, a los que en adelante designaremos como: 

$$
\mathbf {I} _ {\mathrm {x}} = \mathbf {I} _ {\mathrm {y}} = \mathbf {I}
$$

$$
\mathrm {I _ {Z} = I _ {\circ}}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/42c33a09-c096-45c2-a1bc-c0c81b00cc60/74aad468f19f08eb1f550df6b688dcbeb48b2971578f071bcc0d98600cc044b0.jpg)


De la anterior obtenemos que las componentes solidarias de la velocidad angular del cuerpo deberán ser soluciones del sistema de ecuaciones diferenciales: 

$$
\mathrm {I _ {x} \dot {w} _ {x} = (I - I _ {\circ}) w _ {y} w _ {z}}
$$

$$
\mathrm {I _ {y} \dot {w} _ {y} = (I _ {\circ} - I _ {y}) w _ {z} w _ {x}}
$$

$$
\mathrm {I} _ {\mathrm {z}} \dot {\mathrm {w}} _ {\mathrm {z}} = 0
$$

De la última ecuación obtenemos que la componente (z) del vector velocidad angular permanecerá constante, e igual al valor que tenia en el instante inicial. 

$$
\mathrm {w} _ {\mathrm {z}} = \mathrm {w} _ {\mathrm {z 0}}
$$

Teniendo esto en cuenta, derivando la primera y reemplazando en la segunda, obtenemos que la componente (x) de la velocidad angular deberá ser solución de la ecuación diferencial: 

$$
\ddot {w} _ {x} + \left(\frac {I - I _ {\circ}}{I} w _ {z 0}\right) ^ {2} w _ {x} = 0
$$

Con lo que dicha componente vendrá dada por: 

$$
w _ {x} = A s e n (q t)
$$

Donde: 

$$
\mathrm {q} = \frac {\mathrm {I} - \mathrm {I} _ {\circ}}{\mathrm {I}} \mathrm {w} _ {\mathrm {z 0}}
$$

Derivando la solución encontrada para la componente (x), de la primera ecuación diferencial obtenemos que la componente (y) de la velocidad angular vendrá dada por: 

$$
w _ {y} = A \cos (q t)
$$

Donde la constante A involucrada en las soluciones dependerá de las condiciones iniciales, con lo que el módulo de la velocidad angular del cuerpo permanecerá constante ya que vendrá dado por: 

$$
w = \sqrt {A ^ {2} + w _ {z o} ^ {2}}
$$

Teniendo en cuenta que las componentes obtenidas para el vector velocidad angular son componentes según las direcciones solidarias al cuerpo, es claro que el vector velocidad angular precesionará alrededor del eje de simetría del cuerpo como se sugiere en la figura siguiente, generando un cono en el cuerpo cuya abertura permanecerá constante ya que dicho ángulo será tal que: 

$$
\mathrm {t g} \alpha = \frac {\mathrm {A}}{\mathrm {w} _ {\mathrm {z 0}}}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/42c33a09-c096-45c2-a1bc-c0c81b00cc60/bcc05dd0b3757ebc5f611cf3302e3e6a000232868fc601141233f187c670f52e.jpg)


Por otro lado, teniendo en cuenta que el momento es nulo, el vector momento angular permanecerá constante y por lo tanto caracterizará una dirección fija al sistema inercial como se muestra en la figura lateral, donde hemos supuesto que los ejes del sistema inercial están orientados de manera que el eje ( Z ) coincide con la dirección de dicho vector. Así mismo, la nulidad del momento que generan las fuerzas externas garantiza la conservación de la energía cinética de Spin, con lo que: 

$$
\frac {1}{2} \vec {\mathrm {w}} \cdot \vec {\mathrm {L}} _ {\mathrm {c}} = \mathrm {c t e}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/42c33a09-c096-45c2-a1bc-c0c81b00cc60/4a8695b1b6a05146565a005e0e592deb0850d6a4d47b2b425f4ba23138adfabf.jpg)


De donde resulta que el ángulo entre ambas magnitudes deberá ser tal que: 

$$
\frac {1}{2} \mathrm {w L} _ {\mathrm {c}} \cos \beta = \mathrm {c t e}
$$

Por lo tanto dicha magnitud angular deberá permanecer constante, como se sugiere en la figura anterior, con lo que si tenemos en cuenta que el vector velocidad angular precesiona alrededor del eje de simetría del cuerpo, lo indicado recientemente requiere que dicho vector precesione alrededor de la dirección caracterizada por el vector momento angular, generando así un cono en el espacio asociado al sistema de referencia inercial, como se muestra en la figura anterior. 

Finalmente y teniendo en cuenta las conclusiones anteriores es claro que las mismas requieren de una precesión del eje de simetría del cuerpo alrededor de la dirección caracterizada por el vector momento angular, como también se sugiere en la última figura, de manera que el ángulo entre ambas direcciones (suma de las magnitudes angulares consideradas anteriormente) permanezca constante. 

Como una ilustración del tema se recomienda el video Giróscopo.avi 

# 7.5 ECUACIONES DE EULER MODIFICADAS.

Finalmente consideraremos una forma distinta de expresar las componentes cartesianas de la ecuación de momentos, particularmente útil cuando se trabaja con cuerpos que poseen simetría cilíndrica, como el que se muestra en la figura siguiente, en cuyo caso resulta conveniente emplear como sistema auxiliar (xyz) a un sistema que acompaña al cuerpo en su precesión y nutación pero no en su rotación propia y que en adelante reconoceremos como sistema nodal. 

# (XYZ)

Sistema Inercial 

$$
(x y z)
$$

Sistema Nodal 

Velocidad angular del sistema nodal respecto del inercial 

$$
\vec {\mathrm {w}} = \vec {\dot {\Psi}} + \vec {\dot {\theta}}
$$

Velocidad angular del cuerpo respecto del sistema inercial 

$$
\vec {\mathrm {w}} = \vec {\dot {\Psi}} + \vec {\dot {\theta}} + \vec {\dot {\phi}}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/42c33a09-c096-45c2-a1bc-c0c81b00cc60/ab35f966a56c4a6f8242f23eadd8fd78b16bf471bca83fbdac8250772a168083.jpg)


Teniendo en cuenta que el sistema nodal acompaña al cuerpo solamente en su precesión y nutación, las componentes nodales del vector que caracteriza la rotación de dicho sistema respecto del sistema inercial, vendrán dadas por: 

$$
\Omega_ {\mathrm {x}} = \dot {\theta}
$$

$$
\Omega_ {\mathrm {y}} = \dot {\Psi} \sin \theta
$$

$$
\Omega_ {\mathrm {z}} = \dot {\Psi} \cos \theta
$$

Mientras que las componentes nodales del vector que caracteriza la rotación del cuerpo respecto del sistema inercial, vendrán dadas por: 

$$
w _ {x} = \dot {\theta}
$$

$$
w _ {y} = \dot {\Psi} s e n \theta
$$

$$
\mathrm {w} _ {\mathrm {z}} = \dot {\Psi} \cos \theta + \dot {\phi}
$$

Orientando los ejes del sistema nodal de manera que el eje (z) coincida con el eje de simetría del cuerpo, dicho sistema resultara principal y los momentos de inercia involucrados continuarán siendo invariantes temporales a pesar de que el mencionado sistema no está solidario al cuerpo, con lo que las componentes nodales del vector momento angular del cuerpo vendrán dadas por: 

$$
\mathrm {L} _ {\mathrm {x}} = \mathrm {I} \dot {\theta}
$$

$$
\mathrm {L} _ {\mathrm {y}} = \mathrm {I} \dot {\Psi} \mathrm {s e n} \theta
$$

$$
\mathrm {L} _ {\mathrm {Z}} = \mathrm {I} _ {\circ} (\dot {\Psi} \cos \theta + \dot {\phi})
$$

Donde: 

$$
\mathrm {I} _ {\mathrm {x}} = \mathrm {I} _ {\mathrm {y}} = \mathrm {I}
$$

$$
\mathrm {I} _ {\mathrm {Z}} = \mathrm {I} _ {\circ}
$$

Evaluando ahora la derivada temporal del vector momento angular desde el sistema nodal, la forma vectorial de la ecuación de momento vendrá dada por: 

$$
\vec {\mathrm {M}} = \frac {\mathrm {d} \vec {\mathrm {L}}}{\mathrm {d t}} \Bigg | _ {\text {x y z}} + \vec {\Omega} \times \vec {\mathrm {L}}
$$

Teniendo en cuenta que aun cuando el sistema auxiliar (xyz) no esta solidario al cuerpo, los momentos de inercia continúan siendo invariantes temporales, las componentes nodales de la anterior nos quedan: 

$$
\mathrm {M} _ {\mathrm {x}} = \mathrm {I} \ddot {\theta} + \left(\mathrm {I} _ {\circ} - \mathrm {I}\right) \dot {\Psi} ^ {2} \operatorname {s e n} \theta \cos \theta + \mathrm {I} _ {\circ} \dot {\phi} \dot {\Psi} \operatorname {s e n} \theta
$$

$$
\mathrm {M} _ {\mathrm {y}} = \mathrm {I} \ddot {\Psi} \operatorname {s e n} \theta + 2 \mathrm {I} \dot {\Psi} \dot {\theta} \cos \theta - \mathrm {I} _ {\circ} \dot {\theta} (\dot {\phi} + \dot {\Psi} \cos \theta)
$$

$$
\mathrm {L} _ {\mathrm {Z}} = \mathrm {I} _ {\circ} (\ddot {\phi} + \ddot {\Psi} \cos \theta - \dot {\Psi} \dot {\theta} \sin \theta)
$$

Sistema de ecuaciones diferenciales que en adelante reconoceremos como ecuaciones de Euler modificadas, en término de los ángulos de Euler y que a continuación emplearemos para el tratamiento de algunas situaciones de interés particular, donde resulta interesante destacar que la componente (z) coincide con la derivada temporal de la componente (z) del vector momento angular, dado que dicha componente del producto vectorial es nula. 

# Peonza Simétrica Libre de Momentos.

Consideraremos nuevamente las características del movimiento de un cuerpo con simetría de revolución cuando se encuentra libre de momentos, en cuyo caso su vector momento angular permanecerá constante e igual al que tenía en el instante inicial y por lo tanto caracterizará una dirección fija al sistema de referencia inercial. 

$$
\vec {\mathrm {L}} = \mathrm {c t e} = \vec {\mathrm {L}} _ {\circ}
$$

Por otro lado, teniendo en cuenta que la componente ( z ) de las ecuaciones de Euler modificadas coincide con la derivada temporal de la componente ( z ) del vector momento angular, y como el momento que generan las fuerza externas es nulo, entonces: 

$$
L _ {z} = c t e \quad \therefore L _ {\circ} \cos \theta = c t e \quad \therefore \theta = c t e = \theta_ {\circ}
$$

Donde la coordenada angular involucrada, recordemos que corresponde a la coordenada entre la dirección fija caracterizada por el vector momento angular y el eje de simetría del cuerpo, como se sugiere en la figura siguiente: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/42c33a09-c096-45c2-a1bc-c0c81b00cc60/10d88311e47e534f66957ce56820270667ca4b21c1e009fc408a4c6ec6afec3a.jpg)


Teniendo en cuenta esta conclusión en la componente (y) de las ecuaciones de Euler modificadas, resulta: 

$$
\mathrm {I} \ddot {\Psi} \operatorname {s e n} \theta_ {\circ} = 0 \quad \therefore \quad \ddot {\Psi} = 0 \quad \therefore \quad \dot {\Psi} = \mathrm {c t e}
$$

Cuyo valor podemos obtener teniendo en cuenta que de la componente (y) del vector momento angular, obtenemos: 

$$
\mathrm {L} _ {\circ} \operatorname {s e n} \theta_ {\circ} = \mathrm {I} \dot {\Psi} \operatorname {s e n} \theta_ {\circ} \quad \therefore \quad \dot {\Psi} = \frac {\mathrm {L} _ {\circ}}{\mathrm {I}}
$$

Teniendo en cuenta estas conclusiones en la componente (x) de la ecuación de momentos, resulta: 

$$
(I _ {\circ} - I) \dot {\Psi} ^ {2} \operatorname {s e n} \theta_ {\circ} \cos \theta_ {\circ} + I _ {\circ} \dot {\phi} \dot {\Psi} \operatorname {s e n} \theta_ {\circ} = 0
$$

De donde: 

$$
\dot {\phi} = \frac {\left(\mathrm {I} - \mathrm {I} _ {\circ}\right)}{\mathrm {I} _ {\circ}} \dot {\Psi} \cos \theta_ {\circ}
$$

Que en términos del momento angular en el instante inicial nos queda: 

$$
\dot {\phi} = \frac {\left(\mathrm {I} - \mathrm {I} _ {\circ}\right)}{\mathrm {I I} _ {\circ}} \mathrm {L} _ {\circ} \cos \theta_ {\circ}
$$

Con lo que las componentes nodales del vector que caracteriza la rotación del cuerpo, resultan: 

$$
\begin{array}{l} \mathbf {w} _ {\mathrm {x}} = 0 \\ w _ {y} = \frac {L _ {o}}{I} s e n \theta_ {o} \\ w _ {z} = \frac {L _ {o}}{I _ {o}} \cos \theta_ {o} \\ \end{array}
$$

Por lo tanto, el vector velocidad angular del cuerpo precesiona alrededor del vector momento angular juntamente con el sistema nodal, como se sugiere en la figura siguiente: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/42c33a09-c096-45c2-a1bc-c0c81b00cc60/f0641e21aa4cd060136c63d91b4b5feee8fdf917cb7c0d79650ffe8b2dfd9b5e.jpg)


Por otro lado, teniendo en cuenta que un sistema $\left( \mathbf { x } ^ { \prime } \mathbf { y } ^ { \prime } \mathbf { z } ^ { \prime } \right)$ solidario al cuerpo con origen en el mismo punto que el sistema nodal, rota respecto de este con la rotación propia del cuerpo, como se sugiere en la figura siguiente, las componentes solidarias del vector velocidad angular del cuerpo vendrán dadas por: 

$$
\mathrm {w} _ {\mathrm {X} ^ {\prime}} = \frac {\mathrm {L} _ {\circ}}{\mathrm {I}} \mathrm {s e n} \theta_ {\circ} \mathrm {s e n} (\dot {\phi} \mathrm {t})
$$

$$
w _ {y ^ {\prime}} = \frac {L _ {o}}{I} \sin \theta_ {o} \cos (\dot {\phi} t)
$$

$$
w _ {z ^ {\prime}} = \frac {L _ {o}}{I _ {o}} \cos \theta_ {o}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/42c33a09-c096-45c2-a1bc-c0c81b00cc60/55c43cc67fb3d5ea24734b8911b8a19b613d2b3abe73c51c38f65cd62e93617c.jpg)


Y por lo tanto el vector velocidad angular precesiona alrededor del eje de simetría con la velocidad angular que se indica a continuación, generando un cono en el cuerpo como el que se muestra en la figura siguiente: 

$$
\dot {\phi} = \frac {\left(\mathrm {I} - \mathrm {I} _ {\circ}\right)}{\mathrm {I I} _ {\circ}} \mathrm {L} _ {\circ} \cos \theta_ {\circ}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/42c33a09-c096-45c2-a1bc-c0c81b00cc60/c56f008b1ba114e79be86f7ea913a2e428edc8c77b412d9c5ed113d437935b29.jpg)


De donde la relación entre la apertura del cono del cuerpo y el ángulo de nutación resulta: 

$$
\operatorname {t g} \alpha = \frac {\frac {\mathrm {L} _ {\circ}}{\mathrm {I}} \operatorname {s e n} \theta_ {\circ}}{\frac {\mathrm {L} _ {\circ}}{\mathrm {I} _ {\circ}} \cos \theta_ {\circ}}
$$

Por lo tanto: 

$$
\mathrm {t g} \alpha = \frac {\mathrm {I} _ {\circ}}{\mathrm {I}} \mathrm {t g} \theta_ {\circ}
$$

Con lo que en el caso de un cuerpo con aspecto de cilindro, en cuyo caso: 

$$
\mathrm {I} _ {\circ} <   \mathrm {I} \quad \therefore \quad \alpha <   \theta_ {\circ}
$$

La situación será como se sugiere en la figura siguiente: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-06/42c33a09-c096-45c2-a1bc-c0c81b00cc60/95f1809daa77fa52fec7bb297593ef80d622f83de76ce492b87c9e329aa8e51e.jpg)


Mientras que en el caso de un cuerpo con aspecto de plato, en cuyo caso: 

$$
I _ {\circ} > I \quad \therefore \quad \alpha > \theta_ {\circ}
$$

La situación será inversa a la mostrada en la figura anterior. 

# Precesión Estacionaria con Momento No Nulo.

Considerando un cuerpo con simetría de revolución veremos que condiciones deberán darse para que pueda estar animado de una precesión estacionaria, o sea un movimiento tal que: 

$$
\theta = 0 \quad \theta = \mathrm {c t e}
$$

$$
\ddot {\Psi} = 0 \Rightarrow \dot {\Psi} = \mathrm {c t e}
$$

$$
\ddot {\phi} = 0 \quad \dot {\phi} = c t e
$$

En cuyo caso de las componentes nodales de las ecuaciones de Euler modificadas resulta que: 

$$
\mathrm {M} _ {\mathrm {X}} = \left(\mathrm {I} _ {\circ} - \mathrm {I}\right) \dot {\Psi} ^ {2} \operatorname {s e n} \theta \cos \theta + \mathrm {I} _ {\circ} \dot {\phi} \dot {\Psi} \operatorname {s e n} \theta
$$

$$
\mathrm {M} _ {\mathrm {y}} = 0
$$

$$
\mathrm {M} _ {\mathrm {Z}} = 0
$$

Considerando el caso particular de una precesión estacionaria con un ángulo de nutación de $9 0 ^ { \circ }$ de las anteriores resulta que las componentes nodales del momento que generen las fuerzas externas deberá ser tal que: 

$$
\mathrm {M} _ {\mathrm {x}} = \mathrm {I} _ {\circ} \dot {\phi} \dot {\Psi} \quad \therefore \quad \dot {\Psi} = \frac {\mathrm {M} _ {\mathrm {x}}}{\mathrm {I} _ {\circ} \dot {\phi}}
$$

Que nos proporciona la relación entre la rotación propia y la precesión para la situación en consideración. 

Considerando ahora aquella situación en la que el ángulo de nutación sea diferente a $9 0 ^ { \circ }$ , de la componente (x) de la ecuación de momentos resulta que la velocidad de precesión deberá ser tal que: 

$$
\dot {\Psi} = \frac {I _ {\circ} \dot {\phi}}{2 (I - I _ {\circ}) \cos \theta} \left[ 1 \pm \left\{1 - \frac {4 M _ {x} (I - I _ {\circ}) \cos \theta}{I _ {\circ} ^ {2} \dot {\phi} ^ {2} \sin \theta} \right\} ^ {1 / 2} \right]
$$

Que acepta solución real, si y solo si: 

$$
\mathrm {M} _ {\mathrm {x}} \leq \frac {\mathrm {I} _ {\circ} ^ {2}}{4 \left(\mathrm {I} - \mathrm {I} _ {\circ}\right)} \dot {\phi} ^ {2} \operatorname {t g} \theta
$$

En cuyo caso luego de desarrollar el radicando de la anterior en serie de potencias, resulta: 

$$
\dot {\Psi} = \frac {\mathrm {I} _ {\circ} \dot {\phi}}{2 (\mathrm {I} - \mathrm {I} _ {\circ}) \cos \theta} \left[ 1 \pm \left\{1 - \frac {2 \mathrm {M} _ {\mathrm {x}} (\mathrm {I} - \mathrm {I} _ {\circ}) \cos \theta}{\mathrm {I} _ {\circ} ^ {2} \dot {\phi} ^ {2} \sin \theta} + \dots \dots \dots \dots \right\} ^ {1 / 2} \right]
$$

Considerando ahora aquellas situaciones en las que la rotación propia toma valores grandes y despreciando en la anterior los términos de mayor orden, obtenemos las expresiones siguientes como soluciones de nuestro problema, correspondientes a una precesión lenta y rápida, respectivamente. 

Lenta 

$$
\dot {\Psi} = \frac {M _ {x}}{I _ {o} \dot {\phi} s e n \theta}
$$

Rápida 

$$
\dot {\Psi} = \frac {I _ {\circ} \dot {\phi}}{(I - I _ {\circ}) \cos \theta}
$$

Que indudablemente estarán asociadas con dos estados energéticos diferentes, en los que se podrá encontrar el sistema. 

Nuevamente se recomiendo el video Giroscopo.avi, donde podrá observar la precesión estacionaria a $9 0 ^ { \circ }$ de un giróscopo sometido a un momento no nulo. 