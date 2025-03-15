from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
import weather

def dibuja(ciudad):
    clima = weather.Clima()
    datos_clima = clima.extrae_relevantes(ciudad)

    if datos_clima['icono'][-1] == 'd':
        fondo = Color('lightblue')
    else:
        fondo = Color('darkblue')

    with Drawing() as draw:
        draw.stroke_color = Color('black')
        draw.stroke_width = 2
        draw.fill_color = Color('white')
        if datos_clima['icono'] == '01d':
            draw.circle((50, 50), # Center point
                    (25, 25))
        else:
            draw.rectangle(left=10, top=10, right=40, bottom=40)

        with Image(width=400, height=300, background = fondo) as image:
            draw.font = 'assets/fonts/UbuntuMono-Regular.ttf'
            draw.stroke_color = Color('white')
            draw.font_size = 24
            draw.text(150,100, datos_clima['ciudad']) 
            draw.font = 'assets/fonts/arial.ttf'
            draw.stroke_color = Color('orange')
            draw.font_size = 20
            draw.text(50,200, f"{datos_clima['temperatura']} °C") 
            draw.text(250,200, datos_clima['description']) 
            draw(image)
            image.format = 'png'
            png_bin = image.make_blob()
            return png_bin