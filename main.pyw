from tkinter import *

# * Author - Rahul
# * Project - A user friendly calculator
# *Location - Mars


class GUI(Tk):
    def __init__(self):
        super().__init__()
        #! Width of calculator
        self.width = '350'
        #! Height of calculator
        self.height = '400'
        self.geometry(f"{self.width}x{self.height}")
        #! Max height and width of calculator
        self.maxsize(350, 450)
        #! Min height and width of calculator
        self.minsize(350, 450)
        #! Title of calculator
        self.title("Calculator")
        #! Icon of calculator
        self.wm_iconbitmap("icon.ico")

    #! Functions for calculator

    # * This function is for the display screen of calculator
    def inputValue(self):
        global inputValue
        f = Frame(self, borderwidth=1, bg='red')
        inputValue = StringVar()
        inputValue.set('')
        self.valueEntry = Entry(
            f, textvariable=inputValue, font=('Arial 18'))
        self.valueEntry.pack(fill=X)
        f.pack(fill=X, padx=12, pady=4)

    # * This function calculates the value and sets the answer on screen
    def calulateVal(self):
        try:
            self.calc = eval(inputValue.get())
            inputValue.set(self.calc)
        except Exception:
            pass

    # * This Function clears screen
    def clearScreen(self):
        inputValue.set('')

    # * This function removes 1 element from the screen
    def back(self):
        inputvalue = inputValue.get()
        inputValue.set(inputvalue[:-1])

    # * This Function sets value in calculator
    @staticmethod
    def click(event):
        text = event.widget.cget('text')
        inputValue.set(str(inputValue.get())+text)

    # * Creating Buttons for calculator
    def buttons(self):
        global btn
        f = Frame(self, bg="gray")
        btn = Button(f, text='+', bg='red', fg='black', padx=23,
                     pady=12, relief=SUNKEN, font="Arial 10 bold")
        btn.pack(side=LEFT, anchor='n', padx=13, pady=13)
        btn.bind("<Button-1>", self.click)
        btn = Button(f, text='-', bg='red', fg='black', padx=23,
                     pady=12, relief=SUNKEN, font="Arial 10 bold")
        btn.pack(side=LEFT, anchor='n', padx=13, pady=13)
        btn.bind("<Button-1>", self.click)
        btn = Button(f, text='*', bg='red', fg='black', padx=23,
                     pady=12, relief=SUNKEN, font="Arial 10 bold")
        btn.pack(side=LEFT, anchor='n', padx=13, pady=13)
        btn.bind("<Button-1>", self.click)

        # * This button removes last element from the screen I have not added an event because I have already created a function for it
        btn = Button(f, text='CE', bg='red', fg='black', padx=23,
                     pady=12, relief=SUNKEN, font="Arial 10 bold", command=self.back)
        btn.pack(side=LEFT, anchor='n', padx=13, pady=13)

        f.pack(fill=X,)

        f = Frame(self, bg='gray')
        btn = Button(f, text='7', bg='red', fg='black', padx=23,
                     pady=12, relief=SUNKEN, font="Arial 10 bold")
        btn.pack(side=LEFT, anchor='n', padx=13, pady=13)
        btn.bind("<Button-1>", self.click)
        btn = Button(f, text='8', bg='red', fg='black', padx=23,
                     pady=12, relief=SUNKEN, font="Arial 10 bold")
        btn.pack(side=LEFT, anchor='n', padx=13, pady=13)
        btn.bind("<Button-1>", self.click)
        btn = Button(f, text='9', bg='red', fg='black', padx=23,
                     pady=12, relief=SUNKEN, font="Arial 10 bold")
        btn.pack(side=LEFT, anchor='n', padx=13, pady=13)
        btn.bind("<Button-1>", self.click)

        # * This button removes all element from the screen I have not added an event because I have already created a function for it
        btn = Button(f, text='C', bg='red', fg='black', padx=23,
                     pady=12, relief=SUNKEN, font="Arial 10 bold", command=self.clearScreen)
        btn.pack(side=LEFT, anchor='n', padx=13, pady=13)

        f.pack(fill=X)

        f = Frame(self, bg='gray')
        btn = Button(f, text='4', bg='red', fg='black', padx=23,
                     pady=12, relief=SUNKEN, font="Arial 10 bold")
        btn.pack(side=LEFT, anchor='n', padx=13, pady=13)
        btn.bind("<Button-1>", self.click)
        btn = Button(f, text='5', bg='red', fg='black', padx=23,
                     pady=12, relief=SUNKEN, font="Arial 10 bold")
        btn.pack(side=LEFT, anchor='n', padx=13, pady=13)
        btn.bind("<Button-1>", self.click)
        btn = Button(f, text='6', bg='red', fg='black', padx=23,
                     pady=12, relief=SUNKEN, font="Arial 10 bold")
        btn.pack(side=LEFT, anchor='n', padx=13, pady=13)
        btn.bind("<Button-1>", self.click)
        btn = Button(f, text='/', bg='red', fg='black', padx=23,
                     pady=12, relief=SUNKEN, font="Arial 10 bold")
        btn.pack(side=LEFT, anchor='n', padx=13, pady=13)
        btn.bind("<Button-1>", self.click)
        f.pack()

        f = Frame(self, bg='gray')
        btn = Button(f, text='1', bg='red', fg='black', padx=23,
                     pady=12, relief=SUNKEN, font="Arial 10 bold")
        btn.pack(side=LEFT, anchor='n', padx=13, pady=13)
        btn.bind("<Button-1>", self.click)
        btn = Button(f, text='2', bg='red', fg='black', padx=23,
                     pady=12, relief=SUNKEN, font="Arial 10 bold")
        btn.pack(side=LEFT, anchor='n', padx=13, pady=13)
        btn.bind("<Button-1>", self.click)
        btn = Button(f, text='3', bg='red', fg='black', padx=23,
                     pady=12, relief=SUNKEN, font="Arial 10 bold")
        btn.pack(side=LEFT, anchor='n', padx=13, pady=13)
        btn.bind("<Button-1>", self.click)
        btn = Button(f, text='%', bg='red', fg='black', padx=23,
                     pady=12, relief=SUNKEN, font="Arial 10 bold")
        btn.pack(side=RIGHT, anchor='w', padx=13, pady=13)
        btn.bind("<Button-1>", self.click)
        f.pack(fill=X)

        f = Frame(self, bg='gray')
        # * This button evalutes the information available on the screen last element from the screen I have not added an event because I have already created a function for it
        btn = Button(f, text='=', bg='red', fg='black', padx=23,
                     pady=12, relief=SUNKEN, font="Arial 10 bold", command=self.calulateVal)
        btn.pack(side=RIGHT, anchor='w', padx=13,
                 pady=13)

        btn = Button(f, text='0', bg='red', fg='black', padx=23,
                     pady=12, relief=SUNKEN, font="Arial 10 bold")
        btn.pack(side=RIGHT, anchor='w', padx=13, pady=13)
        btn.bind("<Button-1>", self.click)
        btn = Button(f, text='00', bg='red', fg='black', padx=23,
                     pady=12, relief=SUNKEN, font="Arial 10 bold")
        btn.pack(side=RIGHT, anchor='w', padx=13, pady=13)
        btn.bind("<Button-1>", self.click)
        btn = Button(f, text='.', bg='red', fg='black', padx=23,
                     pady=12, relief=SUNKEN, font="Arial 10 bold")
        btn.pack(side=RIGHT, anchor='w', padx=13, pady=13)
        btn.bind("<Button-1>", self.click)
        f.pack(fill=X)


if __name__ == "__main__":
    calculator = GUI()
    calculator.inputValue()
    calculator.buttons()
    calculator.mainloop()
