import tkinter, tkSimpleDialog

root = Tkinter.Tk()
root.withdraw()

numero = tkSimpleDialog.askinteger("Entero", "Introduce un entero")
print (numero)
texto = tkSimpleDialog.askstring("Entero", "Introduce un String")
print (numero)

