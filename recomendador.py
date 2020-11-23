from experta import KnowledgeEngine, Rule, AND, OR, NOT, MATCH
from facts import Inhibe, Aisla, Enfermedad, Medio, Procedimiento, Recomendacion, Preguntado


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
        salience=20
    )
    def preguntar_medio(self):
        self._preguntar_y_declarar('¿Qué medio desea utilizar?', Medio.list, Medio)

    @Rule(
        AND(
            Procedimiento('Aislamiento'),
            NOT(Preguntado(Inhibe)),
            NOT(Recomendacion()),
        )
    )
    def preguntar_inhibe(self):
        self._preguntar_y_declarar('¿Qué desea inhibir?', Inhibe.list, Inhibe)

    @Rule(
        AND(
            Procedimiento('Aislamiento'),
            NOT(Preguntado(Aisla)),
            NOT(Recomendacion()),
        )
    )
    def preguntar_estimula(self):
        self._preguntar_y_declarar('¿Qué desea aislar?', Aisla.list, Aisla)

    @Rule(
        AND(
            Procedimiento('Aislamiento'),
            NOT(Preguntado(Enfermedad)),
            NOT(Recomendacion()),
        )
    )
    def preguntar_enfermedad(self):
        self._preguntar_y_declarar('¿Qué enfermedad(es) desea estudiar?', Enfermedad.list, Enfermedad)


    # ======================================
    # Descartar opciones
    # ======================================

    

    # ======================================
    # Recomendaciones
    # ======================================

    @Rule(
        AND(
            Medio('Agar'),
            OR(
                Inhibe('Gram+'),
                NOT(Inhibe()),
            ),
            OR(
                Aisla('Gram-'),
                NOT(Aisla()),
            ),
            OR(
                Enfermedad('Infección'),
                Enfermedad('Peritonitis'),
                Enfermedad('Tifus'),
                Enfermedad('Cólera'),
                Enfermedad('Peste'),
            )
        )
    )
    def mac_conkey(self):
        self.declare(Recomendacion('Agar MacConkey'))

    @Rule(
        AND(
            Medio('Agar'),
            OR(
                Aisla('Neisseria gonorrhoeae'),
                Aisla('Neisseria meningitidis'),
            ),
            OR(
                Enfermedad('Gonorrea'),
                Enfermedad('Meningitis'),
            )
        )
    )
    def chocolate(self):
        self.declare(Recomendacion('Agar chocolate'))

    # ======================================
    # Resultado
    # ======================================

    @Rule(
        Recomendacion(MATCH.recomendacion),
        salience=100
    )
    def recomendamos(self, recomendacion):
        print('======================================')
        print(f'\nRecomendamos {recomendacion}')

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
