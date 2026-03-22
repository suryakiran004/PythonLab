from breezypythongui import EasyFrame

class TempConverter(EasyFrame):
    def __init__(self):
        super().__init__(title="Temp Converter")

        self.addLabel(text="F", row=0, column=0)
        self.addLabel(text="C", row=0, column=1)

        self.f = self.addFloatField(32.0, row=1, column=0)
        self.c = self.addFloatField(0.0, row=1, column=1)

        self.addButton("F→C", row=2, column=0, command=self.f_to_c)
        self.addButton("C→F", row=2, column=1, command=self.c_to_f)

    def f_to_c(self):
        self.c.setNumber((self.f.getNumber() - 32) * 5/9)

    def c_to_f(self):
        self.f.setNumber(self.c.getNumber() * 9/5 + 32)

TempConverter().mainloop()