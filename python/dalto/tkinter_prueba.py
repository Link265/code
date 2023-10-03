#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 13:57:39 2023

@author: Link
"""

import tkinter as tk

# Crear la ventana
ventana = tk.Tk()
ventana.title("Mi ventana")

# Crear un botón
boton = tk.Button(ventana, text="Haz clic aquí")

# Posicionar el botón en la ventana
boton.pack()

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()