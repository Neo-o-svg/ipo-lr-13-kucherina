from package import *


def show_menu():
    print(f"""Выберите действие с изображением.\n
          1) изменить размер изображения.
          2) измененить формат изображения на JPG.
          3) повернуть изображение на 45 градусов.
          4) применить фильтр повышения резкости.
          5) добавить рамку вокруг изображения с шириной 15 пикселей.
          6) закончить работу и сохранить изображение.
  """)


def check_input(input_num, available_values):

    while True:
        try:
            input_num = int(input_num)
            if input_num in available_values:
                break
            else:
                print("\nНекорректный ввод данных. Повторите ввод.\n")
                input_num = input("Введите номер пункта: ")
        except:
            print("\nНекорректный ввод данных. Повторите ввод.\n")
            input_num = input("Введите номер пункта: ")

    return input_num


def choose_picture():
    print(f"""Выберите изображение.\n
          1) пара счастливых котов.
          2) уставший кот.
          3) "счастливый" котенок.
          4) кот до нашей эры.
          5) крутой гусь и его напарник.
  """)


def get_filepath_by_num(num):
    if num == 1:
        file_path = "./images/image.jpg"
    elif num == 2:
        file_path = "./images/image_1.jpg"
    elif num == 3:
        file_path = "./images/image_2.jpg"
    elif num == 4:
        file_path = "./images/image_4.jpg"
    else:
        file_path = "./images/image_5.jpg"
    return file_path


def to_int(value):
    try:
        value = int(value)
        return value
    except:
        return False


pic_available_values = [1, 2, 3, 4, 5]
menu_available_values = [1, 2, 3, 4, 5, 6]
choose_picture()
num_of_picture = check_input(
    input("Введите номер изображения: "), pic_available_values)
file_path = get_filepath_by_num(num_of_picture)
handler = ImageHandler(file_path)
processor = ImageProcessor(file_path)
handler.load_image()
save_path = "images/new_image.jpg"

while True:
    show_menu()
    num = check_input(input("\nВведите номер пункта: "), menu_available_values)

    if num == 1:
        width = to_int(input("Введите ширину: ").strip())
        while True:
            if width:
                break
            else:
                print(
                    "\nНекорректный ввод данных.\nПовторите ввод, введите целочисленное значение.\n")
                width = to_int(input("Введите ширину: ").strip())

        height = to_int(input("Введите высоту: ").strip())
        while True:
            if height:
                break
            else:
                print(
                    "\nНекорректный ввод данных.\nПовторите ввод, введите целочисленное значение.\n")
                height = to_int(input("Введите высоту: ").strip())

        handler.resize_image(width, height)

    elif num == 2:
        handler.convert_to_jpg(save_path)

    elif num == 3:
        handler.rotate_45_degrees()

    elif num == 4:
        handler.save_image(save_path)
        processor.apply_sharpen_filter()

    elif num == 5:
        processor.add_border()

    elif num == 6:
        handler.save_image(save_path)
        break

    else:
        print("Некорректное значение пункта.\nПовторите ввод.")
