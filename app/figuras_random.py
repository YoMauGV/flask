import json,random

def figuras_random():
    figuras=[]
    nombres = ["cuadrado", "triangulo", "circulo", "pentagono"]
    colores = ["rojo", "verde", "azul", "amarillo", "negro", "blanco", "gris", "morado", "naranja", "rosa", "marrón"]
    for i in range(0, random.randint(2, 10)):
        figuras.append({
            "nombre": nombres[random.randint(0, 3)],
            "x": random.randint(0, 400),
            "y": random.randint(0, 400),
            "medida": random.randint(0, 100),
            "color": colores[random.randint(0, 9)]
        })
    return json.dumps(figuras)