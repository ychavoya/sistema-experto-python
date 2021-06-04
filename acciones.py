"""
Interfaz de consola
"""
from experto_general.engine import Engine
from tkinter import messagebox

# Motor como variable global
engine = Engine()


def insertar(nombre,prop):
    #entrada = input("Nombre de la entrada: ")
    if nombre and prop:
        entry = engine.base.get_or_add_entry(nombre)
        #print("Escriba las propiedades de la entrada, una por línea. Deje una línea vacía para terminar")
        entry.get_or_add_prop(prop)
        print(f"Entrada agregada: {entry}")
    else:
        print("No se admiten vacios")
        messagebox.showinfo(message="No se admiten valores vacios", title="Aviso")


def consultar():
    entry = engine.start()
    if entry is None:
        print("No se encontró ninguna entrada que coincida con las propiedades ingresadas")
    else:
        print(f"El resultado de la consulta es: {entry}")


def get_base_entries():
    
        
    return engine.base.entries
    #print(engine.base.entries)



def guardar(entrada):
    if entrada:
        engine.base.to_json(entrada.strip())
        messagebox.showinfo(message="El archivo fue guardado con exito", title="Guardado")
    else:
        messagebox.showinfo(message="Elije un nombre para el archivo", title="Guardado")


def cargar(entrada):
    if entrada:
        try:
            engine.base.from_json(entrada.strip())
            messagebox.showinfo(message="El archivo fue cargado con exito", title="Cargado")
        except KeyError as e:
            messagebox.showinfo(message="Archivo inválido o con formato incorrecto", title="Cargado")
            
    else:
        messagebox.showinfo(message="Elije un nombre del archivo a cargar", title="Guardado")


