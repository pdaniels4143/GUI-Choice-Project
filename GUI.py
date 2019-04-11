import tkinter as t

class calculator:
    def __init__(self,masterframe):
        #creating the screen of the calculator
        self.results=t.Label(masterframe,
                             text="Test",
                             background = "pink")
        self.results.configure(height=2,
                               width=20,
                               background="blue",
                               font=("", 40))
        self.results.grid(row=0,
                          column=0,
                          columnspan=4)
        #row 1 (clear and division functions)
        self.clear_button=t.Button(masterframe,
                                   text="Clear")
        self.clear_button.configure(height=1,
                                    width=15,
                                    font=("",40))
        self.clear_button.grid(row=1,
                               column=0,
                               columnspan=3)
        self.divide_button=t.Button(masterframe,
                                    text="÷")
        self.divide_button.configure(height=1,
                                     width=5,
                                     font=("",40))
        self.divide_button.grid(row=1,
                                column=3,
                                columnspan=1)
        #row 2 (number 7,8,9, and multiplication function)
        self.num7_button=t.Button(masterframe,
                                  text="7")
        self.num7_button.configure(height=1,
                                   width=5,
                                   font=("",40))
        self.num7_button.grid(row=2,
                              column=0,
                              columnspan=1)
        self.num8_button=t.Button(masterframe,
                                  text="8")
        self.num8_button.configure(height=1,
                                   width=5,
                                   font=("",40))
        self.num8_button.grid(row=2,
                              column=1,
                              columnspan=1)
        self.num9_button=t.Button(masterframe,
                                  text="9")
        self.num9_button.configure(height=1,
                                   width=5,
                                   font=("",40))
        self.num9_button.grid(row=2,
                              column=2,
                              columnspan=1)
        self.multiply_button=t.Button(masterframe,
                                  text="×")
        self.multiply_button.configure(height=1,
                                       width=5,
                                       font=("",40))
        self.multiply_button.grid(row=2,
                                  column=3,
                                  columnspan=1)























def main():
    root=t.Tk()
    calc=calculator(root)
    root.mainloop()

main()
