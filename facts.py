from experta import Fact


class Inhibe(Fact):
    list = [
        'Gram+',
        'Gram-',
    ]


class Estimula(Fact):
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


class Especificacion(Fact):
    pass


class Preguntado(Fact):
    pass


class Recomendacion(Fact):
    pass
