import tkinter as t

class calculator:
    def __init__(self,masterframe):
        #creating the screen of the calculator
        self.results=t.Label(masterframe,
                             text="Test")
        self.results.configure(height=2,
                               width=20,
                               font=("", 40),
                               relief="ridge")
        self.results.grid(row=0,
                          column=0,
                          columnspan=4)
        #row 1 (clear and division functions)
        self.clear_button=t.Button(masterframe,
                                   text="Clear")
        self.clear_button.configure(height=1,
                                    width=15,
                                    font=("",40),
                                    padx=10)
        self.clear_button.grid(row=1,
                               column=0,
                               columnspan=3)
        self.divide_button=t.Button(masterframe,
                                    text="÷")
        self.divide_button.configure(height=1,
                                     width=5,
                                     font=("",40))
        self.divide_button.grid(row=1,
                                column=3)
        #row 2 (numbers 7,8,9, and multiplication function)
        self.num7_button=t.Button(masterframe,
                                  text="7")
        self.num7_button.configure(height=1,
                                   width=5,
                                   font=("",40))
        self.num7_button.grid(row=2,
                              column=0)
        self.num8_button=t.Button(masterframe,
                                  text="8")
        self.num8_button.configure(height=1,
                                   width=5,
                                   font=("",40))
        self.num8_button.grid(row=2,
                              column=1)
        self.num9_button=t.Button(masterframe,
                                  text="9")
        self.num9_button.configure(height=1,
                                   width=5,
                                   font=("",40))
        self.num9_button.grid(row=2,
                              column=2)
        self.multiply_button=t.Button(masterframe,
                                  text="×")
        self.multiply_button.configure(height=1,
                                       width=5,
                                       font=("",40))
        self.multiply_button.grid(row=2,
                                  column=3)
        #row 3 (numbers 4,5,6, and subtraction function)
        self.num4_button = t.Button(masterframe,
                                    text="4")
        self.num4_button.configure(height=1,
                                   width=5,
                                   font=("", 40))
        self.num4_button.grid(row=3,
                              column=0)
        self.num5_button = t.Button(masterframe,
                                    text="5")
        self.num5_button.configure(height=1,
                                   width=5,
                                   font=("", 40))
        self.num5_button.grid(row=3,
                              column=1)
        self.num6_button = t.Button(masterframe,
                                    text="6")
        self.num6_button.configure(height=1,
                                   width=5,
                                   font=("", 40))
        self.num6_button.grid(row=3,
                              column=2)
        self.subtract_button = t.Button(masterframe,
                                    text="-")
        self.subtract_button.configure(height=1,
                                   width=5,
                                   font=("", 40))
        self.subtract_button.grid(row=3,
                              column=3)
        #row 4 (numbers 1,2,3, and addition function)
        self.num1_button = t.Button(masterframe,
                                    text="1")
        self.num1_button.configure(height=1,
                                   width=5,
                                   font=("", 40))
        self.num1_button.grid(row=4,
                              column=0)
        self.num2_button = t.Button(masterframe,
                                    text="2")
        self.num2_button.configure(height=1,
                                   width=5,
                                   font=("", 40))
        self.num2_button.grid(row=4,
                              column=1)
        self.num3_button = t.Button(masterframe,
                                    text="3")
        self.num3_button.configure(height=1,
                                   width=5,
                                   font=("", 40))
        self.num3_button.grid(row=4,
                              column=2)
        self.add_button = t.Button(masterframe,
                                    text="+")
        self.add_button.configure(height=1,
                                   width=5,
                                   font=("", 40))
        self.add_button.grid(row=4,
                              column=3)
        #row 5 (negative,0,decimal point, and equal buttons)
        self.negative_button = t.Button(masterframe,
                                    text="(-)")
        self.negative_button.configure(height=1,
                                   width=5,
                                   font=("", 40))
        self.negative_button.grid(row=5,
                              column=0)
        self.num0_button = t.Button(masterframe,
                                        text="0")
        self.num0_button.configure(height=1,
                                       width=5,
                                       font=("", 40))
        self.num0_button.grid(row=5,
                                  column=1)
        self.decimal_button = t.Button(masterframe,
                                        text=".")
        self.decimal_button.configure(height=1,
                                       width=5,
                                       font=("", 40))
        self.decimal_button.grid(row=5,
                                  column=2)
        self.equal_button = t.Button(masterframe,
                                        text="=")
        self.equal_button.configure(height=1,
                                       width=5,
                                       font=("", 40))
        self.equal_button.grid(row=5,
                                  column=3)






















def main():
    root=t.Tk()
    calc=calculator(root)
    root.mainloop()

main()
