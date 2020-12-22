from tkinter import *
import pandas_datareader as dr
from datetime import datetime



#Functions
def enter(event):
    add_command()

def delete(event):
    delete_stock()

def caps(event):
    stock_name.set(stock_name.get().upper())


def today():
    endDateEntry.insert(0, datetime.now().strftime('%Y-%m-%d'))

def add_command():
    displayBox.insert(END, stock_name.get())
    StockInput.delete(0, END)

def get_selected_row(event):
    global index 
    index = displayBox.curselection()

def delete_stock():
    displayBox.delete(index)

def export_stockData():
    for item in displayBox.get(0, END):
        dr.DataReader(item, "yahoo", start_date.get(), end_date.get()).to_csv(item+'.csv')


window=Tk()
window.wm_title("Stock Collecter")

stockNameLabel = Label(window, text="Stock Name")
stockNameLabel.grid(row=0,column=0)

startDateLabel = Label(window, text="Start Date")
startDateLabel.grid(row=1,column=0)

endDateLabel = Label(window, text="End Date")
endDateLabel.grid(row=1,column=2)

#User Entry

stock_name = StringVar()
StockInput = Entry(window, textvariable=stock_name)
StockInput.grid(row=0, column=1)


#Date Entries
start_date = StringVar()
startDateEntry = Entry(window, textvariable=start_date)
startDateEntry.grid(row=1, column=1)

end_date = StringVar()
endDateEntry = Entry(window, textvariable=end_date)
endDateEntry.grid(row=1, column=3)


#Listboxes

displayBox = Listbox(window, height=6, width=35)
displayBox.grid(row=2, column=0, rowspan=6, columnspan=2)

#Scrollbar

scrollBar = Scrollbar(window)
scrollBar.grid(row=2,column=2,rowspan=6)

#Buttons

todayDateButton = Button(window, text="Today's Date", width=20, command=today)
todayDateButton.grid(row=3, column=3)

addStockButton = Button(window, text="Add Stock", width=20, command=add_command)
addStockButton.grid(row=4, column=3)

deleteStock = Button(window, text="Remove Stock", width=20, command=delete_stock)
deleteStock.grid(row=5, column=3)

exportButton = Button(window, text="Export",bg="lightgreen", width=20, command=export_stockData)
exportButton.grid(row=6, column=3)

#KeyBinds

StockInput.bind('<Return>', enter)
StockInput.bind('<KeyRelease>', caps)

displayBox.bind('<<ListboxSelect>>', get_selected_row)
displayBox.bind('<Delete>', delete)

displayBox.configure(yscrollcommand=scrollBar.set)
scrollBar.configure(command=displayBox.yview)






window.mainloop()