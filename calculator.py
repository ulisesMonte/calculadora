import tkinter as tk

class calculator:
    def __init__(self,master):
        self.master=master
        self.display = tk.Entry(master,width=15,font=("Arial",23),bd=10, insertwidth=1, bg="#6495DE",justify="right")# we define and we set up the widget
        self.display.grid(row=0,column=0,columnspan=4) # we define the window settings for the inputs 
        self.op_verification = False #the variable for the special keys
        self.op= ""
        self.current = ""
        self.total = 0

        row = 1
        col = 0 
        # we define the row and columns for the vector of the buttons 
        buttons =[ # We set up the buttons of them menu
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", ".", "+", 
            "="
        ]


        for button in buttons: #We iterate the buttons and call the buildButtons method
            self.build_button(button,row,col)
            col+=1

            if col > 3: # Set up the builder because when column is equal 3 the iterable must low the column, because thats how the vector is made
                col = 0
                row +=1



    def key_press(self,event):
        if event.char.isdigit(): # if the number is int
            key = event.char
            print(key)

    def click(self, key):
        if self.op_verification:
            self.op_verification = False
        
        self.display.insert(tk.END, key)

        if key in "0123456789" or key == ".":
            self.current += key # We set the variable because when we input the numbers the numbers comnined in one number
        else:
            if self.current:
                if not self.op:
                    self.total = float(self.current) # set the variable as float because we sum the variable as float

            self.current = ""
            self.op_verification = True
            self.op = key



    def clear_display(self):
        self.display.delete(0,tk.END)
        self.op_verification = False
        self.current =""
        self.op= ""
        self.total = 0
        
        
    def calculate(self):
        if self.current and self.op:
            if self.op == "/":
                self.total /= float(self.current)         
            if self.op == "*":
                self.total *= float(self.current)
            if self.op == "+":
                self.total += float(self.current)
            if self.op == "-":
                self.total -= float(self.current)


        self.display.delete(0, tk.END)
        self.op=""
        self.display.insert(tk.END, round(self.total,3))

    def build_button(self,button,row,col):
        if button == "C":
            b = tk.Button(self.master, text=button, width=6,command=lambda: self.clear_display()) #Set up the button
        elif button == "=":
            b = tk.Button(self.master,text=button, width=6, command=lambda: self.calculate())
        else:
            b = tk.Button(self.master, text=button, width=6, command=lambda: self.click(button))
        b.grid(row=row,column=col) # set up the buttons distributions







root = tk.Tk() # major window
my_gui=calculator(root)
root.mainloop()