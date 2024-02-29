from tkinter import *
import math
import sys

class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0.0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"))
        self.lbl.place(x=10, y=50)

        btns = [
            "7", "8", "9", "+", "*",
            "4", "5", "6", "-", "/",
            "1", "2", "3", "xⁿ",
            "±", ".",  "0",
             "π", "sin", "cos",
            "(", ")","C",  "=", "n!", "√", "Exit",
        ]
        self.old_calc = []

        x = 10
        y = 130
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            if bt == "=":
                Button(text=bt, bg="#ABC",
                       font=("Times New Roman", 15),
                       command=com).place(x=x, y=y,
                                          width=160,
                                          height=160)
                x += 240
            else:
                Button(text=bt, bg="#ABC",
                       font=("Times New Roman", 15),
                       command=com).place(x=x, y=y,
                                          width=80,
                                          height=80)

            if 160 < x and 450 < y < 500:
                x = 888
            x += 80
            if x > 360:
                x = 10
                y += 80


    def logarray(self,value):
        if self.formula != "0.0":
            self.formula += value
        else:
            self.formula = value
        self.update()

    def logicalc(self, operation):
        global key
        if operation == "C":
            self.formula = ""
        elif operation == "=":
            if "^" in self.formula:
                self.formula = self.formula.replace("^","**")
                self.formula = self.formula.replace("***", "**")
            if len(self.old_calc) > 5:
                self.old_calc.pop(0)
                self.old_calc.index(str(eval(self.formula)),0)
                self.formula = self.old_calc[0]
            else:
                self.old_calc.append(str(eval(self.formula)))
                self.formula = self.old_calc[-1]
        elif operation == "±":
            if "=" in self.formula:
                self.formula = ""
            if self.formula[0] == "-":
                self.formula = self.formula[1:]
            else:
                self.formula = "-"+self.formula
        elif operation == "π":
            if self.formula != "0.0":
                self.formula = self.formula + "*" + str(math.pi)
            else:
                self.formula = str(math.pi)
        elif operation == ".":
            for i in range(len(self.formula)):
                if not self.formula[i].isdigit() and self.formula[i] != ".":
                    if self.formula[i+1::].isdigit():
                        self.formula = self.formula + operation

        elif operation == "Exit":
            root.after(1, root.destroy)
            sys.exit
        elif operation == "xⁿ":
            if self.formula != "0.0":
                self.formula = self.formula + "^"

        elif operation == "sin":
            self.formula = str(math.sin(int(self.formula)))
        elif operation == "cos":
            self.formula = str(math.cos(int(self.formula)))
        elif operation == "(":
            if self.formula != "0.0":
                self.formula = self.formula + "("
        elif operation == ")":
            if self.formula != "0.0":
                self.formula = self.formula + ")"

        elif operation == "n!":
            self.formula = self.formula + str(math.factorial(int(self.formula)))

        elif operation == "√":
            self.formula = str(math.sqrt(int(self.formula)))

        else:
            if self.formula == "0.0":
                self.formula = ""

            if operation.isdigit():
                self.formula += operation
                key = True

            elif key:
                self.formula += operation
                key = False





            # if operation.isdigit() and self.formula == '':
            #     self.formula += operation
            # elif (operation != self.formula[-1] and not operation.isdigit()):
            #     self.formula += operation
            # elif operation.isdigit():
            #     self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0.0"
        self.lbl.configure(text=self.formula)
        x = 500
        y = 130
        for c in self.old_calc:
            com = lambda x=c: self.logarray(x)
            Button(text=c, bg="#ABC",
                   font=("Times New Roman", 15),
                   command=com).place(x=x, y=y,
                                      width=200,
                                      height=50)
            y += 50
            if y > 560:
                x += 100
                y = 130
            if x > 700:
                x = 500
                y = 130


root = Tk()
root["bg"] = "#CBA"
root.geometry("740x620")
root.title("Калькулятор")
root.resizable(False, False)
app = Main(root)
app.pack()
root.mainloop()