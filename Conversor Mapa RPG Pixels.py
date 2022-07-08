from tkinter import *
from functools import partial

def Calcular():
    print('x:', EntradaX.get(),'\ny:', EntradaY.get(),'\nz:', EntradaZ.get())
    if(str(EntradaX.get()).isnumeric() and str(EntradaY.get()).isnumeric() and str(EntradaZ.get()).isnumeric()):
        Resultado['text'] = str(int(EntradaX.get())/int(EntradaZ.get())), X, str(int(EntradaY.get())/int(EntradaZ.get()))
    else:
        Resultado['text'] = 'Digite apenas números!'

MainWindow = Tk()
MainWindow.title('Roll20 PIXEL to MAP (R20PTM)')
MainWindow.geometry('300x380+500+100')
MainWindow['background'] = 'black'

EntradaX = Entry(MainWindow, width=15)
EntradaX.place(x=20, y=80)

EntradaY = Entry(MainWindow, width=15)
EntradaY.place(x=180, y=80)

EntradaZ = Entry(MainWindow, width=15)
EntradaZ.place(x=100, y=150)

PixelX = Label(MainWindow, bg='white', text='Pixels no ângulo X:')
PixelX.place(x=15, y=55)

PixelY = Label(MainWindow, bg='white', text='Pixels no ângulo Y:')
PixelY.place(x=175, y=55)

Aviso = Label(MainWindow, text='inverter a ordem inverte o resultado, fique atento!')
Aviso.pack(side=TOP, fill=X)

Resultado1 = Label(MainWindow, text='Crie um mapa com as seguintes dimenções:')
Resultado1.place(x=30, y=190)

Razão = Label(MainWindow, bg='white', text='Razão Pixels x Quadrado(1 lado):')
Razão.place(x=70, y=125)

Resultado = Label(MainWindow, text='Resultado', width=25)
Resultado.place(x=65, y=220)

Bt1 = Button(MainWindow, width=13, text='Calcular', command=Calcular)
Bt1.place(x=100, y=300)

MainWindow.mainloop()
