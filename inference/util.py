from PIL import ImageDraw, ImageFont


def draw_rect(text, text_size, face, draw, font, margin, color='green'):
    # bounding box
    draw.rectangle(
        (
            (int(face.bb.left), int(face.bb.top)),
            (int(face.bb.right), int(face.bb.bottom))
        ),
        outline=color,
        width=2
    )

    # text background
    draw.rectangle(
        (
            (int(face.bb.left - margin), int(face.bb.bottom) + margin),
            (int(face.bb.left + text_size[0] + margin), int(face.bb.bottom) + text_size[1] + 3 * margin)
        ),
        fill='black'
    )

    # text
    draw.text(
        (int(face.bb.left), int(face.bb.bottom) + 2 * margin),
        text,
        font=font
    )


def draw_bb_on_img(faces, img):
    draw = ImageDraw.Draw(img)
    fs = max(20, round(img.size[0] * img.size[1] * 0.000005))
    font = ImageFont.truetype('fonts/font.ttf', fs)
    margin = 5

    for face in faces:
        if face.top_prediction.confidence > 0.95:
            text = "%s %.2f%%" % (face.top_prediction.label.upper(), face.top_prediction.confidence * 100)
            text_size = font.getsize(text)
            draw_rect(text, text_size, face, draw, font, margin, color='green')

        else:
            text = 'Unkown'
            text_size = font.getsize(text)
            draw_rect(text, text_size, face, draw, font, margin, color='blue')
        
