
class Auto:
    name = ""
    kind = ""
    color = ""
    value = 100.320545
    _numero_serie = "kjfnasfsaqrioqoijfqw"
    def description(self):
        desc = "%s es un %s %s. Vale $%.2f" % (self.name, self.color, self.kind, self.value)
        return desc

    
car1 = Auto()
car1.name = "Nombre"
car1.color = "Rojo"
car1.value = 34323.32423434215

print(car1.description())
