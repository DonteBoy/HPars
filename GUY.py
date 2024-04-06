import json
from tkinter import *

def create_buttons_from_json(json_file, root):
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    row = 0
    column = 0
    max_width = 565
    max_height = 380
    
    for i, item in enumerate(data):
        photo = PhotoImage(file=item['image_path'])
        command = globals().get(item['command'])  # Получаем функцию по имени
        if command:
            button = Button(root, image=photo, command=command)
        else:
            button = Button(root, image=photo)
        button.image = photo
        button.config(width=max_width, height=max_height)
        
        # Расположение кнопок в зависимости от количества
        if i % 3 == 0 and i != 0:
            row += 1
            column = 0
        button.grid(row=row, column=column)
        column += 1
    
    root.geometry(f"{3 * max_width}x{(row + 1) * max_height}")
    root.resizable(False, False)

# Пример функций
def function_1():
    print("Function 1 executed.")

def function_2():
    print("Function 2 executed.")

root = Tk()
root.title("HPars")

# Путь к вашему JSON файлу
json_file_path = "docs/JSON/buttons_data.json"

# Создание кнопок из JSON файла
create_buttons_from_json(json_file_path, root)

root.mainloop()

