from tkinter import *
from types import coroutine 

ventana = Tk()
ventana.title("Calculadora")

#Pantalla de la calculadora
pantalla_calculadora = Entry(ventana, font=("Calibri 20"), state='normal')
pantalla_calculadora.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

i = 0
#Funciones de la calculadora
def click_boton(valor):
    global i
    pantalla_calculadora.insert(i, valor)
    i += 1

def borrar():
    pantalla_calculadora.delete(0, END)
    i = 0

def resolver_operaciones():
    ecuacion = pantalla_calculadora.get()
    resultado = eval(ecuacion)
    pantalla_calculadora.delete(0, END)
    pantalla_calculadora.insert(0, resultado)
    i = 0
#Botones Numericos de la Calculadora
boton1 = Button(ventana, text="1", width=5, height=2, command= lambda:click_boton(1))
boton2 = Button(ventana, text="2", width=5, height=2, command= lambda:click_boton(2))
boton3 = Button(ventana, text="3", width=5, height=2, command= lambda:click_boton(3))
boton4 = Button(ventana, text="4", width=5, height=2, command= lambda:click_boton(4))
boton5 = Button(ventana, text="5", width=5, height=2, command= lambda:click_boton(5))
boton6 = Button(ventana, text="6", width=5, height=2, command= lambda:click_boton(6))
boton7 = Button(ventana, text="7", width=5, height=2, command= lambda:click_boton(7))
boton8 = Button(ventana, text="8", width=5, height=2, command= lambda:click_boton(8))
boton9 = Button(ventana, text="9", width=5, height=2, command= lambda:click_boton(9))
boton0 = Button(ventana, text="0", width=15, height=2, command= lambda:click_boton(0))

#Botones de simbolos
boton_borrar = Button(ventana, text="AC", width=5, height=2, command=lambda: borrar())
boton_abrir_parentesis = Button(ventana, text="(", width=5, height=2, command= lambda:click_boton("("))
boton_cerrar_parentesis = Button(ventana, text=")", width=5, height=2, command= lambda:click_boton(")"))
boton_coma = Button(ventana, text=",", width=5, height=2, command= lambda:click_boton("."))

#Botones de operadores aritmeticos
boton_div = Button(ventana, text=u"\u00F7", width=5, height=2, command= lambda:click_boton("/"))
boton_multi = Button(ventana, text="x", width=5, height=2, command= lambda:click_boton("*"))
boton_suma = Button(ventana, text="+", width=5, height=2, command= lambda:click_boton("+"))
boton_resta = Button(ventana, text="-", width=5, height=2, command= lambda:click_boton("-"))
boton_igual = Button(ventana, text="=", width=5, height=2, command= lambda:resolver_operaciones())

#Agregar los botones a la calculadora

#==================== FILA 1 ====================#
boton_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_abrir_parentesis.grid(row=1, column=1, padx=5, pady=5)
boton_cerrar_parentesis.grid(row=1, column=2, padx=5, pady=5)
boton_div.grid(row=1, column=3, padx=5, pady=5)

#==================== FILA 2 ====================#
boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
boton_multi.grid(row=2, column=3, padx=5, pady=5)

#==================== FILA 3 ====================#
boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_suma.grid(row=3, column=3, padx=5, pady=5)

#==================== FILA 4 ====================#
boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton_resta.grid(row=4, column=3, padx=5, pady=5)

#==================== FILA 5 ====================#
boton0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
boton_coma.grid(row=5, column=2, padx=5, pady=5)
boton_igual.grid(row=5, column=3, padx=5, pady=5)

ventana.mainloop()