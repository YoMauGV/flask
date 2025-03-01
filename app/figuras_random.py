import json,random

def figuras_random():
    figuras=[]
    nombres = ["cuadrado", "triangulo", "circulo", "pentagono"]
    colores = ["negro", "rojo", "rojo oscuro", "verde", "verde oscuro", "azul", "azul oscuro", "cian", "cian oscuro", "magenta", "magenta oscuro", "amarillo", "amarillo oscuro", "gris", "gris oscuro", "gris claro"]
    for i in range(0, random.randint(2, 10)):
        figuras.append({
            "nombre": nombres[random.randint(0, 3)],
            "x": random.randint(0, 700),
            "y": random.randint(0, 700),
            "medida": random.randint(0, 100),
            "color": colores[random.randint(0, 15)]
        })
    return json.dumps(figuras)