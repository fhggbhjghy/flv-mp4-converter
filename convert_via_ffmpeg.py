import ffmpeg
import tkinter as tk
import os
from tkinter import filedialog

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames()
    return file_paths

def convert(input, output):
    (
        ffmpeg
        .input(input)
        .output(output, acodec='copy', vcodec='copy')
        .overwrite_output()
        .run()
    )

if __name__ == "__main__":
    file_paths = open_file_dialog()

    converted_directory_path = ''

    for file_path in file_paths:
        if not file_path:
            print("No file selected")
            continue

        file_path_info = file_path.rsplit('/',1)
        file_directory = file_path_info[0]
        input_file = file_path
        converted_directory_path = f'{file_directory}/converted'
        output_file = f'{converted_directory_path}/{file_path_info[-1].split('.')[0]}.mp4'

        os.makedirs(converted_directory_path, exist_ok=True)
        convert(input_file, output_file)
    
    if converted_directory_path:
        os.startfile(converted_directory_path)

    