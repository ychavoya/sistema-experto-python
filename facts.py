from experta import Fact


class Inhibe(Fact):
    list = [
        'Gram+',
        'Gram-',
    ]


class Aisla(Fact):
    list = [
        'Gram-',
        'Neisseria gonorrhoeae',
        'Neisseria meningitidis',
    ]


class Enfermedad(Fact):
    list = [
        'Infección',
        'Peritonitis',
        'Tifus',
        'Cólera',
        'Peste',
        'Meningitis',
        'Gonorrea',
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


class Especificacion(Fact):
    pass


class Preguntado(Fact):
    pass


class Recomendacion(Fact):
    pass
