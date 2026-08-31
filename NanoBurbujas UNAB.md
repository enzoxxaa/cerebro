- ¿Gas o PFC? ¿O ambos como ramas? -> PFC: perfluorocarbono
- ¿Cuáles fueron los cálculos de capacidad de carga? La propuesta dice que ya los hicieron y definen tus restricciones de diseño.
- ¿La priorización de péptidos la tomo yo o hay alguien más? Es otro conjunto de habilidades (docking proteína-péptido) y define si tu tesis es interfaces o es mixta.

Que campo de fuerza siula mejor las interacciones gas-gas, y gas-liquido
Gas, gas liquido? No estado semi estacionario gas y liquido.
Potencial z negativo -> hidroxilo? buscar simulaciones
Para revisar la nanoburbuja se ocupa laser -> fenomeno de refraccion, el tamaño se mide a partir de la trayectoria de las nanoburbujas.
NAMD -> restraint esfericos, la formacion es por proceso de cavitacion (generación de burbuja de vacio), este proceso dura del orden de los microsegundos.
Oxigeno tiene mejor difusión en agua que el mismo agua, por lo que al soltar los restraints se llena el vacio con agua.
Tamaño de la interfaz es del orden de 20 angstrom (parecido a capa lipidica)

Desafios:
Interaccion molecula-molecula; molecula-gas. FAse agua-gas es donde con qm se ve el pozo de T4. 
Gas es hidrofobico, permeabiliza membrana a T4
Imaginar esto en porina -> posible eje

1. nanoburbuja de O2
2. agregar pfc a posteriori
3.  Viernes 11 am xtb

---------------------------------------------------------------
necesito:
1. entender el concepto de depositar gaussianas, entender a fondo la retroalimentación tanto estandar como en well-tempered. Se sesga es decir se aplica más fuerza a los atomos de la CV en aquellas configuraciones menos visitadas/mayor energia? 
2. revisar formula de gaussiana que aparece en las slides, no se de donde sale![[Pasted image 20260830214743.png]]
3. que es t1 < t2 < t3??![[Pasted image 20260830213401.png]]
4. que le quites protagonismo a msm matematico y ampliés termo estadistica, ademas que genere un handoff de puras formulas que aparecen en las slides, con alguna variacion de ser necesaria para blindar preguntas.
5. que tambien trate de dejar un anexo con inputs y scripts cortos modelo para correr el protocolo de metadinamica del paper, con especial enfasis en la elección y calculo de la CV con los modulos de plumed que mencionan en metodos.
6. que diga agosto 31, en español
7. darle el peso que merece y las implicancias al hecho de que no se sesgo HV2 pero si se ocupo en tica y msm para sostener la conclusion mecanistica de la humanizacion.
