import tkinter as tk
import acciones
import interfaz.insertarbase as insertar_base
import interfaz.guardar_base as guardar_base


class Interfaz(tk.Frame):
    def __init__(self):
        root = tk.Tk()
        super().__init__(root)
        root.geometry('400x200')
        root.title('Sistema experto chidori')
        root.resizable(width=False, height=False)
        self.master = root
        self.pack()

        self.lbl_base = tk.Label(self, text="Sistema Experto python 7u7")
        self.lbl_base.pack(side="top")
        self.lbl_base.config(font=("Helvetica", 24))

        self.txt_insertar = tk.Button(self, text="Insertar", width=50, command=insertar_base.InsertarBase)
        self.txt_insertar.pack(side="top", padx=5, pady=5)

        self.txt_consultar = tk.Button(self, text="Consultar", width=50, command=acciones.consultar())
        self.txt_consultar.pack(side="top", padx=5, pady=5)

        self.txt_guardar = tk.Button(self, text="Cargar/Guardar", width=50, command=guardar_base.Guardar_base)
        self.txt_guardar.pack(side="top", padx=5, pady=5)

        self.quit = tk.Button(self, text="QUIT", width=50, fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom", padx=5, pady=5)
