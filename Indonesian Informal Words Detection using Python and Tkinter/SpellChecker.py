from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import PhotoImage
from PIL import Image, ImageTk
from nltk.metrics.distance import edit_distance
from time import sleep
import pandas as pd
import re


class cek_kata:
    def cek(kata, data, callback):
        hasil = []
        arr_kata = kata.split()
        for i in range(len(arr_kata)):
            if arr_kata[i] in data:
                hasil.append(arr_kata[i])
            else:
                for x in data:
                    leven = edit_distance(arr_kata[i].lower(), x)
                    kesalahan = callback(leven, len(x))
                    if(kesalahan <= 35):
                        hasil.append(x)
                        break

        return hasil

class perhitungan:
    def presentase(leven, len_kata_benar):
        tingkat_kesalahan = leven / len_kata_benar * 100
        return round(tingkat_kesalahan)


class tampil_hasil:
    def tampilkan(arr_hasil, kata):

        print("============== OUTPUT ==============")
        print("")
        print("Kata : ", kata)
        print("Perbaikan : "+" ".join(arr_hasil))

        print("")
        print("")
        
class get_data:
    def getData():
        read = pd.read_csv("./data kata/data2revisi.csv")
        return read['a'].values.tolist()
    
def raise_frame(frame):
    frame.tkraise()
root = Tk()
root.geometry("800x600")
root.title(" Spell Checker ")
#root.iconbitmap("./data kata/iconspellcheck.ico")
root.configure(background="#f5f0e1")

lucida = Font(
    family = "Lucida Console",
    size = 16,
    weight = "normal",
    )

# FRAME HOMEPAGE
homepage = Frame(root)
homepage.place(x=0, y=0, width=800, height=600)
# FRAME SpellChecker
spellcheckerpage = Frame(root)
spellcheckerpage.place(x=0, y=0, width=800, height=600)


# LOGO di HOMEPAGE
#logo = PhotoImage(file = "./data kata/iconspellcheck.png")
labellogo = Label(homepage)
labeltext = Label(homepage, text = "Selamat Datang di Aplikasi Spell Checker Kami, Ketuk Tombol Spell Checker untuk Memulai")
labeltext.place(x=160, y=10)
labellogo.pack()


# Tombol untuk ke spell checker
tospellchecker =Button(homepage, text="Spell Checker", width="20", font=lucida, bg="gray", fg="white",  command=lambda: raise_frame(spellcheckerpage))
tospellchecker.place(x=250 , y = 400)


        
def final():
    text_input = inputtext.get('1.0', 'end-1c')
    data_read = get_data.getData()
    
    hasil = cek_kata.cek(text_input, data_read, perhitungan.presentase)
    output.insert(END, hasil)

def clear():
    output.delete('1.0', END)



l = Label(spellcheckerpage, text = "================= APLIKASI SPELL CHECKER / LEVENSTHEIN DISTANCE ==================")
g = Label(spellcheckerpage, text = "----------------------------------------------------------------------------------")
k = Label(spellcheckerpage, text = "                           KELOMPOK : 3                                           ")
h = Label(spellcheckerpage, text = "SILAHKAN MASUKKAN KALIMAT KE DALAM KOTAK DI BAWAH INI ",fg="gray", )

inputtext = Text(spellcheckerpage, height = 12, width = 55)    
    
output = Text(spellcheckerpage, height = 12, width = 55)
 
input_n = Entry(spellcheckerpage, width = 5)
    
display = Button(spellcheckerpage, height = 2,
                 width = 20,
                 text ="Check Kata", command = final, font = "aerial 12 bold")


delete_button = Button(spellcheckerpage, text = "Clear Output", command = clear, font = "#1e3d59", bg="salmon", fg="white")
l.pack()
g.pack()
k.pack()
h.pack()
inputtext.pack()
display.pack()
output.pack()
delete_button.pack(side = RIGHT, padx = 15, pady = 20)

# BUTTON BACK TO HOMEPAGE
btn_back = Button(spellcheckerpage, text="Back", width="5", font="Arial,(12)", \
           command=lambda: raise_frame(homepage), bg="#1e3d59", fg="white")
btn_back.place(x=10, y=550)

root.mainloop()