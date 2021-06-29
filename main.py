import tkinter

# main_windows = tkinter.Tk()
# main_windows.mainloop()

def main_screen():
    screen = tkinter.Tk()
    screen.geometry("700x550")
    screen.title('Aplikasi Penggandaan Suku Cadang Menggunakan Metode Regresi Linear')
    tkinter.Label(text='Silahkan Login Disini').pack()
    tkinter.Label(text='').pack()
    tkinter.Label(text=' Username').pack()
    tkinter.Entry(screen).pack()
    tkinter.Label(text='').pack()
    tkinter.Label(text='Password').pack()
    tkinter.Entry(screen).pack()
    tkinter.Label(text='').pack()
    tkinter.Button(screen, text="Login", width=10, height=1).pack()
    tkinter.Label(text='').pack()
    tkinter.Label(text='Copyright JFX CELL Ponorogo').pack()
    tkinter.Label(text='2021').pack()

    # tkinter.Label(text='SISTEM OPLIMALISASI PENGGANDAAN SUKU CADANG TELEPON SELULER', bg='grey', width='300', height='2').pack()
    # tkinter.Label(text='').pack()
    # tkinter.Label(text='Selamat Datang').pack()
    # tkinter.Label(text='di Sistem Optimalisasi Penggandaan Suku Cadang').pack()
    # tkinter.Label(text='JFX CELL Ponorogo').pack()

    
    screen.mainloop()

main_screen()