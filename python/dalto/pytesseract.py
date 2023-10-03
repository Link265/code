#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 14:03:51 2023

@author: Link
"""

from pytesseract import image_to_string as a 
import pytesseract as p
from PIL import Image

# Cargar la imagen
imagen = Image.open("matriz1.png")

# Convertir la imagen a texto utilizando Tesseract OCR
texto = a(imagen)

# Imprimir el texto
print(texto)



