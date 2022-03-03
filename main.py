import tkinter as tk
import fnmatch
import os
from pygame import mixer
import unittest


root = tk.Tk()
root.title("Music mixer")
root.geometry("500x400")
root.config(bg = '#C9C9C9')

rootpath = "D:\\Downloads\music"
pattern = "*mp3"

listBox = tk.Listbox(root, width = 100, font = "12")
listBox.pack(padx = 15, pady = 15)

label = tk.Label(root, text = '', bg = '#C9C9C9',font = "12")
label.pack()

prev = tk.Button(root, text = "Previous", height = 10, width = 10)
prev.pack(pady = 15, padx = 20, side = 'left')

play = tk.Button(root, text = "Play", height = 10, width = 10)
play.pack(pady = 15, padx = 20, side = 'left')

next = tk.Button(root, text = "Next", height = 10, width = 10)
next.pack(pady = 15, padx = 20, side = 'left')

mix = tk.Button(root, text = "Mix", height = 10, width = 10)
mix.pack(pady = 15, padx = 20, side = 'left')





# цикл 1) переходит в директорию 2) ищет файл с расширением mp3
#print("Запуск цикла по нахождению файлов с расширением mp3")
for main, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        # проверка правильности нахождения файлов
        #print("Название песни: ", filename)
        listBox.insert('end', filename)





root.mainloop()



