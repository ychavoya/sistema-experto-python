from experta import KnowledgeEngine, Rule, AND, OR, NOT, MATCH
from facts import *


class RecomendadorAgares(KnowledgeEngine):

    def _preguntar_y_declarar(self, pregunta, lista, factClass):
        print(f'\n{pregunta}')
        print('Escribir todo lo que coincida, separado por comas, o presiona ENTER si no estás seguro o ninguno coincide')
        for idx, item in enumerate(lista):
            print(f'\t{idx}: {item}')

        while True:
            entrada = input('> ')
            if len(entrada) == 0:
                break
            try:
                items = entrada.split(',')
                for item in items:
                    self.declare(factClass(lista[int(item)]))
                break
            except ValueError or IndexError:
                print(f'Entrada no válida, volver a intentar')

        self.declare(Preguntado(factClass))

    def _preguntar_uno_y_declarar(self, pregunta, lista, factClass):
        print(f'\n{pregunta}')
        print('Escribir una sola opción')
        for idx, item in enumerate(lista):
            print(f'\t{idx}: {item}')

        while True:
            entrada = input('> ')
            if len(entrada) == 0:
                break
            try:
                self.declare(factClass(lista[int(entrada)]))
                break
            except ValueError or IndexError:
                print(f'Entrada no válida, volver a intentar')

        self.declare(Preguntado(factClass))


    # ======================================
    # Declarar Facts
    # ======================================

    @Rule(
        AND(
            NOT(Preguntado(Procedimiento)),
            NOT(Recomendacion()),
        ),
        salience=30
    )
    def preguntar_procedimiento(self):
        self._preguntar_y_declarar('¿Qué procedimiento desea realizar?', Procedimiento.list, Procedimiento)

    @Rule(
        AND(
            NOT(Preguntado(Medio)),
            NOT(Recomendacion()),
        ),
        salience=40
    )
    def preguntar_medio(self):
        self._preguntar_y_declarar('¿Qué medio desea utilizar?', Medio.list, Medio)

    @Rule(
        AND(
            Procedimiento('Aislamiento'),
            NOT(Preguntado(Aislamiento)),
            NOT(Recomendacion()),
        )
    )
    def preguntar_aisla(self):
        self._preguntar_y_declarar('¿Qué desea aislar?', Aislamiento.list, Aislamiento)

    @Rule(
        AND(
            Procedimiento('Prueba diferencial'),
            NOT(Preguntado(PruebaDiferencial)),
            NOT(Recomendacion()),
        )
    )
    def preguntar_diferencial(self):
        self._preguntar_y_declarar('¿Qué prueba(s) desea realizar?', PruebaDiferencial.list, PruebaDiferencial)


    # ======================================
    # Descartar opciones
    # ======================================

    @Rule(
        AND(
            Procedimiento('Aislamiento'),
            Aislamiento('Salmonella'),
            NOT(Preguntado(Salmonella)),
            NOT(Recomendacion()),
        )
    )
    def preguntar_salmonella(self):
        self._preguntar_uno_y_declarar('¿Qué prueba de salmonella se realizará?', Salmonella.list, Salmonella)

    # ======================================
    # Recomendaciones
    # ======================================

    @Rule(
        AND(
            Medio('Agar'),
            OR(
                Aislamiento('Gram-'),
            ),
        )
    )
    def mac_conkey(self):
        self.declare(Recomendacion('Agar MacConkey'))

    @Rule(
        AND(
            Medio('Agar'),
            OR(
                Aislamiento('Neisseria gonorrhoeae y Neisseria meningitidis'),
            ),
        )
    )
    def chocolate(self):
        self.declare(Recomendacion('Agar chocolate'))

    @Rule(
        AND(
            Medio('Agar'),
            OR(
                Aislamiento('Hongos, levaduras y mohos'),
            ),
        )
    )
    def saboruraud(self):
        self.declare(Recomendacion('Agar Sabouraud'))

    @Rule(
        AND(
            Medio('Caldo'),
            OR(
                Aislamiento('Bacterias con enzima tetrationato reductasa'),
            ),
        )
    )
    def tetrationato(self):
        self.declare(Recomendacion('Caldo tetrationato'))

    @Rule(
        AND(
            Medio('Caldo'),
            OR(
                Aislamiento('Salmonella'),
            ),
            Salmonella('Diferentes especies de salmonella'),
        )
    )
    def selenito(self):
        self.declare(Recomendacion('Caldo selenito'))

    @Rule(
        AND(
            Medio('Agar'),
            OR(
                Aislamiento('Escherichia Coli'),
            ),
        )
    )
    def emb(self):
        self.declare(Recomendacion('Agar EMB'))

    @Rule(
        AND(
            Medio('Agar'),
            OR(
                AND(
                    Aislamiento('Salmonella'),
                    Salmonella('Aguas contaminadas'),
                ),
                Aislamiento('Shigella'),
            ),
        )
    )
    def ss(self):
        self.declare(Recomendacion('Agar SS'))

    @Rule(
        AND(
            Medio('Agar'),
            OR(
                Aislamiento('Staphylococus Aureus'),
            ),
        )
    )
    def vogel_johnson(self):
        self.declare(Recomendacion('Agar Vogel-Johnson'))

    @Rule(
        AND(
            Medio('Agar'),
            OR(
                Aislamiento('Staphylococus Aureus'),
            ),
        )
    )
    def manitol_sal(self):
        self.declare(Recomendacion('Agar Manitol Sal'))

    @Rule(
        AND(
            Medio('Agar'),
            OR(
                Aislamiento('Legionella y Nocardia'),
            ),
        )
    )
    def bcye(self):
        self.declare(Recomendacion('Agar BCYE'))

    @Rule(
        AND(
            Medio('Agar'),
            OR(
                Aislamiento('Hongos Patógenos'),
            ),
        )
    )
    def bhi(self):
        self.declare(Recomendacion('Agar BHI'))

    @Rule(
        AND(
            Medio('Agar'),
            OR(
                Aislamiento('Staphylococus Aureus'),
                Aislamiento('Bacterias con Coagulasa'),
            ),
        )
    )
    def baird_parker(self):
        self.declare(Recomendacion('Agar Baird-Parker'))

    @Rule(
        AND(
            Medio('Agar'),
            OR(
                AND(
                    Aislamiento('Salmonella'),
                    Salmonella('Diferentes especies de salmonella')
                ),
            ),
        )
    )
    def verde_brillante(self):
        self.declare(Recomendacion('Agar Verde Brillante'))

    @Rule(
        AND(
            Medio('Agar'),
            OR(
                PruebaDiferencial('Capacidad hemolítica de patógenos')
            ),
        )
    )
    def sangre(self):
        self.declare(Recomendacion('Agar sangre'))

    @Rule(
        AND(
            Medio('Caldo'),
            OR(
                PruebaDiferencial('Detección de materia fecal en alimento'),
            ),
        )
    )
    def ec(self):
        self.declare(Recomendacion('Caldo EC'))

    @Rule(
        AND(
            Medio('Agar'),
            OR(
                PruebaDiferencial('Detección de Vibrio'),
            ),
        )
    )
    def tcbs(self):
        self.declare(Recomendacion('Agar TCBS'))

    @Rule(
        AND(
            OR(
                PruebaDiferencial('Determinación de degradación de azúcar'),
            ),
        )
    )
    def tsi(self):
        self.declare(Recomendacion('Medio TSI'))

    @Rule(
        AND(
            OR(
                PruebaDiferencial('Capacidad de uso de citratos como fuente de carbono'),
            ),
        )
    )
    def simmons(self):
        self.declare(Recomendacion('Citrato de Simmons'))

    @Rule(
        AND(
            Medio('Caldo'),
            OR(
                PruebaDiferencial('Capacidad de degradar la urea'),
            ),
        )
    )
    def urea(self):
        self.declare(Recomendacion('Caldo urea'))

    
    @Rule(
        AND(
            OR(
                PruebaDiferencial('Capacidad de la producción de indol'),
            ),
        )
    )
    def sim(self):
        self.declare(Recomendacion('Medio SIM'))

    # ======================================
    # Resultado
    # ======================================

    @Rule(
        AND(
            Recomendacion(MATCH.recomendacion),
            OR(
                AND(
                    Procedimiento('Aislamiento'),
                    Preguntado(Medio),
                    Preguntado(Aislamiento),
                ),
                AND(
                    Procedimiento('Prueba diferencial'),
                    Preguntado(Medio),
                    Preguntado(PruebaDiferencial),
                )
            )
        ),
        salience=100
    )
    def recomendamos(self, recomendacion):
        print('======================================')
        print(f'\nRecomendamos {recomendacion}')
        desc = Recomendacion.descriptions[recomendacion]
        if desc:
            print(f'\n{desc}')

    # No hay recomendaciones y ya preguntamos
    @Rule(
        AND(
            NOT(Recomendacion()),
        ),
        salience=-100
    )
    def no_recomendamos(self):
        print('======================================')
        print(f'\nNo podemos recomendar un medio específico')
