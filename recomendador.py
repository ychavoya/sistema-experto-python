from experta import KnowledgeEngine, Rule, AND, OR, NOT, MATCH
from facts import Inhibe, Estimula, Enfermedad, Recomendacion, Preguntado


class RecomendadorAgares(KnowledgeEngine):

    def _preguntar_y_declarar(self, pregunta, lista, factClass):
        print(f'\n{pregunta}')
        print('Escribir todo lo que coincida, separado por comas, ENTER para ninguno')
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
            NOT(Preguntado(Inhibe)),
            NOT(Recomendacion()),
        )
    )
    def preguntar_inhibe(self):
        self._preguntar_y_declarar('¿Qué desea inhibir?', Inhibe.list, Inhibe)

    @Rule(
        AND(
            NOT(Preguntado(Estimula)),
            NOT(Recomendacion()),
        )
    )
    def preguntar_estimula(self):
        self._preguntar_y_declarar('¿Qué desea estimular?', Estimula.list, Estimula)

    @Rule(
        AND(
            NOT(Preguntado(Enfermedad)),
            NOT(Recomendacion()),
        )
    )
    def preguntar_enfermedad(self):
        self._preguntar_y_declarar('¿Qué enfermedad(es) desea estudiar?', Enfermedad.list, Enfermedad)

    # ======================================
    # Recomendaciones
    # ======================================

    @Rule(
        AND(
            Inhibe('Gram+'),
            Estimula('Gram-'),
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
            OR(
                Estimula('Neisseria gonorrhoeae'),
                Estimula('Neisseria meningitidis'),
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
        salience=1
    )
    def recomendamos(self, recomendacion):
        print('======================================')
        print(f'\nRecomendamos {recomendacion}')

    # No hay recomendaciones y ya preguntamos
    @Rule(
        AND(
            NOT(Recomendacion()),
            Preguntado(Inhibe),
            Preguntado(Estimula),
            Preguntado(Enfermedad)
        ),
        salience=-1
    )
    def no_recomendamos(self):
        print('======================================')
        print(f'\nNo podemos recomendar un agar específico')
