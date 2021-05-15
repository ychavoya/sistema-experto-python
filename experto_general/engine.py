from typing import List
from experto_general.base import BaseConocimientos
from experto_general.entry import Entry
from experto_general.property import Property
from experto_general.response import Response


class Engine:
    """
    Motor de inferencia
    """

    def __init__(self):
        """
        Inicializa una instancia de motor de inferencia
        """
        self.base = BaseConocimientos()
        self.accepted_properties: List[Property] = []
        self.denied_properties: List[Property] = []
    
    def start(self) -> Entry:
        """
        Obtener una entrada en base a propiedades que ingrese el usuario

        :return: Entrada que coincida con las propiedades. None si no coincide ninguna
        """
        self.accepted_properties: List[Property] = []
        self.denied_properties: List[Property] = []

        for entry in self.base.entries:

            correct_entry = True

            if self._check_rule_2(entry) is False:
                continue

            if self._check_rule_3(entry) is False:
                continue

            for property in entry.properties:
                if self._check_rule_1(property) is False:
                    continue
                
                response = self._get_user_response(property)
                if response == Response.YES:
                    self.accepted_properties.append(property)
                else:
                    self.denied_properties.append(property)
                    correct_entry = False
                    break
            
            if correct_entry is True:
                return entry

        return None

    def _check_rule_1(self, property: Property) -> bool:
        """
        Verificar 1ra regla. Que una propiedad no haya sido preguntada anteriormente

        :param property:
        :return: Verdadero si se cumple la regla
        """        
        return (property not in self.accepted_properties and 
                property not in self.denied_properties)

    def _check_rule_2(self, entry: Entry) -> bool:
        """
        Verificar 2da regla. Que una entrada tenga todas las propiedades requeridas

        :param entry:
        :return: Verdadero si se cumple la regla
        """
        for property in self.accepted_properties:
            if property not in entry.properties:
                return False
        return True

    def _check_rule_3(self, entry: Entry) -> bool:
        """
        Verificar 3ra regla. Que una entrada no tenga propiedades rechazadas

        :param entry:
        :return: Verdadero si se cumple la regla
        """
        for property in self.denied_properties:
            if property in entry.properties:
                return False
        return True

    # Método temporal para usar sólo con CLI
    def _get_user_response(self, property: Property) -> Response:
        """
        Obtener confirmación del usuario si cierta propiedad debe ser considerada

        :param property: Propiedad a preguntar
        :return: Respuesta de confirmación o rechazo
        """
        prompt_str = "¿Es/Tiene " + property.name + "? (s/n): "
        response = input(prompt_str).strip().lower()

        while response != 's' and response != 'n':
            prompt_str = "Ingrese una respuesta válida (s/n): "
            response = input(prompt_str).strip().lower()
        
        if response == 's':
            return Response.YES
        return Response.NO
