from PIL import Image
import os

def combine(file_ext):
    loss = Image.open('images/loss.jpg')
    new_image = Image.new('RGB', (625, 790))
    overlay = Image.open('images/overlay.jpg')

    values = [
        {'x0': 65, 'x1': 195, 'y0': 125, 'y1': 400},
        {'x0': 400, 'x1': 475, 'y0': 145, 'y1': 260},
        {'x0': 530, 'x1': 600, 'y0': 200, 'y1': 330},
        {'x0': 50, 'x1': 130, 'y0': 480, 'y1': 770},
        {'x0': 155, 'x1': 290, 'y0': 480, 'y1': 770},
        {'x0': 375, 'x1': 475, 'y0': 440, 'y1': 600},
        {'x0': 400, 'x1': 580, 'y0': 600, 'y1': 630}
    ]

    new_image.paste(loss, (0, 0))

    for i in values:
        overlay0 = overlay.resize(
            (i['x1'] - i['x0'], i['y1'] - i['y0']), Image.ANTIALIAS)
        new_image.paste(overlay0, (i['x0'], i['y0']))

    new_image.save('static/out' + file_ext + '.jpg')