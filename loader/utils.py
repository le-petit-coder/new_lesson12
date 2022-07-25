def save_picture(picture):
    filename = picture.filename
    path = f'./uploads/{filename}'
    picture.save(path)
    return path
