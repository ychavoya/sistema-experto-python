"""
Motor de inferencia
"""
from experto_general.base import BaseConocimientos


class Engine:

    def __init__(self):
        self.base = BaseConocimientos()
