from pathlib import Path

#base = Path.home()
#ruta = Path(base, "Curso Python", Path("Día 6", "practicas_path.py"))

#print(ruta)
#ruta_absoluta =
#print(ruta_absoluta)



#guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada_Familia.txt"))
#guia2 = guia.with_name("La_Pedrera.txt")

#guia = Path(Path.home(), "Europa")


# guia = Path("Europa", "españa", "Barcelona", "Sagrada_Familia.txt")
# en_europa = guia.relative_to(Path("Europa"))
# en_espania = guia.relative_to(Path("Europa", "España"))
#
# print(en_europa)
# print(en_espania)

# Encuentra todos los .txt dentro de la carpeta Europa
guia = Path("Europa")
for txt in guia.glob("*.txt"):
    print(txt)



# Encuentra todos los .txt dentro de la carpeta Europa incluyendo los txt de las subcarpetas
# for txt in Path(guia).glob("**/*.txt"):
#     print(txt)



#print(guia)
#print(guia2)

# pones parent mientras mas adentro quieras llegar en el directorio.
#print(guia.parent.parent)