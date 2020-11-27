from experta import Fact


class Aislamiento(Fact):
    list = [
        'Gram-',
        'Neisseria gonorrhoeae y Neisseria meningitidis',
        'Hongos, levaduras y mohos',
        'Salmonella',
        'Escherichia Coli',
        'Shigella',
        'Staphylococus Aureus',
        'Legionella y Nocardia',
        'Hongos Patógenos',
        'Bacterias con Coagulasa',
        'Bacterias con enzima tetrationato reductasa',
    ]


class Salmonella(Fact):
    list = [
        'Aguas contaminadas',
        'Tipo específico de salmonella',
        'Diferentes especies de salmonella',
    ]


class PruebaDiferencial(Fact):
    list = [
        'Capacidad hemolítica de patógenos',
        'Detección de Vibrio',
        'Detección de materia fecal en alimento',
        'Determinación de degradación de azúcar',
        'Capacidad de uso de citratos como fuente de carbono',
        'Capacidad de degradar la urea',
        'Capacidad de la producción de indol',
    ]

class Medio(Fact):
    list = [
        'Caldo',
        'Agar',
    ]


class Procedimiento(Fact):
    list = [
        'Aislamiento',
        'Prueba diferencial',
    ]


class Preguntado(Fact):
    pass


class Recomendacion(Fact):
    descriptions = {
        'Agar MacConkey': 'El agar MacConkey es un medio de cultivo que inhibe el crecimiento de las bacterias gram positivas y estimula la reproducción de los bacilos gram negativos, los cuales suelen estar detrás de infecciones urinarias, diarreas, enfermedades gastrointestinales, bacteriemias (bacterias en la sangre), peritonitis e incluso el tifus, el cólera o la peste.',
        'Agar chocolate': 'El agar chocolate es el medio de cultivo que se obtiene al calentar el agar sangre. Sea como sea, el más utilizado es aquel en el que se añade vancomicina (un antibiótico) y distintos nutrientes para estimular el crecimiento únicamente de “Neisseria gonorrhoeae” y “Neisseria meningitidis”, bacterias responsables de la gonorrea y meningitis, respectivamente.',
        'Agar Sabouraud': 'El agar Sabouraud es un medio de enriquecimiento y aislamiento de distintas especies de hongos, levaduras y mohos. Por lo tanto, es útil cuando no queremos detectar bacterias (de hecho, tienen distintos antibióticos para impedir su desarrollo), sino este tipo de microorganismos, sean patógenos o no.',
        'Caldo tetrationato': 'El caldo tetrationato es un medio líquido (a diferencia de los agares sólidos que hemos ido viendo) que contiene sales biliares y otras sustancias inhibitorias que impiden el desarrollo de las bacterias gram positivas y el de algunas gram negativas, pues solo nos interesa que crezcan las bacterias que disponen de una enzima determinada, que es la tetrationato reductasa (de ahí el nombre). Este medio de cultivo es muy útil, pues, para el aislamiento de colonias de “Salmonella”, responsable de enfermedades de transmisión alimentaria.',
        'Caldo selenito': 'El caldo selenito es otro medio de cultivo líquido para el aislamiento de “Salmonella”, aunque en este caso su método de acción no se basa en detectar la enzima anterior, sino en inhibir (mediante el selenito) el crecimiento de otras bacterias presentes en nuestro tracto digestivo.',
        'Agar EMB': 'El agar EMB es un medio de cultivo sólido muy útil para el aislamiento de enterobacterias, es decir, aquellas que habitan de forma natural nuestros intestinos pero que, ante determinadas situaciones, pueden pasar a comportarse como patógenos. “Escherichia coli” es el claro ejemplo de ello, y, además, este medio permite que se observen claramente sus colonias, las cuales desarrollan un color brillante negro verdoso.',
        'Agar SS': 'El agar SS es un medio de cultivo sólido utilizado para el aislamiento de, además de “Salmonella”, “Shigella”, una bacteria que normalmente se contagia a través de alimentos o agua contaminada y que provoca una infección que cursa con diarrea (la cual suele contener sangre), fiebre y dolor abdominal.',
        'Agar Vogel-Johnson': 'El agar Vogel-Johnson es un medio de cultivo sólido diseñado para el aislamiento de “Staphylococcus aureus”, una bacteria que puede causar muchos tipos de infecciones distintas, desde enfermedades de la piel (es lo más común) hasta infecciones óseas, pasando por neumonías, bacteriemias, endocarditis (infección del corazón) e intoxicaciones alimentarias. Inhibe el crecimiento de todas las gram negativas y el de algunas gram positivas.',
        'Agar Manitol Sal': 'El agar manitol sal, también conocido como manitol salado, es un medio de cultivo sólido que sigue siendo utilizado para el aislamiento de “Staphylococcus aureus”, aunque en este caso el poder inhibitorio sobre el resto de bacterias es más fuerte. Es decir, es más selectivo que el anterior',
        'Agar BCYE': 'El agar BCYE es un medio de cultivo sólido especialmente diseñado para el aislamiento de “Legionella” y “Nocardia”, dos géneros de bacterias responsables de una neumonía grave (potencialmente mortal) y de una infección pulmonar que puede diseminar, en personas inmunodeprimidas, a otros órganos (piel, cerebro, corazón…), respectivamente.',
        'Agar BHI': 'El agar BHI es un medio de cultivo sólido que vuelve a ser útil para el aislamiento de hongos, aunque en este caso se centra en la detección de aquellos que actúan como patógenos. De nuevo, dispone de varios antibióticos para inhibir el crecimiento de las bacterias.',
        'Agar Baird-Parker': 'El agar Baird-Parker es un medio de cultivo sólido diseñado para el aislamiento de “Staphylococcus aureus”, aunque en este caso permite el crecimiento de otras especies de estafilococos, siempre que sean coagulasa positivos, es decir, que dispongan de esta enzima conocida como coagulasa.',
        'Agar Verde Brillante': 'El verde brillante es una sustancia inhibidora que impide el crecimiento de todas las bacterias gram positivas y de la mayoría de gram negativas. En este sentido, el agar verde brillante es un medio de cultivo sólido utilizado para el aislamiento de distintas especies de “Salmonella”',
        'Agar sangre': 'Como su propio nombre indica, el agar sangre dispone de sangre en su composición, la cual suele ser de ovejas, caballos o, a veces, humanos. Es utilizado para estudiar la función hemolítica de distintos patógenos, es decir, su capacidad para destruir los eritrocitos (glóbulos rojos) cuando circulan por el torrente sanguíneo. Dependiendo de lo que añadamos, permitirá el crecimiento de unas especies concretas, siendo un medio muy selectivo.',
        'Caldo EC': 'El caldo EC es un medio de cultivo líquido diseñado para permitir el crecimiento de coliformes, un grupo de distintos géneros de bacterias que sirven como indicador de la contaminación fecal tanto de aguas como de alimentos.',
        'Agar TCBS': 'El agar TCBS es un medio de cultivo sólido que contiene Tiosulfato, Citrato y Sales Biliares. De ahí el nombre. Sea como sea, estas sustancias estimulan el crecimiento selectivo de distintas especies de “Vibrio”, un género bacteriano que provoca enfermedades gastrointestinales y donde destaca “Vibrio cholerae”, responsable del cólera.',
        'Medio TSI': 'El medio TSI es un medio de cultivo diferencial en el que se busca determinar la capacidad de la bacteria para degradar el azúcar y formar gas y sulfuros de hidrógeno. Dependiendo de lo que observemos (hay perfiles que nos permiten comparar y saber ante qué nos encontramos), podremos determinar qué bacteria había en la muestra.',
        'Citrato de Simmons': 'El citrato de Simmons es un medio de cultivo diferencial útil para, valga la redundancia, diferenciar entre distintas especies de coliformes. El medio se basa en determinar la capacidad de las bacterias para utilizar el citrato como fuente de carbono. Si no es capaz de usarlo, el medio se mantendrá verde. Pero si es capaz, pasará a ser azul',
        'Caldo urea': 'El caldo urea es un medio de cultivo diferencial que permite, de nuevo, diferenciar entre distintas especies. Se basa en determinar la capacidad de la bacteria de degradar la urea. Si la bacteria tiene la enzima necesaria, el color pasará a ser rojo, mientras que si no dispone de ella, se mantendrá en el color original.',
        'Medio SIM': 'El medio SIM es un medio de cultivo diferencial que determina la capacidad de la bacteria para formar indol (un compuesto químico orgánico), producir sulfuro de hidrógeno y moverse. Dependiendo del perfil obtenido, estaremos ante una especie u otra.',
    }
