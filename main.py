import tkinter as tk
import fnmatch
import os
from pygame import mixer
import unittest

# функция запуска песни и присваение тексту название песни
def select():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()

# функция остановки музыки и отмены выбора песни
def stop():
    mixer.music.stop()
    listBox.select_clear('active')

# переключение на следующую песню
def next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)




# инициализация окна
root = tk.Tk()
root.title("Music mixer")
root.geometry("500x400")
root.config(bg = '#C9C9C9')

rootpath = "D:\\Downloads\music"
pattern = "*mp3"

mixer.init()

# настройка элементов формы
listBox = tk.Listbox(root, width = 100, font = "12")
listBox.pack(padx = 15, pady = 15)

label = tk.Label(root, text = '', bg = '#C9C9C9',font = "12")
label.pack()

prev = tk.Button(root, text = "Previous", height = 10, width = 10, command = back)
prev.pack(pady = 15, padx = 10, side = 'left')

play = tk.Button(root, text = "Play", height = 10, width = 10, command = select)
play.pack(pady = 15, padx = 10, side = 'left')

stop = tk.Button(root, text = "Stop", height = 10, width = 10, command = stop)
stop.pack(pady = 15, padx = 10, side = 'left')

next = tk.Button(root, text = "Next", height = 10, width = 10, command = next)
next.pack(pady = 15, padx = 10, side = 'left')

mixed = tk.Button(root, text = "Mixed", height = 10, width = 10)
mixed.pack(pady = 15, padx = 10, side = 'left')








# цикл 1) переходит в директорию 2) ищет файл с расширением mp3
#print("Запуск цикла по нахождению файлов с расширением mp3")
for main, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        # проверка правильности нахождения файлов
        #print("Название песни: ", filename)
        listBox.insert('end', filename)




# зацикливание формы, чтобы не закрылась
root.mainloop()



