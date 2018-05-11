from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, OptionMenu,\
    StringVar
from babel.numbers import list_currencies
import urllib.request
import json

class CurrencyConverter:
    
    rates={}
    
    def __init__(self,url):
        req=urllib.request.Request(url,headers={'User-Agent': 'Real Exchange Rate'})
        data=urllib.request.urlopen(req).read()
        data=json.loads(data.decode('utf-8'))
        self.rates=data["rates"]
          
    def convert(self,amount,from_currency,to_currency):
        initial_amount = amount
        if from_currency == to_currency:
            return amount
        if from_currency!="EUR":
            amount=amount/self.rates[from_currency]
        if to_currency == "EUR":
            return amount
        else:
            return amount * self.rates[to_currency]
        
converter=CurrencyConverter("http://data.fixer.io/api/latest?access_key=450a31e03b85dfc8aa24d58d0ac24f79")



class ExchangeConverter:
    
    def validate(self, input_text):
        if not input_text: # the field is being cleared
            self.entered_number = 0.0
            return True
        if self.enable_operations == False:
            return False
        try:
            self.entered_number = float(input_text)
            self.entered_number = (int)(self.entered_number*100)/100.0
            return True
        except ValueError:
            return False

    def update(self, method):
        print("update")
        if method == "add" and self.enable_operations == True:
            self.total += self.entered_number
            self.amount = converter.convert(self.total, self.tkvar_1.get(), self.tkvar_2.get())
        elif method == "subtract" and self.enable_operations == True:
            self.total -= self.entered_number
            self.amount = converter.convert(self.total, self.tkvar_1.get(), self.tkvar_2.get())
        else: # reset
            self.total = 0.0
            self.amount = 0.0
            self.menu_1.configure(state="active")
            self.menu_2.configure(state="active")
            self.enable_operations = False

        self.total_label_text.set((int)(self.total*100)/100.0)
        self.amount_label_text.set((int)(self.amount*100)/100.0)
        self.entry.delete(0, END)
    
    def confirm(self):
        self.menu_1.configure(state="disable")
        self.menu_2.configure(state="disable")
        self.from_label_text.set(self.tkvar_1.get())
        self.to_label_text.set(self.tkvar_2.get())
        self.enable_operations = True     
    
    def __init__(self, master):
        self.master = master
        #title
        master.title("Foreign Exchange Converter")
        
        #initialize numbers
        self.total = 0.0
        self.entered_number = 0.0
        self.amount = 0.0
        self.enable_operations = False
        
        #convert currency from
        self.label1 = Label(master, text="Convert Currency From")
        #drop-down menu
        self.tkvar_1 = StringVar(master)
        self.tkvar_1.set("CAD")
        self.menu_1=OptionMenu(master,self.tkvar_1,*sorted(list_currencies()))

        #convert to
        self.label2 = Label(master, text="To")
        #drop-down menu
        self.tkvar_2 = StringVar(master)
        self.tkvar_2.set("CAD")
        self.menu_2=OptionMenu(master,self.tkvar_2,*sorted(list_currencies()))
        
        #confirm(disable menu)
        self.confirm_button = Button(master, text="confirm", command=lambda: self.confirm())
        
        #Amount of money(input text)
        #input must be valid numbers(int/double with two decimal places)
        self.label3 = Label(master, text="Amount to convert")
        vcmd = master.register(self.validate)
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        
        #update a section summary 
        #Add/Subtract Button(menu disabled) & Reset(menu active, everything=0)
        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))
        
        #update to total
        #check if valid(unit of currency must align)
        #do the addition/subtraction
        
        #Total
        self.label4 = Label(master, text="Total:")
        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable = self.total_label_text)
        self.from_label_text = StringVar()
        self.from_label_text.set(self.tkvar_1.get())
        self.from_label = Label(master, textvariable = self.from_label_text)

        #Calculated result
        self.eq_label = Label(master, text="≈")
        self.amount_label_text = IntVar()
        self.amount_label_text.set(self.amount)
        self.amount_label = Label(master, textvariable = self.amount_label_text)
        self.to_label_text = StringVar()
        self.to_label_text.set(self.tkvar_2.get())
        self.to_label = Label(master, textvariable = self.to_label_text)
        
        

        
        # LAYOUT
        
        #convert currency from #menu_1
        self.label1.grid(row=1, column=2,sticky=E)
        self.menu_1.grid(row=1, column=4,sticky=W)
        #to #menu_2
        self.label2.grid(row=2, column=2, sticky=E)
        self.menu_2.grid(row=2, column=4,sticky=W)
        #confirm button
        self.confirm_button.grid(row=2,column=5,sticky=W)
        #Amount to convert
        self.label3.grid(row=3, column=2,columnspan=1, sticky=E)
        self.entry.grid(row=3, column=4, columnspan=2, sticky=W)
        #Add, Subtract, Reset
        self.add_button.grid(row=4, column=2)
        self.subtract_button.grid(row=4, column=3)
        self.reset_button.grid(row=4, column=5, sticky=W)
        #total
        self.label4.grid(row=5, column=2, sticky=W+E)
        self.total_label.grid(row=5, column=4, sticky=E)
        self.from_label.grid(row=5,column=5, sticky=W)
        self.eq_label.grid(row=6,column=3, sticky=W)
        self.amount_label.grid(row=6,column=4,sticky=E)
        self.to_label.grid(row=6,column=5, sticky=W)

        

       




root = Tk()
my_gui = ExchangeConverter(root)
root.mainloop()
