import json
import subprocess
import os
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
        plugin = item.get('plugin')
        if plugin:
            button = Button(root, image=photo, command=lambda plug=plugin: on_button_click(root, plug))
        else:
            button = Button(root, image=photo)
        button.image = photo
        button.config(width=max_width, height=max_height)
        
        if i % 3 == 0 and i != 0:
            row += 1
            column = 0
        button.grid(row=row, column=column)
        column += 1
    
    root.geometry(f"{3 * max_width}x{(row + 1) * max_height}")
    root.resizable(False, False)

def on_button_click(root, plugin):
    script_path = os.path.join("docs", "Plugins", f"{plugin}.py")
    try:
        subprocess.run(["python", script_path])
    except FileNotFoundError:
        print(f"Error: Python script '{plugin}.py' not found.")
    root.destroy()

root = Tk()
root.title("HPars")

json_file_path = "docs/JSON/buttons_data.json"

create_buttons_from_json(json_file_path, root)

root.mainloop()

