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
        
        try:
            self.entered_number = float(input_text)
            self.entered_number = (int)(self.entered_number*100)/100.0
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            print(self.entered_number)
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        else: # reset
            self.total = 0

        self.total_label_text.set((int)(self.total*100)/100.0)
        self.entry.delete(0, END)
    
    def updateSummary(self,tkvar_1,tkvar_2):
        self.amount = converter.convert(self.entered_number,tkvar_1.get(),tkvar_2.get())   
    
    def __init__(self, master):
        self.master = master
        #title
        master.title("Foreign Exchange Converter")
        
        #initialize numbers
        self.total = 0.0
        self.entered_number = 0.0
        self.amount = 0.0
        
        #convert currency from(drop-down menu)
        self.label1 = Label(master, text="Convert Currency From")
        #drop-down menu
        #currencies
        tkvar_1 = StringVar(master)
        tkvar_1.set("CAD")
        self.menu_1=OptionMenu(master,tkvar_1,*list_currencies())
        #self.menu_1.pack()
        
        ##MARK FIRST CURRENCY
        
        #convert to(drop-down menu)
        self.label2 = Label(master, text="To")
        #drop-down menu
        tkvar_2 = StringVar(master)
        tkvar_2.set("CAD")
        self.menu_2=OptionMenu(master,tkvar_2,*list_currencies())
        #self.menu_2.pack()
        
        
        #Amount of money(input text)
        #input must be valid numbers(int/double with two decimal places)
        self.label3 = Label(master, text="Amount to convert")
        vcmd = master.register(self.validate)
        print(vcmd)
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.confirm_button = Button(master, text="confirm", command=self.updateSummary(tkvar_1,tkvar_2))
        
        
        
        print(self.entered_number)
        #update a section summary 
        self.amount_label_text = IntVar()
        self.amount_label_text.set(self.amount)
        self.initamount_label_text = IntVar()
        self.initamount_label_text.set(self.entered_number)
        self.label4_0 = Label(master, text="You are converting")
        self.initial_amount_label = Label(master, textvariable=self.initamount_label_text)
        self.label4_1 = Label(master, text=tkvar_1.get()+" to ")
        self.amount_label = Label(master, textvariable=self.amount_label_text)
        self.label4_2 = Label(master, text=tkvar_2.get())
        #self.label4 = Label(master, text="You are converting "+converter.convert(self.entered_number,tkvar_1.get(),tkvar_2.get()))
        
        
        
        
        
        #Add/Subtract Button & Reset
        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))
        
        
        
       
        #update to total
        #check if valid(unit of currency must align)
        #do the addition/subtraction
        
        self.label5 = Label(master, text="Total")
        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)


        
        

        
        # LAYOUT
        
        #convert currency from #menu_1
        self.label1.grid(row=1, column=2,sticky=E)
        self.menu_1.grid(row=1, column=4,sticky=W)
        #to #menu_2
        self.label2.grid(row=2, column=2, sticky=E)
        self.menu_2.grid(row=2, column=4,sticky=W)
        #Amount to convert
        self.label3.grid(row=3, column=2,columnspan=1, sticky=E)
        self.entry.grid(row=3, column=4, columnspan=2, sticky=W)
        #confirm
        self.confirm_button.grid(row=3,column=6)
        
        
        self.label4_0.grid(row=4, column=2, sticky=W)
        
        self.initial_amount_label.grid(row=4, column=2, sticky=E)
        self.label4_1.grid(row=4, column=3, sticky=E)
        self.amount_label.grid(row=4, column=4, sticky=E)
        self.label4_2.grid(row=4, column=6, sticky=E)
        self.label5.grid(row=8, column=2, columnspan=2,sticky=E)
        self.entry.grid(row=3, column=4, columnspan=2, sticky=W+E)
        
        self.total_label.grid(row=8, column=4, columnspan=4, sticky=W)

        

        self.add_button.grid(row=7, column=2)
        self.subtract_button.grid(row=7, column=3)
        self.reset_button.grid(row=7, column=5, sticky=W+E)




root = Tk()
my_gui = ExchangeConverter(root)
root.mainloop()
