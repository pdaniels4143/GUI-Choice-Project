import tkinter as t

class calculator:
    def __init__(self,masterframe):
        #variables
        self.total=""
        self.origin=""
        self.math=""
        #creating the screen of the calculator
        self.results=t.Label(masterframe,
                             text="0")
        self.results.configure(height=2,
                               width=20,
                               font=("", 40),
                               relief="ridge")
        self.results.grid(row=0,
                          column=0,
                          columnspan=4)
        #row 1 (clear and division functions)
        self.clear_button=t.Button(masterframe,
                                   text="Clear",
                                   command=self.clear)
        self.clear_button.configure(height=1,
                                    width=15,
                                    font=("",40),
                                    padx=10)
        self.clear_button.grid(row=1,
                               column=0,
                               columnspan=3)
        self.divide_button=t.Button(masterframe,
                                    text="÷",
                                    command=self.division)
        self.divide_button.configure(height=1,
                                     width=5,
                                     font=("",40))
        self.divide_button.grid(row=1,
                                column=3)
        #row 2 (numbers 7,8,9, and multiplication function)
        self.num7_button=t.Button(masterframe,
                                  text="7",
                                  command=self.seven)
        self.num7_button.configure(height=1,
                                   width=5,
                                   font=("",40))
        self.num7_button.grid(row=2,
                              column=0)
        self.num8_button=t.Button(masterframe,
                                  text="8",
                                  command=self.eight)
        self.num8_button.configure(height=1,
                                   width=5,
                                   font=("",40))
        self.num8_button.grid(row=2,
                              column=1)
        self.num9_button=t.Button(masterframe,
                                  text="9",
                                  command=self.nine)
        self.num9_button.configure(height=1,
                                   width=5,
                                   font=("",40))
        self.num9_button.grid(row=2,
                              column=2)
        self.multiply_button=t.Button(masterframe,
                                  text="×",
                                      command=self.multiplication)
        self.multiply_button.configure(height=1,
                                       width=5,
                                       font=("",40))
        self.multiply_button.grid(row=2,
                                  column=3)
        #row 3 (numbers 4,5,6, and subtraction function)
        self.num4_button = t.Button(masterframe,
                                    text="4",
                                    command=self.four)
        self.num4_button.configure(height=1,
                                   width=5,
                                   font=("", 40))
        self.num4_button.grid(row=3,
                              column=0)
        self.num5_button = t.Button(masterframe,
                                    text="5",
                                    command=self.five)
        self.num5_button.configure(height=1,
                                   width=5,
                                   font=("", 40))
        self.num5_button.grid(row=3,
                              column=1)
        self.num6_button = t.Button(masterframe,
                                    text="6",
                                    command=self.six)
        self.num6_button.configure(height=1,
                                   width=5,
                                   font=("", 40))
        self.num6_button.grid(row=3,
                              column=2)
        self.subtract_button = t.Button(masterframe,
                                    text="-",
                                        command=self.subtraction)
        self.subtract_button.configure(height=1,
                                   width=5,
                                   font=("", 40))
        self.subtract_button.grid(row=3,
                              column=3)
        #row 4 (numbers 1,2,3, and addition function)
        self.num1_button = t.Button(masterframe,
                                    text="1",
                                    command=self.one)
        self.num1_button.configure(height=1,
                                   width=5,
                                   font=("", 40))
        self.num1_button.grid(row=4,
                              column=0)
        self.num2_button = t.Button(masterframe,
                                    text="2",
                                    command=self.two)
        self.num2_button.configure(height=1,
                                   width=5,
                                   font=("", 40))
        self.num2_button.grid(row=4,
                              column=1)
        self.num3_button = t.Button(masterframe,
                                    text="3",
                                    command=self.three)
        self.num3_button.configure(height=1,
                                   width=5,
                                   font=("", 40))
        self.num3_button.grid(row=4,
                              column=2)
        self.add_button = t.Button(masterframe,
                                    text="+",
                                   command=self.addition)
        self.add_button.configure(height=1,
                                   width=5,
                                   font=("", 40))
        self.add_button.grid(row=4,
                              column=3)
        #row 5 (negative,0,decimal point, and equal buttons)
        self.negative_button = t.Button(masterframe,
                                    text="(-)",
                                        command=self.negation)
        self.negative_button.configure(height=1,
                                   width=5,
                                   font=("", 40))
        self.negative_button.grid(row=5,
                              column=0)
        self.num0_button = t.Button(masterframe,
                                        text="0",
                                    command=self.zero)
        self.num0_button.configure(height=1,
                                       width=5,
                                       font=("", 40))
        self.num0_button.grid(row=5,
                                  column=1)
        self.decimal_button = t.Button(masterframe,
                                        text=".",
                                       command=self.decimal)
        self.decimal_button.configure(height=1,
                                       width=5,
                                       font=("", 40))
        self.decimal_button.grid(row=5,
                                  column=2)
        self.equal_button = t.Button(masterframe,
                                        text="=",
                                     command=self.calculate)
        self.equal_button.configure(height=1,
                                       width=5,
                                       font=("", 40),
                                    state="disabled")
        self.equal_button.grid(row=5,
                                  column=3)

    #functions of the buttons
    def clear(self):
        self.total=""
        self.origin=""
        self.math=""
        self.results.configure(text="0")
        self.negative_button.configure(state="normal")
        self.decimal_button.configure(state="normal")
        self.add_button.configure(state="normal")
        self.subtract_button.configure(state="normal")
        self.multiply_button.configure(state="normal")
        self.divide_button.configure(state="normal")
        self.equal_button.configure(state="disabled")
    def zero(self):
        self.total=add(self.total,"0")
        self.results.configure(text=str(self.total))
        self.negative_button.configure(state="disabled")
        self.equal_button.configure(state="normal")
    def one(self):
        self.total=add(self.total,"1")
        self.results.configure(text=str(self.total))
        self.negative_button.configure(state="disabled")
        self.equal_button.configure(state="normal")
    def two(self):
        self.total=add(self.total,"2")
        self.results.configure(text=str(self.total))
        self.negative_button.configure(state="disabled")
        self.equal_button.configure(state="normal")
    def three(self):
        self.total=add(self.total,"3")
        self.results.configure(text=str(self.total))
        self.negative_button.configure(state="disabled")
        self.equal_button.configure(state="normal")
    def four(self):
        self.total=add(self.total,"4")
        self.results.configure(text=str(self.total))
        self.negative_button.configure(state="disabled")
        self.equal_button.configure(state="normal")
    def five(self):
        self.total=add(self.total,"5")
        self.results.configure(text=str(self.total))
        self.negative_button.configure(state="disabled")
        self.equal_button.configure(state="normal")
    def six(self):
        self.total=add(self.total,"6")
        self.results.configure(text=str(self.total))
        self.negative_button.configure(state="disabled")
        self.equal_button.configure(state="normal")
    def seven(self):
        self.total=add(self.total,"7")
        self.results.configure(text=str(self.total))
        self.negative_button.configure(state="disabled")
        self.equal_button.configure(state="normal")
    def eight(self):
        self.total=add(self.total,"8")
        self.results.configure(text=str(self.total))
        self.negative_button.configure(state="disabled")
        self.equal_button.configure(state="normal")
    def nine(self):
        self.total=add(self.total,"9")
        self.results.configure(text=str(self.total))
        self.negative_button.configure(state="disabled")
        self.equal_button.configure(state="normal")
    def negation(self):
        self.total=add(self.total,"-")
        self.negative_button.configure(state="disabled")
        self.equal_button.configure(state="normal")
    def decimal(self):
        self.total=add(self.total,".")
        self.results.configure(text=str(self.total))
        self.decimal_button.configure(state="disabled")
        self.negative_button.configure(state="disabled")
    def addition(self):
        self.origin=self.total
        self.total=""
        self.math="add"
        self.add_button.configure(state="disabled")
        self.subtract_button.configure(state="disabled")
        self.multiply_button.configure(state="disabled")
        self.divide_button.configure(state="disabled")
    def subtraction(self):
        self.origin=self.total
        self.total=""
        self.math="subtract"
        self.add_button.configure(state="disabled")
        self.subtract_button.configure(state="disabled")
        self.multiply_button.configure(state="disabled")
        self.divide_button.configure(state="disabled")
    def multiplication(self):
        self.origin=self.total
        self.total=""
        self.math="multiply"
        self.add_button.configure(state="disabled")
        self.subtract_button.configure(state="disabled")
        self.multiply_button.configure(state="disabled")
        self.divide_button.configure(state="disabled")
    def division(self):
        self.origin=self.total
        self.total=""
        self.math="divide"
        self.add_button.configure(state="disabled")
        self.subtract_button.configure(state="disabled")
        self.multiply_button.configure(state="disabled")
        self.divide_button.configure(state="disabled")
    def calculate(self):
        if self.math=="add":
            self.total=float(self.origin)+float(self.total)
            self.results.configure(text=str(self.total))
        elif self.math=="subtract":
            self.total = float(self.origin) - float(self.total)
            self.results.configure(text=str(self.total))
        elif self.math=="multiply":
            self.total = float(self.origin) * float(self.total)
            self.results.configure(text=str(self.total))
        elif self.math=="divide":
            self.total = float(self.origin) / float(self.total)
            self.results.configure(text=str(self.total))
        self.negative_button.configure(state="normal")
        self.decimal_button.configure(state="normal")
        self.add_button.configure(state="normal")
        self.subtract_button.configure(state="normal")
        self.multiply_button.configure(state="normal")
        self.divide_button.configure(state="normal")

def add(start,number):
    new= str(start)+number
    return new






















def main():
    root=t.Tk()
    calc=calculator(root)
    root.mainloop()
    float(str(-.6))
main()
