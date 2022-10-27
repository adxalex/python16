import os
from pathlib import Path, PureWindowsPath

#carpeta = Path('C:/adx/programador/python/Curso/Dia 6/testdirectorio')
#archivo = carpeta / 'otro.txt'

carpeta = Path('C:/adx/programador/python/Curso/Dia 6/testdirectorio/otro.txt')

ruta_windows = PureWindowsPath(carpeta)

print(ruta_windows)

# print(carpeta.read_text())
# print(carpeta.name)
# print(carpeta.suffix)
# print(carpeta.stem)

# if not carpeta.exists():
#     print("No existe")
# else:
#     print("Genial")