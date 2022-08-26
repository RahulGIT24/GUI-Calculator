from tkinter import *
# * Author - Rahul
# * Project - A user friendly calculator
# *Location - Mars


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x500")
        self.title("Calculator")
        self.wm_iconbitmap("icon.ico")



if __name__ == "__main__":
    calculator = GUI()
    calculator.mainloop()