from PIL import Image


class ImageHandler:

    def __init__(self, file_path):
        self.file_path = file_path
        self.image = None


# ------- Метод для загрузки изображения из файла ------

    def load_image(self):

        try:
            self.image = Image.open(self.file_path)
            print("Изображение успешно загружено.")
        except:
            print(f"Ошибка при загрузке изображения")

# ------- Метод для сохранения изображения на диск -------
    def save_image(self, save_path, format=None):

        if self.image:
            try:
                self.image.save(save_path, format=format)
                print(f"Изображение сохранено по пути: {save_path}")
            except:
                print(f"Ошибка при сохранении изображения")
        else:
            print("Изображения для сохранения не было найдено.")


# ------- Метод для изменения размера изображения -------

    def resize_image(self, width, height):

        if self.image:
            self.image = self.image.resize((width, height))
            print(f"Размер изображения изменён на {width}x{height}.")
        else:
            print("Нет изображения для изменения размера.")

    # ------- Метод для изменения формата изображения на JPG -------

    def convert_to_jpg(self, save_path):
        if self.image:
            try:
                rgb_image = self.image.convert('RGB')
                rgb_image.save(save_path, format='JPEG')
                print(f"""Изображение было преобразовано в формат JPG и сохранено по пути: {
                      save_path}""")
            except:
                print(f"Ошибка при конвертации в JPG")
        else:
            print("Нет изображения для конвертации.")

    # ------- Метод для поворота изображения на 45 градусов -------

    def rotate_45_degrees(self):
        if self.image:
            # Поворачиваем изображение на 45 градусов с расширением холста.
            self.image = self.image.rotate(45, expand=True)
            print("Изображение повернуто на 45 градусов.")
        else:
            print("Нет изображения для поворота.")

    # ------- Метод для получения текущего изображения -------

    def get_image(self):

        return self.image


