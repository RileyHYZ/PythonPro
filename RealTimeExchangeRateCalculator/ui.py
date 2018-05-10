from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E

class ExchangeConverter:
    
    def validate(self, input_text):
        if not input_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(input_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        else: # reset
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

    def __init__(self, master):
        self.master = master
        #title
        master.title("Foreign Exchange Converter")
        
        #initialize numbers
        self.total = 0
        self.entered_number = 0
        
        #convert currency from(drop-down menu)
        self.label1 = Label(master, text="Convert Currency From")
        #convert to(drop-down menu)
        self.label2 = Label(master, text="To")
        
        
        
        
        #Amount of money(input text)
        #input must be valid numbers(int/double with two decimal places)
        self.label3 = Label(master, text="Amount to convert")
        vcmd = master.register(self.validate)
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        
        #update a section summary 
        self.label4 = Label(master, text="You are converting")
        
       
        #Add/Subtract Button & Reset
        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))
        
        
        
       
        #update to total
        #check if valid(unit of currency must align)
        #do the addition/subtraction
        
        
        

        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)


        
        

        
        # LAYOUT

        self.label1.grid(row=1, column=1,columnspan=2, sticky=W)
        self.label2.grid(row=2, column=1, sticky=W)
        self.label3.grid(row=3, column=2, sticky=W)
        self.label4.grid(row=4, column=2, sticky=W)
        self.entry.grid(row=3, column=5, columnspan=3, sticky=W+E)
        
        self.total_label.grid(row=8, column=2, columnspan=4, sticky=E)

        

        self.add_button.grid(row=7, column=2)
        self.subtract_button.grid(row=7, column=3)
        self.reset_button.grid(row=7, column=8, sticky=W+E)

root = Tk()
my_gui = ExchangeConverter(root)
root.mainloop()