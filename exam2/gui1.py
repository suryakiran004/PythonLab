from breezypythongui import EasyFrame

class TempConverter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Temperature Converter")
        
        # Labels
        self.addLabel(text="Fahrenheit", row=0, column=0)
        self.addLabel(text="Celsius", row=0, column=1)
        
        # Fields
        self.fahrField = self.addFloatField(value=32.0, row=1, column=0)
        self.celField = self.addFloatField(value=0.0, row=1, column=1)
        
        # Buttons
        self.addButton(text=">>>>", row=2, column=0, command=self.computeCelsius)
        self.addButton(text="<<<<", row=2, column=1, command=self.computeFahrenheit)
        
    def computeCelsius(self):
        f = self.fahrField.getNumber()
        c = (f - 32) * 5/9
        self.celField.setNumber(c)
        
    def computeFahrenheit(self):
        c = self.celField.getNumber()
        f = (c * 9/5) + 32
        self.fahrField.setNumber(f)

if __name__ == "__main__":
    TempConverter().mainloop()