from PIL import ImageDraw, ImageFont, ImageFilter, Image


class ImageProcessor:
    def __init__(self, image):

        self.image = image

# ------- Метод для применения фильтра к изображению -------
    def apply_filter(self, filter_type):

        if self.image:
            try:
                self.image = self.image.filter(filter_type)
                print(f"Фильтр {filter_type} успешно применён.")
            except:
                print(f"Ошибка при применении фильтра")
        else:
            print("Нет изображения для применения фильтра.")


# ------- Метод для добавления текста на изображение. -------

    def add_text(self, text, position, font_path="../fonts/RobotoMono-VariableFont_wght.ttf", font_size=20, color="black"):

        if self.image:
            try:
                # Создаём объект для рисования на изображении
                draw = ImageDraw.Draw(self.image)
                # Загружаем шрифт с указанными параметрами.
                font = ImageFont.truetype(font_path, font_size)
                # Добавляем текст на изображение.
                draw.text(position, text, fill=color, font=font)
                print("Текст успешно добавлен на изображение.")
            except:
                print(f"Ошибка при добавлении текста")
        else:
            print("Нет изображения для добавления текста.")

# ------- Метод для поворота изображения на заданный угол -------
    def rotate_image(self, angle):

        if self.image:
            # Поворачиваем изображение и расширяем холст.
            self.image = self.image.rotate(angle, expand=True)
            print(f"Изображение повернуто на {angle} градусов.")
        else:
            print("Нет изображения для поворота.")


# ------- Метод для применения фильтра повышения резкости -------

    def apply_sharpen_filter(self):
        self.apply_filter(ImageFilter.SHARPEN)
       

# ------- Метод для добавления рамки вокруг изображения -------

    def add_border(self, border_width=15, color="black"):
        if self.image:
            try:
                width, height = self.image.size
                new_width = width + 2 * border_width
                new_height = height + 2 * border_width
                new_image = Image.new("RGB", (new_width, new_height), color)
                new_image.paste(self.image, (border_width, border_width))
                self.image = new_image
                print(f"Рамка шириной {border_width}px успешно добавлена к изображению.")
            except:
                print(f"Ошибка при добавлении рамки к изображению")
        else:
            print("Нет изображения для добавления рамки.")


# ------- Метод для получения обработанного изображения -------

    def get_processed_image(self):
        """
        Получение обработанного изображения.
        :return: объект изображения
        """
        return self.image
